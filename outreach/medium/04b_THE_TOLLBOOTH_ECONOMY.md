# The Tollbooth Economy

*How "as a Service" became the linguistic signature of enclosure*

**By**: attsi | ecoPrimal
**Status**: Draft — evolving document
**Published**: [pending]
**Series**: Companion to "While They Were Writing Manifestos"

---

In 2016, the World Economic Forum released a video. Sleek. Optimistic. Brief.
A smiling face with a caption: "You'll own nothing and you'll be happy."

The promise was a future where you rent everything — your home, your car,
your tools, your compute — from platforms that own it all. The ownership
disappears. The access persists. The smile stays on.

I watched it. I was furious. Not at the prediction — at the architecture it
described.

---

## The River Keeper

There is a pattern that recurs across human history. Someone finds a river.
The river feeds a valley. The valley becomes a settlement. Someone builds
a tollbooth on the river.

The river keeper does not create the water. He controls the access to it.
He stands between the water and the people who need it, and he charges for
passage. The charge is small — "affordable" — and the alternative is thirst.
So the city pays. Every day. Every cup. Every field irrigated, every child
bathed, every pot of soup. The tollbooth is invisible in any single
transaction. It is totalizing across all of them.

The resource changes. The pattern does not.

The priestly class stood between people and the divine. The feudal lord stood
between people and the land. The colonial company stood between the colony
and the market. The industrial trust stood between people and the ore.

In every case:

1. A resource exists independent of the mediator
2. The mediator positions himself between people and the resource
3. The mediation extracts value proportional to the dependency it creates
4. The dependency is maintained by making alternatives appear impossible

The WEF's prediction was not a vision of the future. It was a description of
the tollbooth, refined to its purest form: *We will own the water. You will
rent it. You will be happy because the alternative is thirst.*

---

## "As a Service"

Software as a Service. Compute as a Service. Storage as a Service.
Intelligence as a Service. Platform as a Service. Infrastructure as a
Service.

The "as a Service" suffix is the linguistic signature of the tollbooth. It
means: someone else owns it, and you pay to cross.

Cloud computing did not invent linear algebra. NVIDIA did not invent matrix
multiplication. Elsevier did not write the papers. Spotify did not compose
the music. Uber did not build the roads.

The platform sits at the chokepoint between the creator and the consumer,
and it extracts rent for occupying the position. The mathematics existed
before the cloud. The GPU instruction sets are hardware — physical
structures etched in silicon — that the vendor *describes* in an SDK but did
not *create* in the mathematical sense. The papers were written by scientists
funded by public grants. The music was composed by artists in bedrooms and
studios. The roads were built by governments with tax revenue.

The tollbooth captures value that other people created. And it does so by
controlling access — by making itself the only route between the source and
the need.

---

## The CUDA Tollbooth

Here is a concrete example.

NVIDIA makes GPUs. Consumer GPUs — the ones in gaming PCs — have silicon
that can do double-precision (f64) floating-point math at roughly half the
speed of single-precision (f32). The silicon is physically there. The
transistors exist.

CUDA, NVIDIA's proprietary programming toolkit, artificially throttles
consumer GPU f64 performance to 1/64th of f32. This is not a hardware
limitation. It is a software restriction. The full f64 throughput is
reserved for datacenter cards that cost 10-40x more.

The math is in the silicon. The restriction is in the software. The
tollbooth is the driver.

Vulkan — an open graphics API — exposes the `VK_KHR_shader_float64`
extension on these same consumer cards. Through Vulkan, the silicon does
what it was built to do. The $300 gaming card runs the same math as the
$10,000 datacenter card. Slower, but at the same precision.

We build our GPU compute pipeline (barraCuda + coralReef) on Vulkan. Not
because we prefer Vulkan's API. Because Vulkan doesn't have the tollbooth.
The same WGSL shaders run on NVIDIA, AMD, Intel, and Apple silicon. The
math is the same. The vendor is irrelevant.

NVIDIA's annual revenue from datacenter GPUs is approximately $47 billion.
A significant fraction of that revenue depends on the tollbooth — on the
artificial restriction that makes consumer silicon insufficient for
professional work. Remove the restriction, and the $300 card is a science
chip. The tollbooth is what makes it "just" a gaming card.

---

## The Institutional Tollbooth

The same pattern applies to scientific computing.

A university researcher who needs GPU compute submits an allocation proposal.
The proposal goes to a committee. The committee evaluates it. Weeks pass.
If approved, the researcher gets access to an HPC cluster — shared with
hundreds of other researchers, queue-managed, scratch-purged every 30 days.

The compute exists. The silicon is there. But between the researcher and the
compute is a tollbooth made of institutional process: proposals, committees,
queues, allocations, quotas.

