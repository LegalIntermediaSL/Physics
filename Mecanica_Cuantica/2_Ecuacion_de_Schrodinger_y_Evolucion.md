# Evolución Temporal y la Ecuación de Schrödinger

A diferencia del violento colapso estocástico que ocurre durante una medición, la evolución de un estado cuántico en ausencia de observaciones es completamente determinista, suave, continua y matemáticamente reversible (Unitaria).

## 1. La Ecuación de Schrödinger
La dinámica está dictada por el Operador Hamiltoniano $\hat{H}$ (que representa la energía total del sistema: Cinética + Potencial).

$$
i\hbar \frac{\partial}{\partial t} |\Psi(t)\rangle = \hat{H} |\Psi(t)\rangle
$$

Si $\hat{H}$ no depende explícitamente del tiempo, la solución formal es una simple rotación unitaria:

$$
|\Psi(t)\rangle = \hat{U}(t) |\Psi(0)\rangle = e^{-i\hat{H}t/\hbar} |\Psi(0)\rangle
$$

## 2. Tres Representaciones de la Dinámica
En cuántica, las predicciones físicas (Valores Esperados $\langle \hat{A} \rangle$) son lo único que medimos en el laboratorio. La matemática nos da tres formas equivalentes (Pictures) de calcular lo mismo:

- **La Imagen de Schrödinger**: Los estados $|\Psi(t)\rangle$ se mueven como manecillas de un reloj. Los operadores (como $\hat{x}$) son fijos e inmóviles.
- **La Imagen de Heisenberg**: Los estados $|\Psi\rangle$ están congelados eternamente en el tiempo. Son los operadores (las reglas de medir) los que cambian dinámicamente según la Ecuación de Movimiento de Heisenberg: $\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \frac{\partial \hat{A}_H}{\partial t}$. (Esto es idéntico a los corchetes de Poisson de la mecánica clásica de Hamilton).
- **La Imagen de Interacción (Dirac)**: Un híbrido usado en Teoría Cuántica de Campos (QFT). Si $\hat{H} = \hat{H}_0 + \hat{V}$, los estados evolucionan debido al potencial perturbativo $\hat{V}$, mientras que los operadores evolucionan debido al Hamiltoniano libre $\hat{H}_0$.
