# [MTH-12] Diferenciación Automática (Autograd) y EDPs

## 1. El Fin de las Mallas (Mesh-Free Physics)
Históricamente, resolver ecuaciones en derivadas parciales (EDPs) requería crear mallas espaciales (Diferencias Finitas, Elementos Finitos), lo cual sufre de "la maldición de la dimensionalidad". Las PINNs evitan esto usando Diferenciación Automática.

## 2. Grafos Computacionales
Una red neuronal $\hat{u}(x,t; \theta)$ es una composición de funciones diferenciables (multiplicaciones matriciales y funciones de activación como `tanh` o `SiLU`). El compilador (PyTorch/JAX) construye un grafo acíclico dirigido de estas operaciones.
Mediante la Regla de la Cadena inversa (*backpropagation*), el compilador calcula derivadas espaciales exactas $\partial \hat{u} / \partial x$ o temporales $\partial \hat{u} / \partial t$ sin errores de truncamiento.

## 3. Integración en el Hamiltoniano
Esto permite que el término de pérdida físico sea exacto. Si resolvemos Navier-Stokes, la red neuronal "conoce" las derivadas exactas de la velocidad y la presión en cualquier punto $(x,y,t)$ del continuo espacio-tiempo, permitiendo flujos de trabajo donde los tensores de estrés se derivan automáticamente del campo de velocidades.
