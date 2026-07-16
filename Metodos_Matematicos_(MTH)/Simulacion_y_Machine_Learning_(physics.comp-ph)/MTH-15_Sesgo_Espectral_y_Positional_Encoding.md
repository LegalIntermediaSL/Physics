# [MTH-15] Sesgo Espectral (Spectral Bias) en Redes Físicas

## 1. El Problema de las Frecuencias Bajas
Las Redes Neuronales Profundas exhiben un "Sesgo Espectral": aprenden rápidamente las componentes de baja frecuencia de una función, pero tienen enormes dificultades para converger en las variaciones de alta frecuencia (detalles finos, turbulencia, ondas estacionarias).

## 2. El Teorema de Aproximación Universal vs Dinámica de Optimización
Aunque una red neuronal puede aproximar teóricamente cualquier función continua, en la práctica el gradiente descendente (Adam/L-BFGS) se estanca al intentar replicar ondas rápidas en problemas de propagación electromagnética u osciladores acoplados rígidos.

## 3. Positional Encoding y Características de Fourier
La solución (importada desde el diseño de redes Transformers y NeRFs) es proyectar las coordenadas de entrada $(x, t)$ a un espacio hiperdimensional utilizando funciones trigonométricas de múltiples frecuencias:

$$
\gamma(v) = (\sin(2^0 \pi v), \cos(2^0 \pi v), \dots, \sin(2^{L-1} \pi v), \cos(2^{L-1} \pi v))
$$

Al alimentar a la red con estas características incrustadas, forzamos su atención matemática hacia las altas frecuencias, mitigando el Spectral Bias y permitiendo simulaciones de dinámica de fluidos multiescala (ej. Kolmogorov micro-scales).
