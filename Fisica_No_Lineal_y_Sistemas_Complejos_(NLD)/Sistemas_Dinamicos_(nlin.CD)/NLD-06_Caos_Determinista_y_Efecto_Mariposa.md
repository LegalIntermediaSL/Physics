# [NLD-06] Caos Determinista, Efecto Mariposa y el Atractor de Lorenz

## 1. El Paradigma del Caos Determinista
Históricamente se pensaba que un sistema determinista (sin ruido ni aleatoriedad cuántica) era perfectamente predecible. Henri Poincaré, al estudiar el problema de los tres cuerpos orbitales, descubrió que sistemas puramente newtonianos pueden exhibir "Sensibilidad Extrema a las Condiciones Iniciales": órbitas infinitesimalmente cercanas divergen exponencialmente rápido.

## 2. El Atractor Extraño de Lorenz (1963)
Edward Lorenz simplificó las ecuaciones de Navier-Stokes para el clima atmosférico en tres ecuaciones diferenciales ordinarias acopladas:
$\frac{dx}{dt} = \sigma(y - x)$
$\frac{dy}{dt} = x(\rho - z) - y$
$\frac{dz}{dt} = xy - \beta z$
El resultado en el espacio de fases (3D) no era un punto fijo, ni un ciclo límite, sino un fractal infinito con forma de mariposa: el **Atractor Extraño**. El estado viaja eternamente alrededor de dos bucles sin jamás cruzarse consigo mismo ni repetir la misma órbita.

## 3. Exponentes de Lyapunov y Dimensión Fractal
Para cuantificar cuán caótico es un sistema, calculamos sus **Exponentes de Lyapunov**. Si el máximo exponente $\lambda > 0$, dos trayectorias se separan como $e^{\lambda t}$, perdiendo toda información inicial en un horizonte de tiempo finito (El "Horizonte de Predecibilidad").
