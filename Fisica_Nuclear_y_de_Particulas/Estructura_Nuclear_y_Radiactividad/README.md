# Estructura Nuclear y Radiactividad
La estructura nuclear trata sobre cómo los protones y neutrones (nucleones) se unen mediante la fuerza nuclear fuerte para formar el núcleo del átomo. La radiactividad es el proceso estocástico por el cual núcleos inestables pierden energía emitiendo radiación.

## 📜 Contexto Histórico
La existencia del núcleo atómico fue revelada en 1911 por el experimento de la lámina de oro de Ernest Rutherford, Hans Geiger y Ernest Marsden, desmintiendo el modelo del pudín de ciruelas. En 1896, Henri Becquerel había descubierto accidentalmente la radiactividad al observar que sales de uranio oscurecían placas fotográficas, un trabajo expandido por Marie y Pierre Curie, quienes aislaron nuevos elementos radiactivos como el radio y el polonio.

## 🧮 Desarrollo Teórico Profundo
La masa de un núcleo atómico es menor que la suma de las masas de sus nucleones individuales debido a la **energía de ligadura** $ B $. La famosa fórmula semiempírica de masas (fórmula de Bethe-Weizsäcker) modela esta energía considerando el núcleo como una gota de líquido:
$$ B(Z, A) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(A-2Z)^2}{A} + \delta(A,Z) $$
donde $ A $ es el número másico (neutrones + protones) y $ Z $ es el número atómico (protones). Los términos representan la energía de volumen, superficie, repulsión de Coulomb, asimetría y un término de emparejamiento.

La ley de desintegración radiactiva es un proceso de Poisson donde la tasa de decaimiento es proporcional al número de núcleos inestables presentes $ N $:
$$ \frac{dN}{dt} = -\lambda N \implies N(t) = N_0 e^{-\lambda t} $$
La constante de desintegración $ \lambda $ está relacionada con el tiempo de vida media $ T_{1/2} $ por:
$$ T_{1/2} = \frac{\ln(2)}{\lambda} $$

## 🛠 Ejemplo Práctico
**Problema:** Una muestra de Carbono-14 ($ ^{14}\text{C} $) tiene una actividad inicial de 15 Bq/gramo. Se encuentra un artefacto de madera con una actividad de 3.75 Bq/gramo. Sabiendo que el periodo de semidesintegración ($ T_{1/2} $) del $ ^{14}\text{C} $ es de 5730 años, ¿cuál es la edad del artefacto?

**Solución paso a paso:**
1. **Determinar la relación de actividades:**
   La actividad $ A(t) $ es directamente proporcional al número de núcleos $ N(t) $: $ A(t) = \lambda N(t) $.
   Por lo tanto, la ley de decaimiento aplica también a la actividad:
   $$ A(t) = A_0 e^{-\lambda t} $$
2. **Despejar el tiempo $ t $:**
   $$ \frac{A(t)}{A_0} = e^{-\lambda t} \implies \ln\left(\frac{A(t)}{A_0}\right) = -\lambda t $$
   $$ t = \frac{-\ln(A(t)/A_0)}{\lambda} $$
3. **Calcular la constante de decaimiento $ \lambda $:**
   $$ \lambda = \frac{\ln(2)}{T_{1/2}} = \frac{0.693}{5730 \text{ años}} \approx 1.209 \times 10^{-4} \text{ años}^{-1} $$
4. **Calcular la edad:**
   $$ t = \frac{-\ln(3.75 / 15)}{1.209 \times 10^{-4}} = \frac{-\ln(0.25)}{1.209 \times 10^{-4}} = \frac{1.386}{1.209 \times 10^{-4}} \approx 11460 \text{ años} $$
   *Método alternativo más rápido:* 3.75 es exactamente $ 15 / 4 $, que equivale a dos periodos de semidesintegración ($ 15 \to 7.5 \to 3.75 $). Así, $ t = 2 \times 5730 = 11460 $ años.

## 📚 Recursos Específicos

### Cursos Online
1. "[Nuclear Physics Fundamentals](https://www.coursera.org/learn/nuclear-physics)" (Coursera)
2. "[Radiation and Radioactivity](https://www.edx.org/course/radiation-and-radioactivity)" (edX)
3. "[Applied Nuclear Physics](https://ocw.mit.edu/courses/nuclear-engineering/22-02-introduction-to-applied-nuclear-physics-spring-2012/)" (MIT OCW)
4. "[Introduction to Nuclear Science](https://online.stanford.edu/)" (Stanford Online)
5. "[Nuclear Reactions and Isotope Production](https://www.coursera.org/)" (Coursera)
6. "[Health Physics and Radiation Protection](https://www.edx.org/)" (edX)

### Artículos y Simulaciones
1. "[Radioactive Dating Game](https://phet.colorado.edu/en/simulations/radioactive-dating-game)" (PhET Interactive Simulations)
2. "[Nuclear Fission](https://phet.colorado.edu/en/simulations/nuclear-fission)" (PhET Interactive Simulations)
3. "[Radioactivity and transmutation of elements](https://www.jstor.org/stable/90831)" (Rutherford & Soddy, 1903)
4. "[Chart of Nuclides](https://www.nndc.bnl.gov/nudat3/)" (NNDC)
5. "[The Mass of the Neutron](https://doi.org/10.1038/129312a0)" (J. Chadwick, 1932)
6. "[On the Constitution of Atoms and Molecules](https://doi.org/10.1080/14786441308634955)" (N. Bohr, 1913)
7. "[Nuclear Data Sheets for A=1 to 294](https://www.nndc.bnl.gov/nds/)" (NNDC)
8. "[Beta Decay and the Neutrino Hypothesis](https://arxiv.org/abs/physics/0609139)" (W. Pauli, 1930)

### 📖 Referencias Útiles y Bibliografía
- Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons.
- Turner, J. E. (2007). *[Atoms, Radiation, and Radiation Protection](https://www.wiley.com/en-us/Atoms%2C+Radiation%2C+and+Radiation+Protection%2C+3rd+Edition-p-9783527406067)*. Wiley-VCH.
- Lilley, J. (2001). *[Nuclear Physics: Principles and Applications](https://www.wiley.com/en-us/Nuclear+Physics%3A+Principles+and+Applications-p-9780471979364)*. Wiley.
- Knoll, G. F. (2010). *[Radiation Detection and Measurement](https://www.wiley.com/en-us/Radiation+Detection+and+Measurement%2C+4th+Edition-p-9780470131480)*. Wiley.
