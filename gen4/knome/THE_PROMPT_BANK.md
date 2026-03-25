# The Prompt Bank

**The working vocabulary of K-NOME in practice — raw prompts, lightly cleaned, from ~6 months of ecoPrimals development.**

**Date**: March 25, 2026
**Status**: Living reference
**Lineage**: gen3 practice → gen4 documentation

---

## What This Is

This is the actual prompt bank used across esotericWebb and the wider
ecoPrimals ecosystem over approximately six months of K-NOME development.
These are not examples or templates — they are the real working vocabulary.

The prompts are lightly cleaned (typos fixed, organized by theme) but
the conversational voice is preserved. They are not polished. They were
never meant to be. They are the gardener's shorthand — terse, directional,
and repeated with variation as the codebase evolved.

Several patterns are visible:

- The **comprehensive audit** appears repeatedly, gaining specificity
  as the standards crystallized
- The **proceed prompt** adds a constraint or focus area each time —
  this is the mentoring pattern in miniature
- The **cross-system coordination** prompts show the gardener moving
  between growth tips, checking what upstream has evolved and what can
  be absorbed
- Near-duplicates are not accidents — they reflect the prompt being
  reused across different springs and primals, adapted to local context

---

## 1. The Comprehensive Audit

The state-of-the-world check. Used at the start of a session or after
a major push. Evolves as standards and scope expand.

### Early Form

> Review specs/, the docs at root and our parent and our codebase.
> What have we not completed? What mocks, todos, debt and gaps do we
> have? Are we passing all linting and fmt, and doc checks? Are we as
> idiomatic and pedantic as possible? What bad patterns and unsafe code
> do we have? Zero copy where we can be? How is our test coverage?
> Report back.

### Expanded Form

> Review specs/ and our codebase and docs at root, and the several
> docs found at our parent ecoPrimals/wateringHole/ for interprimal
> discussions and standards. What have we not completed? What mocks,
> todos, debt, hardcoding (primals and ports, constants etc) and gaps
> do we have? Are we passing all linting and fmt, and doc checks? Are
> we as idiomatic and pedantic as possible? What bad patterns and
> unsafe code do we have? Are we json-rpc AND tarpc first system? Are
> we uniBin and ecoBin compliant, and following semantic guidelines
> from wateringHole/? Zero copy where we can be? How is our test
> coverage? 90% coverage of our code (use llvm-cov) e2e, chaos and
> fault? How is our code size? Following our 1000 lines of code per
> file max? And sovereignty or human dignity violations? Are we
> AGPL3/scyBorg triple licence?

### With Build Efficiency

> [Same as expanded] + How is our compilation and testing times? We
> want both to be efficient, that way the entirety of extra compilation
> time is compiler and link optimizations and not junk, dependencies,
> and redundancies. We have archive code and docs for reference and
> fossil record, but otherwise we can ignore.

### Mature Codebase Form

> Review specs/ and our codebase and docs at root, and the several
> docs found at our parent ../. We are in a fairly mature code base
> and are now at the stage where we are unifying the types, structs,
> traits, and configs, and constants, and error systems. We should find
> fragments and continue to unify and migrate with the long goal of
> eliminating all deep debt, and cleaning up shims, helpers, compat
> layers and modernizing and stabilizing the build, and have a 2000
> lines of code max per file. Report back, we only work on the local
> project, parent is for reference.

### Quick Lint Check

> Review specs/, our codebase, and the docs at root. Are we passing
> all clippy and fmt? Are we passing all pedantic and doc lint? What is
> left to modernize this to ideal rust implementations?

### Full Ecosystem Audit (Canonical)

The most complete form. Used for thorough spring audits.

