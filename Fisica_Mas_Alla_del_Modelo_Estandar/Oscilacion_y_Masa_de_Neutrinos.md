# Oscilación, Matriz PMNS y Masas de Neutrinos

En la formulación original del Modelo Estándar, los neutrinos son fermiones levógiros de Weyl estrictamente sin masa. Sin embargo, los experimentos de detectores de neutrinos solares (SNO) y atmosféricos (Super-Kamiokande) demostraron la metamorfosis de los neutrinos entre diferentes "sabores".

## 1. La Matriz PMNS y Oscilación de Fase Cuántica
La oscilación demuestra que los estados propios de sabor (interacción débil: $\nu_e, \nu_\mu, \nu_\tau$) no coinciden matricialmente con los estados propios de propagación libre o masa ($\nu_1, \nu_2, \nu_3$). 
Están vinculados matemáticamente por la matriz unitaria de mezcla de Pontecorvo-Maki-Nakagawa-Sakata ($U_{\text{PMNS}}$):

$$
|\nu_\alpha \rangle = \sum_i U_{\alpha i} |\nu_i \rangle
$$

Durante la propagación temporal en el vacío a una distancia $L$, los diferentes estados de masa adquieren diferentes fases cuánticas cuántico-mecánicas debido a sus diferencias de masa inercial. La probabilidad exacta asintótica de que un neutrino creado con sabor $\alpha$ sea detectado con sabor $\beta$ viene dada por la diferencia geométrica cuadrada de las masas:

$$
P(\nu_\alpha \to \nu_\beta) = \delta_{\alpha\beta} - 4 \sum_{i>j} \text{Re}(U_{\alpha i}^* U_{\beta i} U_{\alpha j} U_{\beta j}^*) \sin^2\left( \frac{\Delta m_{ij}^2 L}{4E} \right) + \text{términos } CP
$$

Dado que observamos $\Delta m_{ij}^2 \neq 0$, los neutrinos deben poseer innegablemente masa, lo que exige física estricta más allá del Modelo Estándar clásico.

## 2. Masas de Dirac, Majorana y el Mecanismo de Balancín (Seesaw)
Para dotar a los neutrinos de masa en el Lagrangiano, existen dos posibilidades teóricas matemáticamente distintas:
1. **Masa de Dirac**: Requiere la existencia de un neutrino dextrógiro ($\nu_R$) no interactuante estéril acoplado clásicamente con el bosón de Higgs a través de un término $\bar{\nu}_L m_D \nu_R$.
2. **Masa de Majorana**: Dado que el neutrino no tiene carga eléctrica, podría ser su propia antipartícula ($\nu = \bar{\nu}$). Esto permite un término de masa acoplado a sí mismo de la forma $\frac{1}{2} m_M \bar{\nu}_L^c \nu_L$.

El esquema teórico más prometedor combina ambas masas. Construyendo una matriz de masa $2 \times 2$ en la base $(\nu_L, \nu_R^c)$, el estado propio de energía resulta de su diagonalización algebraica:

$$
M = \begin{pmatrix} 0 & m_D \\ m_D & M_R \end{pmatrix}
$$

Si imponemos que la masa de Dirac $m_D$ está en la escala electrodébil ($100 \text{ GeV}$) y asumimos que $M_R$ está en la gigantesca escala de la Gran Unificación (GUT, $10^{15} \text{ GeV}$), la diagonalización proporciona un estado de neutrino observable ultra-ligero con masa matemática:

$$
m_\nu \approx \frac{m_D^2}{M_R}
$$

A este efecto asintótico se le denomina el **Mecanismo de Seesaw (Balancín)**, explicando elegantemente por qué el neutrino observable es millones de veces más ligero que el electrón.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Standard Model (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAvcsqMC6qB9A-M1jEik5Z4S) - Incluye discusiones profundas sobre las lagunas y roturas de simetría (Higgs).
- [CERN Lectures: BSM Physics](https://www.youtube.com/c/CERNlectures) - Seminarios avanzados directos desde los detectores del LHC.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Perimeter Institute Recorded Seminars (PIRSA)](https://pirsa.org/) - Búsquedas de Materia Oscura, Axiones y SUSY.
  - [CERN Document Server (Lectures)](https://cds.cern.ch/) - Cursos de verano para graduados sobre Nueva Física y el LHC.
- **Libros de Texto Canónicos:**
  - *Supersymmetry and String Theory: Beyond the Standard Model* - Michael Dine.
  - *Particle Dark Matter* - Gianfranco Bertone.
  - *Weak Scale Supersymmetry* - Howard Baer & Xerxes Tata.
