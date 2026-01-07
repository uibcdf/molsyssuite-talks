# Slide 07 — MolSysViewer conceptual map (speaker notes, draft)

Purpose of this slide:
- Show that MolSysViewer is a workflow component, not “a viewer”
- Make explicit that architectural coherence extends from MolSysMT to visualization
- Emphasize reproducibility: visualization is scriptable, not manual
- Introduce the two key abstractions: regions (selections) and overlays (annotations)

Core idea:
- MolSysViewer turns visualization into a reproducible, programmable layer
- It operates directly on MolSys, the same consensus molecular system introduced by MolSysMT
- Interactivity is used for exploration, while the artifact remains deterministic and shareable

Conceptual structure of the slide:
- MolSys → MolSysViewer → Interactive visualization

Key elements to convey:
- The molecular system (MolSys) remains the semantic source of truth
- MolSysViewer is an API-first visualization layer, not a GUI-driven application
- The same script can build, analyze, and visualize a molecular system
- Visualization is expressed through regions and overlays

MolSys (consensus molecular system):
- The same MolSys introduced in the previous slide
- Unified semantic and hierarchical representation
- Acts as the stable center for both analysis and visualization

MolSysViewer (visualization layer):
- A visualization API operating directly on MolSys
- Programmatic control of molecular visualization
- Defines the viewer as a canvas, not as a menu-based application
- Extends the MolSysMT model without breaking it

Interactive visualization:
- Exploration based on regions: semantic selections on the molecular system
- Overlays as annotations bound to regions
- Overlays may include geometry, labels, pockets, pharmacophores, and other visual elements
- Designed for use in notebooks and web documentation

Important emphasis:
- MolSysViewer does not replace existing viewers; it organizes visualization workflows
- Reproducibility is a core design constraint
- This is a conceptual map, not an implementation diagram

What NOT to do on this slide:
- Do not explain Mol* or rendering internals
- Do not discuss frontend/backend engineering details
- Do not show code or UI elements
- Do not compare against other viewers by name

Things NOT to explain:
- JavaScript or web technology stacks
- Widget mechanics or data transport
- Performance or rendering details

Role of the short video demo (optional):
- Show a scripted visualization session in a notebook
- Illustrate one region and one overlay
- Reinforce the idea of reproducibility (not a screenshot)

Transition to next slide:
- Emphasize that architectural coherence requires solid engineering foundations
- Prepare the audience to think about sustainability, testing, and maturity

Timing:
- ~3 minutes (plus optional short video)

## Speech (draft)

- “If MolSysMT gives us a coherent definition of the system, MolSysViewer gives us a coherent way to explore it.”

After introducing MolSysMT, we now look at how the same semantic core
enables a coherent visualization layer.

“This slide deliberately mirrors the previous one.”
“At the center, again, is MolSys — the same molecular system.”

“Most visualization tools are designed for manual interaction.”
“You click, you tweak, you take a screenshot.”
“That’s useful for exploration, but it’s hard to make it reproducible.”

“MolSysViewer takes a different approach.”
“Visualization is controlled programmatically, just like analysis.”

Introduce MolSysViewer:

“MolSysViewer is not a traditional viewer.”
“It is a visualization API that operates directly on MolSys.”

Clarify interaction model:

“Interaction is expressed through two simple abstractions.”
“Regions are semantic selections on the system.”
“Overlays are annotations bound to those regions.”

Examples (spoken, not exhaustive):

“Shapes, labels, pockets, pharmacophores…”
“These are examples — the abstraction is the point.”

Context of use:

“This fits naturally in notebooks and in web documentation.”
“Exploration can be interactive, but the science remains reproducible.”

Optional implementation mention (spoken, brief):

“The control happens from Python, while rendering uses web-based technologies.”
“But the important point is not the stack.”

Key takeaway (very important):

“Visualization becomes part of the workflow, not a separate step.”

Prepare the transition:

“To make this sustainable, this architecture needs solid engineering foundations.”
