# Espacios de Hilbert y Notación de Dirac (Bra-Ket)

En Mecánica Cuántica Clásica (como se formula en el siglo XIX), usaríamos ecuaciones en derivadas parciales. Sin embargo, Paul Dirac unificó la Mecánica Matricial de Heisenberg y la Mecánica Ondulatoria de Schrödinger demostrando que ambas son simples proyecciones geométricas sobre un mismo espacio vectorial abstracto: **El Espacio de Hilbert** ($\mathcal{H}$).

## 1. El Espacio de Hilbert
Un Espacio de Hilbert es un espacio vectorial sobre el cuerpo de los números complejos ($\mathbb{C}$) dotado de un **producto interno** (producto escalar), y que además es **completo** (las secuencias de Cauchy convergen dentro del propio espacio, permitiéndonos realizar cálculo analítico con vectores de dimensión infinita).

El estado físico de un sistema cuántico (ej. un electrón en un átomo) está completamente representado por un vector (rayo) unitario abstracto $|\psi\rangle \in \mathcal{H}$.

## 2. Los Kets (Vectores) y los Bras (Covectores)
Para simplificar el álgebra lineal infinita, Dirac inventó su famosa notación:

*   **El Ket ($|\psi\rangle$):** Es un vector columna en el espacio de Hilbert primario.
*   **El Bra ($\langle\phi|$):** Es el covector dual transpuesto conjugado. Vive en el espacio dual $\mathcal{H}^*$. Matemáticamente, es un operador lineal (funcional) que "se come" un Ket y devuelve un número complejo.

## 3. El Producto Interno y Ortogonalidad
Al superponer un Bra sobre un Ket, realizamos el producto interno (bracket):

$$
\langle \phi | \psi \rangle = \int \phi^*(x) \psi(x) dx \quad \in \mathbb{C}
$$

(En representación de posición).

*   Si $\langle \phi | \psi \rangle = 0$, los estados cuánticos son **ortogonales** (son mutuamente excluyentes).
*   La probabilidad física fundamental (Postulado de Born) de que el sistema salte del estado $|\psi\rangle$ al estado $|\phi\rangle$ viene dada por el módulo al cuadrado de esta superposición geométrica:
    

$$
P(\psi \to \phi) = |\langle \phi | \psi \rangle|^2
$$

