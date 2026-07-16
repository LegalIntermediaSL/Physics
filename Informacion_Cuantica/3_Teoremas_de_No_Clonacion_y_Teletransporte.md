# Teoremas de No-Clonación y Teletransporte

La información cuántica se rige por leyes opuestas a la computación clásica. En un PC tradicional puedes copiar el archivo `imagen.jpg` un millón de veces sin alterar el original (la operación COPY existe).
En la mecánica cuántica, la linealidad estricta del álgebra impone un límite absolutista a nuestra capacidad de duplicar información.

## 1. El Teorema de No-Clonación
Propuesto por Wootters, Zurek y Dieks (1982). **Es físicamente imposible construir una máquina (un operador unitario $U$) que cree una copia idéntica de un estado cuántico puro arbitrario e ignoto $|\psi\rangle$.**
**Demostración Rápida:**
Supongamos que existe un operador clonador unitario $U$ que toma el estado y un papel en blanco $|0\rangle$:

$$
U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle
$$

Para un segundo estado ortogonal $|\phi\rangle$, debe hacer lo mismo:

$$
U(|\phi\rangle \otimes |0\rangle) = |\phi\rangle \otimes |\phi\rangle
$$

Debido a que la mecánica cuántica debe ser estrictamente lineal, veamos qué ocurre con una superposición arbitraria $|\alpha\rangle = a|\psi\rangle + b|\phi\rangle$:
$U( (a|\psi\rangle + b|\phi\rangle) \otimes |0\rangle ) = a U(|\psi\rangle |0\rangle) + b U(|\phi\rangle |0\rangle) = a |\psi\rangle|\psi\rangle + b |\phi\rangle|\phi\rangle$
Pero una verdadera clonación requeriría que el resultado final fuera:
$(a|\psi\rangle + b|\phi\rangle) \otimes (a|\psi\rangle + b|\phi\rangle) = a^2|\psi\rangle|\psi\rangle + b^2|\phi\rangle|\phi\rangle + ab(|\psi\rangle|\phi\rangle + |\phi\rangle|\psi\rangle)$
Las expresiones no coinciden matemáticamente a menos que $a=1, b=0$ o $a=0, b=1$. **Ergo, la clonación cuántica universal viola la linealidad del universo.**

## 2. Teletransporte Cuántico
Dado que no podemos copiar (hacer "Ctrl+C"), ¿cómo movemos información cuántica? Con **Teletransporte**, que esencialmente hace "Cut+Paste".
Inventado por Bennett et al., permite transferir un estado desconocido $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ desde Alice hacia Bob utilizando:
1. Un canal cuántico de entrelazamiento pre-compartido (un par de Bell $|\Phi^+\rangle$).
2. Dos bits clásicos de comunicación telefónica.

Alice realiza una Medición de Bell conjunta entre su qubit y su mitad entrelazada. El colapso cuántico destruye el estado original $|\psi\rangle$ (cumpliendo a rajatabla el Teorema de No-Clonación) y proyecta instantáneamente la mitad de Bob en uno de 4 posibles estados disfrazados. Bob recibe la llamada telefónica de Alice con 2 bits (ej: "01"), aplica la compuerta de Pauli de corrección (ej: $\sigma_x$), y **recupera intacto el estado $|\psi\rangle$ original**. La información ha viajado sin cruzar el espacio físico entre ellos.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.370: Quantum Computation](https://ocw.mit.edu/courses/8-370-quantum-computation-fall-2020/) - Prof. Peter Shor (Inventor del Algoritmo de Shor).
  - [Qiskit Textbook (IBM)](https://qiskit.org/textbook/preface.html) - Curso interactivo gratuito de IBM Quantum.
- **Libros de Texto Canónicos:**
  - *Quantum Computation and Quantum Information* - Michael A. Nielsen & Isaac L. Chuang. (Conocido universalmente como "Mike & Ike", la Biblia absoluta del campo).
  - *Quantum Computing since Democritus* - Scott Aaronson.
