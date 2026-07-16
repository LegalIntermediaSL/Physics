# [QFT-03] Segunda Cuantización y Espacio de Fock

La formulación de la "Primera Cuantización" (Ecuación de Schrödinger) adolece de la incapacidad de manejar rigurosamente la creación y destrucción de partículas en procesos de alta energía. Para formular una teoría relativista coherente, los estados físicos se elevan a **Campos Operacionales**.

## 1. Cuantización del Campo Escalar (Klein-Gordon)
El campo escalar real clásico $\phi(x)$ se promueve a un operador cuántico hermítico.
Expandiendo en modos de Fourier (soluciones de ondas planas):

$$
\phi(x) = \int \frac{d^3p}{(2\pi)^3 \sqrt{2E_p}} \left( a_p e^{-ip \cdot x} + a_p^\dagger e^{ip \cdot x} \right)
$$

Los coeficientes algebraicos $a_p$ y $a_p^\dagger$ se reinterpretan ahora como **Operadores de Aniquilación y Creación** de partículas con momento $p$. 
Estos operadores satisfacen las relaciones de conmutación canónicas bosónicas:

$$
[a_p, a_{p'}^\dagger] = (2\pi)^3 \delta^{(3)}(\vec{p} - \vec{p}')
$$

## 2. El Espacio de Fock
El espacio de Hilbert de multipatículas asociado a estos campos se denomina **Espacio de Fock**.
Se construye aplicando iterativamente los operadores de creación $a_p^\dagger$ al **estado de Vacío $|0\rangle$** (definido como el estado aniquilado por todos los operadores: $a_p |0\rangle = 0$):

$$
|p_1, p_2, \dots, p_n\rangle = \frac{1}{\sqrt{n!}} a_{p_1}^\dagger a_{p_2}^\dagger \dots a_{p_n}^\dagger |0\rangle
$$

Para evitar el problema de la energía infinita de punto cero del vacío, se define el **Ordenamiento Normal ($N[\dots]$)**, que empuja sistemáticamente todos los operadores de aniquilación $a_p$ a la derecha.

## 3. Propagador de Feynman
La amplitud mecánica cuántica de que una partícula se propague del punto $y$ al punto $x$ está gobernada por el Propagador de Feynman:

$$
D_F(x - y) = \langle 0 | T\{ \phi(x) \phi(y) \} | 0 \rangle = \int \frac{d^4p}{(2\pi)^4} \frac{i}{p^2 - m^2 + i\epsilon} e^{-ip \cdot (x-y)}
$$

El factor analítico $i\epsilon$ impone la prescripción correcta de contorno para la integración en el plano complejo, garantizando la causalidad física: las antipartículas pueden interpretarse matemáticamente como partículas viajando hacia atrás en el tiempo.

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
