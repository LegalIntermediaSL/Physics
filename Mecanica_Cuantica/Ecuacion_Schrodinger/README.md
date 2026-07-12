# La Ecuación de Schrödinger

La ecuación de Schrödinger es la piedra angular de la mecánica cuántica no relativista, análoga a la segunda ley de Newton en la mecánica clásica. Describe cómo evoluciona en el espacio y el tiempo el estado cuántico (la función de onda) de un sistema físico.

## 📜 Contexto Histórico
* **Erwin Schrödinger (1926):** Inspirado por la tesis de de Broglie, buscó una ecuación de onda continua que describiera a los electrones en los átomos, publicando la ecuación que hoy lleva su nombre.
* **Max Born (1926):** Proporcionó la interpretación física de la función de onda $\Psi$. Afirmó que $\Psi$ en sí no es algo físico, sino que el cuadrado de su módulo $|\Psi|^2$ representa la **densidad de probabilidad** de encontrar a la partícula en un punto del espacio.
* Este trabajo consolidó el formalismo de la mecánica ondulatoria, que se demostró equivalente a la mecánica matricial de Werner Heisenberg.

---

## 🧮 Desarrollo Teórico Profundo

### La Ecuación Dependiente del Tiempo
La evolución temporal de una función de onda $\Psi(\vec{r}, t)$ se rige por:
$$ i\hbar \frac{\partial}{\partial t} \Psi(\vec{r}, t) = \hat{H} \Psi(\vec{r}, t) $$
Donde $\hbar = h/2\pi$ y $\hat{H}$ es el operador Hamiltoniano, que corresponde a la energía total del sistema (cinética + potencial):
$$ \hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r}, t) $$

### La Ecuación Independiente del Tiempo
Si el potencial $V$ no depende explícitamente del tiempo, $V = V(\vec{r})$, podemos aplicar el método de separación de variables: $\Psi(\vec{r}, t) = \psi(\vec{r})e^{-iEt/\hbar}$.
Sustituyendo esto en la ecuación dependiente del tiempo, obtenemos la ecuación de Schrödinger independiente del tiempo (un problema de autovalores):
$$ \left( -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r}) \right) \psi(\vec{r}) = E \psi(\vec{r}) $$
Donde $E$ son los valores posibles de energía (autovalores) y $\psi(\vec{r})$ son los estados estacionarios.

### Interpretación de Born y Normalización
La función de onda debe ser de cuadrado integrable para tener sentido probabilístico. La probabilidad de encontrar la partícula en todo el espacio debe ser 1:
$$ \int_{-\infty}^{\infty} |\Psi(\vec{r}, t)|^2 d^3r = 1 $$

---

## 🛠 Ejemplo Práctico
**Problema:** Demostrar que para un estado estacionario $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$, la densidad de probabilidad no depende del tiempo.

**Solución paso a paso:**
1. Escribimos la expresión para la densidad de probabilidad:
$$ \rho(x,t) = |\Psi(x,t)|^2 = \Psi^*(x,t) \Psi(x,t) $$
2. Sustituimos la forma del estado estacionario. Recordemos que el conjugado complejo de $e^{-iEt/\hbar}$ es $e^{+iEt/\hbar}$:
$$ \Psi^*(x,t) = \psi^*(x)e^{+iEt/\hbar} $$
3. Calculamos el producto:
$$ \rho(x,t) = \left( \psi^*(x)e^{+iEt/\hbar} \right) \left( \psi(x)e^{-iEt/\hbar} \right) $$
4. Los términos exponenciales se cancelan ya que sus exponentes suman cero ($e^{0} = 1$):
$$ \rho(x,t) = \psi^*(x)\psi(x) e^{i(E-E)t/\hbar} = |\psi(x)|^2 $$
Dado que $|\psi(x)|^2$ solo depende de la coordenada espacial $x$, la densidad de probabilidad (y todos los valores esperados de operadores que no dependan explícitamente del tiempo) son constantes en el tiempo. ¡Por eso se llaman *estados estacionarios*!

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
* **MIT 8.04 Quantum Physics I:** Clases sobre la construcción heurística de la ecuación de Schrödinger.
* **Stanford - Quantum Mechanics:** Conferencias de Susskind enfocadas en la evolución temporal y el operador Hamiltoniano.
* **Yale PHYS 201:** Principios Básicos de la Mecánica Cuántica (Prof. Ramamurti Shankar).

### 📝 Artículos e Interactivos Interesantes
* **PhET Interactive Simulations:** *Quantum Wave Interference* (Para visualizar ondas probabilísticas).
* **Visual Quantum Mechanics (VQM):** Simuladores de evolución temporal de paquetes de ondas.
* **Wikipedia:** [Ecuación de Schrödinger](https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_Schr%C3%B6dinger) (Lectura matemática profunda de su derivación y simetrías).
