# [THD-10] Teoremas de Fluctuación: Jarzynski y Crooks

## 1. Termodinámica Estocástica
A escala nanométrica, las fluctuaciones térmicas son comparables al trabajo realizado sobre un sistema. Las leyes de la termodinámica clásica (macroscópicas) se generalizan mediante identidades exactas de no-equilibrio.

## 2. Igualdad de Jarzynski (1997)
Relaciona el trabajo irreversible $W$ realizado durante un proceso de no-equilibrio (ej. estirar una molécula de ADN rápidamente) con la diferencia de energía libre de Helmholtz $\Delta F$ entre los estados de equilibrio inicial y final:

$$
\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}
$$

donde $\beta = 1/(k_B T)$. Esta ecuación es revolucionaria porque permite extraer información de equilibrio ($\Delta F$) a partir de infinitos caminos fuera del equilibrio. Como una consecuencia directa a través de la desigualdad de Jensen, recuperamos la Segunda Ley: $\langle W \rangle \ge \Delta F$.

## 3. Teorema de Fluctación de Crooks (1999)
Relaciona la probabilidad de realizar un trabajo $W$ en un proceso "hacia adelante" ($P_F(W)$) con la probabilidad del trabajo opuesto en el proceso "hacia atrás" ($P_R(-W)$):

$$
\frac{P_F(W)}{P_R(-W)} = e^{\beta (W - \Delta F)}
$$
