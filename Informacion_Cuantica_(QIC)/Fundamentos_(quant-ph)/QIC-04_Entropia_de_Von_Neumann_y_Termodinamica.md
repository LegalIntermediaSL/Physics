# [QIC-04] Entropía de Von Neumann y Termodinámica Cuántica

La Termodinámica Cuántica es la fusión definitiva de la Teoría de la Información (Shannon), la Termodinámica Estadística (Boltzmann) y el Álgebra Lineal (Heisenberg/Schrödinger). Su concepto pilar es la definición profunda de Entropía como Ignorancia Entrelazada.

## 1. La Entropía de Von Neumann
En termodinámica clásica, la entropía es $S = k_B \ln W$. En información clásica, Shannon la redefinió como $H = - \sum p_i \ln p_i$.
John von Neumann extendió esto a matrices de densidad, definiendo la entropía cuántica fundamental:

$$
S(\rho) = -\text{Tr}(\rho \ln \rho)
$$

Si diagonalizas $\rho$, los autovalores $\lambda_i$ representan las probabilidades, por lo que $S = -\sum \lambda_i \ln \lambda_i$.
- Si un estado es Absolutamente Puro ($|\psi\rangle$), $\rho$ tiene un único autovalor $1$ (y los demás $0$). Por lo tanto, $S = -1 \ln 1 = 0$. **Los estados puros no tienen entropía (conocemos todo).**
- Si un estado es totalmente Mixto ($I/d$), la entropía alcanza el límite máximo clásico $S = \ln d$.

## 2. El Demonio de Maxwell y el Principio de Landauer
Históricamente, Maxwell ideó un Demonio: un gnomo que abre una puerta para separar moléculas rápidas (calientes) y lentas (frías), disminuyendo la entropía de un gas y violando la Segunda Ley de la Termodinámica sin realizar trabajo.
Rolf Landauer (1961) y Charles Bennett demostraron que el Demonio no viola la Segunda Ley. El gnomo debe **medir y memorizar** la velocidad de las moléculas en su cerebro (o memoria flash).
El **Principio de Landauer** estipula matemáticamente que la computación lógica reversible (como un cálculo cuántico unitario) no gasta energía. Sin embargo, **borrar un bit de información de la memoria para reiniciar el sistema disipa un mínimo inexorable de calor**:

$$
Q_{borrado} \geq k_B T \ln 2
$$

El Demonio se calienta al borrar su memoria, salvando eternamente la Termodinámica.

## 3. Entrelazamiento como Entropía Térmica
Supón que el Universo entero (Alicia y Bob) está en un estado Puro colosal $|\Psi_{AB}\rangle$ de entropía cero absoluto ($S_{AB} = 0$).
Si Alicia solo tiene acceso a su subsistema $A$, ignorando por completo la existencia de la galaxia $B$, debe realizar una traza parcial: $\rho_A = \text{Tr}_B (|\Psi_{AB}\rangle\langle\Psi_{AB}|)$.
Incluso si el universo entero está frío y perfectamente puro, el subsistema local de Alicia, $\rho_A$, parecerá termodinámicamente caliente y mixto, con una alta Entropía de Von Neumann. **La aparente termodinámica caótica y la temperatura local que experimentamos a diario podrían ser simplemente el resultado del masivo entrelazamiento cuántico oculto con el resto del universo.**

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.370: Quantum Computation](https://ocw.mit.edu/courses/8-370-quantum-computation-fall-2020/) - Prof. Peter Shor (Inventor del Algoritmo de Shor).
  - [Qiskit Textbook (IBM)](https://qiskit.org/textbook/preface.html) - Curso interactivo gratuito de IBM Quantum.
- **Libros de Texto Canónicos:**
  - *Quantum Computation and Quantum Information* - Michael A. Nielsen & Isaac L. Chuang. (Conocido universalmente como "Mike & Ike", la Biblia absoluta del campo).
  - *Quantum Computing since Democritus* - Scott Aaronson.
