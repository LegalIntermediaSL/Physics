# [CLM-09] Transformaciones Canónicas y Ecuación de Hamilton-Jacobi

## 1. La Flexibilidad Topológica de Hamilton
A diferencia de Newton, la mecánica Hamiltoniana vive en el Espacio de Fases (Coordenadas $q$ y Momentos $p$). Las **Transformaciones Canónicas** permiten cambiar de variables sin alterar la física, siempre que conserven los Corchetes de Poisson $\{Q, P\} = 1$. Matemáticamente, equivale a deformaciones simplécticas del volumen de fase.

## 2. Ecuación de Hamilton-Jacobi
Es la joya analítica de la mecánica clásica. Buscamos una Función Generatriz (La "Acción Clásica" $S$) tal que, en las nuevas coordenadas, el Hamiltoniano sea exactamente cero $K=0$. Todas las coordenadas son constantes del movimiento. La ecuación resultante:
$H\left(q_i, \frac{\partial S}{\partial q_i}, t\right) + \frac{\partial S}{\partial t} = 0$
Es matemáticamente análoga a la aproximación eikonal de la óptica, sirviendo como el límite semi-clásico (WKB) directo de la Ecuación Cuántica de Schrödinger.

## 3. Variables Ángulo-Acción e Integrabilidad KAM
Para sistemas periódicos, se pueden encontrar variables donde los Momentos son invariantes topológicos (Acciones $J_i$) y las Coordenadas fluyen linealmente en el tiempo (Ángulos $	heta_i$). Si un sistema posee tantas Acciones conservadas como grados de libertad, es "Totalmente Integrable". Si no, el Teorema KAM (Kolmogorov-Arnold-Moser) nos dicta cómo el orden se rompe lentamente dando lugar al Caos (ej: Péndulo Doble o Problema de 3 Cuerpos).