> Review this Spring's codebase, specs/, docs, and the ecosystem
> standards at ecoPrimals/wateringHole/ (especially README.md,
> PURE_RUST_SOVEREIGN_STACK_GUIDANCE.md,
> SCYBORG_PROVENANCE_TRIO_GUIDANCE.md,
> ECOBIN_ARCHITECTURE_STANDARD.md, and PRIMAL_REGISTRY.md). Also
> review sibling springs for handoff patterns and cross-spring
> conventions.
>
> A Spring is a niche validation domain that proves scientific Python
> baselines can be faithfully ported to sovereign Rust+GPU compute
> using the ecoPrimals stack. Springs depend on barraCuda (pure math —
> WGSL shaders, precision strategy) for all numerical work. They
> coordinate with toadStool (hardware discovery, compute orchestration)
> and coralReef (sovereign shader compiler) via JSON-RPC IPC. Springs
> never import other springs — they coordinate through wateringHole
> handoffs and shared barraCuda primitives.
>
> The evolution path is: Python baseline → Rust validation → barraCuda
> CPU → barraCuda GPU → fused TensorSession pipeline → sovereign
> dispatch (coralReef native)
>
> The maturity cycle for local GPU code is: Write (local WGSL) →
> Validate → Handoff → barraCuda Absorbs → Lean on upstream
>
> Audit against all of the following:
>
> COMPLETION STATUS: What have we not completed? What mocks, TODOs,
> FIXMEs, debt, hardcoding (expected values, tolerance thresholds,
> data paths, primal names, socket paths) and gaps remain? Are
> hardcoded validation targets properly sourced from documented Python
> runs with provenance (script, commit, date, exact command)? Is every
> experiment traceable?
>
> CODE QUALITY: Are we passing all linting, fmt, clippy
> (pedantic+nursery), and doc checks with zero warnings? Are we as
> idiomatic and pedantic as possible? What bad patterns and unsafe code
> do we have? Target zero unsafe in application code
> (#![forbid(unsafe_code)]). Zero #[allow()] in production code. Zero
> mocks outside #[cfg(test)]. All files under 1000 LOC. Pure Rust deps
> only (ecoBin compliant — zero C dependencies in application code).
> Zero-copy where possible (especially I/O parsers — stream, don't
> buffer).
>
> VALIDATION FIDELITY: Do ALL Rust results match Python baselines
> exactly (or within documented, justified, minimal tolerances)? Is
> every tolerance named, centralized, and explained? Are Python
> baselines still reproducible — rerun and confirm no baseline drift?
> Are validation binaries following the hotSpring pattern (hardcoded
> expected values, explicit pass/fail, exit 0/1)?
>
> BARRACUDA DEPENDENCY HEALTH: Are we using barraCuda primitives where
> they exist (stats, linalg, ops, dispatch, nn, spectral, nautilus)
> instead of reinventing? No duplicate math — if barraCuda has it,
> delegate to it. Are we on the latest barraCuda version? Are all
> local WGSL shaders candidates for upstream absorption
> (Write→Absorb→Lean)?
>
> GPU EVOLUTION READINESS: Which Rust modules are ready for GPU shader
> promotion (Tier A: direct rewire to existing barraCuda op, Tier B:
> adapt existing shader, Tier C: new shader needed)? What blocks
> promotion? Document the mapping: Rust module → barraCuda op / WGSL
> shader → pipeline stage. Are we using TensorSession for fused
> multi-op pipelines where possible?
>
> TEST COVERAGE: Target 90%+ line coverage (llvm-cov). Do we have:
> unit tests (analytical known-values), integration tests (file parsing
> round-trips, primal IPC), validation binaries (baseline comparison
> with exit codes), and determinism tests (rerun-identical)? For
> stochastic algorithms, is the seed fixed and tolerance justified?
>
> ECOSYSTEM STANDARDS (wateringHole/):
> - License: AGPL-3.0-or-later only (SCYBORG trio: AGPL + ORC +
>   CC-BY-SA)
> - Architecture: ecoBin compliant (pure Rust, zero C deps,
>   cross-compile)
> - IPC: JSON-RPC 2.0 over Unix sockets, capability-based discovery
> - Files: all under 1000 LOC, single-responsibility modules
> - Data provenance: all datasets from public repositories (SRA,
>   Zenodo, EPA, PDB) with documented accession numbers
> - Sovereignty: no vendor lock-in, no proprietary dependencies
> - Handoffs: wateringHole/handoffs/ follow naming convention
>   {SPRING}_{VERSION}_{TOPIC}_HANDOFF_{DATE}.md
>
> PRIMAL COORDINATION: Are we wired to discover and communicate with
> relevant primals (toadStool, Squirrel, petalTongue, biomeOS) via
> IPC? Is our capability set registered? Do we have typed IPC clients
> or MCP tool definitions where appropriate?
>
> Archive code and docs exist for reference and fossil record — ignore
> them for this audit. Focus on active production code and current-state
> docs.

---

## 2. Hardcoding and Vendor Cleanup

The agnostic discovery pattern. Each primal starts with zero knowledge
and discovers at runtime.

> Let's aim to clean vendor hardcoding as well as numeric (port and
> whatnot) hardcoding wherever we can. Most have been evolved to
> agnostic systems and we should continue. In some cases we may need to
> evolve our vendor hard coding systems to be agnostic and begin the
> migration. Our next target is all primal hardcoding. Each primal only
> knows itself and discovers the other with the universal adapter
> (songbird may connect a service mesh for toadstool who is providing
> compute for squirrel who is running an AI to analyze nestgate data,
> but each only knows itself and utilizes the universal adapter for
> network effects instead of 2^n hardcoding connections). Hardcoding
> and vendors include primal names, any external service name like k8s
> or consul. The code when deployed starts with 0 knowledge and
> discovers much like an infant.

