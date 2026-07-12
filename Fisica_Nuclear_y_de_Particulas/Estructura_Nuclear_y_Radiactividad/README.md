# Estructura Nuclear y Radiactividad
La estructura nuclear trata sobre cómo los protones y neutrones (nucleones) se unen mediante la fuerza nuclear fuerte para formar el núcleo del átomo. La radiactividad es el proceso estocástico por el cual núcleos inestables pierden energía emitiendo radiación.

## 📜 Contexto Histórico
La existencia del núcleo atómico fue revelada en 1911 por el experimento de la lámina de oro de Ernest Rutherford, Hans Geiger y Ernest Marsden, desmintiendo el modelo del pudín de ciruelas. En 1896, Henri Becquerel había descubierto accidentalmente la radiactividad al observar que sales de uranio oscurecían placas fotográficas, un trabajo expandido por Marie y Pierre Curie, quienes aislaron nuevos elementos radiactivos como el radio y el polonio.

## 🧮 Desarrollo Teórico Profundo
La masa de un núcleo atómico es menor que la suma de las masas de sus nucleones individuales debido a la **energía de ligadura** $ B $. La famosa fórmula semiempírica de masas (fórmula de Bethe-Weizsäcker) modela esta energía considerando el núcleo como una gota de líquido:
$ B(Z, A) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(A-2Z)^2}{A} + \delta(A,Z) $
donde $ A $ es el número másico (neutrones + protones) y $ Z $ es el número atómico (protones). Los términos representan la energía de volumen, superficie, repulsión de Coulomb, asimetría y un término de emparejamiento.

La ley de desintegración radiactiva es un proceso de Poisson donde la tasa de decaimiento es proporcional al número de núcleos inestables presentes $ N $:
$ \frac{dN}{dt} = -\lambda N \implies N(t) = N_0 e^{-\lambda t} $
La constante de desintegración $ \lambda $ está relacionada con el tiempo de vida media $ T_{1/2} $ por:
$ T_{1/2} = \frac{\ln(2)}{\lambda} $

## 🛠 Ejemplo Práctico
**Problema:** Una muestra de Carbono-14 ($ ^{14}\text{C} $) tiene una actividad inicial de 15 Bq/gramo. Se encuentra un artefacto de madera con una actividad de 3.75 Bq/gramo. Sabiendo que el periodo de semidesintegración ($ T_{1/2} $) del $ ^{14}\text{C} $ es de 5730 años, ¿cuál es la edad del artefacto?

**Solución paso a paso:**
1. **Determinar la relación de actividades:**
   La actividad $ A(t) $ es directamente proporcional al número de núcleos $ N(t) $: $ A(t) = \lambda N(t) $.
   Por lo tanto, la ley de decaimiento aplica también a la actividad:
   $ A(t) = A_0 e^{-\lambda t} $
2. **Despejar el tiempo $ t $:**
   $ \frac{A(t)}{A_0} = e^{-\lambda t} \implies \ln\left(\frac{A(t)}{A_0}\right) = -\lambda t $
   $ t = \frac{-\ln(A(t)/A_0)}{\lambda} $
3. **Calcular la constante de decaimiento $ \lambda $:**
   $ \lambda = \frac{\ln(2)}{T_{1/2}} = \frac{0.693}{5730 \text{ años}} \approx 1.209 \times 10^{-4} \text{ años}^{-1} $
4. **Calcular la edad:**
   $ t = \frac{-\ln(3.75 / 15)}{1.209 \times 10^{-4}} = \frac{-\ln(0.25)}{1.209 \times 10^{-4}} = \frac{1.386}{1.209 \times 10^{-4}} \approx 11460 \text{ años} $
   *Método alternativo más rápido:* 3.75 es exactamente $ 15 / 4 $, que equivale a dos periodos de semidesintegración ($ 15 \to 7.5 \to 3.75 $). Así, $ t = 2 \times 5730 = 11460 $ años.

## 📚 Recursos Específicos
### Cursos
- "Nuclear Physics Fundamentals" (Coursera)
- "Radiation and Radioactivity" (edX)
- "Applied Nuclear Physics" (MIT OCW)

### Artículos y Simulaciones
- PhET Interactive Simulations: "Radioactive Dating Game"
- PhET Interactive Simulations: "Nuclear Fission"
- "Radioactivity and transmutation of elements" (Rutherford & Soddy, 1903)
- NNDC (National Nuclear Data Center) Chart of Nuclides
