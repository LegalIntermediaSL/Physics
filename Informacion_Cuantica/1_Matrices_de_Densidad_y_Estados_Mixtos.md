# Matrices de Densidad y Estados Mixtos

El formalismo de vectores de estado ($|\psi\rangle$) es insuficiente cuando interactuamos con el mundo real. Un ket solo describe un **estado puro**: un sistema aislado del que poseemos información máxima y perfecta.
En el laboratorio, los sistemas sufren descoherencia térmica, ruido y entrelazamiento con el entorno. Para describir nuestra ignorancia estadística sobre un sistema cuántico, John von Neumann introdujo el formalismo supremo de la mecánica cuántica: la **Matriz de Densidad ($\rho$)**.

## 1. Definición Formal
Un estado mixto es un ensamble estadístico cuántico donde el sistema tiene una probabilidad clásica $p_i$ de encontrarse en el estado puro cuántico $|\psi_i\rangle$. La matriz de densidad se define como:

$$
\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

Donde $\sum_i p_i = 1$ y $p_i \geq 0$.

## 2. Propiedades Matemáticas Obligatorias
Toda matriz de densidad física debe cumplir tres postulados férreos:
1. **Hermiticidad**: $\rho = \rho^\dagger$ (Sus autovalores representan probabilidades físicas reales).
2. **Traza Unitaria**: $\text{Tr}(\rho) = 1$ (La suma de todas las probabilidades debe ser el 100%).
3. **Semi-definida Positiva**: $\langle \phi | \rho | \phi \rangle \geq 0$ para todo $|\phi\rangle$ (No existen probabilidades negativas).

## 3. Pureza: El Test del Estado
Para discernir matemáticamente si estamos ante un estado puro o un batiburrillo ruidoso (estado mixto), evaluamos la **Pureza**, definida como la traza del cuadrado de la matriz:

$$
\mathcal{P} = \text{Tr}(\rho^2)
$$

- Si $\text{Tr}(\rho^2) = 1$, el estado es **Absolutamente Puro**.
- Si $\text{Tr}(\rho^2) < 1$, el estado es **Mixto**.
Para un sistema de dimensión $d$, el estado máxima y caóticamente mixto (como ruido blanco cuántico puro) es proporcional a la matriz identidad $\rho = \frac{1}{d} I$, cuya pureza cae a su mínimo teórico $\frac{1}{d}$.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.370: Quantum Computation](https://ocw.mit.edu/courses/8-370-quantum-computation-fall-2020/) - Prof. Peter Shor (Inventor del Algoritmo de Shor).
  - [Qiskit Textbook (IBM)](https://qiskit.org/textbook/preface.html) - Curso interactivo gratuito de IBM Quantum.
- **Libros de Texto Canónicos:**
  - *Quantum Computation and Quantum Information* - Michael A. Nielsen & Isaac L. Chuang. (Conocido universalmente como "Mike & Ike", la Biblia absoluta del campo).
  - *Quantum Computing since Democritus* - Scott Aaronson.
