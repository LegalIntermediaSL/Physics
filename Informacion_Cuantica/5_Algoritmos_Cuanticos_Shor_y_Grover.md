# Algoritmos Cuánticos (Shor y Grover)

Una Computadora Cuántica universal es un dispositivo que opera unitariamente sobre $n$ qubits usando el espacio de Hilbert completo de dimensión $2^n$. El poder no reside en el simple "paralelismo" de probar todo a la vez, sino en la **Interferencia Cuántica**: diseñar algoritmos donde las respuestas incorrectas cancelen sus fases (interferencia destructiva) y la respuesta correcta sume sus fases constructivamente.

## 1. Algoritmo de Shor (El Fin de la Criptografía RSA)
Toda nuestra seguridad bancaria e internet (RSA) depende de que factorizar un número primo masivo $N = p \times q$ toma un tiempo exponencial a una computadora clásica.
Peter Shor descubrió en 1994 que el problema de la factorización puede mapearse matemáticamente a un problema de encontrar el "período" $r$ de la función modular $f(x) = a^x \pmod N$.
El núcleo del milagro computacional es la **Transformada de Fourier Cuántica (QFT)**, un operador unitario que halla la periodicidad global de una superposición masiva en tiempo polinomial $\mathcal{O}((\log N)^3)$.
- Un PC requeriría la edad del universo para factorizar una clave moderna. Una PC cuántica lo haría en segundos, obligando a la humanidad a migrar al Post-Quantum Cryptography.

## 2. Algoritmo de Grover (Búsqueda Acelerada)
Imagina que buscas un nombre específico en una guía telefónica desordenada de $N$ páginas. Clásicamente debes leer, en promedio, $N/2$ páginas (tiempo lineal $\mathcal{O}(N)$).
Lov Grover (1996) diseñó un algoritmo iterativo usando la reflexión sobre el estado promedio de Hilbert (Inversión sobre la Media). Al aplicar el Oráculo (que marca la solución con una fase $-1$) y el operador de Difusión de Grover repetidas veces, la amplitud de probabilidad de la respuesta correcta crece, mientras el resto decae.
El estado cuántico converge en la solución correcta en exactamente $\mathcal{O}(\sqrt{N})$ pasos. Es una aceleración matemática cuadrática probada e imposible de batir.
