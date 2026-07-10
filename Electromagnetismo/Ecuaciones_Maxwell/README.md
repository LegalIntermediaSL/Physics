# Ecuaciones de Maxwell

En 1865, James Clerk Maxwell unificó todas las leyes empíricas previas de la electricidad y el magnetismo en cuatro elegantes ecuaciones, y al hacerlo, descubrió que la luz es una onda electromagnética.

## Forma Diferencial

1. **Ley de Gauss para Electricidad** (Las cargas producen campos eléctricos):
$ \nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0} $

2. **Ley de Gauss para Magnetismo** (No existen monopolos magnéticos):
$ \nabla \cdot \vec{B} = 0 $

3. **Ley de Faraday de la Inducción** (Campos magnéticos variables producen campos eléctricos rotacionales):
$ \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $

4. **Ley de Ampère-Maxwell** (Corrientes y campos eléctricos variables producen campos magnéticos rotacionales):
$ \nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t} $
El término $\mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}$ (corriente de desplazamiento) fue la aportación crucial de Maxwell.

## Ondas Electromagnéticas
En el vacío ($\rho = 0, \vec{J} = 0$), las ecuaciones de Maxwell se pueden combinar para formar la ecuación de onda tridimensional:
$ \nabla^2 \vec{E} = \mu_0 \epsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2} $
La velocidad de propagación teórica predicha es $v = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$, lo que exactamente equivale a la velocidad de la luz $c = 3 \times 10^8$ m/s.
