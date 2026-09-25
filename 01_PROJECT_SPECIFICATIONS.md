# 01 — Project Specifications & Structural Engineering

This document establishes the structural parameters, dimensional constraints,
and engineering considerations for the 4.0 m × 3.0 m freestanding timber
pergola.

---

## 1. Dimensional Summary

### 1.1 Plan View Geometry

* **Post-to-Post Spacing (Centre-to-Centre):**
  * Long direction (Beam run): **4000 mm (4.00 m)**
  * Short direction (Rafter run): **3000 mm (3.00 m)**
  * Diagonal (Corner-to-Corner check): **5000 mm (5.00 m)** *(Exact 3-4-5 right triangle)*
* **Post Outside-to-Outside Dimensions:**
  * Long dimension: 4000 mm + 150 mm = **4150 mm**
  * Short dimension: 3000 mm + 150 mm = **3150 mm**
* **Usable Interior Clearance (Inside Face to Inside Face of Posts):**
  * Long opening: 4000 mm − 150 mm = **3850 mm**
  * Short opening: 3000 mm − 150 mm = **2850 mm**
* **Cantilever Overhangs:**
  * Beams: **300 mm** overhang beyond post centre on each end
  * Rafters: **300 mm** overhang beyond beam centreline on each end
* **Overall Roof Footprint:**
  * Length: 4000 mm + (2 × 300 mm) = **4600 mm**
  * Width: 3000 mm + (2 × 300 mm) = **3600 mm**
  * Covered area: 4.6 m × 3.6 m = **16.56 m²**

---

## 2. Vertical Elevations & Height Budget

Every vertical elevation is calibrated from the **finished patio paver level (0 mm datum)**:

| Component | Elevation / Dimension | Cumulative Top Elevation |
| :--- | :--- | :--- |
| **Finished Patio Level** | **Datum (0 mm)** | 0 mm |
| **Standoff Post Base Clearance** | +35 mm air gap | +35 mm |
| **Clearance Under Main Beams** | **2200 mm (~7 ft 2.5 in)** | **+2200 mm** *(Headroom)* |
| **Post Shoulder Cut Height** | Timber height: 2200 − 35 = 2165 mm | +2200 mm |
| **Main Support Beams (47×225 mm)** | Depth: 225 mm | +2425 mm |
| **Post Total Top Height (Tongue)** | Timber height: 2165 + 225 = 2390 mm | +2425 mm *(flush with beams)* |
| **Rafter Birdsmouth Seat** | Depth of notch: 25 mm into rafter | — |
| **Rafter (47×150 mm) Effective Rise** | 150 mm − 25 mm = +125 mm | +2550 mm |
| **Top Purlins (38×50 mm laid flat)** | Thickness: +38 mm | **+2588 mm (~2.59 m)** |

```text
 ▲ +2588 mm  ────────────────────────────────────────────────  Top of Purlins (38 mm)
 │
 │ +2550 mm  ════════════════════════════════════════════════  Top of Rafters (150 mm)
 │           [ 25 mm birdsmouth notch locks over beam ]
 │ +2425 mm  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  Top of Beams & Post Tongue
 │           │ 47x225 mm Sandwich Beams                      │
 │ +2200 mm  ────────────────────────────────────────────────  Underside of Beams (Clearance)
 │           │                                               │
 │           │                                               │
 │           │ 150x150 mm C24 Post                           │  Headroom: 2.20 m (~7 ft 3 in)
 │           │                                               │
 │           │                                               │
 │   +35 mm  ────────────────────────────────────────────────  Bottom of Timber Post
 │           [ Galvanised Elevated Standoff Base ]             Air gap for water drainage
 ▼     0 mm  ════════════════════════════════════════════════  Finished Patio Pavers
```

---

## 3. Structural Engineering & Timber Calculations

### 3.1 Timber Grade: C24 Softwood

* **Bending Strength (f_m,k):** 24 N/mm² (vs 16 N/mm² for C16).
* **Modulus of Elasticity (E_0,mean):** 11.0 kN/mm² (denser, 35% stiffer than C16).
* **Density:** ~420 kg/m³ (tighter growth rings, minimal knots, straighter grain).
* **Treatment:** High-pressure copper azole preservative (Use Class 3 external
  above-ground), kiln-dried to <20% moisture before profiling to planed-all-round
  (PAR) eased-edge.

