# [QIC-11] Códigos de Corrección de Errores Cuánticos

## 1. El Problema del Ruido Cuántico
A diferencia de los bits clásicos (que sufren *bit-flips*), los qubits sufren errores continuos:
1.  **Bit-flip ($X$):** El estado $|0\rangle$ se convierte en $|1\rangle$.
2.  **Phase-flip ($Z$):** El estado $|+\rangle$ se convierte en $|-\rangle$ (decoherencia).
3.  Errores continuos (rotaciones arbitrarias parciales).

Además, el **Teorema de No-Clonación** impide copiar qubits para hacer redundancia clásica (como enviar 000 en lugar de 0). Por último, medir un qubit para comprobar si tiene un error, destruye su superposición.

## 2. El Código de Shor (9-Qubits)
Peter Shor inventó el primer código capaz de corregir tanto *bit-flips* como *phase-flips*. Funciona entrelazando 1 qubit lógico en 9 qubits físicos.

El qubit lógico $|0\rangle_L$ se define como:
$$
|0\rangle_L = \frac{1}{2\sqrt{2}} (|000\rangle + |111\rangle) \otimes (|000\rangle + |111\rangle) \otimes (|000\rangle + |111\rangle)
$$
El qubit lógico $|1\rangle_L$ invierte los signos:
$$
|1\rangle_L = \frac{1}{2\sqrt{2}} (|000\rangle - |111\rangle) \otimes (|000\rangle - |111\rangle) \otimes (|000\rangle - |111\rangle)
$$

Los errores se detectan midiendo el "síndrome" (paridad) de pares de qubits usando puertas CNOT auxiliares (ancillas), sin medir el estado del qubit en sí mismo.

## 3. Códigos Topológicos (Surface Codes)
El estándar moderno para el hardware escalable son los Códigos de Superficie (*Surface Codes*), desarrollados por Alexei Kitaev. 
Aquí, los qubits se disponen en un retículo (lattice) 2D. 
*   **Data Qubits:** Residen en las aristas del retículo.
*   **Measurement Qubits (Ancillas):** Residen en las caras y vértices. Miden operadores estabilizadores $X^{\otimes 4}$ (estrellas) y $Z^{\otimes 4}$ (plaquetas).

Si ocurre un error, los estabilizadores adyacentes reportan valores defectuosos. Encontrar la corrección óptima se reduce al problema clásico de Minimum Weight Perfect Matching (MWPM) sobre un grafo, haciendo que la corrección de errores cuánticos sea extremadamente robusta al ruido local.
