# Teoría de Sturm-Liouville y Problemas de Autovalores

Casi todas las ecuaciones diferenciales lineales de segundo orden que aparecen en física (como la ecuación de Schrödinger para el átomo de hidrógeno, o la ecuación de Laplace en coordenadas esféricas) pueden reescribirse en una forma estándar conocida como la **Ecuación de Sturm-Liouville**.

## 1. El Operador de Sturm-Liouville ($\mathcal{L}$)
Cualquier ecuación diferencial lineal de segundo orden de la forma $P(x)y'' + Q(x)y' + R(x)y = 0$ puede multiplicarse por un factor integrante para llevarla a la forma auto-adjunta (hermítica) de Sturm-Liouville:

$$
\mathcal{L} y = -\frac{d}{dx} \left[ p(x) \frac{dy}{dx} \right] + q(x)y = \lambda w(x) y
$$

Donde:
*   $p(x) > 0$ y $w(x) > 0$ son funciones reales.
*   $w(x)$ es la **función de peso**.
*   $\lambda$ es el autovalor (eigenvalue) del operador $\mathcal{L}$.

## 2. Espectro y Ortogonalidad
El inmenso poder de la teoría de Sturm-Liouville radica en sus propiedades espectrales, que garantizan matemáticamente la existencia de soluciones fundamentales (los autovectores o eigenfunciones) que forman una **base completa**.

1.  **Autovalores Reales:** Todos los autovalores $\lambda_n$ son números reales (fundamental para que la energía o la frecuencia en un sistema físico sean medibles y reales).
2.  **Ortogonalidad:** Las eigenfunciones $y_n(x)$ y $y_m(x)$ correspondientes a autovalores distintos ($\lambda_n \neq \lambda_m$) son siempre ortogonales respecto a la función de peso $w(x)$:
    

$$
\int_a^b y_n(x) y_m(x) w(x) dx = 0 \quad (\text{si } n \neq m)
$$

3.  **Completitud:** Cualquier función "razonable" (cuadrado integrable) $f(x)$ que cumpla las mismas condiciones de contorno puede ser expandida como una suma lineal infinita de estas eigenfunciones (Generalización de las Series de Fourier):
    

$$
f(x) = \sum_{n=0}^{\infty} c_n y_n(x)
$$

    Donde los coeficientes se hallan proyectando: $c_n = \frac{\int f(x)y_n(x)w(x)dx}{\int y_n^2(x)w(x)dx}$.

## 3. Condiciones de Contorno
Para que el operador sea estrictamente hermítico, el sistema debe cumplir ciertas condiciones en los bordes del intervalo $[a,b]$.
*   **Dirichlet:** $y(a) = y(b) = 0$ (Cuerda atada en los extremos).
*   **Neumann:** $y'(a) = y'(b) = 0$ (Extremos libres o aislados térmicamente).
*   **Periódicas:** $y(a) = y(b)$ y $y'(a) = y'(b)$ (Estructuras en forma de anillo, como redes cristalinas).
