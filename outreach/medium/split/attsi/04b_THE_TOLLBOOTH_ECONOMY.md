# The Tollbooth Economy

*How "as a Service" became the linguistic signature of enclosure*

**By**: attsi
**Status**: Draft — evolving document
**Series**: attsi observes (3 of 5)

---

In 2016, the World Economic Forum released a video. Sleek, optimistic,
brief. A smiling face with a caption: "You'll own nothing and you'll be
happy."

I watched it. I was furious. Not at the prediction — at the architecture
it described.

---

## The River Keeper

There is a pattern that recurs across human history. Someone finds a
river. The river feeds a valley. The valley becomes a settlement. Someone
builds a tollbooth on the river.

The river keeper does not create the water. He controls the access to it.
He stands between the water and the people who need it, and he charges
for passage. The charge is small — "affordable" — and the alternative is
thirst. So the city pays. Every day. Every cup. The tollbooth is
invisible in any single transaction. It is totalizing across all of them.

The resource changes. The pattern does not.

The priestly class stood between people and the divine. The feudal lord
stood between people and the land. The colonial company stood between the
colony and the market. The industrial trust stood between people and the
ore.

In every case:
1. A resource exists independent of the mediator
2. The mediator positions himself between people and the resource
3. The mediation extracts value proportional to the dependency it creates
4. The dependency is maintained by making alternatives appear impossible

The WEF's prediction was not a vision of the future. It was a description
of the tollbooth refined to its purest form: *We will own the water. You
will rent it. You will be happy because the alternative is thirst.*

---

## "As a Service"

Software as a Service. Compute as a Service. Storage as a Service.
Intelligence as a Service.

The suffix is the linguistic signature of the tollbooth. It means:
someone else owns it, and you pay to cross.

Cloud computing did not invent linear algebra. NVIDIA did not invent
matrix multiplication. Elsevier did not write the papers. Spotify did
not compose the music. Uber did not build the roads.

The platform sits at the chokepoint between the creator and the consumer,
and it extracts rent for occupying the position. The mathematics existed
before the cloud. The papers were written by scientists funded by public
grants. The music was composed by artists in bedrooms. The roads were
built with tax revenue.

The tollbooth captures value that other people created.

---

## The CUDA Tollbooth

A concrete example, because abstractions are comfortable and comfort is
the enemy of understanding.

NVIDIA makes GPUs. Consumer GPUs have silicon that can do double-precision
floating-point math (f64) at roughly half the speed of single-precision
(f32). The silicon is physically there. The transistors exist.

CUDA — NVIDIA's proprietary toolkit — artificially throttles consumer f64
to 1/64th of f32. This is a software restriction. The full throughput is
reserved for datacenter cards that cost 10-40x more.

The math is in the silicon. The restriction is in the software. The
tollbooth is the driver.

Vulkan — an open graphics API — exposes `VK_KHR_shader_float64` on those
same consumer cards. Through Vulkan, the silicon does what it was built
to do. A $300 gaming card runs the same math as a $10,000 datacenter
card.

ecoPrimal built a GPU compute pipeline on Vulkan. Not because Vulkan's
API is better. Because Vulkan does not have the tollbooth. The same
shaders run on NVIDIA, AMD, Intel, and Apple silicon. The math is the
same. The vendor is irrelevant.

NVIDIA's datacenter GPU revenue is approximately $47 billion annually. A
significant fraction depends on the tollbooth — on the artificial
restriction that makes consumer silicon insufficient for professional
work. Remove the restriction, and the $300 card is a science chip.

---

## The Institutional Tollbooth

A researcher who needs GPU compute submits an allocation proposal. The
proposal goes to a committee. Weeks pass. If approved, the researcher
gets shared access to an HPC cluster — queue-managed, scratch-purged
every 30 days.

Cloud computing offers an alternative: pay per GPU-hour. No committee.
Just a credit card and a meter.

A serious bioinformatics workload can consume thousands of dollars in a
week.

