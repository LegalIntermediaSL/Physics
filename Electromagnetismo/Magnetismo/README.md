# Magnetismo

El magnetismo es la rama de la física que describe los fenómenos magnéticos, que surgen como resultado del movimiento de cargas eléctricas (corrientes) y de momentos magnéticos intrínsecos de las partículas elementales (espín).

## 📜 Contexto Histórico
Durante milenios, el magnetismo se consideró un fenómeno misterioso asociado a la magnetita. En 1820, Hans Christian Ørsted descubrió de forma accidental que una brújula se desviaba cerca de un cable con corriente, estableciendo la primera conexión entre electricidad y magnetismo. Poco después, Jean-Baptiste Biot y Félix Savart formularon la ley empírica que describe el campo generado por un segmento de corriente. André-Marie Ampère extendió estos trabajos y demostró que las corrientes se atraen o repelen de forma análoga a los imanes, fundando la electrodinámica. Finalmente, Hendrik Lorentz formalizó la fuerza que experimenta una carga móvil dentro de un campo electromagnético.

---

## 🧮 Desarrollo Teórico Profundo

### Fuerza Magnética y Fuerza de Lorentz
Una carga $q$ que se mueve con velocidad $\vec{v}$ en presencia de un campo magnético $\vec{B}$ experimenta una fuerza dada por:
$$ \vec{F}_m = q (\vec{v} \times \vec{B}) $$
Si además existe un campo eléctrico $\vec{E}$, la fuerza total es la Fuerza de Lorentz:
$$ \vec{F} = q(\vec{E} + \vec{v} \times \vec{B}) $$

### Ley de Biot-Savart
El campo magnético $d\vec{B}$ creado en un punto en el espacio por un elemento diferencial de corriente $Id\vec{l}$ viene dado por:
$$ d\vec{B} = \frac{\mu_0}{4\pi} \frac{I \, d\vec{l} \times \hat{r}}{r^2} $$
donde $\mu_0 = 4\pi \times 10^{-7} \, \text{T}\cdot\text{m}/\text{A}$ es la permeabilidad magnética del vacío, y $\vec{r}$ es el vector que va desde el elemento al punto.

### Ley de Ampère
La Ley de Ampère es el equivalente magnético de la Ley de Gauss para situaciones de alta simetría. Relaciona la circulación del campo magnético a lo largo de una curva cerrada $C$ con la corriente total $I_{\text{enc}}$ que la atraviesa:
$$ \oint_C \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}} $$
En forma diferencial: $\nabla \times \vec{B} = \mu_0 \vec{J}$.

### Flujo Magnético y Ausencia de Monopolos
A diferencia de las cargas eléctricas, no existen fuentes aisladas (monopolos) de campo magnético. Por tanto, las líneas de campo magnético siempre son cerradas. Matemáticamente, el flujo a través de cualquier superficie cerrada es nulo (Ley de Gauss para el magnetismo):
$$ \oint_S \vec{B} \cdot d\vec{A} = 0 \quad \implies \quad \nabla \cdot \vec{B} = 0 $$

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular el campo magnético $\vec{B}$ a una distancia $r$ de un hilo recto e infinito que transporta una corriente constante $I$.

**Solución paso a paso:**
1. **Identificar la simetría:** El sistema tiene simetría cilíndrica. Las líneas de campo magnético formarán círculos concéntricos alrededor del hilo.
2. **Aplicar la Ley de Ampère:** 
   Seleccionamos un bucle amperiano circular de radio $r$ centrado en el hilo. Por simetría, la magnitud de $\vec{B}$ es constante a lo largo de este bucle, y el vector $\vec{B}$ es tangente a la curva en cada punto.
3. **Calcular la circulación:**
   $$ \oint \vec{B} \cdot d\vec{l} = B \oint dl = B (2\pi r) $$
4. **Relacionar con la corriente:**
   La corriente encerrada por el bucle es $I$. Por lo tanto:
   $$ B (2\pi r) = \mu_0 I $$
5. **Resultado final:**
   $$ B = \frac{\mu_0 I}{2\pi r} $$
   La dirección se obtiene usando la regla de la mano derecha.

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
* **MIT 8.02 (Electricity and Magnetism):** Lecciones sobre campos magnéticos y la Ley de Ampère.
* **The Feynman Lectures on Physics:** Vol. 2, Capítulos 13 y 14 (Magnetostatics & Magnetic Field in Various Situations).
* **Yale Fundamentals of Physics II (PHYS 201):** Clases del Profesor Ramamurti Shankar sobre magnetismo y fuerzas sobre cargas.

### 📝 Artículos e Interactivos Interesantes
* **PhET - Laboratorio Electromagnético de Faraday:** Permite interactuar con imanes, bobinas y visualizar los campos magnéticos creados por corrientes.
* **HyperPhysics - Magnetism:** Un árbol de conceptos muy útil sobre la teoría magnética.
* **Oersted's Experiment (Artículo Histórico):** Leer acerca de los experimentos originales de Ørsted que relacionaron la aguja de una brújula con la corriente eléctrica.
