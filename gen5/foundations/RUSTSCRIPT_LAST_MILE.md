# RustScript — Last Mile UI Safety for a Pure Rust Ecosystem

**Date**: Jul 14, 2026 | **Wave**: 139a
**Lineage**: gen4/products → gen5/foundations/COMPOSITION_ROUTING_PATTERN → this
**Origin**: footPrint (protoKarya) — empirical validation of Rust safety patterns in TypeScript

---

## Thesis

ecoPrimals is a pure Rust ecosystem. Every primal, every deployment pipeline, every
cryptographic operation, every data provenance chain is Rust. The question is: what
happens at the last mile, where the system meets a human browser?

RustScript is the answer we discovered empirically. It is not a language. It is a
zero-dependency TypeScript library that encodes Rust's safety constraints as types
and runtime primitives. It exists because browsers execute JavaScript, not Rust — and
until WASM matures to full DOM access, the last mile remains TypeScript territory.

RustScript does not compromise the ecosystem's Rust identity. It **validates** it.
Every primitive in RustScript is a controlled experiment proving that Rust's constraints
are correct and necessary — because when you remove the compiler and enforce them at
runtime, the same bugs that Rust prevents at compile time surface as runtime errors.
The library is evidence for pure Rust, not a bridge away from it.

---

## Why RustScript, Not TypeScript

TypeScript is a type system over JavaScript. It provides structural typing, generics,
and compile-time checks for shape conformance. What it does not provide:

| Constraint | Rust | TypeScript | RustScript |
|-----------|------|-----------|------------|
| **Ownership** | Compile-time move semantics, use-after-move is a compiler error | No concept — all values are references, shared freely | `Owned<T>`: runtime affine types, `UseAfterMoveError` on access after `transfer()` |
| **Borrowing** | `&T` / `&mut T`, borrow checker enforces exclusivity at compile time | No concept — any reference can mutate anything | `RefCell<T>`: runtime borrow checker, N immutable OR 1 mutable, RAII via `using` |
| **Error handling** | `Result<T, E>` forces handling both paths, `?` operator for propagation | `try/catch` with untyped exceptions, or `T \| undefined` that can be silently ignored | `Result<T, E>`: discriminated union, `unwrap()` panics on `Err`, `match()` for exhaustive handling |
| **Null safety** | `Option<T>` — no null, explicit `Some`/`None`, pattern matching | `T \| null \| undefined` — triple-nullable, easy to forget | `Option<T>`: `Some(v)` / `None`, `fromNullable()` bridges JS nulls into safe access |
| **Exhaustive matching** | `match` is exhaustive — compiler errors on missing variants | `switch` has no exhaustiveness guarantee without workarounds | `exhaustive()`: TypeScript's `never` type as runtime assertion — unmatched variants throw |
| **Clone-on-write** | `Cow<'a, T>` — defer cloning until mutation needed | No concept — everything is reference-shared or manually spread | `Cow<T>`: lazy cloning, `mutate()` clones only on first write |
| **Iterators** | Zero-cost lazy iterators, `map`/`filter`/`fold` chains fuse at compile time | Eager `Array.map()` allocates intermediate arrays on every step | `Iter<T>`: lazy pull-based iterators, composable without intermediate allocation |
| **Bounded collections** | `Vec<T>` with `get()` returning `Option<T>`, panic on out-of-bounds index | Arrays silently return `undefined` on out-of-bounds access | `RustVec<T>`: `get()` returns `Option<T>`, `push()`/`pop()` with `Result` semantics |
| **Channels** | `mpsc::channel` — ownership-transferring message passing | No built-in — `EventEmitter` or manual queues with no ownership semantics | `channel<T>()`: `Sender`/`Receiver` with `Owned<T>` transfer, bounded/unbounded variants |
| **Newtypes** | `struct Meters(f64)` — zero-cost type distinction via newtype pattern | Type aliases (`type Meters = number`) offer zero runtime safety | Branded newtypes via `TryFrom` pattern — `entityId()`, `parseHexColor()` with validation |