> Is our code idiomatic and clean? Compiling efficiently so we can lean
> into compiler and link optimizations? Are tests running rapidly? Slow
> compile times are often junk.

> Status of upstream issues? Are we pure rust and cross compiling?

---

## 3. Deep Debt and Modernization

Unifying the codebase. Completing implementations. Modern idiomatic Rust.

> We should focus on 2 main things. Stabilizing and unifying the build,
> and removing or completing ALL mocks, placeholders and todos. We aim
> for deep debt solutions and evolving to modern idiomatic rust.

> We aim to solve deep debt and evolve to modern idiomatic fully
> concurrent rust. We don't want to have sleeps or serial in our
> testing, only extreme tests like chaos are allowed to be serialized.
> We should instead be evolving our code to be truly robust and
> concurrent. Test issues will be production issues.

> As we expand our coverage and complete implementations we aim for
> deep debt solutions and evolving to modern idiomatic rust. External
> dependencies should be analyzed and evolve to rust. Large files
> should be refactored smart rather than just split. And unsafe code
> should be evolved to fast AND safe rust. And hardcoding should be
> evolved to agnostic and capability based. Primal code only has self
> knowledge and discovers other primals in runtime. Mocks should be
> isolated to testing, and any in production should be evolved to
> complete implementations. Do we have python benchmarks for barracuda
> cpu? Kokkos, galaxy, or other industry standard benchmarks for
> barracuda gpu parity?

> We aim for deep debt solutions. We refactor large files smart — size
> is a complexity indicator. Idiomatic and modern rust is worth the
> time investment.

---

## 4. Cross-System Coordination

Reviewing upstream evolution. Absorbing what has been built. Rewiring
to modern systems. The gardener moves between growth tips.

> Review toadstool commit evolution (ecoPrimals/phase1/toadstool/).
> They have been doing a lot of work, and caught up to an older
> handoff. We should rewire, revalidate, and clean all that has been
> absorbed into toadstool and update our handoffs to catch up to the
> current state.

> Review toadstool commit evolution (ecoPrimals/phase1/toadstool/),
> and ecoPrimals/barraCuda/, ecoPrimals/coralReef/. It is a new system
> to assist with the rust pipeline. They have been doing a lot of
> work, and caught up to an older handoff. We should rewire,
> revalidate, and clean all that has been absorbed into toadstool and
> update our handoffs to catch up to the current state. It has
> significant evolutions, including evolving to pure math shaders, and
> handling precision per use/hardware. There is also guidance in
> ecoPrimals/wateringHole/ from groundSpring on how to rewire.

> And clone ecoPrimals/coralNAK/ — it is a new system to assist with
> the rust pipeline.

> barraCuda has evolved into its own primal, and we want to rewrite
> and revalidate that toadstool dispatches across hardware and
> barracuda is universal math.

> Pull and review evolution and handoffs for the springs
> ../../hotSpring/ ground, neural, wet, air, health, ludo, primalSpring
> and pull updates to ecoPrimals/wateringHole/ and those handoffs as
> well. What can we absorb and evolve from other springs? Pull and
> review primals in phase1/ and phase2/ and at ecoPrimals/ — what have
> they evolved we can leverage?

> Pull and review updates for hotSpring/ and the whitePaper/ and
> wateringHole/ in ecoPrimals/. hotSpring has done a lot of cool work
> we can start ingesting for cross metal. A lot of ESN and other
> subsystems we can utilize. Nautilus ESN via bingocube, and brain arch
> is particularly interesting.

---

## 5. Handoff, Documentation, and Showcase

