# [MTH-14] Operadores Neuronales: DeepONets y FNO

## 1. Mapeo de Función a Función
Las redes neuronales clásicas mapean puntos de un espacio euclidiano finito (ej. un vector de píxeles) a otro vector. Los Operadores Neuronales generalizan esto mapeando un Espacio de Funciones (ej. las condiciones iniciales de un fluido) a otro Espacio de Funciones (ej. el campo de velocidades futuro).

## 2. Fourier Neural Operator (FNO)
Aprovecha que la convolución de funciones continuas es una multiplicación en el dominio de la frecuencia. La red FNO aplica Transformadas Rápidas de Fourier (FFT), filtra las altas frecuencias no esenciales del espacio funcional, aplica multiplicaciones matriciales lineales, y hace la iFFT.
Esto permite resolver ecuaciones como Navier-Stokes hasta 1000 veces más rápido que un solver tradicional de CFD, independientemente de la resolución de la malla elegida en la inferencia (*Zero-Shot Super Resolution*).
