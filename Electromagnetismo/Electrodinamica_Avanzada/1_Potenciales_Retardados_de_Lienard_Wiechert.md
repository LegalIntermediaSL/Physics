# Potenciales Retardados de Liénard-Wiechert

## 1. El Retardo en la Propagación
En electrostática de Coulomb clásica, los campos eléctricos reaccionan instantáneamente. En electrodinámica relativista, los campos electromagnéticos se propagan a la velocidad de la luz $c$. Si una carga se mueve, el campo que "siente" un observador distante no corresponde a donde está la carga *ahora*, sino donde estaba en el **tiempo retardado** $t_{ret} = t - R/c$.

## 2. Potenciales de Liénard-Wiechert
Los potenciales cuadrivectoriales relativistas exactos para una partícula puntual de carga $q$ moviéndose en una trayectoria $\vec{r}'(t)$ a una velocidad $\vec{v}(t)$ son:

- **Potencial Escalar:**

$$
\phi(\vec{r}, t) = \frac{1}{4\pi\varepsilon_0} \left[ \frac{q}{(1 - \vec{\beta}\cdot\hat{n})R} \right]_{ret}
$$

- **Potencial Vectorial:**

$$
\vec{A}(\vec{r}, t) = \frac{\mu_0}{4\pi} \left[ \frac{q\vec{v}}{(1 - \vec{\beta}\cdot\hat{n})R} \right]_{ret}
$$

Donde $\vec{\beta} = \vec{v}/c$ y los corchetes $[ \dots ]_{ret}$ indican que todo debe evaluarse explícitamente en el tiempo retardado.

## 3. Campos Eléctricos y Magnéticos Exactos
Al derivar los potenciales ($\vec{E} = -\nabla\phi - \partial\vec{A}/\partial t$), el campo eléctrico resultante se escinde en dos términos fundamentales:
1. **Campo de Velocidad (Campo de Coulomb generalizado):** Cae como $1/R^2$. Es estático si no hay aceleración.
2. **Campo de Aceleración (Campo de Radiación):** Cae como $1/R$ (viaja infinito sin disiparse) y es directamente proporcional a la **aceleración** de la carga.

¡Esta es la demostración matemática formal de que toda carga que acelera *debe* emitir radiación electromagnética (luz)!
