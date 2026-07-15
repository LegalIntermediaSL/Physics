# Anomalías Cuánticas y Simetría Quiral

En física clásica, el Teorema de Noether garantiza que por cada simetría continua existe una corriente conservada ($\partial_\mu j^\mu = 0$). Sin embargo, las reglas cambian drásticamente cuando se introducen fluctuaciones cuánticas (lazos de diagramas de Feynman).

Una **Anomalía Cuántica** ocurre cuando una simetría del Lagrangiano clásico es *explícitamente destruida* por el proceso de cuantización y regularización matemática (la medida de la Integral de Camino).

## 1. La Anomalía de Adler-Bell-Jackiw (ABJ)
El ejemplo canónico es la Anomalía Quiral ABJ.
Considera fermiones sin masa (como los quarks u y d en el límite quiral). El Lagrangiano clásico tiene una simetría quiral global: puedes rotar independientemente las fases de los fermiones zurdos y diestros, lo que implica que la corriente axial $j^\mu_5 = \bar{\psi} \gamma^\mu \gamma_5 \psi$ está conservada clásicamente:

$$
\partial_\mu j^\mu_5 = 0
$$

Sin embargo, cuando intentas calcular la conservación a 1-lazo cuántico (un diagrama triangular donde un quark emite dos fotones), la integral es divergente. Al usar regularización de Pauli-Villars o dimensional para hacer las integrales finitas, fuerzas a la teoría a romper la simetría quiral, resultando en:

$$
\partial_\mu j^\mu_5 = \frac{e^2}{16\pi^2} \epsilon^{\mu\nu\alpha\beta} F_{\mu\nu} F_{\alpha\beta} \neq 0
$$

*(La anomalía es puramente proporcional al campo electromagnético topológico).*

## 2. Decaimiento del Pión a dos Fotones ($\pi^0 \to \gamma \gamma$)
Lejos de ser un fallo molesto de las matemáticas, la Anomalía ABJ es una predicción gloriosa verificada en laboratorios.
Sin la anomalía, el pión neutro (formado por un par quark-antiquark que actuaría como seudo-bosón de Goldstone de la simetría quiral) casi no podría desintegrarse electromagnéticamente.
Gracias a la anomalía cuántica del triángulo, el pión neutro decae casi instantáneamente en dos fotones libres. La tasa teórica predicha por la anomalía coincide perfectamente con el experimento, confirmando que existen exactamente 3 colores en la Cromodinámica Cuántica.
