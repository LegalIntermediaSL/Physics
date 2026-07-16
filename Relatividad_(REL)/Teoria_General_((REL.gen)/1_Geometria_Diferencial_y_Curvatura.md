# Geometría Diferencial de la Relatividad General

## 1. Variedades Riemannianas
La Relatividad General abandona el espacio plano pseudoeuclidiano. El universo es modelado como una **Variedad Lorentziana** (una superficie curva de 4 dimensiones, topológicamente suave). 
La geometría local está completamente dictada por el **Tensor Métrico Cuadridimensional $g_{\mu\nu}$**, un tensor simétrico de rango 2 que es función de las coordenadas $x^\mu$:

$$
ds^2 = g_{\mu\nu} dx^\mu dx^\nu
$$

## 2. Símbolos de Christoffel (Conexión Afín)
Para derivar en una superficie curva, no podemos simplemente restar vectores en puntos adyacentes porque "apuntan" en espacios tangentes distintos. Necesitamos la **Derivada Covariante** $\nabla_\mu$.
La forma en que las bases cambian de un punto a otro está dada por los **Símbolos de Christoffel** $\Gamma^\lambda_{\mu\nu}$, derivados de la métrica:

$$
\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\rho} (\partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu})
$$

Físicamente, los $\Gamma^\lambda_{\mu\nu}$ actúan como los "campos de fuerza" inerciales o de gravedad local.

## 3. El Tensor de Riemann (La Verdadera Curvatura)
El indicador absoluto de curvatura. Mide cuánto "gira" un vector al ser transportado en un lazo cerrado diminuto (conmutador de derivadas covariantes):

$$
R^\rho_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}
$$

Si $R^\rho_{\sigma\mu\nu} = 0$ en todos los puntos, el espacio es plano (Minkowski). Si es diferente de cero, hay fuerzas de marea y curvatura gravitacional intrínseca.
