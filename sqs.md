# SQS — Structural Intelligence Quotient Module Script
*Block-structured intake for the SQS SPA test engine*
**Version: Control-first validation**

@if (module.skip == true)
    @allow("skip")
@endif

@if (module.skip != true)
    @require(module.fields == 10)
@endif

---

## Flow Overview
The sequence runs forward only: FL → RR → MF → SC → PH → SSC → Results.
No backward navigation is defined or permitted.

---

## Module: Fractal Learning (FL)
@module(fl)
@title(Fractal Learning)
@fields
1. Identify the recurring pattern across four visual sequences.
2. Choose the structure that completes the recursive grid.
3. Map the nested triangle rules to the missing symbol.
4. Extend the fractal curve by selecting the next segment.
5. Determine the pivot rule in the alternating matrix.
6. Match the mirror rule that governs the inner tiles.
7. Infer the substitution driving the self-similar chain.
8. Predict the iteration that balances the spiral set.
9. Align the scaling rule for the stepped pyramid.
10. Resolve the rotation that keeps the tiling coherent.
@endfields
@next(rr)

---

## Module: Recursive Reasoning (RR)
@module(rr)
@title(Recursive Reasoning)
@fields
1. Trace the dependency loop to find the stable node.
2. Select the rule that untangles the circular reference.
3. Identify the invariant that survives each recursion.
4. Choose the step that halts the runaway process.
5. Detect the base case hidden in the branching tree.
6. Align the priority that resolves the deadlock chain.
7. Spot the repeating fault that propagates downstream.
8. Determine which condition shortens the recursion depth.
9. Pick the operator that preserves referential integrity.
10. Balance the feedback path to stop oscillation.
@endfields
@next(mf)

---

## Module: Mental Flexibility (MF)
@module(mf)
@title(Mental Flexibility)
@fields
1. Translate the abstract icon set into a working rule.
2. Reorder the timeline to satisfy all constraints.
3. Choose the mapping that unifies the competing models.
4. Swap the dimensions to minimize the conflict cost.
5. Integrate the outlier datapoint without losing fit.
6. Convert the symbolic code into its physical analogue.
7. Flip the hierarchy to expose the hidden shortcut.
8. Reframe the grid so both objectives can coexist.
9. Select the pivot that unlocks a cleaner schema.
10. Re-sequence the actions to keep throughput stable.
@endfields
@next(sc)

---

## Module: Systemic Chronology (SC)
@module(sc)
@title(Systemic Chronology)
@fields
1. Position the missing event that keeps causality intact.
2. Align the checkpoints so the schedule never overlaps.
3. Choose the trigger that correctly cascades the steps.
4. Match the timestamp that preserves dependency order.
5. Insert the buffer that prevents timeline contention.
6. Identify the earliest slot that satisfies all locks.
7. Assign the phase that stabilizes downstream timing.
8. Anchor the milestone that keeps the chain synchronized.
9. Choose the delay that neutralizes cyclical drift.
10. Finalize the order that maintains sequential integrity.
@endfields
@next(ph)

---

## Module: Physical Heuristics (PH)
@module(ph)
@title(Physical Heuristics)
@fields
1. Select the force diagram that balances the vector set.
2. Match the torque direction to the gear alignment.
3. Choose the material path that dissipates heat safely.
4. Identify the pivot that minimizes load stress.
5. Place the fulcrum that preserves angular momentum.
6. Pick the joint that prevents binding under motion.
7. Route the current to avoid resonance in the coil.
8. Set the counterweight that stabilizes the frame.
9. Align the axis to keep the assembly level.
10. Secure the brace that protects against shear.
@endfields
@next(ssc)

---

## Module: Social Systems Cognition (SSC)
@module(ssc)
@title(Social Systems Cognition)
@fields
1. Select the communication path that reduces escalation.
2. Assign the mediator who keeps both factions engaged.
3. Choose the policy that preserves group trust.
4. Time the announcement to prevent rumor cascades.
5. Route the feedback to the most resilient channel.
6. Align the incentives to stabilize participation.
7. Identify the signal that rebuilds psychological safety.
8. Balance transparency against operational security.
9. Choose the governance loop that prevents capture.
10. Set the cadence that sustains collaborative flow.
@endfields
@next(results)

---

## Results
@module(results)
@title(Results Summary)
@fields
1. Present composite SQS score.
2. Provide module-level subscores.
3. Display self-assessment alignment.
4. Offer percentile estimates.
5. Suggest growth focus areas.
6. Summarize response consistency.
7. Highlight outstanding strengths.
8. Recommend next assessment window.
9. Capture participant acknowledgement.
10. Confirm completion receipt.
@endfields
@complete
