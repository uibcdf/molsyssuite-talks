# MolSysMT architecture – speaker notes (draft)

Goal of this slide:
- Make explicit that MolSysMT is about redefining what a molecular system is
- Emphasize coherence over convenience

Key ideas to convey:
- We usually jump between representations without a unifying model
- MolSysMT introduces a consensus system model
- Once the system is coherent, workflows become simpler

Possible phrases:
- "We realized the real problem was not formats, but semantics"
- "MolSysMT sits between data and workflows"

Things NOT to explain:
- Exact class hierarchy
- Performance details
- Internal implementation choices

Timing:
- ~3 minutes
Script (draft):

When we started working on MolSysMT, we quickly realized that the main
challenge was not just dealing with multiple file formats. The real issue was
that each molecular system representation came with its own semantics and API,
making it difficult to create coherent workflows.