The table reveals the pattern: TypeScript provides structural safety (shape). Rust
provides semantic safety (behavior). RustScript brings Rust's semantic safety to
TypeScript's structural environment.

---

## How RustScript Differs from TypeScript

### TypeScript: Correct Shapes

```typescript
interface Project {
  name: string;
  layers: Layer[];
}

function save(project: Project): void {
  // TypeScript guarantees `project` has `name` and `layers`
  // But it cannot prevent:
  //   - saving a project that's already been "consumed" by another operation
  //   - two concurrent saves mutating the same project
  //   - silently ignoring a save failure
  //   - accessing layers[99] on a 3-layer project
}
```

### RustScript: Correct Behavior

```typescript
function save(project: Owned<Project>): Result<void, SaveError> {
  // Owned<Project> guarantees this is the ONLY reference
  // Result<void, SaveError> forces the caller to handle failure
  // After this function, the caller's reference is invalidated

  const data = consume(project);  // project is now moved — caller can't use it
  const result = writeToStore(data);
  return isOk(result) ? Ok(undefined) : Err(result.error);
}

// Caller:
const proj = Owned.of(myProject);
const saved = save(proj);
// proj.value → throws UseAfterMoveError (moved into save)
// saved must be matched — cannot silently ignore
```

### The Difference Is Semantic

TypeScript answers: "Does this value have the right shape?"
RustScript answers: "Is this value being used correctly?"

The first prevents `project.naem` (typo). The second prevents
"I saved a project that another handler was still reading."

---

## Architecture — Where RustScript Fits

```
┌─────────────────────────────────────────────────┐
│                  Browser (last mile)             │
│                                                  │
│  footPrint / tideGlass / future compositions     │
│  ┌──────────────────────────────────────────┐    │
│  │           RustScript Layer               │    │
│  │  Result, Option, Owned, RefCell, Iter,   │    │
│  │  RustVec, Cow, channel, newtypes         │    │
│  └──────────────────────────────────────────┘    │
│  ┌──────────────────────────────────────────┐    │
│  │     Application Code (TypeScript)        │    │
│  │  Leaflet maps, CAD tools, data viz       │    │
│  └──────────────────────────────────────────┘    │
│                      │                           │
│              drawbridge (weak bonds)             │
│         /ext/nominatim, /ext/fema, etc.          │
└──────────────────────┬───────────────────────────┘
                       │ HTTPS (Caddy TLS termination)
┌──────────────────────┴───────────────────────────┐
│              Sovereign Infrastructure             │
│                                                   │
│  petalTongue (Rust) — UI rendering, SSR           │
│  nestGate (Rust) — content-addressed storage      │
│  bearDog (Rust) — TLS, FIDO2, entropy             │
│  songBird (Rust) — mesh federation                │
│  biomeOS (Rust) — orchestration, Neural API       │
│  loamSpine (Rust) — provenance ledger             │
│                                                   │
│  100% pure Rust. No TypeScript. No Node.js.       │
└───────────────────────────────────────────────────┘
```

The boundary is the browser. Everything below the browser is Rust. The browser
itself runs RustScript-hardened TypeScript. The drawbridge weak bonds cross the
boundary — Caddy terminates TLS upstream, the client only sees same-origin
requests. Data flows: outer membrane (NCBI, PubChem, FEMA, USGS) → drawbridge
→ nestGate CAS → compositions → browser (RustScript).

---

## RustScript as Evidence for Pure Rust

The conventional argument for multi-language systems is "use the right tool for the
job." RustScript inverts this: it demonstrates that Rust's constraints are so
universally correct that even in a language without them (TypeScript), you end up
reimplementing them from first principles.

Every RustScript primitive is a controlled experiment:

- **Owned<T>**: Without Rust's borrow checker, you need `UseAfterMoveError` at runtime.
  This proves the borrow checker prevents real bugs, not theoretical ones.

- **RefCell<T>**: Without Rust's compile-time exclusivity, you need a runtime lock counter.
  This proves `&mut T` exclusivity is necessary, not restrictive.

