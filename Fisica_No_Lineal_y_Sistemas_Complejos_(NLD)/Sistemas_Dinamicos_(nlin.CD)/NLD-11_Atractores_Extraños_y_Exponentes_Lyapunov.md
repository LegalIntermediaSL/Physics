# [NLD-11] Caos Determinista: Atractores y Lyapunov

## 1. Sensibilidad a Condiciones Iniciales (El Efecto Mariposa)
En un sistema caótico determinista, dos trayectorias que comienzan en puntos separados por una distancia infinitesimal $\delta x_0$ en el espacio de fases divergirán exponencialmente con el tiempo:
$$
|\delta x(t)| \approx e^{\lambda t} |\delta x_0|
$$
donde $\lambda > 0$ es el **Exponente de Lyapunov** máximo. A largo plazo, el sistema es fundamentalmente impredecible pese a no tener ningún elemento probabilístico.

## 2. Atractores Extraños
Los sistemas dinámicos disipativos (donde el volumen del espacio de fases se contrae) pueden evolucionar hacia un "Atractor". En sistemas caóticos (ej. Ecuaciones de Lorenz para convección atmosférica), este atractor tiene geometría fractal y se denomina "Atractor Extraño".
La trayectoria orbita la región indefinidamente sin cruzarse jamás consigo misma, exhibiendo aperiodicidad perpetua en un espacio acotado.
