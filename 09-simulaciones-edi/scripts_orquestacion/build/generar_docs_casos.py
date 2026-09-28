#!/usr/bin/env python3
"""RETIRADO 2026-09-28 — generar_docs_casos.py.

Este script generaba 5 docs por caso (arquitectura, protocolo, indicadores,
validación C1-C5, reproducibilidad) en el árbol espejo
TesisDesarrollo/02_Modelado_Simulacion/<caso>/docs/ con metadatos fijos de
29 casos. Ese árbol ya no existe y los docs reales viven en
09-simulaciones-edi/<caso>/docs/ (protocolo_simulacion.md en 32/32 casos,
mantenido a mano): re-apuntar este generador wholesale los destruiría con
contenido de plantilla desactualizado.

Para documentar un caso nuevo, el camino es:
  cd 09-simulaciones-edi && ./tesis scaffold --id <NN> --name <slug>

El código original se conserva en el historial git previo al retiro.
"""
import sys

print(
    "[ERROR] generar_docs_casos.py retirado 2026-09-28: generaba docs del "
    "árbol TesisDesarrollo/ (inexistente) con plantilla de 29 casos. Los docs "
    "reales están en 09-simulaciones-edi/<caso>/docs/ y son prosa a mano. "
    "Para casos nuevos usa './tesis scaffold'.",
    file=sys.stderr,
)
sys.exit(2)
