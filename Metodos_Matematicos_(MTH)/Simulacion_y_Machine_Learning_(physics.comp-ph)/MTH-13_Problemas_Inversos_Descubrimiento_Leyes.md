# [MTH-13] Problemas Inversos y Descubrimiento de Leyes (Equation Discovery)

## 1. ¿Qué es un Problema Inverso?
El "Forward Problem" es calcular el estado de un sistema conociendo la ecuación. El "Inverse Problem" es deducir la ecuación subyacente o sus coeficientes físicos conociendo solo mediciones parciales o ruidosas del sistema.

## 2. Inferencia de Coeficientes con PINNs
Supongamos que observamos un fluido pero no conocemos su viscosidad cinemática $\nu$. Definimos $\nu$ como un parámetro entrenable de la red (junto a los pesos $\theta$).
La EDP de Navier-Stokes en la pérdida residual se convierte en:

$$
\mathcal{R} = \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} + \nabla p - \nu_{train} \nabla^2 \mathbf{u}
$$

Durante el entrenamiento, el gradiente descendente actualiza $\nu_{train}$ para minimizar $\mathcal{R}$. Mágicamente, el parámetro converge al valor real de la viscosidad física. Esto permite inferir propiedades inobservables (como la presión en un flujo sanguíneo 3D a partir de resonancias magnéticas de velocidad).
