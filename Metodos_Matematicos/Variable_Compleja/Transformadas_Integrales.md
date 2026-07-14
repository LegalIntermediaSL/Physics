# Transformadas Integrales: Fourier y Laplace

Las ecuaciones diferenciales de la física a menudo relacionan derivadas espaciales o temporales cruzadas que son difíciles de resolver en el "espacio de posiciones". Las transformadas integrales nos permiten mapear estas ecuaciones desde el **Espacio Real** hacia el **Espacio de Frecuencias o Momentos**, convirtiendo cálculo diferencial en álgebra simple.

## 1. La Transformada de Fourier
La Transformada de Fourier descompone una función del espacio o del tiempo $f(x)$ en una superposición continua de ondas armónicas (ondas planas $e^{ikx}$) con número de onda $k$:

$$
\tilde{f}(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) e^{-ikx} dx
$$

La transformada inversa nos devuelve al espacio real:

$$
f(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \tilde{f}(k) e^{ikx} dk
$$

**Propiedad Fundamental:** La derivada espacial $\partial/\partial x$ en el espacio real se transforma matemáticamente en una simple multiplicación por $ik$ en el espacio de Fourier. Esta es la razón profunda por la que el operador Momento Cuántico se define como $\hat{p} = -i\hbar \nabla$.

## 2. La Transformada de Laplace
Mientras que la transformada de Fourier requiere que la función decaiga a infinito para ser integrable, la Transformada de Laplace puede manejar funciones que crecen en el tiempo (como exponenciales). Mapea funciones del tiempo $f(t)$ a una variable compleja $s = \sigma + i\omega$:

$$
\mathcal{L}\{f(t)\} = F(s) = \int_{0}^{\infty} f(t) e^{-st} dt
$$

Es la herramienta reina para resolver **Problemas de Valores Iniciales** (Sistemas transitorios, circuitos RLC, o cinética química), ya que incorpora intrínsecamente las condiciones del sistema en $t=0$ en el espacio algebraico transformado.
