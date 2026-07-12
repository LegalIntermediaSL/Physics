# Dinámica de Fluidos

La dinámica de fluidos estudia cómo se mueven líquidos y gases bajo la acción de fuerzas, gradientes de presión y condiciones de contorno. Es esencial para describir el flujo sanguíneo, la atmósfera, la aerodinámica, las tuberías, la oceanografía y una enorme cantidad de sistemas naturales y tecnológicos.

## Conceptos Fundamentales

- **Campo de velocidad**: Cada punto del fluido tiene asociada una velocidad $\vec{v}(\vec{r},t)$.
- **Descripción euleriana**: Observa el flujo desde puntos fijos en el espacio.
- **Descripción lagrangiana**: Sigue el movimiento de partículas del fluido.
- **Caudal**: Cantidad de fluido que cruza una sección por unidad de tiempo.

## Ecuaciones Clave

- **Conservación de masa**:
  $$ \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0 $$
- **Fluido incompresible**:
  $$ \nabla \cdot \vec{v} = 0 $$
- **Bernoulli**:
  $$ p + \frac{1}{2}\rho v^2 + \rho g z = \text{cte} $$
- **Balance de momento**:
  Base para llegar a las ecuaciones de Euler y Navier-Stokes.

## Temas Importantes

### 1. Flujo ideal vs viscoso
El modelo ideal es muy útil, pero los efectos viscosos suelen dominar cerca de superficies y en conductos.

### 2. Vorticidad
Permite entender rotación local, remolinos y circulación.

### 3. Números adimensionales
El número de Reynolds, entre otros, ayuda a comparar regímenes físicos muy distintos.

## 📚 Recursos
### Cursos Específicos
1. ["Introduction to Fluid Dynamics" - Coursera](https://www.coursera.org/learn/fluid-dynamics)
2. ["Advanced Fluid Dynamics" - MIT OpenCourseWare](https://ocw.mit.edu/courses/mechanical-engineering/2-25-advanced-fluid-mechanics-fall-2013/)
3. ["Computational Fluid Dynamics" - edX](https://www.edx.org/course/computational-fluid-dynamics)
4. ["Fluid Mechanics and Its Applications" - NPTEL](https://nptel.ac.in/courses/112105171)
5. ["Astrophysical Fluid Dynamics" - Coursera](https://www.coursera.org/learn/astrophysics)
6. ["Aerodynamics and Fluid Flow" - Udemy](https://www.udemy.com/course/aerodynamics/)

### Artículos y Simulaciones
1. ["Hydrodynamica" - Daniel Bernoulli](https://archive.org/details/hydrodynamica00bern)
2. ["On the Equations of Motion of a Viscous Fluid" - G.G. Stokes](https://royalsocietypublishing.org/)
3. [OpenFOAM Tutorials and Simulations](https://www.openfoam.com/documentation/tutorial-guide)
4. [PhET Fluid Pressure and Flow Simulation](https://phet.colorado.edu/en/simulations/fluid-pressure-and-flow)
5. [Ansys Fluent Basic Simulations Guide](https://www.ansys.com/products/fluids/ansys-fluent)
6. ["The Theory of Homogeneous Turbulence" - G.K. Batchelor](https://www.amazon.com/Theory-Homogeneous-Turbulence-Cambridge-Science/dp/0521041171)
7. [CFD Online Reference Flow Problems](https://www.cfd-online.com/)
8. [NASA's FoilSim educational software](https://www.grc.nasa.gov/WWW/K-12/FoilSim/index.html)
9. ["A Mathematical Theory of Fluid Mechanics" - J. Serrin](https://link.springer.com/chapter/10.1007/978-3-642-46015-9_3)
10. ["Visualized Fluid Dynamics" - National Committee for Fluid Mechanics Films](http://web.mit.edu/hml/ncfmf.html)

### 📖 Referencias Útiles y Bibliografía
1. [*Fluid Mechanics* - L.D. Landau y E.M. Lifshitz](https://www.amazon.com/Fluid-Mechanics-Second-Theoretical-Physics/dp/0080339336)
2. [*Fluid Mechanics* - Pijush K. Kundu, Ira M. Cohen](https://www.amazon.com/Fluid-Mechanics-Pijush-K-Kundu/dp/012405935X)
3. [*An Introduction to Fluid Dynamics* - G.K. Batchelor](https://www.amazon.com/Introduction-Fluid-Dynamics-Cambridge-Mathematical/dp/0521663962)
4. [*Introduction to Fluid Mechanics* - R.W. Fox, A.T. McDonald](https://www.amazon.com/Fox-McDonalds-Introduction-Fluid-Mechanics/dp/1119616175)
