# Fisión y Fusión
La fisión y la fusión nuclear son procesos opuestos que implican transmutaciones de núcleos atómicos con el fin de liberar grandes cantidades de energía, según la curva de energía de ligadura por nucleón. 

## 📜 Contexto Histórico
La fisión nuclear fue descubierta en diciembre de 1938 por los químicos alemanes Otto Hahn y Fritz Strassmann, y explicada teóricamente poco después por Lise Meitner y Otto Robert Frisch. Esto condujo al Proyecto Manhattan y la primera bomba atómica, y luego a la energía nuclear civil. La fusión nuclear, el proceso que alimenta a las estrellas, fue propuesta por Arthur Eddington en la década de 1920 y demostrada teóricamente por Hans Bethe en 1939 (ciclo CNO y cadena protón-protón).

## 🧮 Desarrollo Teórico Profundo
La liberación de energía en estas reacciones se debe a la diferencia de masa entre los reactivos y los productos, gobernada por la equivalencia masa-energía de Einstein:
$$ Q = (\Delta M) c^2 = (m_{\text{reactivos}} - m_{\text{productos}}) c^2 $$
Para que $ Q > 0 $ (reacción exotérmica), los productos deben estar más fuertemente ligados que los reactivos.

**Fisión (núcleos pesados, ej. Uranio-235):**
Un neutrón térmico induce la fisión:
$$ ^{235}_{92}\text{U} + ^{1}_{0}\text{n} \to ^{236}_{92}\text{U}^* \to ^{141}_{56}\text{Ba} + ^{92}_{36}\text{Kr} + 3 ^{1}_{0}\text{n} + Q $$
$ Q \approx 200 \text{ MeV} $. Los neutrones liberados pueden inducir una reacción en cadena.

**Fusión (núcleos ligeros, ej. D-T):**
$$ ^{2}_{1}\text{H} + ^{3}_{1}\text{H} \to ^{4}_{2}\text{He} + ^{1}_{0}\text{n} + Q $$
Para superar la repulsión de Coulomb (barrera de Coulomb $ V_C = \frac{1}{4\pi\epsilon_0} \frac{Z_1 Z_2 e^2}{R} $), los núcleos requieren energías cinéticas elevadas (altas temperaturas, $ \sim 10^8 $ K), posibilitadas en las estrellas gracias a la penetración de barrera por efecto túnel cuántico.

## 🛠 Ejemplo Práctico
**Problema:** Calcula la energía liberada ($ Q $) en la reacción de fusión Deuterio-Tritio.
Masas atómicas en u (unidades de masa atómica):
$$ m(^{2}\text{H}) = 2.014102 \text{ u} $$
$$ m(^{3}\text{H}) = 3.016049 \text{ u} $$
$$ m(^{4}\text{He}) = 4.002603 \text{ u} $$
$$ m(\text{n}) = 1.008665 \text{ u} $$
*Nota: $ 1 \text{ u} \approx 931.5 \text{ MeV}/c^2 $*.

**Solución paso a paso:**
1. **Calcular la masa de los reactivos:**
   $$ m_{\text{reactivos}} = m(^{2}\text{H}) + m(^{3}\text{H}) = 2.014102 + 3.016049 = 5.030151 \text{ u} $$
2. **Calcular la masa de los productos:**
   $$ m_{\text{productos}} = m(^{4}\text{He}) + m(\text{n}) = 4.002603 + 1.008665 = 5.011268 \text{ u} $$
3. **Calcular el defecto de masa ($ \Delta m $):**
   $$ \Delta m = m_{\text{reactivos}} - m_{\text{productos}} = 5.030151 - 5.011268 = 0.018883 \text{ u} $$
4. **Convertir el defecto de masa a energía:**
   $$ Q = \Delta m \times 931.5 \text{ MeV/u} $$
   $$ Q = 0.018883 \times 931.5 \approx 17.59 \text{ MeV} $$
Esta enorme liberación de energía por cada reacción a nivel atómico ilustra por qué la fusión es una prometedora fuente de energía limpia.

## 📚 Recursos Específicos

### Cursos Online
1. "[Plasma Physics and Applications](https://www.edx.org/course/plasma-physics-and-applications)" (edX - EPFL)
2. "[Nuclear Reactor Physics Basics](https://www.coursera.org/learn/nuclear-reactor-physics)" (Coursera)
3. "[Energy Processing in Stars](https://ocw.mit.edu/courses/physics/8-284-modern-astrophysics-spring-2006/)" (University of Arizona OCW / MIT)
4. "[Introduction to Plasma Physics](https://ocw.mit.edu/courses/nuclear-engineering/22-611j-introduction-to-plasma-physics-i-fall-2003/)" (MIT OCW)
5. "[Fusion Energy: Principles and Technology](https://online.stanford.edu/)" (Stanford Online)
6. "[Advanced Nuclear Reactor Engineering](https://www.edx.org/)" (edX)

### Artículos y Simulaciones
1. "[ITER Educational Resources (Simulador Tokamak)](https://www.iter.org/education/)"
2. "[Energy production in stars](https://doi.org/10.1103/PhysRev.55.434)" (H. Bethe, 1939)
3. "[The Discovery of Nuclear Fission](https://doi.org/10.1038/143239a0)" (L. Meitner, O. R. Frisch, 1939)
4. "[IAEA Nuclear Data Section](https://www-nds.iaea.org/)"
5. "[The Mechanism of Nuclear Fission](https://doi.org/10.1103/PhysRev.56.426)" (N. Bohr and J. A. Wheeler, 1939)
6. "[Nuclear Fission](https://phet.colorado.edu/en/simulations/nuclear-fission)" (PhET Interactive Simulations)
7. "[Plasma confinement in Tokamaks](https://www.iter.org/mach/Tokamak)" (Review Article)
8. "[Inertial Confinement Fusion](https://lasers.llnl.gov/science/icf)" (NIF Publications)
9. "[Design and Operation of Pressurized Water Reactors](https://www.iaea.org/publications)" (IAEA Bulletin)

### 📖 Referencias Útiles y Bibliografía
- Lamarsh, J. R., & Baratta, A. J. (2001). *[Introduction to Nuclear Engineering](https://www.pearson.com/en-us/subject-catalog/p/introduction-to-nuclear-engineering/P200000006763)*. Prentice Hall.
- Chen, F. F. (1984). *[Introduction to Plasma Physics and Controlled Fusion](https://link.springer.com/book/10.1007/978-1-4757-5595-4)*. Springer.
- Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons.
- Stacey, W. M. (2010). *[Fusion Plasma Physics](https://www.wiley.com/en-us/Fusion+Plasma+Physics%2C+2nd+Edition-p-9783527411344)*. Wiley-VCH.
