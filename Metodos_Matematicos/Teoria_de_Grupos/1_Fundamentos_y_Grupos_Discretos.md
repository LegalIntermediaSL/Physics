# Fundamentos de la Teoría de Grupos (Discretos)

En física, la simetría es equivalente a la invarianza bajo transformaciones. La herramienta matemática suprema para formalizar la simetría es la **Teoría de Grupos**, desarrollada originalmente por Évariste Galois.

## 1. Los Axiomas de Grupo
Un grupo $G$ es un conjunto de elementos (transformaciones) junto con una operación binaria (composición $\cdot$) que satisface cuatro axiomas inflexibles:
1.  **Clausura**: Si $a, b \in G$, entonces $a \cdot b \in G$.
2.  **Asociatividad**: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
3.  **Elemento Identidad**: Existe un único elemento $e \in G$ tal que $a \cdot e = e \cdot a = a$ (La transformación de "no hacer nada").
4.  **Inverso**: Para cada $a \in G$, existe un $a^{-1} \in G$ tal que $a \cdot a^{-1} = e$.

Si además la operación conmuta ($a \cdot b = b \cdot a$), el grupo se denomina **Abeliano**. En física cuántica y de campos, la no-conmutatividad (Grupos No-Abelianos) es la raíz profunda de fuerzas fundamentales como la Fuerza Fuerte y Débil.

## 2. Grupos Discretos y Cristalografía
Un grupo es discreto si su número de elementos (el **Orden del Grupo**, $|G|$) es finito o contablemente infinito.
En física del estado sólido y la química cuántica, los grupos discretos dominan:
-   **$Z_n$ (Grupos Cíclicos)**: Rotaciones discretas en el plano (ej. un copo de nieve).
-   **$S_n$ (Grupos Simétricos)**: Las permutaciones de $n$ objetos. Vital para entender la estadística cuántica (Bosones vs Fermiones surgen de las representaciones del grupo de permutación de partículas idénticas).
-   **Grupos Puntuales y Espaciales**: Las 230 formas únicas en que los átomos pueden ordenarse en un cristal 3D (redes de Bravais con simetría de traslación discreta).

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Carl Bender: Mathematical Physics (Washington University)](https://www.youtube.com/playlist?list=PL1B1123DDB9DD4668) - Brillantes clases de perturbaciones, asintóticos y WKB impartidas por un genio del análisis.
- [ICTP: Mathematics for Physicists](https://www.youtube.com/user/ictp) - Herramientas analíticas puras desde Trieste.
