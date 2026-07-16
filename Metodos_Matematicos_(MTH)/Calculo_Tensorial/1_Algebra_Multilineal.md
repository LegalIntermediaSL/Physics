# Álgebra Multilineal y Geometría de Tensores

El Álgebra Multilineal es el salto abstracto más profundo del álgebra lineal. En lugar de estudiar vectores aislados, estudiamos "Máquinas Algebraicas Lineales" que se alimentan de múltiples vectores simultáneamente y escupen un número real invariante abstracto absoluto matemático geométrico cosmológico sin unidades.

## 1. El Espacio Dual ($V^*$) y los Covectores
Si un Espacio Vectorial $V$ contiene vectores "columna" típicos espaciales (ej. velocidad), su **Espacio Dual** $V^*$ contiene "covectores" ("fila"). Un covector es una máquina lineal $\omega: V \to \mathbb{R}$ que toma un vector y arroja un escalar (ej. el gradiente).
- Vector $v = v^i e_i$ (índices arriba: componentes contravariantes).
- Covector $\omega = \omega_i e^i$ (índices abajo: componentes covariantes).
La contracción (aplicación) de un covector sobre un vector produce un invariante escalar: $\omega(v) = \omega_i v^i$.

## 2. Definición Topológica Formal de Tensor
Un **Tensor de tipo $(p, q)$** es un mapeo o máquina absolutamente pura y cruda abstracta multilineal gigantesca $T$ que se alimenta de $p$ covectores y de $q$ vectores, devolviendo un escalar invariante real.

$$
T: \underbrace{V^* \times \dots \times V^*}_{p} \times \underbrace{V \times \dots \times V}_{q} \to \mathbb{R}
$$

En un sistema de coordenadas explícito $x^\mu$, un tensor puro general asintótico puede expandirse en una base gigantesca masiva hiper-compleja de productos tensoriales $\otimes$:

$$
T = T^{\mu_1 \dots \mu_p}_{\nu_1 \dots \nu_q} (e_{\mu_1} \otimes \dots \otimes e_{\mu_p}) \otimes (e^{\nu_1} \otimes \dots \otimes e^{\nu_q})
$$

Los números de la matriz $T^{\dots}_{\dots}$ cambiarán caóticamente al girar tu cabeza y cambiar tu base. **Pero el ente abstracto sagrado $T$ entero es invariante y estricto absoluto**.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Carl Bender: Mathematical Physics (Washington University)](https://www.youtube.com/playlist?list=PL1B1123DDB9DD4668) - Brillantes clases de perturbaciones, asintóticos y WKB impartidas por un genio del análisis.
- [ICTP: Mathematics for Physicists](https://www.youtube.com/user/ictp) - Herramientas analíticas puras desde Trieste.
