# MolSysMT: the core semantic layer

# Slide 04 — MolSysMT: the core semantic layer (speaker notes, draft)

Purpose of this slide:
- Introduce MolSysMT as the core component of MolSysSuite
- Make the architecture tangible without going into implementation details
- Establish MolSysMT as the semantic foundation for workflows, visualization, and AI

Core idea:
- MolSysMT treats molecular systems as first-class objects
- The molecular system becomes the primary entity, not files or formats

Key points to convey:
- MolSysMT defines a unified representation of molecular systems
- This representation integrates information coming from different formats and toolchains
- Operations are defined on the system itself, independently of its origin or destination
- MolSysMT provides the stable core on which workflows can be built coherently

Clarifications to keep in mind:
- MolSysMT does not replace existing tools
- It does not aim to hide physics, chemistry, or simulation details
- It provides structure and consistency across heterogeneous workflows

What NOT to do on this slide:
- Do not explain data structures
- Do not show code
- Do not list supported formats explicitly
- Do not describe performance or benchmarks

Transition to next slide:
- Prepare the audience for a more explicit architectural view
- Signal that the next slide will show *how* this abstraction is implemented

Timing:
- ~3 minutes

---

## Speech (draft, flexible)

Opening (connect to previous slide):
- “If MolSysSuite is the architectural response, MolSysMT is its core.”

Introduce the key concept:
- “MolSysMT treats molecular systems as first-class objects.”
- Alternative phrasing:
  - “By first-class objects, we mean that the molecular system itself is the primary entity.”
  - “The system comes first — not the file, not the format.”

Clarify what this means in practice:
- “In many workflows, we end up operating on files or on library-specific objects.”
- “In MolSysMT, operations are defined on the molecular system itself.”

Alternative phrasing:
- “Selections, transformations, and analyses are applied to the system, not to a specific representation.”
- “Formats and toolchains become views of the same underlying system.”

Emphasize identity and persistence:
- “The molecular system has an identity that survives conversions and transformations.”
- Alternative phrasing:
  - “The system does not disappear every time we switch tools.”

Reinforce the architectural role:
- “This unified representation allows us to build workflows that remain coherent over time.”
- “MolSysMT acts as the stable semantic layer of the ecosystem.”

Prepare the transition:
- “To make this more concrete, let me show how this is reflected in the architecture.”
- “The next slide shows how MolSysMT sits between different toolchains and workflows.”


“MolSysMT is the core of the ecosystem.
It treats molecular systems as first-class objects,
provides a unified representation across tools,
and exposes a consistent API for building workflows.”

“By first-class objects we mean that the molecular system itself is the primary entity,
not the files or formats used to represent it.”

“Operations in MolSysMT are defined on molecular systems,
not on specific file formats or third-party objects.”

“The molecular system has an identity that survives conversions, transformations, and analyses.”
