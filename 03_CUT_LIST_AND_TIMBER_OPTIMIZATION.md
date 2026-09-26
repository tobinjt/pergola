# 03 — Cut List & Timber Optimization

This document specifies the exact cutting schedule for every piece of timber in
the pergola, along with stock optimization layouts to minimize waste from
standard merchant lumber lengths (4.8 m, 3.6 m, 2.7 m, 2.4 m).

---

## 1. Master Component Cut Schedule

<!-- markdownlint-disable MD013 -->
| ID | Description | Count | Finished Dimensions (T × W × L) | Finished Weight (Treated) | Stock Purchased | Cut Details & Features |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P-01 to P-04** | Corner Posts | 4 | **150 × 150 × 2390 mm** | **~25–28 kg** (heaviest) | 4 × 2.7 m (150×150) | Top notched 47 mm deep × 225 mm tall on 2 opposing faces; bottom squared |
| **B-01 to B-04** | Main Sandwich Beams | 4 | **47 × 225 × 4600 mm** | **~24–27 kg** | 4 × 4.8 m (47×225) | 45° chamfer (75×75 mm) cut on both bottom corners; pre-drilled for M12 coach bolts |
| **R-01 to R-10** | Roof Rafters | 10 | **47 × 150 × 3600 mm** | **~12–14 kg** | 10 × 3.6 m (47×150) | 45° chamfer (75×75 mm) cut on both bottom corners; two 150 mm wide × 25 mm deep birdsmouth notches |
| **S-01 to S-10** | Top Shade Purlins | 10 | **38 × 50 × 4600 mm** | **~4.4–4.8 kg** | 10 × 4.8 m (38×50) | Ends cut square or 45° pencil chamfer (25×25 mm); pre-drilled for 5 mm screws |
| **K-01 to K-08** | Corner Knee Braces | 8 | **100 × 100 × ~735 mm** | **~3.7–4.1 kg** | 3 × 2.4 m (or 2 × 3.0 m) | Both ends mitred at parallel 45° angles (450 mm × 450 mm right-angle leg projection) |
<!-- markdownlint-enable MD013 -->

---

## 2. Detailed Cutting Geometry

### 2.1 Corner Posts (150 mm × 150 mm × 2390 mm)

