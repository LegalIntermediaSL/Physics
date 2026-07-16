# [NLD-06] Sincronización y Modelo de Kuramoto

## 1. Sincronización Espontánea en la Naturaleza
El fenómeno del bloqueo de fase y sincronización colectiva de osciladores biológicos (luciérnagas sincronizadas, marcapasos neuronales, láseres) emerge sin un controlador central, impulsado por acoplamiento mutuo de sistemas dinámicos.

## 2. El Modelo Acoplado de Kuramoto
Osciladores de fase no lineales, cada uno con frecuencia natural $\omega_i$, interactuando globalmente con una fuerza de acoplamiento $K$:

$$
\frac{d\theta_i}{dt} = \omega_i + \frac{K}{N} \sum_{j=1}^N \sin(\theta_j - \theta_i) \quad \text{para } i=1, \dots, N
$$

## 3. Parámetro de Orden de Kuramoto
Para medir la sincronización macroscópica se define el parámetro de orden en el plano complejo $re^{i\psi}$:

$$
re^{i\psi} = \frac{1}{N} \sum_{j=1}^N e^{i\theta_j}
$$

Donde:
- $0 \le r \le 1$ es el nivel de coherencia (1=sincronización total).
- $\psi$ es la fase media de la población colectiva.

Reemplazando en las ecuaciones:

$$
\frac{d\theta_i}{dt} = \omega_i + K r \sin(\psi - \theta_i)
$$

## 4. Transición de Fase
Para una distribución lorentziana o gaussiana simétrica de frecuencias $g(\omega)$ de varianza $\gamma$, el estado de sincronía parcial estalla drásticamente mediante una bifurcación supercrítica cuando el acoplamiento $K$ excede un umbral crítico $K_c$:

$$
K_c = \frac{2}{\pi g(0)}
$$

Por encima de este valor, una fracción de la población entra en enclavamiento de fase, comportándose como una "condensación de Bose-Einstein" clásica.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Santa Fe Institute (Complexity Explorer)](https://www.complexityexplorer.org/) - Cursos en Dinámica No Lineal, Caos y Sistemas Complejos.
  - [MIT 2.050J: Nonlinear Dynamics and Chaos](https://ocw.mit.edu/courses/18-062j-mathematics-of-machine-learning-fall-2015/) - Prof. Steven Strogatz (Cornell Lectures, muy populares en YouTube).
- **Libros de Texto Canónicos:**
  - *Nonlinear Dynamics and Chaos* - Steven H. Strogatz. (La "Biblia" introductoria).
  - *Classical Mechanics* (Sección de Caos) - John R. Taylor.
  - *Fractal Geometry of Nature* - Benoit Mandelbrot.
