# Inestabilidades MHD (Kink y Sausage)

## 1. Dinámica No Lineal en el Tokamak
En un Tokamak, el plasma conduce corrientes eléctricas inmensas. Desafortunadamente, cualquier gas conductor con corriente paralela a su campo magnético es un sistema MHD estructuralmente precario; la más mínima perturbación aleatoria térmica o acústica tiende a amplificarse no-linealmente hasta estrellar el núcleo magnético contra la pared del reactor.

## 2. Inestabilidad Kink (De Torcedura)
Supongamos que la columna de plasma cilíndrica se curva ligeramente por azar. La densidad de líneas magnéticas poloidales generadas por la corriente axial $I_z$ se comprime en el radio interior de la curva, y se dilata en el exterior.
Dado que la Presión Magnética es $P_m = B^2/2\mu_0$, la presión magnética es mayor en el interior de la curva y literalmente empuja para que la curva se agrave aún más, hasta destrozar el lazo plasmático.

## 3. Límite de Kruskal-Shafranov
Para suprimir la inestabilidad Kink macroscópica (modo $m=1$), los teóricos soviéticos Kruskal y Shafranov demostraron que el paso helicoidal (el *Safety Factor* $q$) de la línea de campo debe ser lo suficientemente estricto: el campo toroidal de fondo debe ser extremadamente fuerte respecto a la corriente inyectada.
El **Límite de Estabilidad Kruskal-Shafranov** se define geométricamente como:

$$
q = \frac{r B_t}{R B_p} > 1
$$

Donde $R$ es el radio mayor del toroide, $r$ el menor, $B_t$ campo toroidal y $B_p$ poloidal inducido. Si $q < 1$, el plasma inevitablemente desarrolla modos topológicos de torsión anudada y colapsa (Disrupción).
