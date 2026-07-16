# Teoría de Bifurcaciones y Estabilidad

## 1. ¿Qué es una Bifurcación?
Es un cambio topológico cualitativo en la estructura de las soluciones de un sistema dinámico $\dot{x} = f(x, r)$ al variar un parámetro de control $r$. 

## 2. Bifurcaciones Unidimensionales (Nodos y Ensilladuras)
**Bifurcación Silla-Nodo (Saddle-Node):**
Ocurre la creación/destrucción de pares de puntos fijos.
Forma normal:

$$
\dot{x} = r - x^2
$$

**Bifurcación Transcrítica:**
Los puntos fijos intercambian su estabilidad al cruzarse.
Forma normal:

$$
\dot{x} = rx - x^2
$$

**Bifurcación de Tridente (Pitchfork):**
Supercrítica: Un punto fijo estable se vuelve inestable y crea dos nuevos puntos estables.
Forma normal:

$$
\dot{x} = rx - x^3
$$

## 3. Bifurcación de Hopf (Dimensión $\ge 2$)
Transición de un punto fijo a un ciclo límite oscilatorio (creación de ritmos espontáneos). Ocurre cuando un par de valores propios complejos conjugados de la matriz Jacobiana cruza el eje imaginario.

En coordenadas polares, la forma normal (supercrítica) es:

$$
\dot{r} = \mu r - r^3
$$

$$
\dot{\theta} = \omega + b r^2
$$

Cuando $\mu > 0$, el origen se desestabiliza y emerge un ciclo límite circular estable de radio $r = \sqrt{\mu}$.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Santa Fe Institute (Complexity Explorer)](https://www.complexityexplorer.org/) - Cursos en Dinámica No Lineal, Caos y Sistemas Complejos.
  - [MIT 2.050J: Nonlinear Dynamics and Chaos](https://ocw.mit.edu/courses/18-062j-mathematics-of-machine-learning-fall-2015/) - Prof. Steven Strogatz (Cornell Lectures, muy populares en YouTube).
- **Libros de Texto Canónicos:**
  - *Nonlinear Dynamics and Chaos* - Steven H. Strogatz. (La "Biblia" introductoria).
  - *Classical Mechanics* (Sección de Caos) - John R. Taylor.
  - *Fractal Geometry of Nature* - Benoit Mandelbrot.
