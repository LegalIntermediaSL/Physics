# Conceptos Básicos de Plasma

El plasma es a menudo considerado el cuarto estado de la materia, constituyendo más del 99% del universo visible. Se caracteriza por ser un gas cuasineutro de partículas cargadas y neutras que exhibe un comportamiento colectivo.

## 📜 Contexto Histórico

El término "plasma" fue acuñado por Irving Langmuir en 1928, inspirado en la forma en que el plasma sanguíneo transporta corpúsculos, ya que el plasma ionizado "transporta" electrones e iones. Su estudio se intensificó durante el desarrollo de tubos de vacío y más tarde, en la década de 1950, con la investigación en fusión termonuclear controlada.

## 🧮 Desarrollo Teórico Profundo

El comportamiento colectivo del plasma se debe a las interacciones de largo alcance de Coulomb. Una de las escalas espaciales más importantes es la **Longitud de Debye** ($\lambda_D$), que representa la distancia sobre la cual la carga de una partícula es apantallada por partículas de signo opuesto. Se define como:

$$ \lambda_D = \sqrt{\frac{\epsilon_0 k_B T_e}{n_e e^2}} $$

Donde:
- $\epsilon_0$ es la permitividad del vacío.
- $k_B$ es la constante de Boltzmann.
- $T_e$ es la temperatura de los electrones.
- $n_e$ es la densidad de electrones.
- $e$ es la carga elemental.

La condición fundamental de cuasineutralidad requiere que las dimensiones del sistema $L$ sean mucho mayores que $\lambda_D$ ($L \gg \lambda_D$).

Otra cantidad crucial es la **Frecuencia de Plasma** ($\omega_{pe}$), que describe la frecuencia característica de las oscilaciones de densidad de electrones en el plasma, proporcionando la escala temporal más rápida de respuesta electrostática:

$$ \omega_{pe} = \sqrt{\frac{n_e e^2}{m_e \epsilon_0}} $$

Donde $m_e$ es la masa del electrón.

Finalmente, el **Parámetro de Plasma** ($\Lambda$) indica el número de electrones dentro de una esfera de Debye. Para que un gas ionizado sea considerado un plasma, debe cumplirse que:

$$ \Lambda = \frac{4\pi}{3} n_e \lambda_D^3 \gg 1 $$

## 🛠 Ejemplo Práctico

**Problema:** Calcular la longitud de Debye y la frecuencia de plasma para el núcleo del Sol, asumiendo una densidad electrónica $n_e = 10^{32} \, \text{m}^{-3}$ y una temperatura de $T_e = 1.5 \times 10^7 \, \text{K}$.

**Solución paso a paso:**

1. **Datos:**
   - $n_e = 10^{32} \, \text{m}^{-3}$
   - $T_e = 1.5 \times 10^7 \, \text{K}$
   - $\epsilon_0 = 8.854 \times 10^{-12} \, \text{F/m}$
   - $k_B = 1.38 \times 10^{-23} \, \text{J/K}$
   - $e = 1.6 \times 10^{-19} \, \text{C}$
   - $m_e = 9.11 \times 10^{-31} \, \text{kg}$

2. **Cálculo de la Longitud de Debye ($\lambda_D$):**
   $$ \lambda_D = \sqrt{\frac{8.854 \times 10^{-12} \times 1.38 \times 10^{-23} \times 1.5 \times 10^7}{10^{32} \times (1.6 \times 10^{-19})^2}} $$
   $$ \lambda_D = \sqrt{\frac{1.83 \times 10^{-27}}{2.56 \times 10^{-6}}} \approx \sqrt{7.15 \times 10^{-22}} \approx 2.67 \times 10^{-11} \, \text{m} $$

3. **Cálculo de la Frecuencia de Plasma ($\omega_{pe}$):**
   $$ \omega_{pe} = \sqrt{\frac{10^{32} \times (1.6 \times 10^{-19})^2}{9.11 \times 10^{-31} \times 8.854 \times 10^{-12}}} $$
   $$ \omega_{pe} = \sqrt{\frac{2.56 \times 10^{-6}}{8.06 \times 10^{-42}}} \approx \sqrt{3.17 \times 10^{35}} \approx 1.78 \times 10^{17} \, \text{rad/s} $$

4. **Frecuencia lineal ($f_{pe}$):**
   $$ f_{pe} = \frac{\omega_{pe}}{2\pi} \approx 2.83 \times 10^{16} \, \text{Hz} $$

## 📚 Recursos Específicos

### Cursos Específicos
1. [Plasma Physics - Part 1 (MIT OCW)](https://ocw.mit.edu)
2. [Introduction to Plasmas (Coursera/Princeton)](https://www.coursera.org)
3. [Fundamentals of Plasmas - NPTEL](https://nptel.ac.in)

### Artículos y Simulaciones
1. Chen, F. F., *Introduction to Plasma Physics*. (Libro texto fundamental).
2. [NRL Plasma Formulary](https://www.nrl.navy.mil/) - Referencia de ecuaciones.
3. Langmuir, I. (1928). *Oscillations in Ionized Gases*. Proc. Natl. Acad. Sci.
4. [PhET Interactive Simulations - Charges and Fields](https://phet.colorado.edu/en/simulations/charges-and-fields)
