# La Ecuación de Schrödinger

Erwin Schrödinger (1926) formuló la ecuación diferencial que rige la evolución temporal de las "ondas de materia".

## Función de Onda ($\Psi$)
El estado cuántico de un sistema está completamente especificado por $\Psi(\vec{r}, t)$. 
- **Interpretación de Born**: La probabilidad de encontrar la partícula en un volumen $dV$ es proporcional a la magnitud al cuadrado de la función de onda:
$ dP = |\Psi(\vec{r}, t)|^2 dV $
La función debe estar normalizada: $\int |\Psi|^2 dV = 1$.

## La Ecuación Dependiente del Tiempo
Para una partícula de masa $m$ en un potencial $V(\vec{r}, t)$:
$ i\hbar \frac{\partial \Psi}{\partial t} = \left[ -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r},t) \right] \Psi $
El término entre corchetes es el operador Hamiltoniano ($\hat{H}$).

## La Ecuación Independiente del Tiempo
Si el potencial no depende del tiempo ($V(\vec{r})$), podemos separar variables ($\Psi(\vec{r},t) = \psi(\vec{r})e^{-iEt/\hbar}$). Obtenemos una ecuación de autovalores:
$ \hat{H} \psi = E \psi $
Donde $E$ son los niveles de energía discretos permitidos y $\psi$ son los estados estacionarios.