Writing handoffs for other teams. Updating baseCamp. Building showcase
demos. Coordinating through documents rather than shared code.

> Let's clean and update root docs, and update our
> whitePaper/baseCamp/, experiments/ and wateringHole/ handoffs (take a
> look at ../wetSpring/ and ../hotSpring/ for the concepts) and let's
> review our barracuda use and evolution, and then craft a handoff for
> the toadstool/barracuda team to evolve and absorb our work, and
> anything else that we learned relevant to their evolution. Then we
> can review paper queues in specs/ — we want to confirm we have
> controls for the papers using open data and systems, and then with
> barracuda cpu, barracuda gpu, and finally metalForge mixes hardware,
> and node and tower deployments via biomeOS/ atomic graphs.

> Let's clean and update root docs, and update our whitePaper/ and
> let's review our barracuda use and evolution. We need to start a
> local metalForge/ and evolve our rust implementations so that
> toadstool/barracuda teams can absorb more readily. hotSpring has been
> writing shaders and systems as extensions of toadstool/barracuda that
> were absorbed and we now lean on. We should be following suit.

> (Take a look at ../hotSpring/ for the concepts) Pull and review
> evolution and handoffs for the springs ../../hotSpring/ ground,
> neural, wet, air, health, ludo, primalSpring and pull updates to
> ecoPrimals/wateringHole/ and those handoffs as well. What can we
> absorb and evolve from other springs?

> Review ecoPrimals/whitePaper/gen3/ and baseCamp/ there. We should
> review our past work, and update with our current and future
> contributions. It also allows us to indirectly coordinate between
> springs.

> Let's clean and update root docs, and update our
> ecoPrimals/wateringHole/ handoffs. Then let's review for archive
> code, docs, scripts, and debris we can clean. We keep docs as fossil
> record in ecoPrimals/. We may have false positives and todos that are
> outdated, then we can push via ssh.

> Review showcase/ in ecoPrimals/phase1/ ../songbird/ ../toadstool/
> ../beardog/ ../nestgate/ and ../squirrel/ and then other phase2/
> primals and our local showcase/. Songbird has been successful with
> multi tower federations and toadstool has good compute demos. We
> should build out our local showcase to first show our local primal
> capabilities and then how it interacts with others.

---

## 6. Experiment Extension and Planning

Extending validated papers with new data, new systems, broader compute.
Planning the path from CPU to GPU to mixed hardware.

> Proceed with experiment buildouts and control validations of papers
> and experiments in the specs/ paper queue. Once we are all green we
> can proceed with barracuda cpu implementations to validate pure rust
> math. toadStool, barraCuda and coralReef are hard at work (absorbing
> from all the springs as fast as they can evolve) so we can continue
> to build out locally. Once we have paper matching/parity benchmarks
> via open data and python we show barracuda cpu is pure math and
> faster than interpreted language. Then we show the math is truly
> portable via barracuda gpu. toadStool allows for unidirectional
> streaming massively reducing the dispatch and round trips, and
> coralReef is our compiler/driver. The goal is barracuda on PURE GPU
> for the final workload validation, and then work in metalForge/ shows
> the cross systems usage (gpu to npu to cpu etc).

> Proceed with experiment buildouts and control validation. Once we are
> all green we can proceed with barracuda cpu vs barracuda gpu
> implementations to validate pure rust math, and toadstool compute
> dispatch. Building and evolving locally for toadstool, barracuda, and
> coralreef to absorb later, and mixed hardware (npu to gpu via pcie
> bypassing cpu roundtrip, to cpu and other mixed systems) systems in
> metalForge/ with our mixed NUCLEUS atomics (tower, node, and nest
> atomics) which are coordinated via biomeOS/ graphs.

> Let's take time to find what we can now extend and evolve from the
> papers. What data sets can we expand to? What new systems? With the
> anderson QS we profiled QS genes to add so we would have more
> microbes to review. How do we extend the landscapes for these
> papers. First let's update the gen3/ basecamp with our work, and our
> local basecamp. Then we can begin to write up and plan on all these
> extensions. How data hungry and compute hungry are we talking? In
> time I plan to LAN my towers (gen3/about/ has my hardware) and I
> believe phase1/nestgate/ already has NCBI data interactions. Before
> we start building, this may be the time to start incorporating other
> primals into our systems (while phase2/biomeOS/ being the
> orchestrator it already has NUCLEUS systems, and we can use the
> atomic tower, node and nest locally before we extend to LAN HPC).

