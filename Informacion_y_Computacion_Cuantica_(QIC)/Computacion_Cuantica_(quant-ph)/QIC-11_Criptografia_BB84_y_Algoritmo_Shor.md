# [QIC-11] Criptografía BB84 y Factorización de Shor

## 1. Protocolo BB84 (1984)
Es el primer protocolo de Distribución de Claves Cuánticas (QKD). Utiliza estados de polarización de fotones individuales. Alice envía fotones eligiendo al azar entre dos bases no ortogonales (ej. Rectilínea $+$, Diagonal $\times$).
La seguridad radica en el **Teorema de No-Clonación** y en que cualquier "espía" (Eve) inevitablemente colapsará el estado superpuesto introduciendo una tasa de error (QBER) detectable por Alice y Bob.

## 2. Algoritmo de Shor
El algoritmo clásico más rápido para factorizar un número entero $N$ es sub-exponencial. El Algoritmo de Shor es polinómico $\mathcal{O}((\log N)^3)$.
Reduce la factorización al problema de "Búsqueda de Periodo" (Period Finding), utilizando para ello la Transformada Cuántica de Fourier (QFT) sobre una superposición masiva de estados de fase, causando interferencia constructiva exactamente en la solución periódica.
