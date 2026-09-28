#!/usr/bin/env python3
"""RETIRADO 2026-09-28 — regenerar_readmes.py.

Este script regeneraba por mayor los README.md del árbol espejo
TesisDesarrollo/02_Modelado_Simulacion/ desde metrics.json. Ese árbol ya no
existe (consolidación mono-repo) y los README reales viven en
09-simulaciones-edi/<caso>/README.md con prosa mantenida a mano:
re-apuntar este generador wholesale los destruiría.

Para refrescar cifras dentro de docs sin tocar prosa, el camino es:
  1. Añadir bloques <!-- AUTO:RESULTS:START/END --> o <!-- AUTO:clave -->
     al README del caso.
  2. Correr:  cd 09-simulaciones-edi && ./tesis sync [--case <filtro>]

El código original se conserva en el historial git previo al retiro.
"""
import sys

print(
    "[ERROR] regenerar_readmes.py retirado 2026-09-28: regeneraba READMEs del "
    "árbol TesisDesarrollo/ (inexistente). Los README reales están en "
    "09-simulaciones-edi/<caso>/README.md y son prosa a mano — no se "
    "sobrescriben por mayor. Usa bloques AUTO + './tesis sync'.",
    file=sys.stderr,
)
sys.exit(2)
