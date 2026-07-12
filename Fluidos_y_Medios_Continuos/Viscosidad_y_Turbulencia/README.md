# Viscosidad y Turbulencia
Los fluidos reales poseen fricción interna, conocida como viscosidad. Dependiendo de la velocidad y geometría, el flujo puede ser ordenado (laminar) o caótico y mezclado (turbulento). El estudio de la turbulencia es uno de los mayores problemas abiertos de la física clásica.

## 📜 Contexto Histórico
Isaac Newton fue el primero en modelar la viscosidad en 1687. En el siglo XIX, Claude-Louis Navier y George Gabriel Stokes derivaron las ecuaciones fundamentales de flujo viscoso. En 1883, Osborne Reynolds demostró experimentalmente la transición entre flujo laminar y turbulento, definiendo el Número de Reynolds.

## 🧮 Desarrollo Teórico Profundo
**Ley de Viscosidad de Newton:**
El esfuerzo cortante $ \tau $ es proporcional al gradiente de velocidad:
$$ \tau = \mu \frac{\partial u}{\partial y} $$
donde $ \mu $ es la viscosidad dinámica.

**Número de Reynolds ($ Re $):**
Un número adimensional que predice el régimen de flujo:
$$ Re = \frac{\rho v D}{\mu} = \frac{v D}{\nu} $$
donde $ D $ es una longitud característica (como el diámetro de un tubo) y $ \nu = \mu/\rho $ es la viscosidad cinemática.
- $ Re < 2100 $: Flujo Laminar
- $ 2100 < Re < 4000 $: Transición
- $ Re > 4000 $: Flujo Turbulento

**Ecuaciones de Navier-Stokes:**
La forma vectorial para fluido incompresible es:
$$ \rho \left( \frac{\partial \mathbf{v}}{\partial t} + \mathbf{v} \cdot \nabla \mathbf{v} \right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f} $$

**Ley de Poiseuille:**
Para flujo laminar a través de un tubo cilíndrico de radio $ R $ y longitud $ L $, el caudal volumétrico es:
$$ Q = \frac{\pi R^4 \Delta P}{8 \mu L} $$

## 🛠 Ejemplo Práctico
**Problema:** Sangre a $ 37^\circ \text{C} $ ($ \rho = 1060 \text{ kg/m}^3 $, $ \mu = 4 \times 10^{-3} \text{ Pa}\cdot\text{s} $) fluye a través de una arteria de $ 4 \text{ mm} $ de diámetro a una velocidad promedio de $ 0.3 \text{ m/s} $. Determina si el flujo es laminar o turbulento y calcula la caída de presión en una longitud de $ 10 \text{ cm} $.

**Solución paso a paso:**
1. Calculamos el Número de Reynolds ($ D = 0.004 \text{ m}, v = 0.3 \text{ m/s} $):
   $$ Re = \frac{\rho v D}{\mu} = \frac{1060 \times 0.3 \times 0.004}{4 \times 10^{-3}} = \frac{1.272}{0.004} = 318 $$
   Como $ Re = 318 < 2100 $, el flujo es fuertemente **laminar**.
2. Al ser laminar, podemos aplicar la Ley de Poiseuille. Relacionamos $ Q $ con $ v $:
   $$ Q = v A = v (\pi r^2) $$
3. Sustituyendo $ Q $ en la ecuación de Poiseuille ($ r = 0.002 \text{ m} $):
   $$ v \pi r^2 = \frac{\pi r^4 \Delta P}{8 \mu L} \implies \Delta P = \frac{8 \mu L v}{r^2} $$
4. Calculamos $ \Delta P $ ($ L = 0.1 \text{ m} $):
   $ \Delta P = \frac{8 (4 \times 10^{-3}) (0.1) (0.3)}{(0.002)^2} = \frac{9.6 \times 10^{-4}}{4 \times 10^{-6}} = 240 \text{ Pa} $.

## 📚 Recursos
### Cursos Específicos
1. ["Turbulent Flows" - NPTEL](https://nptel.ac.in/courses/112106266)
2. ["Advanced Fluid Mechanics: Turbulence" - MIT OCW](https://ocw.mit.edu/courses/mechanical-engineering/)
3. ["Viscous Fluid Flow and Turbulence" - Coursera](https://www.coursera.org/)
4. ["Computational Fluid Dynamics: Turbulent Models" - edX](https://www.edx.org/)
5. ["Physics of Fluids" - Coursera](https://www.coursera.org/)
6. ["Introduction to Turbulence Modeling" - NPTEL](https://nptel.ac.in/)

### Artículos y Simulaciones
1. [*Transport Phenomena* - Bird, Stewart, Lightfoot (Capítulos de Viscosidad)](https://www.amazon.com/Transport-Phenomena-Revised-2nd-Byron/dp/0470115394)
2. ["The Local Structure of Turbulence in Incompressible Viscous Fluid" - A.N. Kolmogorov (1941)](https://rspa.royalsocietypublishing.org/content/434/1890/9)
3. [OpenFOAM: Tutorials on k-epsilon and k-omega models](https://www.openfoam.com/)
4. [SimScale: Turbulent Pipe Flow Simulation](https://www.simscale.com/docs/content/simwiki/fluiddynamics/turbulence.html)
5. ["On the Dynamical Theory of Incompressible Viscous Fluids and the Determination of the Criterion" - Osborne Reynolds](https://royalsocietypublishing.org/doi/10.1098/rstl.1895.0004)
6. [NASA Wind Tunnel Virtual Simulators](https://www.grc.nasa.gov/WWW/K-12/airplane/wtunnel.html)
7. ["Direct Numerical Simulation of Turbulence" - Annual Review of Fluid Mechanics](https://www.annualreviews.org/journal/fluid)
8. [Ansys Fluent: Large Eddy Simulation (LES) Guide](https://www.ansys.com/)
9. ["Navier-Stokes Equations and Turbulence" - Clay Mathematics Institute](https://www.claymath.org/millennium-problems/navier-stokes-equation)
10. [JHU Turbulence Database (JHTDB) datasets](http://turbulence.pha.jhu.edu/)

### 📖 Referencias Útiles y Bibliografía
1. [*Fluid Mechanics* (Vol. 6) - L.D. Landau y E.M. Lifshitz](https://www.amazon.com/Fluid-Mechanics-Second-Theoretical-Physics/dp/0080339336)
2. [*Turbulence: The Legacy of A. N. Kolmogorov* - Uriel Frisch](https://www.amazon.com/Turbulence-Legacy-Kolmogorov-Uriel-Frisch/dp/0521457130)
3. [*Fluid Mechanics* - Pijush K. Kundu y Ira M. Cohen](https://www.amazon.com/Fluid-Mechanics-Pijush-K-Kundu/dp/012405935X)
4. [*A First Course in Turbulence* - H. Tennekes y J.L. Lumley](https://www.amazon.com/First-Course-Turbulence-MIT-Press/dp/0262200198)
