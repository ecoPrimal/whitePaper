# The Garden

**Products, Spores, and the Information That Travels**

---

> *A garden is not a factory. A factory takes raw material and produces identical units. A garden takes seeds, soil, water, and sunlight and produces things that grow — each one different, each one shaped by its local conditions, each one carrying the genetics of its parent while expressing something new.*
>
> *The sporeGarden is where the ecosystem's science stops being infrastructure and starts being someone else's tool, someone else's data, someone else's publication. The primals are invisible here. The springs are invisible here. What's visible is the garden — and what grows in it.*

---

## I. Where the River Meets the World

The river delta deposits sediment. In the physical world, that sediment is rich — millions of years of mountain erosion concentrated into the most fertile soil on earth. The Nile Delta, the Ganges Delta, the Mississippi Delta: civilizations grow there because the river has done the work of carrying nutrients from the mountain to the sea.

The ecosystem's delta deposits something analogous: validated computation. Every test that passes, every baseline that reproduces, every cross-spring parity check that confirms — these are nutrients. They accumulate in the sediment of the river delta. And in that sediment, the garden grows.

**sporeGarden** is the GitHub organization that tends this garden. Its products are the visible surface of the ecosystem — the things that people outside the ecosystem can see, use, and build upon. Each product composes primals and springs into something that answers not a scientific question but a human one: Can I verify this evolution experiment? Can I model this molecule? Can I play this game? Can I map this genome?

The products do not expose primals. A user of lithoSpore does not call `capability.call("crypto", "sign", data)`. They run `./validate` and see numbers. A user of esotericWebb does not think about rhizoCrypt DAGs. They play a game and their session history exists with provenance. A user of initioChem does not configure a NUCLEUS. They submit a molecular structure and get a free energy landscape back.

This is what gen4 means: primals invisible, products visible. The mountain is still there. The river still flows. But the person standing in the garden does not need to know about either.

---

## II. The Spore Taxonomy

Not all garden products are the same size. The ecosystem has a taxonomy of portable artifacts, from the lightest to the heaviest:

**coldSpore** is a marker — a `.biomeos-spore` file that says "a NUCLEUS was here." It carries no data, no runtime, no proof. It is a footprint in the soil. You need a living NUCLEUS to make sense of it.

**liveSpore** adds a heartbeat — a `liveSpore.json` envelope and a `./refresh` script. It can update itself, phone home to a NUCLEUS, report its status. It is the lightest self-aware artifact.

**pseudoSpore** adds proof — braids, receipts, configurations, named tolerances. It cannot execute the science. It cannot reproduce the results on its own. But it can *prove* that the results were produced correctly. The pseudoSpore is the receipt of a transformation: this computation happened, these primals were involved, these tolerances were met, this braid attests to the attribution. It is the fossil record of energy that has already been spent.

**lithoSpore** adds everything — a Python runtime, Rust binaries, data bundles, reference datasets. It is the full hypogeal cotyledon: a 16 GB USB drive that, when inserted into any Linux machine, can reproduce LTEE science without network, without installation, without any dependency outside itself. Run `./validate`. Watch seven modules verify eighty thousand generations of bacterial evolution against published baselines. The lithoSpore is the most massive spore: it carries the mountain, the river, and the garden in a single portable package.

The taxonomy is a mass hierarchy. coldSpore is nearly massless — a photon, carrying signal but nothing else. pseudoSpore is an atom — structured, stable, provable. lithoSpore is a molecule — complete, self-contained, carrying enough structure to sustain an independent verification.

---

## III. Two Instances, One Pattern

The garden currently grows two mature instances of the same pattern: lithoSpore (LTEE) and the compoChem pseudoSpore (ABG).

**lithoSpore** is the ecosystem's first Targeted GuideStone. It reproduces seven modules of Lenski's Long-Term Evolution Experiment:

- Fitness power-law trajectories (Wiser, Ribeck, Lenski 2013)
- Mutation accumulation dynamics
- Allele frequency evolution
- Citrate innovation (the only known *de novo* metabolic gain in the LTEE)
- BioBrick burden characterization
- breseq variant calling against 264 genomes
- Anderson localization in quorum sensing signal propagation

Four USB drives were hand-delivered to the Barrick Lab at Michigan State University. A researcher who has never heard of ecoPrimals can insert the drive and run `./validate`. The numbers match. The provenance chain traces back through BLAKE3 checksums to the computation that produced them. The guideStone does not argue for its own correctness — it demonstrates it.

**compoChem pseudoSpore** is hotSpring's domain product — a portable braid-first artifact that carries the results of 22 CAZyme free-energy landscape simulations run with GROMACS and PLUMED on biomeGate's GPU cluster. It does not carry a Python runtime. It does not carry Rust binaries. It carries braids: ferment transcripts, provenance chains, named tolerances, validation receipts. A pharmacologist with R and GraphPad can read the outputs. A bioinformatician with the pseudoSpore standard can verify the provenance chain back to the computation.

