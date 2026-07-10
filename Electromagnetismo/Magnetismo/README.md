# Magnetismo

Estudia los campos magnéticos, los cuales son producidos por cargas eléctricas en movimiento (corrientes) y por materiales magnéticos intrínsecos (imanes).

## Campo Magnético ($\vec{B}$)
Se mide en Teslas (T). Las líneas de campo magnético siempre forman bucles cerrados, indicando que no existen monopolos magnéticos aislados.

## Fuerza Magnética de Lorentz
La fuerza que experimenta una carga $q$ moviéndose con velocidad $\vec{v}$ en un campo $\vec{B}$:
$ \vec{F}_B = q(\vec{v} \times \vec{B}) $
Para un segmento de cable con corriente $I$:
$ \vec{F}_B = I(\vec{L} \times \vec{B}) $

## Fuentes de Campo Magnético
### Ley de Biot-Savart
Calcula el campo producido por un elemento de corriente $Id\vec{l}$:
$ d\vec{B} = \frac{\mu_0 I}{4\pi} \frac{d\vec{l} \times \hat{r}}{r^2} $

### Ley de Ampère
Relaciona el campo magnético integrado a lo largo de un bucle cerrado con la corriente que lo atraviesa:
$ \oint \vec{B} \cdot d\vec{l} = \mu_0 I_{enc} $

## Inducción Magnética (Ley de Faraday y Lenz)
Un flujo magnético ($\Phi_B = \int \vec{B} \cdot d\vec{A}$) variable en el tiempo induce una fuerza electromotriz (FEM) en un circuito:
$ \mathcal{E} = -\frac{d\Phi_B}{dt} $
El signo negativo representa la **Ley de Lenz**: la corriente inducida se opone al cambio de flujo magnético.
