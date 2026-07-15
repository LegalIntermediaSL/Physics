# Aproximación WKB y Mecánica Semi-Clásica

El Método WKB (Wentzel-Kramers-Brillouin) es la técnica fundamental para aproximar soluciones de ecuaciones diferenciales lineales ordinarias cuya derivada de mayor orden está multiplicada por un factor "pequeño" (como la constante de Planck $\hbar \to 0$, que marca el límite clásico).

## 1. El Ansätze WKB
Para resolver la Ecuación de Schrödinger con un potencial arbitrario variante $V(x)$:

$$
-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} + V(x)\psi = E\psi
$$

Asumimos que la función de onda se comporta como una exponencial compleja clásica fuertemente oscilatoria (similar a la Eikonal en óptica), pero con una fase (acción $S$) que cambia lentamente comparada con la longitud de onda de De Broglie del sistema:

$$
\psi(x) = A(x) \exp\left( \frac{i}{\hbar} S(x) \right)
$$

## 2. La Derivación Semi-Clásica (Expansión en $\hbar$)
Al sustituir esto y expandir $S$ en potencias de $\hbar$, orden por orden, llegamos a soluciones analíticas. 
En la **Región Clásicamente Permitida** ($E > V(x)$), el momento local $p(x) = \sqrt{2m(E - V(x))}$ es un número real, y la función oscila (onda material de De Broglie ordinaria):

$$
\psi(x) \approx \frac{C}{\sqrt{p(x)}} \exp\left( \pm \frac{i}{\hbar} \int p(x) dx \right)
$$

*(Nota que la amplitud decae como $1/\sqrt{p}$; si la partícula se mueve más rápido, tiene menos probabilidad de ser encontrada geométricamente en esa región, restaurando el límite de la cinemática clásica pura de Newton).*

En la **Región Clásicamente Prohibida** (bajo una barrera, $E < V(x)$), $p(x)$ es imaginario. La solución WKB pasa automáticamente de funciones trigonométricas a exponenciales decaimiento, permitiendo modelar matemáticamente y numéricamente el Efecto Túnel Cuántico.

## 3. Puntos de Retorno y Funciones de Airy
El colapso matemático del método WKB ocurre exactamente en el **Punto de Retorno Clásico**, el punto del espacio donde la partícula agota su energía y frena ($E = V(x)$), y por tanto $p(x) = 0$. La función WKB diverge grotescamente hacia el infinito: $\frac{1}{\sqrt{0}} \to \infty$.

Para evitar el fin de las matemáticas, los físicos parchean la solución cerca del punto usando aproximaciones lineales para el potencial $V(x) \approx ax$. La ecuación diferencial linealizada se vuelve la infame **Ecuación Diferencial de Airy**. Insertando Funciones Matemáticas de Airy de forma microscópica, y conectándolas a las oscilaciones WKB de forma macroscópica (Fórmulas de Conexión), la física vuelve a operar milagrosamente y extrae las Reglas de Cuantización de Bohr-Sommerfeld.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Carl Bender: Mathematical Physics (Washington University)](https://www.youtube.com/playlist?list=PL1B1123DDB9DD4668) - Brillantes clases de perturbaciones, asintóticos y WKB impartidas por un genio del análisis.
- [ICTP: Mathematics for Physicists](https://www.youtube.com/user/ictp) - Herramientas analíticas puras desde Trieste.
