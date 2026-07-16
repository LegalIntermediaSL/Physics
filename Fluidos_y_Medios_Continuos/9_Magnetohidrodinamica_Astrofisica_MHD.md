# Magnetohidrodinámica (MHD) Estelar

## 1. El Acoplamiento entre Maxwell y Navier-Stokes
La Magnetohidrodinámica (MHD) es el estudio de fluidos conductores de electricidad (plasmas, metales líquidos). En el sol y las estrellas, el gas está tan caliente que se ioniza. Las ecuaciones MHD combinan el electromagnetismo clásico con la dinámica de fluidos.

La fuerza impulsora adicional en la Ecuación de Navier-Stokes es la **Fuerza de Lorentz** volumétrica $\vec{J} \times \vec{B}$:

$$
\rho \left( \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla) \vec{v} \right) = -\nabla p + \vec{J} \times \vec{B} + \mu \nabla^2 \vec{v}
$$

## 2. Ecuación de Inducción
Usando la Ley de Ohm generalizada para un plasma en movimiento $\vec{J} = \sigma_e (\vec{E} + \vec{v} \times \vec{B})$ y la Ley de Faraday $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$, derivamos la **Ecuación de Inducción Magnética**:

$$
\frac{\partial \vec{B}}{\partial t} = \nabla \times (\vec{v} \times \vec{B}) + \eta \nabla^2 \vec{B}
$$

Donde $\eta = \frac{1}{\mu_0 \sigma_e}$ es la difusividad magnética. 
El primer término a la derecha representa la **Convección** (el fluido arrastra el campo), y el segundo representa la **Difusión** (el campo magnético se desvanece por resistencia).

## 3. Teorema de Alfvén y Flujo Congelado
El Número de Reynolds Magnético ($Rm = \frac{vL}{\eta}$) dictamina qué término domina. En plasmas astrofísicos (estrellas, galaxias), las escalas $L$ son tan enormes que $Rm \to \infty$.

Bajo estas condiciones de conductividad perfecta ($\eta \to 0$), aplica el **Teorema de Alfvén**: el flujo magnético a través de un circuito de fluido que se mueve con la velocidad $\vec{v}$ es constante. Las líneas de campo magnético están "congeladas" en el plasma. Si el plasma se retuerce por turbulencia convectiva estelar, las líneas de campo se retuercen con él, amplificando el campo magnético (Efecto Dinamo).
