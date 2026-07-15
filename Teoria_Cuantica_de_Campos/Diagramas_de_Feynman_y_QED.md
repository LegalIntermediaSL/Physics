# Matriz S, Teorema de Wick y Electrodinámica Cuántica (QED)

El objetivo final de QFT es calcular probabilidades teóricas observables para compararlas con experimentos en aceleradores de partículas (secciones eficaces, tasas de decaimiento). Esto requiere evaluar la evolución cuántica entre un estado inicial y uno final.

## 1. La Matriz S y Expansión Perturbativa
La **Matriz de Dispersión (Matriz S)** es un operador unitario que mapea estados asintóticamente libres en el pasado remoto ($t \to -\infty$) a estados libres en el futuro remoto ($t \to +\infty$).
Su desarrollo formal pertubativo viene dado por la serie de Dyson:

$$
S = T \exp\left( -i \int d^4x \, \mathcal{H}_I(x) \right)
$$

Donde $T$ es el operador de ordenamiento temporal, asegurando la preservación de la causalidad.

## 2. El Teorema de Wick
Para calcular de manera pragmática los valores esperados de vacío de cadenas ordenadas temporalmente $\langle 0 | T\{ \dots \} | 0 \rangle$, se utiliza el **Teorema de Wick**. 
Este teorema reduce un producto complejo de operadores de campo a una suma de todas las posibles contracciones a pares (emparejamientos). Físicamente, cada contracción corresponde a un **Propagador de Feynman** interno.

## 3. Electrodinámica Cuántica (QED) y Sección Eficaz
El Lagrangiano de QED describe la interacción fundamental entre la materia cargada (fermión de Dirac $\psi$) y el campo electromagnético cuántico (fotón $A_\mu$):

$$
\mathcal{L}_{QED} = \bar{\psi} (i\gamma^\mu D_\mu - m) \psi - \frac{1}{4} F_{\mu\nu} F^{\mu\nu}
$$

Con la derivada covariante $D_\mu = \partial_\mu + i e A_\mu$.
Las **Reglas de Feynman** abstraen el cálculo algebraico en topología gráfica:
- **Vértice**: Contribuye con un factor de acoplamiento $-ie\gamma^\mu$.
- **Propagador Fermiónico interno**: $i / (\gamma^\mu p_\mu - m)$.
- **Propagador del Fotón interno**: $-i\eta_{\mu\nu}/q^2$.
Sumando estos diagramas topológicos obtenemos la amplitud de transición invariante $\mathcal{M}$, a partir de la cual extraemos la **Sección Eficaz Diferencial (Cross-Section)** $d\sigma \sim |\mathcal{M}|^2 d\Pi_{LIPS}$, verificable empíricamente.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Harvard Physics 253a: Quantum Field Theory (Sidney Coleman)](https://www.youtube.com/playlist?list=PLhsb6tmzSpiwrZerOUkt_pUFKOGrwzsCW) - Las lecturas legendarias e históricas de Coleman. Obligatorias.
- [David Tong: Lectures on Quantum Field Theory (Cambridge)](https://www.youtube.com/playlist?list=PLbBsZ8Y0xR422Dts1AILp5-Fm4m_Uo4w7) - Modernas, elegantes y clarísimas.
- [Stanford: Advanced Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLGjGECIym1354Fh8a8H1lJb6pLox56F-F) - Puente perfecto entre QM y Segunda Cuantización.
