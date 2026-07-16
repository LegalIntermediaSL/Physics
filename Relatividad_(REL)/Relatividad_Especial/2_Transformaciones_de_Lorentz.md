# Transformaciones de Lorentz

## 1. Sustituyendo a Galileo
En la física clásica, cambiar de sistema de referencia (ej. moverse en un tren a velocidad constante $v$ en el eje $x$) se describía con las Transformaciones de Galileo: $x' = x - vt$, $t' = t$. 
Sin embargo, estas ecuaciones no preservan la velocidad de la luz $c$, por lo que fallan ante las Ecuaciones de Maxwell.

Las **Transformaciones de Lorentz** son las rotaciones hiperbólicas del espacio-tiempo que preservan la métrica de Minkowski y garantizan que $c$ es absoluta.

## 2. Factor de Lorentz ($\gamma$)
El corazón matemático de la relatividad especial es el factor de contracción/dilatación:

$$
\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
$$

## 3. Ecuaciones Algebraicas (Boost en Eje X)
Para un observador $O'$ que se mueve a velocidad $v$ respecto a $O$ a lo largo del eje $x$:

$$
t' = \gamma \left( t - \frac{v x}{c^2} \right)
$$

$$
x' = \gamma (x - vt)
$$

$$
y' = y
$$

$$
z' = z
$$

Estas simples ecuaciones generan los fenómenos de **Dilatación del Tiempo** (el tiempo corre más lento para el reloj en movimiento) y **Contracción de la Longitud** (los objetos se acortan en la dirección de su movimiento).

## 4. Representación Matricial y Grupo de Lorentz $SO(1,3)$
Definiendo el parámetro de rapidez $\beta = v/c$, el "boost" se representa como una matriz que multiplica un cuadrivector de coordenadas $X^\mu$:

$$
\begin{pmatrix} ct' \\ x' \\ y' \\ z' \end{pmatrix} = \begin{pmatrix} \gamma & -\gamma\beta & 0 & 0 \\ -\gamma\beta & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} ct \\ x \\ y \\ z \end{pmatrix}
$$

