# Termodinámica de Sistemas Fuera del Equilibrio

## 1. La Flecha del Tiempo Irreversible
La termodinámica del equilibrio (Clausius, Gibbs) describe estados estáticos asintóticos donde $\Delta S \ge 0$. La física de no equilibrio modela los *flujos* irreversibles que transportan energía e información al disipar gradientes.

## 2. Producción de Entropía
En el continuo, el cambio local de entropía $s(\vec{r}, t)$ se desglosa en el flujo divergente de la corriente de entropía $\vec{J}_s$ y la tasa de producción interna de entropía $\sigma$:

$$
\frac{\partial s}{\partial t} + \nabla \cdot \vec{J}_s = \sigma, \quad \sigma \ge 0
$$

Donde $\sigma$ asegura la Segunda Ley de manera local.

## 3. Fuerzas y Flujos Termodinámicos Lineales
Para desviaciones pequeñas del equilibrio, los flujos microscópicos $J_i$ (calor, masa, carga) se asumen proporcionales a las "fuerzas afines" o gradientes termodinámicos $X_k$ (como $\nabla (1/T)$, $\nabla (\mu/T)$):

$$
J_i = \sum_k L_{ik} X_k
$$

Donde $L_{ik}$ son los coeficientes fenomenológicos de conductividad, difusión, etc. La producción de entropía se vuelve una forma cuadrática:

$$
\sigma = \sum_i J_i X_i = \sum_{i,k} L_{ik} X_i X_k \ge 0
$$

## 4. Relaciones Recíprocas de Onsager
Galardonado con el Nobel en 1968, Lars Onsager demostró que, debido a la reversibilidad microscópica de las ecuaciones hamiltonianas de movimiento de las partículas, la matriz de coeficientes acoplados es siempre simétrica (ausente campo magnético):

$$
L_{ik} = L_{ki}
$$

Esto interconecta, de forma profunda, procesos diametralmente opuestos (ej., Efecto Peltier y Seebeck termoeléctricos).
