# Slide 05 — MolSysMT conceptual map (speaker notes, draft)

Purpose of this slide:
- Make the architectural philosophy of MolSysMT explicit and memorable
- Show how fragmented representations are transformed into a coherent system
- Separate clearly the molecular system (MolSys) from the toolkit (MolSysMT)
- Make explicit that MolSysMT is about redefining what a molecular system is
- Emphasize coherence over convenience

Core idea:
- MolSysMT is built around a consensus molecular system (MolSys)
- This system acts as a stable semantic core across heterogeneous inputs
- The toolkit (MolSysMT) operates on this core to enable coherent workflows

Conceptual structure of the slide:
- External representations → MolSys → MolSysMT workflows

Key elements to convey:
- We usually jump between representations without a unifying model
- MolSysMT introduces a consensus system model
- Once the system is coherent, workflows become simpler

External representations:
- Molecular systems appear in many heterogeneous forms
- Files, trajectories, library-specific objects, URLs, and databases
- Often, the same system exists simultaneously in multiple representations

MolSys (consensus molecular system):
- A unified molecular system representation
- Integrates attributes observed across different third-party formats
- Explicit hierarchical structure (atoms, groups, components, molecules, chains, entities)
- Treated as a first-class molecular object

MolSysMT (multi-toolkit layer):
- A unified API operating on MolSys
- Core operations: selection, conversion, modification, analysis
- Enables workflows that are independent of data origin or destination

Important emphasis:
- MolSysMT does not eliminate heterogeneity; it organizes it
- The goal is coherence, not abstraction for its own sake
- This is a conceptual map, not a software diagram

What NOT to do on this slide:
- Do not list all supported formats
- Do not enumerate all available functions
- Do not explain data structures or implementation details
o- Do not turn the slide into a catalog of tools

Things NOT to explain:
- Exact class hierarchy
- Performance details
- Internal implementation choices

Role of the short video demo:
- Illustrate the conceptual flow shown in the diagram
- Show the same molecular system moving across representations
- Reinforce the idea, not replace the explanation

Transition to next slide:
- Prepare the audience to see how visualization builds on this core
- Emphasize that MolSysViewer operates directly on MolSys

Timing:
- ~3 minutes (plus optional short video)

Timing:
- ~3 minutes
Script (draft):

## Speech

- "We realized the real problem was not formats, but semantics"
- "MolSysMT sits between data and workflows"
- I have to say that the implementation is done in Python + Numba.

When we started working on MolSysMT, we quickly realized that the main
challenge was not just dealing with multiple file formats. The real issue was
that each molecular system representation came with its own semantics and API,
making it difficult to create coherent workflows.

“This slide summarizes the core idea behind MolSysMT.”
“It is a conceptual map, not a technical diagram.”

External world:

“We usually work with molecular systems through many different representations.”
“Files, trajectories, library objects, URLs, databases.”
“Often, the same molecular system exists in several forms at the same time.”

Transition to the core:

“The problem is not heterogeneity itself.”
“The problem is that there is no stable center.”

Introduce MolSys:

“At the center of MolSysMT there is what we call the MolSys.”
“A consensus molecular system representation.”

Alternative phrasing:

“MolSys is the molecular system itself, treated as a first-class object.”
“It integrates the attributes and structure observed across different tools.”

Explain hierarchy (briefly):

“This system has an explicit hierarchical structure.”
“Atoms, groups, components, molecules, chains, entities.”

Move to MolSysMT:

“MolSysMT is the multi-toolkit that operates on this system.”
“It provides a unified API for selection, conversion, modification, and analysis.”

Examples (spoken, not exhaustive):

“This includes things like alignment, RMSD fitting, contact maps, hydrogen bonds, PCA.”
“Just as examples — listing functions is not the point of this talk.”

Key takeaway (very important):

“Once you have this core, the workflow finally becomes coherent.”

Prepare the transition:

“This same core is what makes a coherent visualization layer possible.”
“That’s where MolSysViewer comes in.”
