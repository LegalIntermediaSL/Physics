# Magnetohidrodinámica

La magnetohidrodinámica (MHD) es el estudio de la dinámica de fluidos conductores de electricidad (como plasmas, metales líquidos, o agua salada) bajo la influencia de campos magnéticos.

## 📜 Contexto Histórico

El campo de la MHD fue iniciado por Hannes Alfvén, quien en 1942 descubrió las ondas electromagnéticas en plasmas (Ondas de Alfvén), trabajo por el cual recibió el Premio Nobel de Física en 1970. Su desarrollo inicial se enfocó en comprender fenómenos astrofísicos y geofísicos (como el campo magnético terrestre).

## 🧮 Desarrollo Teórico Profundo

El conjunto de ecuaciones de la MHD ideal combina las ecuaciones de Navier-Stokes para fluidos con las ecuaciones de Maxwell para el electromagnetismo, asumiendo un fluido perfectamente conductor (resistividad nula, $\eta = 0$).

**1. Ecuación de Continuidad (Masa):**
$$ \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0 $$

**2. Ecuación de Momento (Navier-Stokes con fuerza de Lorentz):**
$$ \rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{v} \right) = -\nabla p + \mathbf{J} \times \mathbf{B} $$
Donde $\mathbf{J} \times \mathbf{B}$ es la fuerza magnética, que se puede descomponer usando $\mathbf{J} = \frac{1}{\mu_0} \nabla \times \mathbf{B}$:
$$ \mathbf{J} \times \mathbf{B} = -\nabla\left(\frac{B^2}{2\mu_0}\right) + \frac{1}{\mu_0}(\mathbf{B} \cdot \nabla)\mathbf{B} $$
El primer término es la *presión magnética* y el segundo es la *tensión magnética*.

**3. Ley de Ohm Ideal:**
Para un fluido perfectamente conductor:
$$ \mathbf{E} + \mathbf{v} \times \mathbf{B} = 0 $$

**4. Ecuación de Inducción Magnética:**
Combinando la Ley de Ohm ideal con la Ley de Faraday ($\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$):
$$ \frac{\partial \mathbf{B}}{\partial t} = \nabla \times (\mathbf{v} \times \mathbf{B}) $$
Esto da lugar al **Teorema de Alfvén (Congelamiento del flujo)**: las líneas de campo magnético están "congeladas" en el fluido que se mueve.

## 🛠 Ejemplo Práctico

**Problema:** Calcular la velocidad de Alfvén ($v_A$) en el viento solar cerca de la Tierra, asumiendo un campo magnético de $B = 5 \times 10^{-9} \, \text{T}$ y una densidad de protones $n_p = 5 \times 10^6 \, \text{m}^{-3}$.

**Solución paso a paso:**

1. **Datos:**
   - $B = 5 \times 10^{-9} \, \text{T}$
   - $n_p = 5 \times 10^6 \, \text{m}^{-3}$
   - Masa del protón $m_p \approx 1.67 \times 10^{-27} \, \text{kg}$
   - $\mu_0 = 4\pi \times 10^{-7} \, \text{T}\cdot\text{m/A}$

2. **Calcular la densidad de masa ($\rho$):**
   $$ \rho = n_p m_p = 5 \times 10^6 \times 1.67 \times 10^{-27} = 8.35 \times 10^{-21} \, \text{kg/m}^3 $$

3. **Fórmula de la Velocidad de Alfvén ($v_A$):**
   $$ v_A = \frac{B}{\sqrt{\mu_0 \rho}} $$

4. **Cálculo:**
   $$ \mu_0 \rho = (4\pi \times 10^{-7}) \times (8.35 \times 10^{-21}) \approx 1.05 \times 10^{-26} $$
   $$ \sqrt{\mu_0 \rho} \approx 1.02 \times 10^{-13} $$
   $$ v_A = \frac{5 \times 10^{-9}}{1.02 \times 10^{-13}} \approx 49,000 \, \text{m/s} = 49 \, \text{km/s} $$

La velocidad característica de las perturbaciones magnéticas en el viento solar es de 49 km/s.

## 📚 Recursos Específicos

### Cursos Específicos
1. [MHD Theory - Princeton Plasma Physics Lab (PPPL)](https://www.pppl.gov/)
2. [Introduction to Magnetohydrodynamics (Coursera)](https://www.coursera.org)
3. [Astrophysical Fluid Dynamics - Cambridge](https://www.maths.cam.ac.uk/)

### Artículos y Simulaciones
1. Alfvén, H. (1942). *Existence of Electromagnetic-Hydrodynamic Waves*. Nature.
2. Biskamp, D. (1993). *Nonlinear Magnetohydrodynamics*. Cambridge University Press.
3. [Athena++ Astrophysical MHD Code](https://github.com/PrincetonUniversity/athena)
4. [PLUTO Code for Computational Astrophysics](http://plutocode.ph.unito.it/)