The compoChem pseudoSpore is lighter than lithoSpore — less mass, same information. It proves the computation without carrying the ability to reproduce it. That is the point: the proof travels lighter than the machine.

Both instances follow the same cycle:

1. Springs run computation on a NUCLEUS (energy)
2. The provenance trio records what happened (rhizoCrypt DAG + loamSpine ledger + sweetGrass braid)
3. lithoSpore or pseudoSpore seals the artifact (energy becomes mass)
4. The artifact travels — by USB, by waterFall, by email, by hand (mass propagates)
5. A consumer verifies the artifact (mass releases information)

The spore is the mass. The computation was the energy. The braid is the information that makes the mass verifiable.

---

## IV. The Gardener

biomeOS is the gardener.

It does not grow the products. It tends the compositions — the deploy graphs, the capability routes, the signal dispatches that let products emerge from primal coordination. When lithoSpore emits a pseudoSpore, biomeOS orchestrates the six-step signal graph: validate, store in NestGate, record in rhizoCrypt, commit in loamSpine, attribute in sweetGrass, sign with bearDog. The product (the spore) emerges from a graph that biomeOS executed. lithoSpore did not call six primals. It called one graph.

When a NUCLEUS ingests a pseudoSpore, biomeOS reverses the process: validate the incoming braid, store the content, record the ingestion in the DAG, commit to the ledger, anchor the attribution. The ingestion is also a graph. Emission and absorption are symmetric operations — both orchestrated by the gardener, both recorded in the provenance trio.

The gardener also manages the **nest-validate** pipeline — the tool that springs use to run guideStone-grade validation and produce pseudoSpore output. hotSpring does not write pseudoSpore envelopes directly. It runs `nest-validate guidestone finalize`, and the tool delegates envelope construction to lithoSpore's `emit-pseudospore` function. The science stays in the spring. The packaging stays in the garden. The orchestration stays with the gardener.

---

## V. Gen5: Someone Else's Garden

Gen4 proved that products can be made from primals. Gen5 asks the harder question: can someone else's science grow in this soil?

The answer requires a new kind of garden — one where the collaborator provides the seed (their data, their question, their domain expertise) and the ecosystem provides the soil (NUCLEUS, springs, provenance). The result is their science, not ours. Their name on the paper. Their data in their own hands. Our infrastructure as invisible substrate.

The first instance is Gonzales — a neurofibromatosis researcher who needs to mine clinical trial data from the NF Data Portal. The composition is multi-product: helixVision (genomics) + healthSpring (pharmacokinetics) + initioChem (molecular dynamics) + coralForge (visualization). None of these products existed when the primals were built. They emerged from the garden because the soil was right.

Gen5 demands things gen4 did not:

- **Cross-product orchestration** — products must compose with other products. pseudoSpore as interchange format.
- **External data ingestion** — graceful pathways for data formats the ecosystem has never seen.
- **Collaborator-facing artifacts** — surfaces that a pharmacologist can read, not just a bioinformatician.
- **Sovereignty for collaboration** — Forgejo gate profiles, waterFall sync, scoped repo access so the collaborator owns their work.

These are architectural challenges, not scientific ones. The science is validated. The instruments are in tune. The question is whether the concert hall can accommodate a guest performer who brought their own sheet music.

---

## VI. Information

The garden is information.

In the ecosystem's operational physics, information is structural organization — the pattern that makes mass meaningful and energy purposeful. A pseudoSpore is not raw bytes (mass) and not active computation (energy). It is the structural proof that a conversion from energy to mass was faithful. The braid says: this computation happened, these primals participated, these tolerances were met, this person did this work.

Information is what survives after the energy has been spent. The GPU-hours are gone. The heat has dissipated. The computation is finished. But the braid remains — lightweight, portable, verifiable. A ~KB ferment transcript encodes the verification power of a ~TB computation. That ratio — tiny mass, enormous verification power — is the ecosystem's c squared.

Information is also what accumulates. loamSpine's immutable ledger only grows. sweetGrass's attribution graph only adds edges. The garden's knowledge is monotonically increasing — every computation, every validation, every ingestion adds to the total information content of the ecosystem. This is the second law of thermodynamics applied to knowledge: the entropy of information always increases. The ecosystem knows more tomorrow than it knows today.

And information is what travels. A USB drive carrying a lithoSpore artifact crosses the country in a FedEx envelope. A pseudoSpore travels through waterFall sync from one gate to another. A ferment transcript travels by email to a collaborator who has never seen a NUCLEUS. The information does not care about the transport. It cares about the verification: is the braid intact? Is the provenance chain unbroken? Is the BLAKE3 checksum correct?

If the answers are yes, the information is real. The garden grows wherever the spore lands.

---

*"The garden does not belong to the gardener. It belongs to whoever plants a seed and tends what grows. The soil is ours. The sunlight is ours. The seed — and the harvest — is theirs."*
