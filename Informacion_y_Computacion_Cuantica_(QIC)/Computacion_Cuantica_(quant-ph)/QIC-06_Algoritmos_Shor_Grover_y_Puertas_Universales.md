# [QIC-06] Computación Cuántica: Puertas Universales, Shor y Grover

## 1. Arquitectura Matricial: Qubits y Productos Tensoriales
En un ordenador clásico, el estado de n bits tiene tamaño $n$. En un ordenador cuántico, n Qubits requieren un Espacio de Hilbert de tamaño $2^n$ complejo. El estado total se construye mediante productos tensoriales $\otimes$. Una puerta lógica cuántica no es más que una **Matriz Unitaria U** ($U^{\dagger} U = I$) actuando sobre ese vector colosal, por lo que todo cálculo computacional cuántico es una rotación matemática pura y completamente reversible.

## 2. El Algoritmo de Búsqueda de Grover
Para encontrar un elemento específico en una base de datos desordenada clásica de tamaño $N$, tardas un orden de $O(N)$. Grover descubrió que aplicando iterativamente un Operador de Difusión Cuántica ("Reflexión sobre el Promedio") y un Oráculo de Fase, las amplitudes de probabilidad de todas las soluciones incorrectas se destruyen (interferencia destructiva), y la respuesta correcta se amplifica hasta $P=1$. Tardando sólo $O(\sqrt{N})$.

## 3. Destruyendo RSA: El Algoritmo de Shor
El cifrado militar y bancario de internet (RSA) asume que factorizar un número primo gigante $N = P \times Q$ es clásicamente incomputable. Peter Shor combinó la Teoría Cuántica con la Teoría de Números (Transformada de Fourier Cuántica, QFT). Transformó el problema de factorización en un problema de búsqueda de periodicidad modular. Un ordenador cuántico suficientemente grande factoriza a escala de tiempo Polinómica $O(\log^3 N)$, destruyendo por completo la criptografía moderna de un solo golpe cuántico.