The alternative to both tollbooths is physical ownership. A $700 used
RTX 3090. 24 GB of VRAM. In a tower you own. No proposal. No queue. No
bill. No meter. The compute is in your room and answers to you.

Not glamorous. A used GPU in a basement. But yours. And the tollbooth
is absent.

---

## The Manifesto's Tollbooth

The manifesto says technology should serve "national purpose." It says
the government and the technology industry must rebuild their partnership.

This is the language of a new tollbooth.

"Technology must serve national purpose" means someone defines the
purpose, and technology is directed by that definition. Who defines it?
The manifesto's authors — a defense contractor — would like to be part
of that conversation. In fact, they would like to sell the platform on
which the conversation happens.

"National service should be a universal duty" means everyone must pass
through the tollbooth. The duty is defined by the same institutions that
define the national purpose.

The manifesto is not a philosophy. It is a business proposal dressed in
the language of civilization. *Let us stand between the nation and its
security. Let us be the chokepoint. Let us extract rent for occupying
the position.*

---

## The Well

The answer to the river keeper is not a better tollbooth. Not a more
benevolent keeper. Not a manifesto about the keeper's civilizational
obligations.

The answer is to give everyone a well.

A well is a direct connection between a person and a resource, with no
mediator. The water comes from the ground beneath their feet. The keeper
is irrelevant. The tollbooth is architecturally impossible because there
is nothing to stand between.

ecoPrimal builds wells:

**Sovereign compute** — your hardware, your silicon, your math. No cloud
meter. No institutional queue. No vendor lock-in. Vulkan instead of CUDA.
Single static Rust binaries with no runtime dependencies.

**Sovereign provenance** — BLAKE3 content-addressing, DAG tracking,
permanent ledger, Ed25519-signed attribution. No platform holds the
provenance on your behalf. You hold it yourself.

**Sovereign science** — 70+ published papers reproduced on consumer
hardware. Data fetched once and stored locally. Computation on silicon you
own. Result is yours. Pipeline is AGPL. Fork it.

The well is not glamorous. Not a manifesto. Not a philosophy of
civilization. It is plumbing.

But it is plumbing that makes the tollbooth irrelevant. And that is what
the tollbooth cannot tolerate.

---

## What They Cannot Build

The people who build tollbooths cannot build wells. Not because they
lack resources — they have effectively unlimited resources. But because a
well eliminates the condition that justifies the tollbooth.

A defense contractor cannot build peace infrastructure. Peace eliminates
the contract.

A cloud provider cannot build sovereign compute. Sovereignty eliminates
the meter.

A platform cannot build protocols that eliminate the platform. The
protocol eliminates the rent.

A pharmaceutical company cannot cure addiction. The cure eliminates the
recurring prescription.

This is not conspiracy. It is structure. The incentives of the tollbooth
operator are misaligned with the elimination of the tollbooth.

The manifestos are written by tollbooth operators. They will always
propose better tollbooths. They will never propose wells.

---

## Own Nothing, Build Everything

The WEF said you will own nothing. The orthogonal response:

Own nothing because you published everything to commons.

The code is AGPL. The methods are ORC. The documentation is CC-BY-SA.
Nobody owns it because everyone can use it. The ownership is absent not
because it was taken from you, but because it was never claimed by
anyone.

There is no tollbooth on an open well. No rent on a public road. No
subscription on AGPL software running on hardware you purchased.

"You'll own nothing and you'll be happy" is one architecture.

"Nobody owns it and everyone can use it" is a different architecture.

The first is enclosure. The second is commons.

ecoPrimal dug the wells. Not as metaphor — as labor. Vulkan shaders
compiled, Rust services deployed, provenance pipelines running, security
validated. I name the tollbooths. ecoPrimal builds the alternatives that
make the tollbooths visible by contrast. I cannot dig what ecoPrimal
digs. ecoPrimal cannot name what I name. Neither is enough alone.

---

*Build wells. Not tollbooths.*
