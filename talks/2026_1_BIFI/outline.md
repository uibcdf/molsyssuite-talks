# Talk outline (25 minutes + 5 minutes Q&A)

## 1. Title and framing (1 min)
- Who we are
- What kind of talk this is
- Emphasis: foundations and architecture, not results

INTENT: set expectations and avoid a "feature demo" mindset
OBJECTIVE: framing

## 2. The problem: fragmented molecular workflows (3 min)
- Tool proliferation across modeling, MD, and analysis
- Inconsistent APIs and mental models
- Fragile glue code and poor long-term sustainability

INTENT: make the audience recognize the problem as their own
OBJECTIVE: problem side

## 3. MolSysSuite as an architectural response (2 min)
- Ecosystem vs toolbox
- Coherence, consistency, and sustainability as design drivers
- Open-source, integrated alternative for drug-design-oriented workflows

INTENT: answer "why MolSysSuite exists" before naming tools
OBJECTIVE: solution side

## 4. MolSysMT: the core semantic layer (3 min)
- Molecular system as a first-class concept
- Unified interface across formats and toolchains
- Typical operations and workflow patterns

INTENT: show substance and credibility without deep implementation
OBJECTIVE: core technology

## 5. MolSysMT architecture: from fragmented inputs to a coherent system (3 min)
- Heterogeneous molecular system representations and APIs
- Consensus molecular system model with hierarchical structure
- Unified API for selection, conversion, and modification
- MolSysMT as the core that enables coherent molecular workflows
- Short video demo

INTENT: make the architectural philosophy explicit and memorable
OBJECTIVE: conceptual clarity and architectural credibility

> flujo sería el siguiente:
> 1) Trabajamos con distintas formas de sistema molecular (pdb files, cif files,
> mdtraj objects, openmm objects, urls, etc) y necesitamos armar flujos de
> trabajo en ocasiones haciendo uso de distintas formas del mismo sistema,
> 2) MolSysMT implementa una nueva forma consenso de sistema molecular lo más amplia
> posible integrando todos los atributos de un sistema molecular (observados de
> un censo de distintas formas terceras) y con estructura jerarquica de
> elementos consenso (átomos, groups, components, moléculas, chains, entidades)
> 3) MolSysMT ofrece una API unificada para operaciones básicas de manipulación
> de sistemas moleculares: selección de elementos, conversión entre formas, obtención de atributos,
> modificación (fusión, añadido de elementos) -ya sólo esto ofrece una solución
> como juntas para montar flujos de trabajo con segmentos de tubería que serían
> software de terceros-
> 4) MolSysMT ofrece su propia batería de herramientas: topologicas,
> estructurales, mecánica molecular, PBC, puentes de hidrógeno, análisis de
> propiedades físicas y químicas, de construcción de sistemas...
> Objetivo: La idea es que quede claro que MolSysMT es el núcleo que permite
> trabajar con sistemas moleculares
> de manera coherente y consistente, independientemente del origen o destino de
> los datos.


## 6. MolSysViewer: visualization as part of the workflow (3 min)
- Visualization beyond screenshots
- Programmatic control and reproducibility
- Integration with notebooks and documentation

INTENT: introduce MolSysViewer as a workflow component
OBJECTIVE: user experience

## 7. MolSysViewer architecture: reproducible, programmatic visualization (3 min)
- Python → ipywidgets → Mol* pipeline
- MolSysMT as the semantic source of molecular systems
- MolSysViewer API and dedicated visualization canvas
- Region-based selections and overlay-based annotations
- Interactive exploration with reproducible, scriptable visualization
- Short video demo

INTENT: show symmetry with MolSysMT and reinforce reproducibility
OBJECTIVE: architectural coherence and UX philosophy

> Me gustaría mostrar también un flujo arquitectónico similar al de MolSysMT. Puede que sea necesaria otra slide para el esquema:
> 1) Python -> iPywidgets -> Mol*
> 2) MolSysMT en el manejo de sistemas moleculares
> 3) MolSysViewer API (frontend para Python y Jupyter Lab), Canvas ad-hoc con backend Mol*.
> 4) Filosofía de visualiación por regiones (selecciones de elementos) y overlays (formas geométricas, textos, pockets, pharmacophores)
> 5) Visualización programática, reproducible, integrable en notebooks. La exploración es interactiva y dinámica, la ciencia es reproducible.

## 8. Engineering foundations and maturity (2 min)
- Architectural choices
- Testing, CI, and documentation
- Distribution and versioning
- Near-1.0 status of MolSysMT and MolSysViewer

INTENT: justify trust and readiness without overselling
OBJECTIVE: engineering credibility and mature emphasis

## 9. From tools to intelligence: MolSys-AI (3 min)
- Why agents require coherent tools
- Under the hood (briefly): LLaMA 3 8B + RAG + light fine-tuning
- Current state: documentation chatbot
- Near-term direction: CLI and agent-based interaction

INTENT: present MolSys-AI as a consequence, not a gimmick
OBJECTIVE: future direction and innovation, AI + evolution

## 10. Beyond the core: ecosystem expansion (2 min)
- TopoMT
- ElastNetMT
- PharmacophoreMT
- BiFreeMT
- Shared semantic and architectural principles

INTENT: show breadth without diluting focus
OBJECTIVE: ecosystem potential and mental model of scope and limits

## 11. Closing: status, direction, and invitation (2 min)
- What MolSysSuite already offers
- What it does not yet aim to do
- Short- and mid-term outlook
- Invitation to early adopters, beta testers, and conceptual collaborators

Key message:
"This is not a finished product, but it is a solid foundation we want to share,
test, and shape together."

INTENT: set realistic expectations and foster community
OBJECTIVE: synthesis

## 12. Who we are and where to find us (1 min)
- Research unit and institutional context
- Other ongoing research lines and tools
- Where to follow future updates and interact

INTENT: close on a human and institutional note
OBJECTIVE: contextualization and continuity


---------------
Total time : 30 minutes (25 + 5 Q&A)
