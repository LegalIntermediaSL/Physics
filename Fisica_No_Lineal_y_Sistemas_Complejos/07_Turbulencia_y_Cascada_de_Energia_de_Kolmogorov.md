# Turbulencia y Cascada de Energía de Kolmogorov

## 1. El Régimen Turbulento de Navier-Stokes
Para fluidos altamente inerciales (Número de Reynolds $Re = \frac{UL}{\nu} \gg 1$), el flujo pierde estabilidad y entra en régimen turbulento. Las soluciones de la ecuación de Navier-Stokes exhiben dinámica caótica espacio-temporal de grados de libertad infinitos, con torbellinos interaccionando en todas las escalas.

## 2. Hipótesis de Kolmogorov de 1941 (K41)
Richardson describió la turbulencia cualitativamente: "los torbellinos grandes se rompen en pequeños para transferir su energía cinética, y estos en otros menores, hasta la disipación viscosa". Kolmogorov lo formalizó asumiendo isotropía estadística local.

## 3. La Ley de los $5/3$
La tasa de disipación de energía viscosa por unidad de masa es $\epsilon$. Según Kolmogorov, en el **rango inercial** (torbellinos más pequeños que la escala integral pero más grandes que la escala viscosa de Kolmogorov $\eta$), el espectro de energía $E(k)$ depende únicamente de $\epsilon$ y el número de onda $k$.

Por análisis dimensional absoluto:

$$
[\epsilon] = L^2 T^{-3}, \quad [k] = L^{-1}, \quad [E(k)] = L^3 T^{-2}
$$

La única combinación dimensionalmente consistente genera la famosa Ley $K41$:

$$
E(k) = C_K \epsilon^{2/3} k^{-5/3}
$$

Donde $C_K \approx 1.5$ es la constante universal de Kolmogorov.

## 4. Microescala de Kolmogorov
Las escalas más pequeñas del fluido, donde la energía se quema térmicamente por la viscosidad cinemática $\nu$, vienen dadas por la escala de longitud:

$$
\eta = \left( \frac{\nu^3}{\epsilon} \right)^{1/4}
$$