- **Result<T, E>**: Without Rust's `?` operator and exhaustive matching, you need
  discriminated unions and explicit unwrap-or-match patterns. This proves
  `try/catch` is insufficient for composable error handling.

- **Iter<T>**: Without Rust's zero-cost abstractions, you need manual lazy evaluation.
  This proves eager `Array.map()` chains are wasteful, not idiomatic.

The RustScript library validates the ecosystem's pure Rust choice. It does not
contradict it. The goal remains: as WASM matures, petalTongue renders the UI in
Rust, and RustScript becomes a fossil record of the constraints it taught us.

---

## Absorption Path

RustScript is portable. It has zero dependencies and no framework coupling. The
absorption path:

1. **Current**: Lives in `protists/footPrint/src/rustscript/`. Used by footPrint's
   core entity system, agent bridge, and data pipelines.

2. **Near-term**: Extract to a standalone npm package (`@protoKarya/rustscript`).
   Any composition needing frontend safety primitives imports it directly.

3. **Medium-term**: petalTongue's TypeScript rendering layer (if needed before
   full WASM) imports RustScript for UI state management safety.

4. **Long-term**: petalTongue renders via WASM (Rust compiled to browser). RustScript
   fossilizes — its constraints are now enforced at compile time by Rust itself.
   The library becomes a teaching artifact and historical record.

---

## Primitives Inventory

### Phase 1 — Safety

| Primitive | Rust Equivalent | File | Purpose |
|-----------|----------------|------|---------|
| `Result<T, E>` | `std::result::Result` | `result.ts` | Explicit error handling, no silent ignoring |
| `Option<T>` | `std::option::Option` | `option.ts` | Null elimination, explicit absence |
| `RefCell<T>` | `std::cell::RefCell` | `refcell.ts` | Runtime borrow checker (N shared OR 1 exclusive) |
| `exhaustive()` | `match` exhaustiveness | `exhaustive.ts` | Compile-time + runtime variant coverage |
| `Brand<T>` | newtype pattern | `newtype.ts` | Type-safe identifiers with validation |

### Phase 2 — Composition

| Primitive | Rust Equivalent | File | Purpose |
|-----------|----------------|------|---------|
| `Owned<T>` | Move semantics | `owned.ts` | Affine types, use-after-move detection |
| `Iter<T>` | `Iterator` trait | `iter.ts` | Lazy, composable data pipelines |
| `RustVec<T>` | `Vec<T>` | `vec.ts` | Bounds-checked, Option-returning collection |
| `Cow<T>` | `Cow<'a, T>` | `cow.ts` | Clone-on-write smart pointer |
| `channel<T>()` | `mpsc::channel` | `channel.ts` | Ownership-transferring message passing |

Each primitive encodes exactly **one** Rust constraint. Composability emerges from
their interaction — the same design philosophy as the primals themselves.

---

## Relationship to the Ecosystem

| Ecosystem Layer | Technology | RustScript Role |
|----------------|-----------|----------------|
| **Primals** | Pure Rust | None — Rust's compiler is the safety system |
| **biomeOS Neural API** | Pure Rust (JSON-RPC) | None — IPC, no browser |
| **petalTongue** | Rust (Axum + SSR) | Future: may import for TS rendering layer |
| **Live compositions** | TypeScript + RustScript | **Primary consumer** — safety bridge |
| **drawbridge bonds** | Caddy reverse proxy | Outer membrane data flows through RustScript-hardened client code |
| **sporePrint** | Zola (Rust static site gen) | None — pure HTML/CSS output |

RustScript exists at exactly one seam: the browser/server boundary. It never
touches the backend. It never replaces a primal. It makes the last mile behave
as if it were Rust, until the last mile actually becomes Rust.

---

*RustScript validates the ecosystem's pure Rust thesis by proving that Rust's safety
constraints are universally correct — even when you must reimplement them in another
language. Each primitive is a controlled experiment. The evidence says: Rust is right.
The frontier is the browser. And the frontier is shrinking.*
