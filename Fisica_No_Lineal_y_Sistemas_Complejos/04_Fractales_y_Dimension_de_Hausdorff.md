# Fractales y Dimensión de Hausdorff

## 1. Geometría Fractal
Un fractal es un objeto matemático que exhibe auto-similitud a cualquier escala de observación y posee una dimensión no entera. Son las estructuras canónicas que subyacen a los atractores extraños en el caos y a procesos físicos rugosos de agregación limitada por difusión.

## 2. Dimensión de Capacidad (Box-Counting Dimension)
Para medir la dimensión topológica rugosa de un conjunto $S$, lo cubrimos con cajas de longitud de lado $\epsilon$. Sea $N(\epsilon)$ el número de cajas con al menos un punto de $S$. La dimensión fractal es:

$$
D_0 = \lim_{\epsilon \to 0} \frac{\ln N(\epsilon)}{\ln(1/\epsilon)}
$$

## 3. Conjunto de Cantor
El fractal arquetípico. Se obtiene al eliminar el tercio central de un segmento y repetir al infinito.
- Factor de escala: $1/\epsilon = 3$
- Número de segmentos: $N = 2$
Su dimensión es estrictamente fraccionaria:

$$
D = \frac{\ln 2}{\ln 3} \approx 0.6309
$$

## 4. Dinámica Compleja y el Conjunto de Mandelbrot
Generado iterando una ecuación polinomial no lineal en el plano complejo $z \in \mathbb{C}$:

$$
z_{n+1} = z_n^2 + c
$$

El conjunto de Mandelbrot $\mathcal{M}$ es el conjunto de parámetros $c$ para los cuales la sucesión $z_n$ (iniciando en $z_0=0$) está acotada. El límite del conjunto es un fractal hiper-complejo. Para un $c$ fijo, el conjunto de puntos iniciales $z_0$ estables forma el **Conjunto de Julia**, $J_c$.
