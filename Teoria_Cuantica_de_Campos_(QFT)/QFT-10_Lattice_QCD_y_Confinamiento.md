# [QFT-10] CromoDinámica Cuántica en el Retículo (Lattice QCD)

La Cromodinámica Cuántica (QCD) es la teoría gauge que describe la fuerza fuerte entre los Quarks mediada por los Gluones ($SU(3)$). Presenta dos propiedades asintóticas límite extremas y opuestas. A altísimas energías goza de **Libertad Asintótica**: los quarks apenas interactúan. Pero a bajas energías, el acoplamiento diverge, invalidando cualquier cálculo perturbativo estándar. 

## 1. Acción de Wilson y Plaquetas
Para poder realizar cálculos físicos en el régimen no-perturbativo de bajas energías, discretizamos el espaciotiempo continuo euclidiano en una cuadrícula discreta o **Lattice (Retículo)**.
En este marco analítico, los campos continuos de gluones $A_\mu$ se reemplazan por **Enlaces (Links) $U_\mu(x)$**, matrices discretas situadas en las aristas del retículo conectando puntos vecinos.
La Acción gauge de Yang-Mills se evalúa multiplicando las matrices de estos enlaces conformando cuadrados geométricos elementales cerrados, denominados **Plaquetas ($W_{\mu\nu}$)**. Esta construcción geométrica garantiza la invarianza gauge de forma exacta sin necesidad de fijar un gauge (gauge-fixing).

## 2. El Confinamiento de Color
La técnica de Lattice QCD ha permitido demostrar, mediante simulaciones computacionales formidables, el fenómeno del **Confinamiento Cuántico**.
Al tratar de separar experimental y analíticamente dos quarks, el flujo del campo gluónico no se disipa en el espacio como ocurre con el campo eléctrico clásico. En cambio, por la auto-interacción no abeliana de los gluones, se condensa formando un "tubo de flujo" tenso de dimensiones casi 1D.
La energía potencial del sistema crece linealmente con la distancia $V(r) \sim \sigma r$. Antes de poder separar los quarks y observar un quark aislado, el tubo acumula energía suficiente para romperse rompiendo el vacío topológico, induciendo la creación de un nuevo par quark-antiquark. Consecuentemente, el color gauge permanece eternamente confinado.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Harvard Physics 253a: Quantum Field Theory (Sidney Coleman)](https://www.youtube.com/playlist?list=PLhsb6tmzSpiwrZerOUkt_pUFKOGrwzsCW) - Las lecturas legendarias e históricas de Coleman. Obligatorias.
- [David Tong: Lectures on Quantum Field Theory (Cambridge)](https://www.youtube.com/playlist?list=PLbBsZ8Y0xR422Dts1AILp5-Fm4m_Uo4w7) - Modernas, elegantes y clarísimas.
- [Stanford: Advanced Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLGjGECIym1354Fh8a8H1lJb6pLox56F-F) - Puente perfecto entre QM y Segunda Cuantización.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Cambridge DAMTP: Quantum Field Theory](http://www.damtp.cam.ac.uk/user/tong/qft.html) - David Tong. (Las notas de clase en vídeo más famosas de la década).
  - [Harvard: Quantum Field Theory I](https://scholar.harvard.edu/schwartz) - Matthew Schwartz.
- **Libros de Texto Canónicos:**
  - *An Introduction to Quantum Field Theory* - Michael E. Peskin & Daniel V. Schroeder. (El estándar de oro para cálculos con diagramas de Feynman).
  - *Quantum Field Theory in a Nutshell* - A. Zee. (Enfoque conceptual y fascinante).
  - *Quantum Field Theory and the Standard Model* - Matthew D. Schwartz.