Cloud computing offers an alternative: pay per GPU-hour. No committee. No
queue. Just a credit card. But the meter runs. A serious bioinformatics
workload — large metagenomics assembly, molecular dynamics, Monte Carlo
simulation — can consume thousands of dollars in a week. The tollbooth is
the bill.

The alternative to both tollbooths is physical ownership. A $700 used RTX
3090 with 24 GB of VRAM, installed in a tower that you own, running
software that you control. No proposal. No queue. No bill. The compute
exists in your room and answers to you.

This is what sovereignty looks like at the hardware level. It's not
glamorous. It's a used GPU in a tower in a basement. But it's yours. And
the tollbooth is absent.

---

## The Manifesto's Tollbooth

Palantir's manifesto says technology should serve "national purpose." It
says Silicon Valley has a "moral debt." It says the government and the
technology industry must rebuild their partnership.

This is the language of a new tollbooth.

"Technology must serve national purpose" means: someone defines the
national purpose, and technology is directed by that definition. Who
defines it? The manifesto's authors — a $70 billion defense contractor
— would like to be part of that conversation. In fact, they would like to
sell the platform on which that conversation happens. Their products are
literally the software that militaries and intelligence agencies use to
define priorities and allocate resources.

"National service should be a universal duty" means: everyone must pass
through the tollbooth. The duty is defined by the same institutions that
define the national purpose. The people who build the toll infrastructure
also define who must pay the toll.

The manifesto is not a philosophy. It is a business proposal. Dress it in
the language of civilization, of duty, of purpose, and it is still a pitch:
*Let us stand between the nation and its security. Let us be the
chokepoint. Let us extract rent for occupying the position.*

---

## The Well

The answer to the river keeper is not a better tollbooth. It is not a
more benevolent keeper. It is not a manifesto about the keeper's
civilizational obligations.

The answer is to give everyone a well.

A well is a direct connection between a person and a resource, with no
mediator. The water comes from the ground beneath their feet. The keeper
is irrelevant. The tollbooth is architecturally impossible because there
is nothing to stand between.

This is what we build.

**Sovereign compute**: your hardware, your silicon, your math. No cloud
meter. No institutional queue. No vendor lock-in. Vulkan instead of CUDA.
WGSL shaders that run on any GPU. Single static Rust binaries with no
runtime dependencies.

**Sovereign provenance**: BLAKE3 content-addressing, DAG tracking,
permanent ledger, Ed25519-signed attribution. The chain is cryptographic.
The verification is mathematical. No platform holds the provenance on
your behalf. You hold it yourself.

**Sovereign science**: 70+ published papers reproduced on consumer
hardware. The data is fetched once and stored locally. The computation
runs on silicon you own. The result is yours. The pipeline is AGPL. Fork
it, modify it, run it. Nobody can turn it off.

The well is not glamorous. It is not a manifesto. It is not a philosophy
of civilization. It is plumbing.

But it is plumbing that makes the tollbooth irrelevant. And that is what
the tollbooth cannot tolerate.

---

## What They Can't Build

The people who build tollbooths cannot build wells. Not because they lack
resources — they have effectively unlimited resources. But because a well
eliminates the condition that justifies the tollbooth.

A defense contractor cannot build peace infrastructure, because peace
eliminates the defense contract.

A cloud provider cannot build sovereign compute infrastructure, because
sovereignty eliminates the metered compute bill.

A platform cannot build protocols that eliminate the platform, because the
protocol eliminates the rent.

A pharmaceutical company cannot cure addiction, because the cure eliminates
the recurring prescription.

This is not conspiracy. It is structure. The incentives of the tollbooth
operator are misaligned with the elimination of the tollbooth. The same
system that allows the Sackler family to profit from manufacturing
addiction also prevents the system from prioritizing the cure. The same
system that allows NVIDIA to throttle consumer silicon also prevents the
system from democratizing compute.

The manifestos are written by tollbooth operators. They will always
propose better tollbooths. They will never propose wells.

---

## Own Nothing, Build Everything

The WEF said you'll own nothing. Here is the orthogonal response:

Own nothing because you published everything to commons.

The code is AGPL. The methods are ORC. The documentation is CC-BY-SA.
Nobody owns it because everyone can use it. The ownership is absent not
because it was taken from you, but because it was never claimed by anyone.

There is no tollbooth on an open well. There is no rent on a public road.
There is no subscription on AGPL software running on hardware you
purchased.

"You'll own nothing and you'll be happy" is one architecture. "Nobody
owns it and everyone can use it" is a different architecture. The first is
enclosure. The second is commons.

We chose the second.

The repos are public. The silicon is sovereign. The math belongs to no one.

---

*Build wells. Not tollbooths.*