* **Starting Stock:** 2700 mm length (uncut blank weighs ~30–33 kg treated; ~25.5 kg dry).
* **Finished Weight:** **~25–28 kg treated** (~21.3 kg dry), making it the heaviest single component in the build.
* **Bottom Cut:** Trim 10–20 mm off the factory end to ensure a crisp, 90° square base to sit squarely inside the standoff post shoe.
* **Finished Height:**
  * **Option 2 (Simpson APB100/150):** Measure exactly **2390 mm** for all four
    posts, since the base plates are leveled via the threaded standoff hardware.
  * **Option 1 (Fixed Box Shoes):** Measure **2390 mm** for Post 1 (highest corner),
    and **2390 mm + corner drop** for Posts 2, 3, and 4 (where the drop is that
    corner's measured fall below Post 1) so that the top beam shoulders finish dead
    level across the sloping patio. The 2700 mm stock provides 310 mm of surplus
    length to accommodate any standard patio fall.
* **Post Shoulder Notches (Top):**
  * Measure down **225 mm** from the top end.
  * Cut a shoulder notch **47 mm deep** into the outer and inner faces.
  * Leaves a central **56 mm tongue** (150 − 47 − 47 = 56 mm) to receive
    the two 47 mm sandwich beams.
  * *Tip:* Kerf multiple saw cuts across the 225 mm face using a circular saw set to 47 mm depth, then chisel out and smooth with a router or chisel.

```text
       ◄── 150 mm ──►
       ┌───┬─────┬───┐ ▲
       │   │     │   │ │ 225 mm (Beam Depth)
       │   │  T  │   │ │
       └───┤     ├───┘ ▼
         ▲ │     │
  47 mm  │ │     │
  Shoulder │     │
  Cutout   │     │
           │     │
           │     │ (2165 mm timber to post base)
           │     │
           │     │
           │     │
           └─────┘
```

---

### 2.2 Main Support Beams (47 mm × 225 mm × 4600 mm)

* **Starting Stock:** 4800 mm length.
* **Length Cut:** Trim 100 mm off each end to achieve a clean **4600 mm** finished length.
* **Post Position Layout:**
  * Mark post centreline at **300 mm** in from each end.
  * Distance between post centrelines = **4000 mm**.
* **Decorative Tail Chamfers (Both Ends):**
  * From bottom corner, measure **75 mm** inward along the bottom edge, and **75 mm** upward along the vertical end edge.
  * Connect points with a straight line at 45° and cut with the sliding mitre saw.

```text
        ◄──────────────────────── 4600 mm Total Beam Length ────────────────────────►
        300 mm                                                                300 mm
        Overhang               ◄─────── Post Centres: 4000 mm ───────►        Overhang
       ┌─────────────────────────────────────────────────────────────────────────────┐
       │     │                                                         │             │ 225 mm
       /     │                                                         │             \
      /  45° │                                                         │          45° \
     └───────┴─────────────────────────────────────────────────────────┴───────────────┘
     ◄ 75 mm ►                                                               ◄ 75 mm ►
```

---

### 2.3 Roof Rafters (47 mm × 150 mm × 3600 mm)

* **Starting Stock:** 3600 mm length (standard merchant length; zero waste!).
* **Decorative Tail Chamfers:**
  * Cut 45° chamfer (75 mm × 75 mm) on both bottom corners, exactly matching the beam tails.
* **Birdsmouth Seat Notches:**
  * Each rafter requires **two 150 mm wide × 25 mm deep flat seat notches** that drop over the sandwich beam pairs.
  * **Notch 1 (Front Beam):** Centred at **300 mm** from front end (cut from 225 mm to 375 mm).
  * **Notch 2 (Rear Beam):** Centred at **3300 mm** from front end (cut from 3225 mm to 3375 mm).
  * *Distance between notch centres:* Exactly **3000 mm** (locks the front and back beam frames in parallel!).

```text
       ◄─────────────────────── 3600 mm Total Rafter Length ───────────────────────►
        300 mm                                                               300 mm
       ┌───────────┬─────┬─────────────────────────────────────┬─────┬─────────────┐
       │           │     │                                     │     │             │ 150 mm
       /           │     │                                     │     │             \
      /  45°       └──┬──┘ 25 mm deep                          └──┬──┘ 25 mm deep 45°\
     └────────────────┴───────────────────────────────────────────┴─────────────────┘
                   ◄150 mm►                                    ◄150 mm►
                      ▲                                           ▲
                      │◄────────── Notch Centres: 3000 mm ───────►│
```

---

### 2.4 Corner Knee Braces (100 mm × 100 mm × ~735 mm)

* **Geometry:** 45° isosceles right triangle against post and beam/rafter.
* **Leg Projections:** 450 mm along post vertical, 450 mm along beam/rafter horizontal.
* **Cut Angles:** Both ends cut at **45° parallel mitres**.
* **Cut Blank Length:** **736 mm** (long point to long point = 877 mm).
* **Nesting:** 3 knee braces cut per 2.4 m timber board (3 × 736 = 2208 mm ≤ 2400 mm).
* Total stock needed: **3 lengths of 2.4 m** (yields 9 braces — 8 needed + 1 test/spare).

```text
                 ◄────── 450 mm to Corner ──────►
               ┌─────────────────────────────────┐
               │ Beam / Rafter                   │
               └───────────────┬─────────────────┘
                               │\  45° Mitre Cut
                               │ \
                               │  \
         450 mm to Corner      │   \  Knee Brace
                               │    \ (100x100 mm)
                               │     \
                               │ 45°  \
                               ├───────┘
                               │ Post
                               │
```

---

### 2.5 Top Shade Purlins (38 mm × 50 mm × 4600 mm)

* **Starting Stock:** 4800 mm length.
* **Finished Length:** Trim to **4600 mm** (matching total beam length).
* **End Profiles:** Clean 90° square crosscut or subtle 25 mm × 25 mm 45° chamfer.
* **Count:** 10 battens laid flat (50 mm face horizontal, 38 mm vertical).

---

## 3. Stock Optimization & Merchant Order Summary

| Stock Size | Standard Length | Qty to Buy | Used For | Waste / Offcuts |
| :--- | :--- | :--- | :--- | :--- |
| **150 × 150 mm C24 PAR** | 2.7 m | **4** | Posts P-01 to P-04 | 4 × ~310 mm offcuts (useful for test cuts) |
| **47 × 225 mm C24 PAR** | 4.8 m | **4** | Main Beams B-01 to B-04 | 4 × 200 mm offcuts |
| **47 × 150 mm C24 PAR** | 3.6 m | **10** | Rafters R-01 to R-10 | **0 mm waste** (exact fit) |
| **38 × 50 mm Treated Batten** | 4.8 m | **10** | Purlins S-01 to S-10 | 10 × 200 mm offcuts |
| **100 × 100 mm C24 PAR** | 2.4 m | **3** | Knee Braces K-01 to K-08 | 3 × ~190 mm offcuts |
| **38 × 75 mm Rough Timber** | 3.0 m | **4** | Temporary Post Braces | Reusable scrap timber |