### 3.2 Main Support Beam Sizing (4.0 m Span)

* Each side uses a **twin beam** (sandwich assembly) of **two 47 mm × 225 mm C24**
  members flanking the notched post.
* Total combined beam width: 47 mm × 2 = 94 mm.
* **Effective Span with Knee Braces:**
  * 45° knee braces extend 500 mm horizontally from each post.
  * Clear beam span: 3850 mm.
  * Effective unsupported span between brace points: 3850 − (2 × 500) = **2850 mm (2.85 m)**.
* **Deflection Check:**
  * For open rafters + purlins (dead load ~0.20 kN/m² + temporary snow load 0.60 kN/m²),
    total load per 4m beam is ~3.5 kN uniformly distributed.
  * Maximum calculated deflection δ_max < 3.2 mm, which is well inside the strict
    British/Irish architectural limit of *L* / 360 = 2850 / 360 ≈ 7.9 mm.
  * **Result:** Zero perceptible sag, exceptionally rigid.

### 3.3 Rafter Sizing (3.0 m Span)

* Rafters: **47 mm × 150 mm C24** spanning 3.0 m between front and back beams.
* Number of rafters: **10 rafters total** across the 4.6 m length (spaced at ~510 mm centres).
* Maximum rafter span is 3000 mm, reduced to 2000 mm by diagonal knee braces at the end bays.
* Rafter capacity far exceeds requirements for open pergola purlin loads.

### 3.4 Racking & Wind Stability (Triangulation)

* Freestanding outdoor pergolas are exposed to cyclic lateral wind pressure.
* **Primary Anti-Racking Mechanism:**
  * Eight 45° solid timber knee braces (500 mm × 500 mm leg triangle).
  * 4 braces along the 4.0 m beam axis + 4 braces along the 3.0 m rafter axis.
  * This triangulation prevents the rectangular frame from shearing into a parallelogram.
* **Secondary Anti-Racking Mechanism:**
  * 25 mm birdsmouth notches cut into all 10 rafters lock the roof horizontally
    against the 150 mm wide beam assemblies, preventing any twisting or racking
    of the upper roof plane.

---

## 4. Foundation & Groundworks Engineering

### 4.1 Wind Overturning & Uplift

* Although open rafters have low aerodynamic profile compared to a solid roof,
  high gusts (e.g. 80–100 km/h Irish winter storms) exert significant uplift
  and overturning moments on the 2.6 m high posts.
* Surface-anchoring into 30–50 mm patio pavers laid on loose sand will fail
  under lateral wind loads.
* Therefore, each post is anchored into a **mass-concrete pier foundation**
  excavated through the patio sub-base.

### 4.2 Concrete Pier Sizing

* **Hole Dimensions:** 300 mm × 300 mm square (or 300 mm diameter round) × **500 mm deep** below patio paver level.
* **Concrete Volume per Pier:** ≈ 0.045 m³ (≈ 100 kg
  of cured concrete per post, providing 400 kg total ballast weight anchoring the structure down).
* **Concrete Specification:** Rapid-setting Postcrete (2.5 bags per hole) or standard
  C25/30 mix (1 part cement, 2 parts sharp sand, 3 parts 20 mm gravel).
* **Elevation of Pier Top:** Poured to finish **~30–40 mm below the top paver level**
  (flush with the bedding sand), allowing the lifted patio paver to be notched/cut
  and re-bedded around the post shoe for an unbroken patio appearance.

---

## 5. Planning Permission & Building Regulations

* **Ireland (Planning and Development Regulations — Class 3 Exempted Development):**
  * Freestanding pergolas and garden structures for domestic recreation situated
    to the rear of the house are **exempt from planning permission** provided:
    1. The structure is located in the rear garden (not in front of the house building line).
    2. Total area of all garden structures does not reduce remaining private open garden space below 25 m². (Our covered area is 16.5 m²).
    3. Height does not exceed 3.0 m (our total height is 2.59 m).
* **United Kingdom (Permitted Development — Class E):**
  * If within 2.0 m of a boundary fence/wall, the maximum permitted height for
    a flat roof / pergola is 2.5 m. Because this build has a total height of
    ~2.59 m, ensure the posts/overhangs are positioned **at least 2.0 m away from
    boundary fences**, or consult your local planning authority if located closer.
