# Corpus EDI inter-escala: prueba de portabilidad computacional

> **[BORRADOR-IA · requires: H-J2/H-J8]** La reducción del alcance ontológico requiere firma autoral.

## Tesis del capítulo

El corpus inter-escala muestra que la arquitectura EDI puede formularse y ejecutarse con sondas distintas en diez escalas nominales. No demuestra que exista una ontología común entre esas escalas. Como los datos son sintéticos y los parámetros proceden de la literatura, el resultado defendible es portabilidad computacional y especificidad parcial de las sondas.

## 1. Escalas cubiertas

| Escala | Longitud nominal | Tiempo nominal | Caso |
|---|---:|---:|---|
| Atómica | ~10⁻¹⁰ m | ~10⁻¹⁵ s | 32 Espín-órbita |
| Cuántica | ~10⁻⁹ m | ~10⁻⁶ s | 31 Decoherencia |
| Molecular | ~10⁻⁹ m | ~10⁻⁶ s | 33 Villin |
| Bioquímica | ~10⁻⁸ m | ~10⁻³ s | 34 Michaelis-Menten |
| Celular | ~10⁻⁵ m | ~10² s | 35 Ciclo celular, 36 NF-κB |
| Individual | ~1 m | ~1 s | 37 HRV, 38 Locomoción |
| Astrofísica | ~10¹¹ m | ~10⁵ s | 39 Cefeida |
| Astrofísica masiva | ~10¹⁷ a 10²⁰ m | ~10¹⁴ s | 40 Cúmulo globular |

Las longitudes y tiempos son etiquetas asociadas a los modelos de origen, no propiedades verificadas sobre datos crudos. La expresión "treinta órdenes de magnitud" describe el rango nominal de las parametrizaciones y no una validación empírica continua.

## 2. Resultados crudos ejecutados

**Tabla 5.6.1.**

| # | Caso | Escala | EDI | Categoría cruda | Sonda |
|---|---|---|---:|---|---|
| 31 | Decoherencia qubit | Cuántica | 0.91 | Strong | Lindblad con T2(T_bath) |
| 32 | Espín-órbita | Atómica | 0.83 | Strong | H_eff con coupling |
| 33 | Villin Headpiece | Molecular | 0.00 | Null | Equilibrio de dos estados |
| 34 | Michaelis-Menten | Bioquímica | 0.46 | Strong | Michaelis-Menten |
| 35 | Ciclo celular | Celular | 0.13 | Weak | Tyson-Novak |
| 36 | NF-κB | Celular oscilatoria | 0.59 | Strong | Hoffmann reducido |
| 37 | HRV cardíaco | Individual | 0.58 | Strong | Mackey-Glass |
| 38 | Locomoción τ-dot | Individual | -1.34 | Failure mode | τ-dot |
| 39 | Cefeida pulsante | Astrofísica | 0.92 | Strong | Relación período-luminosidad |
| 40 | Cúmulo globular | Astrofísica masiva | 0.43 | Strong | Plummer + marea |

La tabla conserva la clasificación del motor en su régimen crudo: siete Strong, un Weak, un Null y un failure mode. No equivale a estatus confirmatorio B-T2.1.

## 3. Qué muestran los resultados

### 3.1 Portabilidad

Los diez casos usan una interfaz común para comparar una predicción acoplada con una reducida. Cambian la sonda y los parámetros, pero se conserva la lógica ablativa. Esto prueba que el esquema es implementable fuera del dominio macro-poblacional.

### 3.2 Especificidad parcial

El test cruzado V4-01 reporta 0/12 detecciones sobre datos no propios de la sonda. El resultado reduce la sospecha de intercambiabilidad trivial entre las sondas ensayadas. No elimina la posibilidad de que los generadores sintéticos favorezcan la estructura de sus propias sondas.

### 3.3 Capacidad de reportar fallos

El caso 33 produce EDI cercano a cero: la ablación no separa las predicciones bajo la sonda de equilibrio. El caso 38 produce EDI negativo: τ-dot predice peor que el baseline sobre datos con reinicios discretos. El segundo es un fallo de la sonda propuesta, no un null estructural. Ninguno de los dos confirma la ontología por el hecho de ser reportado.

## 4. Límite de la inferencia ontológica

Aplicar un mismo formato estadístico a escalas heterogéneas no prueba que esas escalas compartan una estructura ontológica. Para sostener esa inferencia harían falta al menos:

- datos reales abiertos en cada escala;
- parámetros medidos fuera del ajuste;
- pre-registro y block-permutation post-fix;
- convergencia entre sondas estructuralmente distintas;
- comparación contra rivales con presupuesto equivalente;
- replicación independiente por especialistas del dominio.

Por tanto, "ontología general multiescalar" funciona aquí como hipótesis programática H-J2. El corpus aporta una condición necesaria, la portabilidad del protocolo, pero no una condición suficiente de verdad ontológica.

## 5. Relación con el corpus inter-dominio

| Dimensión | Inter-dominio | Inter-escala |
|---|---|---|
| Casos | 30 | 10 |
| Datos | Públicos, proxies y algunas fases sintéticas | Sintéticos parametrizados desde literatura |
| Régimen estricto | B-T2.1 incompleto | B-T2.4 pendiente |
| Resultado defendible | Mapa de resultados locales y fallos | Portabilidad computacional |
| Inferencia ontológica | Abierta | Abierta |

Los dos corpus son complementarios como pruebas del método. No deben sumarse como cuarenta corroboraciones independientes.

## 6. Deuda de elevación

1. sustituir datos sintéticos por fuentes abiertas, priorizando IBM Quantum, BRENDA, PhysioNet, OGLE y Gaia;
2. reejecutar el corpus después de las correcciones de `detrended_edi` y block-permutation;
3. registrar pre-registros genuinos antes de cada adquisición;
4. publicar una tabla pre/post con decisiones de clasificación;
5. obtener revisión de especialistas por escala.

## 7. Cierre

El corpus inter-escala expande el alcance del instrumento y, al mismo tiempo, impone una restricción a la conclusión. La misma arquitectura puede viajar entre escalas; de ese hecho no se sigue que la ontología sea idéntica en todas ellas. La contribución actual es haber hecho ejecutable esa pregunta y haber especificado qué evidencia adicional permitiría responderla.
