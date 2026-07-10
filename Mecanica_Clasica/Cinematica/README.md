# Cinemática

La cinemática (del griego $\kappa\iota\nu\eta\mu\alpha$, kinema, "movimiento") es la rama de la mecánica clásica que describe el movimiento de puntos, cuerpos y sistemas de cuerpos sin considerar las fuerzas que provocan dicho movimiento.

## Conceptos Fundamentales

- **Posición ($\vec{r}$)**: Vector que indica la ubicación de un objeto en el espacio respecto a un sistema de coordenadas.
- **Desplazamiento ($\Delta\vec{r}$)**: Cambio neto en la posición. Es un vector independiente de la trayectoria tomada: $\Delta\vec{r} = \vec{r}_f - \vec{r}_i$.
- **Velocidad ($\vec{v}$)**: Tasa de cambio de la posición respecto al tiempo. 
  - Velocidad media: $\vec{v}_{med} = \frac{\Delta\vec{r}}{\Delta t}$
  - Velocidad instantánea: $\vec{v} = \frac{d\vec{r}}{dt}$
- **Aceleración ($\vec{a}$)**: Tasa de cambio de la velocidad respecto al tiempo.
  - Aceleración instantánea: $\vec{a} = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$

## Tipos de Movimiento

### 1. Movimiento Rectilíneo Uniforme (MRU)
Movimiento a velocidad constante y aceleración nula.
$ x(t) = x_0 + v t $

### 2. Movimiento Rectilíneo Uniformemente Acelerado (MRUA)
Movimiento bajo una aceleración constante $a$. Ecuaciones clave:
- $ v(t) = v_0 + a t $
- $ x(t) = x_0 + v_0 t + \frac{1}{2} a t^2 $
- $ v_f^2 = v_0^2 + 2a(x_f - x_0) $

### 3. Movimiento de Proyectiles (Tiro Parabólico)
Es la superposición de dos movimientos: un MRU horizontal y un MRUA vertical (caída libre bajo la gravedad $g$).
- $ x(t) = v_0 \cos(\theta) t $
- $ y(t) = v_0 \sin(\theta) t - \frac{1}{2} g t^2 $
