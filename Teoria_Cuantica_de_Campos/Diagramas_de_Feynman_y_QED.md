# Diagramas de Feynman y Electrodinámica Cuántica (QED)

La **Electrodinámica Cuántica (QED)** fue la primera QFT verdaderamente completa. Describe cómo la luz (fotones) y la materia (electrones) interactúan, y está considerada la teoría física más precisa jamás concebida por el ser humano (concordancia entre teoría y experimento hasta en 10 cifras decimales para el momento magnético anómalo del electrón).

## 1. La Matriz S (Matriz de Dispersión)
Cuando dos partículas chocan (ej. dos electrones en el vacío cuántico), interactúan intercambiando fotones virtuales. 

El estado inicial $| i \rangle$ en $t \to -\infty$ evoluciona al estado final $| f \rangle$ en $t \to +\infty$ mediante el Operador de Evolución $S$. El cuadrado de la amplitud de probabilidad nos da la "sección eficaz" $\sigma$ de que ocurra esa colisión particular:

$$
\mathcal{M} = \langle f | S | i \rangle
$$

## 2. Expansión Perturbativa
Debido a que las interacciones cuánticas son brutalmente complejas, calculamos la matriz $S$ usando la Serie de Dyson, que la expande en potencias de la constante de estructura fina $\alpha \approx \frac{1}{137}$ (que actúa como constante de acoplamiento de la QED).

$$
S = I - i \int dt_1 H_I(t_1) + \frac{(-i)^2}{2!} \int dt_1 dt_2 \mathcal{T} [ H_I(t_1) H_I(t_2) ] + ...
$$

Puesto que $\alpha \ll 1$, cada término sucesivo (orden superior) es más pequeño, permitiendo aproximar el resultado de la colisión sumando los primeros términos.

## 3. Diagramas de Feynman
En 1948, Richard Feynman revolucionó la física inventando una herramienta visual y topológica para calcular estos integrales monstruosos: los Diagramas de Feynman. 

Cada término matemático de la serie perturbativa se dibuja:
- **Líneas rectas:** Fermiones (electrones, quarks). Matemáticamente son *Propagadores Fermiónicos*.
- **Líneas onduladas:** Bosones gauge (fotones). Representan *Propagadores Bosónicos*.
- **Vértices:** Puntos donde las líneas se unen. Es donde ocurre la interacción fundamental (ej. un electrón emite un fotón). Se asocia un factor de $-i e \gamma^\mu$.

Al dibujar todas las topologías posibles de un choque y sumar sus traducciones matemáticas (Reglas de Feynman), obtenemos la probabilidad total de que el evento físico suceda en la vida real.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Harvard Physics 253a: Quantum Field Theory (Sidney Coleman)](https://www.youtube.com/playlist?list=PLhsb6tmzSpiwrZerOUkt_pUFKOGrwzsCW) - Las lecturas legendarias e históricas de Coleman. Obligatorias.
- [David Tong: Lectures on Quantum Field Theory (Cambridge)](https://www.youtube.com/playlist?list=PLbBsZ8Y0xR422Dts1AILp5-Fm4m_Uo4w7) - Modernas, elegantes y clarísimas.
- [Stanford: Advanced Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLGjGECIym1354Fh8a8H1lJb6pLox56F-F) - Puente perfecto entre QM y Segunda Cuantización.
