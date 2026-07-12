# Electrostática

La electrostática es la rama de la física que estudia los efectos mutuos que se producen entre los cuerpos como consecuencia de sus cargas eléctricas en reposo. Constituye la base fundamental del electromagnetismo y describe cómo las cargas interactúan mediante fuerzas a distancia, creando campos eléctricos y acumulando energía potencial.

## 📜 Contexto Histórico
El estudio de la electrostática se remonta a la antigüedad clásica, cuando Tales de Mileto observó que frotar ámbar (cuyo nombre en griego es *elektron*) atraía objetos ligeros. Sin embargo, el estudio formal comenzó en el siglo XVIII. Benjamin Franklin propuso el principio de conservación de la carga y acuñó los términos positivo y negativo. En 1785, Charles-Augustin de Coulomb formuló la ley de la fuerza electrostática mediante experimentos con una balanza de torsión. Posteriormente, Michael Faraday introdujo el concepto revolucionario de "campo eléctrico", transformando la física de la acción a distancia en una teoría de campos locales, y Carl Friedrich Gauss formuló el teorema de flujo eléctrico, estableciendo un pilar matemático esencial.

---

## 🧮 Desarrollo Teórico Profundo

### Ley de Coulomb
La fuerza $\vec{F}$ entre dos cargas puntuales $q_1$ y $q_2$ separadas por una distancia $r$ en el vacío está dada por:
$$ \vec{F} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2} \hat{r} $$
donde $\varepsilon_0 \approx 8.854 \times 10^{-12} \, \text{C}^2/(\text{N}\cdot\text{m}^2)$ es la permitividad del vacío.

### Campo Eléctrico
El campo eléctrico $\vec{E}$ se define como la fuerza por unidad de carga que experimentaría una carga de prueba $q_0$:
$$ \vec{E} = \frac{\vec{F}}{q_0} $$
Para una carga puntual $q$, el campo generado a una distancia $r$ es:
$$ \vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r} $$
El principio de superposición establece que el campo total creado por una distribución de cargas es la suma vectorial de los campos individuales: $\vec{E} = \sum \vec{E}_i$.

### Ley de Gauss
La Ley de Gauss relaciona el flujo eléctrico $\Phi_E$ a través de una superficie cerrada $S$ con la carga neta $Q_{\text{enc}}$ encerrada por dicha superficie:
$$ \oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} $$
Esta ley es extremadamente poderosa para calcular campos eléctricos en sistemas con alta simetría (esférica, cilíndrica o plana).

### Potencial Eléctrico
Dado que la fuerza electrostática es conservativa ($\nabla \times \vec{E} = 0$), el campo eléctrico puede expresarse como el gradiente negativo de un potencial escalar $V$:
$$ \vec{E} = -\nabla V $$
La diferencia de potencial entre dos puntos $A$ y $B$ es el trabajo por unidad de carga necesario para mover la carga:
$$ V_B - V_A = -\int_A^B \vec{E} \cdot d\vec{l} $$

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular el campo eléctrico a una distancia $r$ del centro de una esfera aislante de radio $R$ que tiene una carga total $Q$ distribuida uniformemente en todo su volumen.

**Solución paso a paso:**
1. **Identificar la simetría:** La distribución tiene simetría esférica. Por tanto, el campo eléctrico debe ser radial: $\vec{E} = E(r)\hat{r}$.
2. **Definir la densidad de carga:** La densidad volumétrica de carga es $\rho = \frac{Q}{\frac{4}{3}\pi R^3}$.
3. **Aplicar la Ley de Gauss en el interior ($r < R$):**
   Consideramos una superficie gaussiana esférica de radio $r$.
   $$ \oint_S \vec{E} \cdot d\vec{A} = E(4\pi r^2) $$
   La carga encerrada es $Q_{\text{enc}} = \rho (\frac{4}{3}\pi r^3) = Q \frac{r^3}{R^3}$.
   $$ E(4\pi r^2) = \frac{Q}{\varepsilon_0} \frac{r^3}{R^3} \implies \vec{E}_{\text{int}} = \frac{Q}{4\pi\varepsilon_0 R^3} r \, \hat{r} $$
4. **Aplicar la Ley de Gauss en el exterior ($r \ge R$):**
   La carga encerrada es total, $Q_{\text{enc}} = Q$.
   $$ E(4\pi r^2) = \frac{Q}{\varepsilon_0} \implies \vec{E}_{\text{ext}} = \frac{Q}{4\pi\varepsilon_0 r^2} \hat{r} $$

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
* **MIT 8.02 (Electricity and Magnetism):** Las famosas clases del profesor Walter Lewin. La primera parte se enfoca intensamente en electrostática.
* **The Feynman Lectures on Physics:** Volumen II, Capítulos 4-12, lectura obligatoria para una comprensión profunda e intuitiva.
* **Khan Academy - Física (Electrostática):** Para un repaso de los conceptos con ejemplos rápidos paso a paso.

### 📝 Artículos e Interactivos Interesantes
* **PhET Interactive Simulations - Charges and Fields:** Una excelente herramienta para visualizar campos eléctricos y líneas equipotenciales.
* **Artículo de Wikipedia sobre la Balanza de Torsión de Coulomb:** Detalles experimentales históricos sobre cómo se midió $\varepsilon_0$.
* **PhET - Globos y Electricidad Estática:** Para entender la polarización e inducción de cargas a un nivel básico e intuitivo.
