# Slide 06 — MolSysViewer: visualization as part of the workflow (speaker notes, draft)

Purpose of this slide:
- Introduce MolSysViewer as the visualization layer of MolSysSuite
- Emphasize visualization as an integral part of workflows, not a side activity
- Show complementarity with MolSysMT without repeating concepts

Core idea:
- MolSysViewer treats visualization as a programmable, reproducible component of workflows
- Visualization is driven by the same molecular system abstraction defined in MolSysMT

Key points to convey:
- MolSysViewer is not a standalone visualization program
- It is a visualization layer designed to integrate directly with workflows
- It exposes a Python API for controlling visualization programmatically
- It is fully integrated with Jupyter notebooks and documentation

Clarifications to keep in mind:
- MolSysViewer is not meant to replace existing viewers
- It is not focused on interactive GUIs or menus
- The emphasis is on reproducibility and scriptable control

What NOT to do on this slide:
- Do not explain Mol* internals
- Do not discuss frontend/backend implementation details
- Do not show code yet
- Do not compare with other viewers explicitly

Transition to next slide:
- Prepare the audience for an architectural view
- Make explicit that MolSysViewer builds directly on MolSysMT

Timing:
- ~3 minutes

---

## Speech (draft, flexible)

Opening (mirror of slide 04):
- “If MolSysMT is the semantic core of the ecosystem, MolSysViewer is the interaction layer.”

Introduce the key concept:
- “MolSysViewer treats visualization as part of the workflow.”
- Alternative phrasing:
  - “Visualization is not an afterthought.”
  - “Visualization is something you can script, reproduce, and integrate.”

Clarify the philosophy:
- “In many workflows, visualization is used to generate screenshots.”
- “In MolSysViewer, visualization is driven by code.”

Alternative phrasing:
- “The same script that builds or analyzes a system can also visualize it.”
- “Visualization becomes reproducible, not manual.”

Explain integration:
- “MolSysViewer works directly with the molecular systems defined by MolSysMT.”
- “Selections, regions, and overlays are defined on the same underlying system.”

Emphasize the medium:
- “It is designed to work naturally in Jupyter notebooks.”
- “It also integrates with web-based documentation.”

Reinforce complementarity:
- “MolSysMT defines what the system is.”
- “MolSysViewer defines how we explore and communicate it.”

Prepare the transition:
- “To understand why this integration matters, it helps to look at the architecture.”
- “The next slide shows how MolSysMT and MolSysViewer fit together.”

