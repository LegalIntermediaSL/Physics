# Renormalización y el Grupo de Renormalización (RG)

Al evaluar diagramas de Feynman que contienen bucles (loops) internos, como la auto-energía del electrón o la polarización del vacío, el momento del bucle virtual no está restringido cinemáticamente. La integral sobre todos los momentos posibles estalla frecuentemente hacia el infinito. Esta divergencia a altas energías se denomina **Divergencia Ultravioleta (UV)**.

## 1. Regularización Dimensional y Esquema MS-bar
Para aislar matemáticamente y entender estos infinitos temporales, 't Hooft y Veltman introdujeron la **Regularización Dimensional**.
Consiste en extender analíticamente la dimensión del espaciotiempo desde 4 hasta una dimensión abstracta $d = 4 - \epsilon$. 
Las divergencias UV se manifiestan algebraicamente como polos matemáticos de la forma $1/\epsilon$.
Mediante el proceso de renormalización sistemática, estos polos infinitos se absorben redefiniendo (escalando) los parámetros fundamentales de la teoría: la masa "desnuda" $m_0$ se renorma a $m$, la carga desnuda $e_0$ a $e$, en el popular esquema de substracción mínima modificada ($\overline{MS}$).

## 2. La Ecuación de Callan-Symanzik y Flujo de RG
La física real observable de las interacciones cuánticas no puede depender de la escala arbitraria de renormalización $\mu$ introducida durante la regularización dimensional. 
Esta invarianza forzada se condensa en la **Ecuación de Callan-Symanzik**, la cual rige cómo cambian los parámetros físicos de la teoría.
La consecuencia directa es el **Grupo de Renormalización (RG)**, que revela que las constantes de "acoplamiento" no son realmente constantes. "Fluyen" o evolucionan en función de la escala de energía a la que se sondea el sistema.
- En QED, la carga eléctrica efectiva *aumenta* a muy altas energías (distancias cortas).
- En QCD, la carga de color efectiva *disminuye* drásticamente a muy altas energías.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Harvard Physics 253a: Quantum Field Theory (Sidney Coleman)](https://www.youtube.com/playlist?list=PLhsb6tmzSpiwrZerOUkt_pUFKOGrwzsCW) - Las lecturas legendarias e históricas de Coleman. Obligatorias.
- [David Tong: Lectures on Quantum Field Theory (Cambridge)](https://www.youtube.com/playlist?list=PLbBsZ8Y0xR422Dts1AILp5-Fm4m_Uo4w7) - Modernas, elegantes y clarísimas.
- [Stanford: Advanced Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLGjGECIym1354Fh8a8H1lJb6pLox56F-F) - Puente perfecto entre QM y Segunda Cuantización.
