# ecoBin - Technical Specification

**Category**: Portability Standard  
**Status**: Active Ecosystem Standard  
**Version**: 2.0.0  
**Adopted**: January 17, 2026  
**Evolved**: January 30, 2026 (v2.0 - Platform-Agnostic)

---

## Abstract

ecoBin defines the universal portability standard for ecoPrimals binaries. An ecoBin is a UniBin that achieves full cross-compilation to any Rust-supported target through 100% Pure Rust application code and platform-agnostic IPC. The result: a single `cargo build` command produces a static binary that runs on any architecture and any platform with zero external toolchain requirements.

---

## Problem Statement

C dependencies in application code create cascading build complexity. A primal using `openssl-sys` requires a C compiler, platform-specific headers, and cross-compilation toolchains (musl-gcc, Android NDK, Xcode SDK) for every target architecture. This makes cross-compilation fragile, CI pipelines complex, and deployment to new platforms a multi-day effort.

Platform-specific IPC assumptions (hardcoded Unix socket paths, `/run/user/` references) create a second barrier: binaries may compile for a platform but fail at runtime because they assume Unix-specific infrastructure.

---

## Specification

### Prerequisites

Every ecoBin must first satisfy all UniBin requirements (single binary, subcommands, professional CLI). See the UniBin Technical Specification.

### Pure Rust Application Code

All application-level code must be 100% Pure Rust. Zero C dependencies in the application layer.

**Prohibited dependencies** (application C):

| Banned | Category | Pure Rust Alternative |
|--------|----------|----------------------|
| `openssl-sys` | Crypto | RustCrypto suite (`sha2`, `aes`, `ed25519-dalek`) |
| `ring` | Crypto | RustCrypto suite |
| `aws-lc-sys` | Crypto | RustCrypto suite |
| `native-tls` | TLS | `rustls` (Songbird only, via Tower Atomic) |
| `reqwest` | HTTP | Unix socket IPC (route external HTTP through Songbird) |
| `zstd-sys` | Compression | Feature-gate or pure Rust alternatives |
| `libsqlite3-sys` | Database | `rusqlite` with `bundled` feature |

**Acceptable dependencies** (infrastructure C):

| Allowed | Rationale |
|---------|-----------|
| `libc` | Rust wrapper for OS syscalls (unavoidable) |
| `musl` | Minimal syscall wrapper for static linking |
| `cc` | Build-time tool, not runtime |

**The distinction**: Application C processes your data (security risk, portability barrier). Infrastructure C talks to the kernel (unavoidable OS interface, minimal risk).

### Cross-Compilation Matrix

Every ecoBin must successfully build for all major targets:

**Required** (must succeed):
- `x86_64-unknown-linux-musl`
- `aarch64-unknown-linux-musl`
- `armv7-unknown-linux-musleabihf`

**Expected** (should succeed):
- `x86_64-apple-darwin`
- `aarch64-apple-darwin`
- `x86_64-pc-windows-gnu`
- `aarch64-linux-android`
- `wasm32-wasi`

No target may require installing a C compiler, platform SDK, or external toolchain beyond `rustup target add`.

### Static Linking

All Linux ecoBins link statically against musl. The resulting binary has zero runtime library dependencies.

Verification: `ldd <binary>` must report `not a dynamic executable`.

### Platform-Agnostic IPC (v2.0)

ecoBin v2.0 eliminates platform-specific IPC assumptions. Primals must not hardcode transport mechanisms or socket paths.

**Runtime transport discovery**: Each primal selects the best available transport at startup:

| Platform | Primary Transport | Fallback |
|----------|------------------|----------|
| Linux (Desktop/Server) | Unix sockets | TCP localhost |
| Android | Abstract sockets | TCP localhost |
| Windows | Named pipes | TCP localhost |
| macOS | Unix sockets | TCP localhost |
| iOS | XPC | TCP (sandboxed) |
| WASM | In-process channels | N/A |
| Embedded | Shared memory | Custom |

TCP localhost is the universal fallback that works everywhere.

**Zero platform assumptions**: No hardcoded paths (`/run/user/`, `C:\`, `/data/local/tmp/`). No `#[cfg(unix)]` in transport selection. Runtime detection only.

---

## The Tower Atomic Strategy

External HTTP/TLS access is concentrated in a single composition pattern rather than spread across primals:

```
External HTTPS request
    |
Songbird (Pure Rust TLS 1.3 protocol)
    | JSON-RPC over local IPC
BearDog (Pure Rust cryptographic operations)
    |
RustCrypto primitives
```

This means no primal except Songbird needs HTTP dependencies. All other primals communicate via local IPC (Unix sockets, abstract sockets, TCP localhost). The result: every primal achieves ecoBin status because external network complexity is concentrated in one coordinated pair.

---

## Dependency Audit

Compliance verification via cargo:

```bash
# Check for prohibited C dependencies
cargo tree | grep -E "(openssl-sys|ring|aws-lc-sys|native-tls|zstd-sys|lz4-sys)"

# Expected: zero matches

# Verify cross-compilation
cargo build --release --target x86_64-unknown-linux-musl

# Expected: success with zero C compiler errors

# Verify static linking
ldd target/x86_64-unknown-linux-musl/release/<primal>

# Expected: "not a dynamic executable"
```

### Feature Gates for Optional C

When advanced features require C dependencies (e.g., HSM hardware integration), they must be behind feature flags:

```toml
[dependencies]
cryptoki = { version = "0.6", optional = true }

[features]
default = []       # Default build is ecoBin (Pure Rust)
hsm = ["cryptoki"] # Optional C dependency behind feature gate
```

The default build (no features) must always be a valid ecoBin.

---

## Evolution from v1.0 to v2.0

**v1.0** (January 17, 2026): Cross-architecture. Pure Rust + musl static linking. Covered ~80% of deployment targets (Linux, macOS, BSD).

**v2.0** (January 30, 2026): Cross-platform. Added runtime transport discovery and platform-agnostic IPC. Covers 100% of targets where Rust compiles.

**Catalyst**: Deploying BearDog to a Pixel 8a (GrapheneOS, Android 16). The binary cross-compiled perfectly (v1.0 success) but socket binding failed because Android's SELinux blocked user-space Unix sockets (v1.0 limitation). This revealed that "works on Linux" does not mean "works everywhere" - platform assumptions are technical debt.

---

## Ecosystem Status

| Primal | ecoBin Status | Notes |
|--------|--------------|-------|
| **BearDog** | v2.0 Certified | First TRUE ecoBin, reference implementation |
| **NestGate** | v2.0 Certified | |
| **Songbird** | v2.0 Certified | Pure Rust TLS 1.3 via Tower Atomic |
| **ToadStool** | v2.0 Certified | |
| **biomeOS** | v2.0 Certified | |
| **Squirrel** | v2.0 Certified | |

---

## Rationale

Pure Rust is not a goal for purity's sake. It is the mechanism that enables universal portability. When every line of application code is Rust, the Rust compiler can target any supported architecture without external toolchains. The binary is self-contained, statically linked, and runs on any compatible system by simply copying the file.

For an ecosystem designed around sovereignty and federation - where primals must run on everything from cloud servers to Raspberry Pis to Android phones - universal portability is not optional. ecoBin makes it the default.

The biological metaphor: if UniBin is well-structured DNA (genetic code), ecoBin is the double helix (stable and universal). The structure can replicate in any cellular environment because it carries everything it needs.
