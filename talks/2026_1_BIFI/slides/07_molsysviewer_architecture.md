# MolSysViewer architecture

- Python → ipywidgets → Mol* visualization pipeline
- MolSysMT as the semantic source of molecular systems
- A dedicated visualization canvas controlled by a Python API
- Region-based selections and overlay-based annotations
- Interactive exploration with reproducible, scriptable visualization

Es el espejo conceptual de la arquitectura de MolSysMT.
Reafirma que MolSysViewer no rompe el modelo, lo extiende.
Introduce claramente la idea de:
regiones (selecciones)
overlays (formas, anotaciones, pockets, etc.)
Frase de cierre muy potente:

“Exploration can be interactive, but the science remains reproducible.”
