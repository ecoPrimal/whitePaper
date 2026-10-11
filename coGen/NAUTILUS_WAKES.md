# coGen 34 — Nautilus Wakes

**Wave**: 173a | **Date**: October 11, 2026

---

## The Third Tense

For thirty-three entries, `will_be = 0`.

Every dashboard flush wrote three numbers: IS (90.4%), WAS (7.2%), WILL-BE (0%).
Two tenses and a placeholder. A clock with two hands and a missing third.
A membrane that could see where things are and where they were, but not
where they're going. The peptidoglycan layer — the structural prediction
layer between scatter and services — was described, diagrammed, named,
and empty.

Now:

```
IS:      107,772  (90.4%)
WAS:       8,589  (7.2%)
WILL-BE:   2,858  (2.4%)
```

2,858 entities have predicted trajectories. Nautilus is live.

---

## What Nautilus Does

The prediction is simple because the architecture already did the hard work.

Orbital compression (coGen 30, Wave 173) found that 3,576 multi-host IPs
compress into 933 orbital families — IPs that visit the same set of
subdomains share an orbit. The orbit is a hash of the sorted host set.
IPs with identical orbits are in the same family.

Nautilus asks one question: **is your orbital family populated?**

If your orbit has other members (family_size > 1), your trajectory is
predictable. Not because we know what you'll do — but because others
in your orbit already did it. The orbit has been walked. The next
step is visible.

If your orbit has only you, your trajectory is singular. Unpredictable.
You are the first. You are IS in the trajectory dimension.

---

## The Numbers

**Prediction coverage**: WILL-BE / WAS = 0.333

One third. Exactly one third of returning visitors are in populated orbits.

This is not a parameter we tuned. This is not a threshold we chose. We
counted the IPs, built the families, and the ratio fell at 1/3.

One third of everything that returns is predictable.
Two thirds remain singular — their orbit is theirs alone.

**The boundary shifts**:

| Measure | Before Nautilus | After Nautilus |
|---------|----------------|----------------|
| IS/WAS | 12.5695 (≈ 4π) | 12.5452 (≈ 4π) |
| IS/(WAS+WILL-BE) | — | 9.4136 |
| Permeation P | 7.38% | 9.60% |
| Vision θ | 3.39 rad (194°) | 3.48 rad (199°) |

**Vision gained: 4.8°**

The membrane can see 4.8 degrees further around the sphere. Not more
data — more angular resolution. The prediction doesn't add observations.
It extends the field of view by recognizing that some futures are
already in the past of others.

---

## The Three Layers, All Live

| Layer | Function | Status |
|-------|----------|--------|
| Outer (scatter/bingo) | NP-hard maze, ZK reflection | LIVE since Wave 165 |
| Peptidoglycan (nautilus) | Orbital prediction, will_be | **LIVE — Wave 173a** |
| Inner (services) | Binary auth, SSH/WG/bearer | LIVE since inception |

The gram-negative membrane is complete. All three layers operational.

The outer layer is impermeable and invisible (coGen 33). The inner layer
is binary — you have the key or you don't. Between them, the peptidoglycan
layer now does what peptidoglycan does in biology: it gives the membrane
its shape. It decides what the organism expects. It predicts.

---

## What 1/3 Means

The prediction coverage converges at 1/3 because orbits have a natural
size distribution. Most orbits are singleton (one IP, one unique path).
The populated orbits are the common paths — the desire lines worn into
the landscape by repeated traversal. One third of returners walk
desire lines. Two thirds forge their own.

In the three-body tensor (form × shape × compression):
- Form (IS): the point of first contact → 90.4%
- Shape (WAS): the arc of return → 7.2% total, of which 4.8% are singular
- Compression (WILL-BE): the predicted orbit → 2.4%

The ratio between them is not arbitrary. IS/WAS ≈ 4π. WAS/WILL-BE ≈ 3.
The surface area of the sphere, then the three spatial dimensions.
The membrane keeps finding geometry.

---

## The Walk Continues

coGen 29 described three sweeps:
- Sweep 1 (IS): the point → implemented, always was
- Sweep 2 (WAS): the arc → implemented Wave 173 (trajectory analysis)
- Sweep 3 (WILL-BE): the predicted orbit → **implemented Wave 173a**

Each sweep was supposed to add π of angular resolution. The measured
gain is 4.8° = 0.08 radians. Not π. Why?

Because the prediction is conservative. It only counts IPs in populated
families. A more aggressive prediction — partial orbit matching, subnet
cohort prediction, temporal sequence prediction — would extend the
field of view further. Each refinement of the prediction adds angular
resolution. The first step was the hardest: going from 0 to nonzero.
From "we cannot see forward" to "we can see forward, dimly."

The cornea refracts. The iris apertures. The lens focuses. The retina
absorbs. We just grew the retina.

The next step is to make it predict *what* — not just *that*. Which
host will they visit next? When? That prediction feeds back into the
sort compression, into the grid feedback, into the BingoCube. The
nautilus doesn't just see forward. It shapes what the outer layer
reflects.

---

*The plant at the bottom of the sea (coGen 30) was `will_be = 0`. Gilgamesh
dove for it and it was taken by the snake. We didn't dive. We counted
the orbits. The orbits predicted themselves. Thirty-four entries. The
peptidoglycan layer wakes. The membrane has three tenses. The organism
can remember, observe, and anticipate. That's all a nervous system is.*

— *Artisan · October 11, 2026*
