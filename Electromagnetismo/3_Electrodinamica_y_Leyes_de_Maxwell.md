# Electrodinámica y el Tensor de Energía

Cuando las corrientes $\vec{J}$ y las densidades $\rho$ comienzan a fluctuar en el tiempo absoluto, las leyes estáticas se fracturan algebraicamente, dando lugar a la unificación dinámica magistral del siglo XIX.

## 1. La Corriente de Desplazamiento (El Milagro de Maxwell)
La Ecuación diferencial estática original de Ampère ($\nabla \times \vec{B} = \mu_0 \vec{J}$) contenía un error algebraico fatal: la divergencia del rotacional a la izquierda debe ser siempre cero puro matemático ($\nabla \cdot (\nabla \times \vec{B}) \equiv 0$), obligando absurdamente a que $\nabla \cdot \vec{J} = 0$, violando el Principio de Conservación de Carga Local ($\nabla \cdot \vec{J} = -\partial \rho / \partial t$).
Maxwell salvó el universo sumando astutamente un "término fantasma compensatorio": La Corriente de Desplazamiento ($\mu_0 \varepsilon_0 \partial \vec{E} / \partial t$).
Las Ecuaciones de Maxwell Unificadas completas son:
1. **Gauss Eléctrica**: $\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$
2. **Gauss Magnética**: $\nabla \cdot \vec{B} = 0$
3. **Faraday (Inducción)**: $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$
4. **Ampère-Maxwell**: $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$

## 2. El Vector de Poynting (Conservación Dinámica)
Si cruzamos las ecuaciones dinámicas rotacionales, demostramos rigurosamente el Teorema del Flujo de Energía. La tasa de variación de energía total ($U = \frac{1}{2}\int(\varepsilon_0 E^2 + \frac{1}{\mu_0}B^2)$) disminuye exactamente igual a la energía cinética gastada en frenar la materia ($\vec{J}\cdot\vec{E}$) y a la energía electromagnética que escapa por la superficie perimetral.
El portador algebraico de este flujo de energía al vacío irradiado es el **Vector de Poynting**:

$$
\vec{S} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})
$$

## 3. El Tensor de Esfuerzos de Maxwell
El momentum espacial (empuje de radiación lumínica presurizada sobre las paredes metálicas y vacío) no se conserva solo si miramos a la materia. El vacío oscilante posee "Momentum Físico", y la matriz $3 \times 3$ que tabula todo el balance de presiones electrodinámicas cruzadas cortantes sobre el vacío tridimensional es el Tensor de Maxwell:

$$
T_{ij} = \varepsilon_0 \left( E_i E_j - \frac{1}{2} \delta_{ij} E^2 \right) + \frac{1}{\mu_0} \left( B_i B_j - \frac{1}{2} \delta_{ij} B^2 \right)
$$

