# Fusión Nuclear y Confinamiento

La fusión nuclear es el proceso mediante el cual dos núcleos atómicos ligeros se combinan para formar uno más pesado, liberando inmensas cantidades de energía. Replicar este proceso de forma controlada requiere confinar plasmas a condiciones extremas.

## 📜 Contexto Histórico

La teoría de que el sol brilla debido a la fusión nuclear fue propuesta por Arthur Eddington en los años 20 y detallada por Hans Bethe en 1939. En 1950, los científicos soviéticos Andrei Sakharov e Igor Tamm propusieron el diseño del "Tokamak" (cámara toroidal con bobinas magnéticas), que sigue siendo el enfoque líder para la fusión magnética en proyectos como ITER (International Thermonuclear Experimental Reactor).

## 🧮 Desarrollo Teórico Profundo

La reacción de fusión más prometedora para reactores terrestres involucra isótopos de hidrógeno: Deuterio ($D$) y Tritio ($T$):

$$ ^2_1\text{D} + ^3_1\text{T} \rightarrow ^4_2\text{He} (3.5 \, \text{MeV}) + ^1_0\text{n} (14.1 \, \text{MeV}) $$

La energía total liberada por reacción es $Q = 17.6 \, \text{MeV}$.

Para que la fusión sea comercialmente viable, el plasma debe encenderse (ignition), lo que significa que el calentamiento interno (por las partículas alfa $^4_2\text{He}$) supera las pérdidas de energía. Esto se resume en el **Criterio de Lawson** modificado, también conocido como la condición de producto triple:

$$ n T \tau_E \geq \frac{12 k_B}{E_\alpha \langle \sigma v \rangle} $$

Para la reacción D-T a $T \approx 10-20 \, \text{keV}$ ($100-200$ millones de grados Celsius), el producto triple debe ser:

$$ n T \tau_E \approx 3 \times 10^{21} \, \text{m}^{-3} \cdot \text{keV} \cdot \text{s} $$

Donde:
- $n$ es la densidad iónica.
- $T$ es la temperatura del plasma.
- $\tau_E$ es el tiempo de confinamiento de energía.

**Confinamiento Magnético:**
En un Tokamak, el campo magnético helicoidal $\mathbf{B}$ necesario para estabilizar el plasma se crea mediante un campo toroidal $B_\phi$ (por bobinas externas) y un campo poloidal $B_\theta$ (inducido por una corriente en el plasma). El factor de seguridad $q$ mide el "pitch" o paso de las líneas de campo y es vital para la estabilidad MHD:

$$ q = \frac{r B_\phi}{R B_\theta} > 1 $$

## 🛠 Ejemplo Práctico

**Problema:** Un reactor Tokamak D-T opera a una temperatura de $T = 15 \, \text{keV}$ y una densidad iónica de $n = 10^{20} \, \text{m}^{-3}$. Calcular el tiempo de confinamiento de energía $\tau_E$ requerido para alcanzar la ignición.

**Solución paso a paso:**

1. **Datos del Criterio de Lawson para D-T (Producto Triple):**
   $$ n T \tau_E \approx 3 \times 10^{21} \, \text{m}^{-3} \cdot \text{keV} \cdot \text{s} $$
   - $n = 10^{20} \, \text{m}^{-3}$
   - $T = 15 \, \text{keV}$

2. **Despejar $\tau_E$:**
   $$ \tau_E = \frac{3 \times 10^{21}}{n T} $$

3. **Cálculo:**
   $$ \tau_E = \frac{3 \times 10^{21}}{(10^{20}) (15)} = \frac{3 \times 10^{21}}{1.5 \times 10^{21}} = 2 \, \text{segundos} $$

Para que este reactor alcance la ignición (autosostenibilidad sin calentamiento externo), el plasma debe mantener su energía confinada por al menos 2 segundos.

## 📚 Recursos Específicos

### Cursos Específicos
1. [Nuclear Energy - MIT OpenCourseWare](https://ocw.mit.edu)
2. [Introduction to Fusion Energy - TU/e (Coursera)](https://www.coursera.org)
3. [Fusion Materials - NPTEL](https://nptel.ac.in)
4. [ITER E-Learning Courses](https://www.iter.org/)
5. [Inertial Confinement Fusion - LLNL Short Courses](https://lasers.llnl.gov)
6. [Thermonuclear Reactor Design - Tokyo Institute of Technology](https://www.titech.ac.jp)

### Artículos y Simulaciones
1. [Lawson, J. D. (1957). *Some Criteria for a Power Producing Thermonuclear Reactor*. Proc. Phys. Soc.](https://doi.org/10.1088/0370-1301/70/1/303)
2. [Nuckolls, J., Wood, L., Thiessen, A., & Zimmerman, G. (1972). *Laser Compression of Matter to Super-High Densities*. Nature.](https://www.nature.com/articles/239139a0)
3. [Hurricane, O. A., et al. (2014). *Fuel gain exceeding unity in an inertially confined fusion implosion*. Nature.](https://www.nature.com/articles/nature13008)
4. [Rebut, P. H. (1995). *ITER: The first experimental fusion reactor*. Fusion Engineering and Design.](https://doi.org/10.1016/0920-3796(95)90103-5)
5. [Abu-Shumays, I. K., et al. (1999). *Simulations for ICF Experiments*.](https://doi.org/10.1109/99.757313)
6. [ITER - The Way to New Energy (Sitio oficial)](https://www.iter.org/)
7. [National Ignition Facility (NIF) - Confinamiento Inercial](https://lasers.llnl.gov/)
8. [HELIOS](https://www.prism-cs.com/Software/Helios/Helios.html) - 1D Radiation Magnetohydrodynamics Code for ICF.
9. [FLASH](https://flash.rochester.edu/) - Multiphysics code for laser fusion.

### 📖 Referencias Útiles y Bibliografía
1. [Atzeni, S., & Meyer-ter-Vehn, J. (2004). *The Physics of Inertial Fusion*. Oxford University Press.](https://global.oup.com/academic/product/the-physics-of-inertial-fusion-9780198562641)
2. [Wesson, J. (2011). *Tokamaks* (Vol. 149). Oxford University Press.](https://global.oup.com/academic/product/tokamaks-9780199592234)
3. [McCracken, G., & Stott, P. (2012). *Fusion: The Energy of the Universe*. Academic Press.](https://www.sciencedirect.com/book/9780123846563/fusion)
4. [Stacey, W. M. (2010). *Fusion Plasma Physics*. Wiley-VCH.](https://www.wiley.com/en-us/Fusion+Plasma+Physics%2C+2nd+Edition-p-9783527409679)
