# Los Muchos Mundos: Decoherencia y Matrices Densidad

La Interpretación de los Muchos Mundos (Many-Worlds Interpretation, MWI) fue desarrollada por Hugh Everett III en su tesis doctoral de Princeton (1957). Para entender la potencia matemática de esta interpretación, debemos formular el "Problema de la Medición" en términos rigurosos.

## 1. El Problema de Von Neumann-Wigner

En la interpretación ortodoxa (Copenhague/Von Neumann), la evolución del estado cuántico obedece dos leyes contradictorias y mutuamente exclusivas:

* **Proceso 1 (Dinámica Unitaria):** Si el sistema no se observa, evoluciona de manera determinista, reversible, local y lineal según la Ecuación de Schrödinger:
  $$
   |\Psi(t)\rangle = e^{-i \hat{H} t / \hbar} |\Psi(0)\rangle 
  $$
* **Proceso 2 (Postulado de Colapso):** Al momento de realizarse una "medición" por un aparato macrosópico (clásico), la evolución unitaria se interrumpe violenta y no-localmente. La función de onda del sistema $|\Psi\rangle = \sum c_i |a_i\rangle$ colapsa aleatoriamente hacia uno de los estados propios del observable $|a_k\rangle$ con probabilidad absoluta $p_k = |c_k|^2$ (Regla de Born).

El absurdo epistemológico de Copenhague es el dualismo: ¿Dónde está exactamente el "corte de Heisenberg" entre lo cuántico (microscópico unitario) y lo clásico (macroscópico colapsante)? Everett argumentó astutamente que este corte es un artefacto inexistente; **todo el universo, de principio a fin, debe regirse puramente por el Proceso 1 (la Ecuación de Schrödinger).**

## 2. El Formalismo del Entrelazamiento Observador-Sistema

Supongamos un electrón en una superposición pura de espín vertical:
$$
 |\psi\rangle_e = \alpha |\uparrow\rangle + \beta |\downarrow\rangle 
$$
Y un aparato de medición (o un humano) inicialmente en un estado neutral: $|M\rangle_{ready}$.

En la formulación de Everett, el aparato interactúa con el electrón a través de un Hamiltoniano de interacción cuántica estándar. La evolución unitaria produce una transición entrelazada:
Si $|\uparrow\rangle |M\rangle_{ready} \to |\uparrow\rangle |M\rangle_{\text{lee arriba}}$
y $|\downarrow\rangle |M\rangle_{ready} \to |\downarrow\rangle |M\rangle_{\text{lee abajo}}$

Por el principio de linealidad de la Ecuación de Schrödinger, el estado combinado (Universo) tras la medición es ineludiblemente:
$$
 |\Psi_{universo}\rangle = \alpha \left( |\uparrow\rangle \otimes |M\rangle_{\text{lee arriba}} \right) + \beta \left( |\downarrow\rangle \otimes |M\rangle_{\text{lee abajo}} \right) 
$$

**La función de onda no ha colapsado.** Simplemente, el aparato de medición (el observador) ha entrado en un estado entrelazado con el electrón. Desde la perspectiva estricta del sub-estado $|M\rangle_{\text{lee arriba}}$, el electrón está definitivamente hacia arriba. Desde la perspectiva de $|M\rangle_{\text{lee abajo}}$, el electrón está hacia abajo. Everett llamó a esto "Estados Relativos". El universo se ha escindido en dos ramas (dos mundos) igualmente reales.

## 3. La Decoherencia Cuántica (H. Dieter Zeh y Wojciech Zurek)

Un desafío masivo a MWI era la "Base Preferida": ¿Por qué la superposición matemática colapsa en estados espaciales o posiciones concretas (estado de un gato vivo o muerto) y no en combinaciones lineales arbitrarias raras?

La respuesta matemática moderna es la **Decoherencia Ambiental**. El observador no solo interacciona con el electrón, sino con un gigantesco "Baño Ambiental" (fotones parásitos, moléculas de aire, $10^{23}$ átomos): $|E\rangle$.

Si introducimos el ambiente, el estado global evoluciona rápidamente a:
$$
 |\Psi_{total}\rangle = \alpha |\uparrow\rangle |M\rangle_{arriba} |E\rangle_{\uparrow} + \beta |\downarrow\rangle |M\rangle_{abajo} |E\rangle_{\downarrow} 
$$
La distinción crucial es que los estados ambientales de un sistema macroscópico son **ortogonales** rápidamente: $\langle E_{\uparrow} | E_{\downarrow} \rangle \to 0$.

### La Matriz Densidad Reducida
El observador nunca tiene acceso a medir cada fotón del universo para demostrar la interferencia entre ramas. Matemáticamente, debemos hacer la **traza parcial** sobre los grados de libertad del entorno ($\text{Tr}_E$) para obtener la matriz densidad reducida del sistema (Electrón + Aparato):
$$
 \rho_S = \text{Tr}_E \left( |\Psi_{total}\rangle \langle \Psi_{total}| \right) 
$$
$$
 \rho_S \approx |\alpha|^2 \left( |\uparrow\rangle |M\rangle_{\uparrow} \right) \left( \langle \uparrow| \langle M|_{\uparrow} \right) + |\beta|^2 \left( |\downarrow\rangle |M\rangle_{\downarrow} \right) \left( \langle \downarrow| \langle M|_{\downarrow} \right) 
$$
¡Los términos de interferencia fuera de la diagonal (que demostrarían la superposición cuántica macroscópica) han sido aniquilados exponencialmente por la ortogonalidad del ambiente! 

La matriz densidad se ha vuelto estrictamente **diagonal**, imitando perfectamente una mezcla estadística clásica de probabilidades para el observador interno. La mecánica cuántica unitaria pura explica, sin necesidad de postulados místicos de colapso, por qué el universo experimenta divisiones clásicas probabilísticas.

## 4. La Regla de Born y el Teorema de Gleason

La principal crítica moderna a la MWI es el origen de las probabilidades. Si la función de onda es totalmente determinista y todas las ramas ocurren físicamente, ¿qué significa que una rama con $\alpha = \sqrt{0.9}$ es "más probable" que una con $\beta = \sqrt{0.1}$?

La justificación más potente descansa en el **Teorema de Gleason (1957)**, modificado mediante aproximaciones de teoría de decisión y argumentos de conteo (David Wallace, Simon Saunders). El teorema establece que en un espacio de Hilbert de dimensión $\ge 3$, la *única* asignación matemática consistente de medidas de peso (medidas probabilísticas aditivas) a los subespacios de Hilbert debe tomar la forma $\text{Tr}(\rho P_k)$, que es directamente equivalente a la Regla de Born $p_k = |c_k|^2$. La probabilidad no refleja una aleatoriedad ontológica, sino una "medida de peso o densidad ontológica" en el espacio de Hilbert estático del universo.