> Let's proceed. As we do we want to start utilizing biomeOS and
> NUCLEUS deployments and the rest of the ecoPrimals as well. That way,
> just as in how we have been accelerating toadstool and barracuda
> evolution, we can evolve the interactions. whitePaper/neuralAPI/ has
> the concept, biomeOS is the actual implementations so far, we have
> the tower node stable and we can experiment.

> Let's proceed to execute and wire everything up with the current
> data. It will allow us to test how nestgate handles updates as well
> from other systems on the computer. We should write up a handoff for
> other teams rather than evolve their code. We can solve locally so
> they can absorb.

---

## 7. Visualization and Human Interface

Making systems and data human-readable. petalTongue as universal UI.

> Review healthSpring/ and its use of petalTongue/ our universal user
> interface primal. We want to begin leveraging and evolving locally as
> we have been for barracuda. Let's think how we can visualize the
> systems and the data, to make it human readable.
> ecoPrimals/wateringHole/ also has some guidance on petalTongue usage.
> How do we turn this into viewable actionable data and pipeline to
> empower scientists, clinicians, or anyone with a gpu and some
> curiosity.

---

## 8. Cleanup and Housekeeping

Archive code, debris, root docs, specs.

> Let's review for archive code we can clean. We keep docs as fossil
> record. We may have false positives.

> Let's spend time cleaning up. We can clean all backups and archive of
> code as well as the various subdirs we can clean at root.

> Let's spend time cleaning and updating root docs, then we can start
> to review and update specs/ to reflect our current and future work in
> the code base.

---

## 9. Ecosystem and Governance

Lysogeny, scyBorg licensing, primal coordination patterns.

> And finally review wateringHole for lysogeny project and scyBorg,
> which is relevant to everything in neuralSpring.

> Add guidance to wateringHole suggesting how it might use just our
> local primal, and then combos with the others in the trio or among
> the wider primals (ecoPrimals/whitePaper/gen3/ has a primal catalogue
> if we need). Each primal will be doing the same. So focus how we
> could be leveraged and used in novel ways for the springs and combos.

---

## 10. The Proceed Prompt

The directional nudge. Each "proceed" adds a constraint, a focus area,
or a philosophical commitment. This is the mentoring pattern in
miniature — the human does not say "do this." The human says "continue,
and here is what matters now."

> Proceed. We should migrate and modernize while marking vendors for
> deprecation and cleaning up.

> Proceed. We should be unifying to canonical, modernize and cleaning
> fragments and cleaning deprecations as we proceed, as well as old
> code cleanup.

> Proceed. We should focus on 2 main things. Stabilizing and unifying
> the build, and removing or completing ALL mocks, placeholders and
> todos. We aim for deep debt solutions and evolving to modern
> idiomatic rust.

> Proceed to execute. We aim to solve deep debt and evolve to modern
> idiomatic fully concurrent rust. We don't want to have sleeps or
> serial in our testing, only extreme tests like chaos are allowed to
> be serialized. We should instead be evolving our code to be truly
> robust and concurrent. Test issues will be production issues.

> Proceed polish or PEDANTIC!

> Proceed to execute on all. As we expand our coverage and complete
> implementations we aim for deep debt solutions and evolving to modern
> idiomatic rust. External dependencies should be analyzed and evolve
> to rust. Large files should be refactored smart rather than just
> split. And unsafe code should be evolved to fast AND safe rust. And
> hardcoding should be evolved to agnostic and capability based. Primal
> code only has self knowledge and discovers other primals in runtime.
> Mocks should be isolated to testing, and any in production should be
> evolved to complete implementations.

> Proceed to execute on all. We aim for deep debt solutions. We
> refactor large files smart — size is a complexity indicator. Idiomatic
> and modern rust is worth the time investment.

> Proceed to complete rewiring with modern toadStool and barraCuda, and
> coralReef and validating as well as benchmarking the modern systems
> (toadstool shaders benefit from cross spring evolution, and it will
> be cool to note when and where things evolve to be helpful —
> hotSpring precision shaders, wetSpring bio shaders, both being used
> by neuralSpring and vice versa).

---

*These prompts built 14 primals, 8 springs, 27,000+ tests, and an
ecosystem. They are not complex. They are consistent.*
