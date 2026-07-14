# Física Computacional

La física computacional representa el "tercer pilar" del método científico, complementando la teoría y la experimentación. Involucra el diseño de algoritmos, simulaciones numéricas, modelado y análisis de datos para estudiar problemas físicos que son demasiado complejos (como interacciones de muchos cuerpos o sistemas caóticos) para resolverse analíticamente con papel y lápiz.

## 📜 Contexto Histórico

Los orígenes de la física computacional se encuentran durante el Proyecto Manhattan en la década de 1940, donde figuras como Stanislaw Ulam, John von Neumann y Nicholas Metropolis desarrollaron el Método de Montecarlo (nombrado así por los casinos de Mónaco) para simular la difusión de neutrones utilizando una de las primeras computadoras, la ENIAC. En los años 50, Fermi, Pasta y Ulam ejecutaron las primeras simulaciones de dinámica molecular numérica. Desde entonces, el crecimiento del poder de cómputo y los algoritmos eficientes (como la FFT, transformada rápida de Fourier) han hecho de la computación una herramienta indispensable en astrofísica, materia condensada, partículas y biología molecular.

## 🧮 Desarrollo Teórico Profundo

Existen varios enfoques algorítmicos fundamentales:

1. **Dinámica Molecular (MD):** Simula el movimiento de partículas resolviendo numéricamente las ecuaciones de Newton. Un algoritmo crucial para mantener la estabilidad simpléctica y conservar la energía es el algoritmo de **Verlet**:

   

$$
\mathbf{r}(t + \Delta t) \approx 2\mathbf{r}(t) - \mathbf{r}(t - \Delta t) + \frac{\mathbf{F}(t)}{m} \Delta t^2
$$

   
2. **Métodos de Montecarlo (MC):** Se utilizan para muestrear integrales de alta dimensión o termodinámica estadística estadística. El **Algoritmo de Metropolis-Hastings** genera una caminata aleatoria que converge a la distribución de Boltzmann. Una transición de un estado $\mu$ a un estado $\nu$ se acepta con una probabilidad:

   

$$
A(\mu \to \nu) = \min\left( 1, e^{-\beta(E_\nu - E_\mu)} \right)
$$

3. **Ecuaciones en Derivadas Parciales (PDEs):** Para sistemas continuos (mecánica de fluidos, electromagnetismo, ecuación de Schrödinger). Se utilizan los métodos de **Diferencias Finitas (FDM)** o **Elementos Finitos (FEM)**. Por ejemplo, el Laplaciano discreto en 2D:

   

$$
\nabla^2 \phi(x,y) \approx \frac{\phi_{i+1,j} + \phi_{i-1,j} + \phi_{i,j+1} + \phi_{i,j-1} - 4\phi_{i,j}}{(\Delta x)^2}
$$

## 🛠 Ejemplo Práctico

**Problema:** Integración numérica de caída libre usando el método de Euler vs. Verlet.

Asuma $a = -g = -9.8$. Condiciones iniciales: $y_0 = 10$, $v_0 = 0$, paso $\Delta t = 0.1$. Calcular $y(0.2)$.

**Solución paso a paso:**
1. **Solución Analítica:** $y(t) = y_0 - \frac{1}{2}gt^2$.
   Para $t=0.2$: $y(0.2) = 10 - 0.5(9.8)(0.04) = 10 - 0.196 = 9.804$.
2. **Método de Euler (Primer Orden):**
   Iteración 1 ($t=0.1$):

   

$$
y_1 = y_0 + v_0 \Delta t = 10 + (0)(0.1) = 10
$$

   

$$
v_1 = v_0 - g \Delta t = 0 - 9.8(0.1) = -0.98
$$

   Iteración 2 ($t=0.2$):

   

$$
y_2 = y_1 + v_1 \Delta t = 10 - 0.98(0.1) = 9.902
$$

   *Error de Euler:* $9.902 - 9.804 = +0.098$.
3. **Método de Verlet:** Requiere conocer un paso previo. Usaremos el de Euler inverso para $y_{-1}$: $y_{-1} = y_0 - v_0\Delta t + 0.5(-g)\Delta t^2 = 10 - 0 - 0.049 = 9.951$.
   Iteración 1 ($t=0.1$):

   

$$
y_1 = 2y_0 - y_{-1} - g\Delta t^2 = 2(10) - 9.951 - 9.8(0.01) = 20 - 9.951 - 0.098 = 9.951
$$

   Iteración 2 ($t=0.2$):

   

$$
y_2 = 2y_1 - y_0 - g\Delta t^2 = 2(9.951) - 10 - 0.098 = 19.902 - 10 - 0.098 = 9.804
$$

**Conclusión:** El método de Verlet provee el resultado analítico exacto para aceleración constante (error de precisión de máquina), demostrando por qué es vastamente superior a Euler para dinámicas sin disipación.

## 📚 Recursos Específicos

### Cursos
1. [**Computational Physics (Coursera/Vanderbilt)**](https://www.coursera.org/learn/computational-physics)
2. [**MIT 8.290 - Computational Physics**](https://ocw.mit.edu/courses/8-290-computational-physics-fall-2004/)
3. [**University of Michigan - Physics 411/415**](http://www-personal.umich.edu/~mejn/cp/)
4. [**Computational Science and Engineering (MIT 18.085)**](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-fall-2008/)
5. [**Kaggle - Learn Python & Machine Learning**](https://www.kaggle.com/learn)
6. [**Simulación de Sistemas Físicos (Coursera)**](https://www.coursera.org/learn/simulacion)

### Artículos y Simulaciones
1. [**GROMACS**](https://www.gromacs.org/)
2. [**LAMMPS**](https://www.lammps.org/)
3. [**PhET Interactive Simulations - Quantum Phenomena**](https://phet.colorado.edu/es/simulations/filter?subjects=quantum-phenomena)
4. [**SciPy Cookbook**](https://scipy-cookbook.readthedocs.io/)
5. [**Project Jupyter**](https://jupyter.org/)
6. [**Artículo Clásico**: "Equation of State Calculations by Fast Computing Machines"](https://aip.scitation.org/doi/10.1063/1.1699114)
7. [**Artículo Clásico**: "Computer Simulation of Liquids"](https://academic.oup.com/book/35070)
8. [**Qiskit Tutorials**](https://qiskit.org/learn/)
9. [**Simulaciones CFD (OpenFOAM)**](https://www.openfoam.com/)

### 📖 Referencias Útiles y Bibliografía
- [*Computational Physics* por Mark Newman](http://www-personal.umich.edu/~mejn/cp/)
- [*Numerical Recipes: The Art of Scientific Computing* de William H. Press et al.](http://numerical.recipes/)
- [*Introduction to Computational Physics* de Tao Pang](https://www.cambridge.org/core/books/an-introduction-to-computational-physics/E1A1184F59CBECC2EB4B10B9DBDF15F5)
- [*Computer Simulation of Liquids* por M. P. Allen y D. J. Tildesley](https://global.oup.com/academic/product/computer-simulation-of-liquids-9780198803195)
- [*A First Course in Computational Physics* por Paul L. DeVries](https://www.wiley.com/en-us/A+First+Course+in+Computational+Physics%2C+2nd+Edition-p-9781118482094)
