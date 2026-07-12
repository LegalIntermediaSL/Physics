# Fisión y Fusión
La fisión y la fusión nuclear son procesos opuestos que implican transmutaciones de núcleos atómicos con el fin de liberar grandes cantidades de energía, según la curva de energía de ligadura por nucleón. 

## 📜 Contexto Histórico
La fisión nuclear fue descubierta en diciembre de 1938 por los químicos alemanes Otto Hahn y Fritz Strassmann, y explicada teóricamente poco después por Lise Meitner y Otto Robert Frisch. Esto condujo al Proyecto Manhattan y la primera bomba atómica, y luego a la energía nuclear civil. La fusión nuclear, el proceso que alimenta a las estrellas, fue propuesta por Arthur Eddington en la década de 1920 y demostrada teóricamente por Hans Bethe en 1939 (ciclo CNO y cadena protón-protón).

## 🧮 Desarrollo Teórico Profundo
La liberación de energía en estas reacciones se debe a la diferencia de masa entre los reactivos y los productos, gobernada por la equivalencia masa-energía de Einstein:
$ Q = (\Delta M) c^2 = (m_{\text{reactivos}} - m_{\text{productos}}) c^2 $
Para que $ Q > 0 $ (reacción exotérmica), los productos deben estar más fuertemente ligados que los reactivos.

**Fisión (núcleos pesados, ej. Uranio-235):**
Un neutrón térmico induce la fisión:
$ ^{235}_{92}\text{U} + ^{1}_{0}\text{n} \to ^{236}_{92}\text{U}^* \to ^{141}_{56}\text{Ba} + ^{92}_{36}\text{Kr} + 3 ^{1}_{0}\text{n} + Q $
$ Q \approx 200 \text{ MeV} $. Los neutrones liberados pueden inducir una reacción en cadena.

**Fusión (núcleos ligeros, ej. D-T):**
$ ^{2}_{1}\text{H} + ^{3}_{1}\text{H} \to ^{4}_{2}\text{He} + ^{1}_{0}\text{n} + Q $
Para superar la repulsión de Coulomb (barrera de Coulomb $ V_C = \frac{1}{4\pi\epsilon_0} \frac{Z_1 Z_2 e^2}{R} $), los núcleos requieren energías cinéticas elevadas (altas temperaturas, $ \sim 10^8 $ K), posibilitadas en las estrellas gracias a la penetración de barrera por efecto túnel cuántico.

## 🛠 Ejemplo Práctico
**Problema:** Calcula la energía liberada ($ Q $) en la reacción de fusión Deuterio-Tritio.
Masas atómicas en u (unidades de masa atómica):
$ m(^{2}\text{H}) = 2.014102 \text{ u} $
$ m(^{3}\text{H}) = 3.016049 \text{ u} $
$ m(^{4}\text{He}) = 4.002603 \text{ u} $
$ m(\text{n}) = 1.008665 \text{ u} $
*Nota: $ 1 \text{ u} \approx 931.5 \text{ MeV}/c^2 $*.

**Solución paso a paso:**
1. **Calcular la masa de los reactivos:**
   $ m_{\text{reactivos}} = m(^{2}\text{H}) + m(^{3}\text{H}) = 2.014102 + 3.016049 = 5.030151 \text{ u} $
2. **Calcular la masa de los productos:**
   $ m_{\text{productos}} = m(^{4}\text{He}) + m(\text{n}) = 4.002603 + 1.008665 = 5.011268 \text{ u} $
3. **Calcular el defecto de masa ($ \Delta m $):**
   $ \Delta m = m_{\text{reactivos}} - m_{\text{productos}} = 5.030151 - 5.011268 = 0.018883 \text{ u} $
4. **Convertir el defecto de masa a energía:**
   $ Q = \Delta m \times 931.5 \text{ MeV/u} $
   $ Q = 0.018883 \times 931.5 \approx 17.59 \text{ MeV} $
Esta enorme liberación de energía por cada reacción a nivel atómico ilustra por qué la fusión es una prometedora fuente de energía limpia.

## 📚 Recursos Específicos
### Cursos
- "Plasma Physics and Applications" (edX - EPFL)
- "Nuclear Reactor Physics Basics" (Coursera)
- "Energy Processing in Stars" (University of Arizona OCW)

### Artículos y Simulaciones
- ITER Educational Resources (Simulador Tokamak)
- "Energy production in stars" (H. Bethe, 1939)
- "The Discovery of Nuclear Fission" (L. Meitner, O. R. Frisch, 1939)
- IAEA Nuclear Data Section
