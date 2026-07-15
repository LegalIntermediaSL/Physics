# Momento Angular y Espín

El Momento Angular ($\mathbf{L} = \mathbf{r} \times \mathbf{p}$) es el generador matemático de las rotaciones espaciales en mecánica cuántica. Sin embargo, los electrones poseen un momento angular intrínseco (Espín $\mathbf{S}$) que no tiene ningún análogo en la física clásica (no es una bola girando, es una propiedad puntual fundamental).

## 1. El Álgebra $SU(2)$ de las Rotaciones
Independientemente de si es Orbital ($\mathbf{L}$) o Espín ($\mathbf{S}$), cualquier operador genérico de momento angular $\mathbf{J}$ debe obedecer las Reglas de Conmutación del álgebra de Lie $\mathfrak{su}(2)$:

$$
[\hat{J}_i, \hat{J}_j] = i\hbar\epsilon_{ijk} \hat{J}_k
$$

Dado que $J_x, J_y, J_z$ no conmutan entre sí, no podemos medirlos a la vez. Sin embargo, el operador de magnitud total $\hat{J}^2$ sí conmuta con todos ellos. Elegimos medir simultáneamente $\hat{J}^2$ y $\hat{J}_z$.

## 2. Los Números Cuánticos ($j, m$)
La teoría de representaciones demuestra que los autovalores están matemáticamente obligados a ser discretos:

$$
\hat{J}^2 |j, m\rangle = \hbar^2 j(j+1) |j, m\rangle
$$

$$
\hat{J}_z |j, m\rangle = \hbar m |j, m\rangle
$$

Donde $j$ puede ser entero o semientero ($0, 1/2, 1, 3/2, 2...$), y $m$ va desde $-j$ hasta $+j$ en pasos enteros.

## 3. Armónicos Esféricos vs Matrices de Pauli
- Para el **Momento Angular Orbital ($L$)**, $j$ se denomina $l$ y solo toma valores *enteros* ($0, 1, 2...$). Su representación espacial real produce funciones trigonométricas en la esfera: los **Armónicos Esféricos** $Y_l^m(\theta, \phi)$ (las formas de los orbitales atómicos s, p, d, f).
- Para el **Espín del Electrón ($S$)**, $j$ toma el valor semientero $1/2$. Esto no se puede dibujar en el espacio tridimensional real. Requiere la representación matemática en espacios de Espinores bidimensionales, donde los operadores se escriben como las **Matrices de Pauli** ($\sigma_x, \sigma_y, \sigma_z$). Un giro de 360 grados en una partícula de espín $1/2$ no la devuelve a su estado original, invierte su signo cuántico (fase -1). Se necesitan 720 grados para volver a la normalidad topológica.
