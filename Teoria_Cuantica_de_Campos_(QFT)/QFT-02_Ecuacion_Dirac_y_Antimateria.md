# [QFT-02] Ecuación de Dirac, Espinores y Antimateria

Paul Dirac buscaba formular una ecuación de onda relativista que fuera lineal tanto en derivadas espaciales como temporales, garantizando así densidades de probabilidad positivas que la ecuación de Klein-Gordon inicialmente fallaba en proveer.

## 1. Álgebra de Clifford y la Ecuación de Dirac
Para linealizar el operador diferencial relativista de d'Alembert $\partial^2 + m^2$, Dirac postuló la existencia de cuatro matrices anticomutantes $\gamma^\mu$, conocidas como las **Matrices de Dirac**.
Estas matrices satisfacen el Álgebra de Clifford:

$$
\{ \gamma^\mu, \gamma^\nu \} = \gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2\eta^{\mu\nu} \mathbb{I}_{4\times4}
$$

La Ecuación de Dirac resultante se expresa elegantemente como:

$$
(i\gamma^\mu \partial_\mu - m) \psi = 0
$$

La función de onda $\psi(x)$ no es un campo escalar ni un vector espacial, sino un **Espinor de Dirac** de cuatro componentes complejas.

## 2. Anticonmutación y el Principio de Exclusión
Al cuantizar el campo espinorial de Dirac para electrones, nos topamos con un problema fundamental: el hamiltoniano carece de cota inferior si usamos conmutadores bosónicos estándar (produciendo el colapso del vacío). 
Para resolverlo y asegurar una energía positiva definida, debemos cuantizar el campo fermiónico utilizando **Anticonmutadores**:

$$
\{ \psi_\alpha(\vec{x}), \psi^\dagger_\beta(\vec{y}) \} = \delta^{(3)}(\vec{x} - \vec{y}) \delta_{\alpha\beta}
$$

Esta sencilla imposición algebraica es el origen riguroso del **Principio de Exclusión de Pauli**.
La expansión en modos del espinor cuantizado requiere dos conjuntos de soluciones de polarización: $u^s(p)$ para partículas de materia (electrones) y $v^s(p)$ para estados de energía negativa, que reinterpretamos como las antipartículas (positrones).

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
