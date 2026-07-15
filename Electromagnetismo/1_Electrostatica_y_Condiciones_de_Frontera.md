# Electrostática y Problemas de Valores en la Frontera

La electrostática es el régimen donde las densidades de carga están estáticas ($\partial \rho / \partial t = 0$), lo que desactiva el Campo Magnético. El campo eléctrico $\vec{E}$ se vuelve puramente conservativo ($\nabla \times \vec{E} = 0$), permitiendo la definición global de un Potencial Escalar Unívoco: $\vec{E} = -\nabla \Phi$.

## 1. La Ecuación de Poisson y Laplace
Sustituyendo el potencial en la Ley de Gauss Diferencial ($\nabla \cdot \vec{E} = \rho/\varepsilon_0$), obtenemos la ecuación rectora absoluta de la estática:

$$
\nabla^2 \Phi = -\frac{\rho}{\varepsilon_0}
$$

En el vacío (lejos de las fuentes), esto colapsa a la Ecuación de Laplace ($\nabla^2 \Phi = 0$).
Las soluciones de Laplace son **Funciones Armónicas**. Matemáticamente, carecen de máximos o mínimos locales en el interior de su dominio (Teorema del Valor Medio), y quedan rígidamente fijadas por las Condiciones de Contorno de Dirichlet (voltaje fijado) o Neumann (derivada normal fijada) en los bordes metálicos.

## 2. Expansión Multipolar
Cuando observamos una nube de cargas (moléculas, antenas) desde muy lejos ($r \to \infty$), no percibimos la estructura geométrica fina. Expandiendo el factor geométrico $\frac{1}{|\vec{r} - \vec{r}'|}$ en Polinomios de Legendre, obtenemos la Expansión Multipolar exacta:

$$
\Phi(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \left[ \frac{Q}{r} + \frac{\vec{p} \cdot \hat{r}}{r^2} + \frac{1}{2 r^3} \sum_{i,j} \hat{r}_i \hat{r}_j Q_{ij} + \dots \right]
$$

- **Monopolo ($Q$)**: Carga neta. Cae como $1/r$.
- **Dipolo ($\vec{p}$)**: Asimetría espacial lineal. Cae como $1/r^2$.
- **Cuadrupolo ($Q_{ij}$)**: Tensor de asimetría elipsoidal. Cae como $1/r^3$.

## 3. El Método de las Cargas Imágenes
Para resolver problemas de frontera con metales conductores perfectos (equipotenciales $\Phi=0$), el Teorema de Unicidad de Dirichlet permite reemplazar el muro metálico con el vacío, situando espejismos abstractos de "Cargas Imágenes" fuera del dominio físico, de modo que sus interferencias fuercen el potencial a cero en la frontera original. 

## 4. Formalismo de Funciones de Green
La Ecuación de Poisson es lineal. El potencial es la suma integral de las perturbaciones infinitesimales esféricas puntuales. La Función de Green $G(\vec{r}, \vec{r}')$ es la respuesta topológica impulsional del universo a una sola carga puntual $\delta$-Dirac colocada en $\vec{r}'$:

$$
\nabla^2 G(\vec{r}, \vec{r}') = -4\pi \delta(\vec{r} - \vec{r}')
$$

La solución universal (Identidad de Green) para cualquier geometría es:

$$
\Phi(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \rho(\vec{r}') G \, d\tau' + \frac{1}{4\pi} \oint_S \left[ G \frac{\partial \Phi}{\partial n'} - \Phi \frac{\partial G}{\partial n'} \right] da'
$$

