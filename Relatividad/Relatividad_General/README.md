# Relatividad General

La Relatividad General es la teoría métrica de la gravitación publicada por Albert Einstein en 1915, que describe la gravedad no como una fuerza, sino como una curvatura del espacio-tiempo causada por la masa y la energía.

## 📜 Contexto Histórico

Tras formular la Relatividad Especial en 1905, Einstein se dio cuenta de que esta teoría no era compatible con la ley de la gravitación universal de Newton, la cual implicaba una acción a distancia instantánea, violando el límite de la velocidad de la luz. 

Durante una década de intensa investigación y colaboración matemática con Marcel Grossmann, Einstein formuló el **Principio de Equivalencia** (1907), que postula que la gravedad y la aceleración son localmente indistinguibles. Usando la geometría diferencial de Riemann, Einstein concluyó que la presencia de masa o energía curva el espacio-tiempo. En noviembre de 1915, presentó las Ecuaciones de Campo de Einstein a la Academia Prusiana de las Ciencias. La teoría fue confirmada dramáticamente en 1919 por Arthur Eddington durante un eclipse solar al medir la deflexión de la luz de las estrellas, consolidando la fama mundial de Einstein.

---

## 🧮 Desarrollo Teórico Profundo

El núcleo de la Relatividad General son las **Ecuaciones de Campo de Einstein** (EFE). Son un conjunto de 10 ecuaciones diferenciales parciales no lineales (escritas como una única ecuación tensorial) que relacionan la geometría del espacio-tiempo con la distribución de materia y energía.

$$R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

Donde:
- $R_{\mu\nu}$: Tensor de curvatura de Ricci.
- $R$: Escalar de Ricci (curvatura escalar).
- $g_{\mu\nu}$: Tensor métrico (describe la métrica del espacio-tiempo).
- $\Lambda$: Constante cosmológica.
- $G$: Constante de gravitación universal.
- $c$: Velocidad de la luz.
- $T_{\mu\nu}$: Tensor de energía-impulso (densidad y flujo de energía y momento).

El lado izquierdo representa la **curvatura del espacio-tiempo**, y el lado derecho representa el **contenido de materia y energía**. En palabras de John Archibald Wheeler: *"El espacio-tiempo le dice a la materia cómo moverse; la materia le dice al espacio-tiempo cómo curvarse."*

**La Métrica de Schwarzschild:**
La primera solución exacta a estas ecuaciones fue encontrada por Karl Schwarzschild (1916) para una masa esférica y no rotatoria en el vacío. La métrica es:

$$ds^2 = \left(1 - \frac{r_s}{r}\right)c^2 dt^2 - \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 - r^2(d\theta^2 + \sin^2\theta d\phi^2)$$

Donde $r_s = \frac{2GM}{c^2}$ es el **Radio de Schwarzschild**. Si un objeto colapsa por debajo de este radio, se forma un agujero negro, de donde ni siquiera la luz puede escapar.

---

## 🛠 Ejemplo Práctico

**Problema:** Calcula el radio de Schwarzschild para el Sol ($M = 1.989 \times 10^{30}$ kg). Si el Sol colapsara a un agujero negro sin perder masa, ¿cuál sería el radio de su horizonte de sucesos?

**Solución paso a paso:**
1. Datos conocidos:
   - $G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$
   - $M = 1.989 \times 10^{30} \text{ kg}$
   - $c = 3 \times 10^8 \text{ m/s}$
2. Aplicamos la fórmula del radio de Schwarzschild:
   $$r_s = \frac{2GM}{c^2}$$
3. Sustituimos los valores:
   $$r_s = \frac{2 \times (6.674 \times 10^{-11}) \times (1.989 \times 10^{30})}{(3 \times 10^8)^2}$$
4. Realizamos los cálculos:
   - Numerador: $2 \times 6.674 \times 1.989 \times 10^{19} \approx 26.549 \times 10^{19}$
   - Denominador: $9 \times 10^{16}$
   $$r_s = \frac{26.549 \times 10^{19}}{9 \times 10^{16}} \approx 2.95 \times 10^3 \text{ metros}$$
5. Conclusión: El radio de Schwarzschild del Sol es aproximadamente 2.95 km (o $\approx 3$ km).

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
- **General Relativity por Leonard Susskind** (Stanford) - Introducción matemática profunda a la gravedad y tensores.
- **MIT 8.962 General Relativity** - Curso avanzado para entender matemáticas a nivel de posgrado.
- **Relatividad General (Canal Javier Santaolalla o Date un Vlog)** - Para intuición física general.

### 📝 Artículos e Interactivos Interesantes
- [Black Hole Simulator (Test of Relativity)](https://a-way-to-go.com/) o visualizaciones de simulaciones paramétricas de métricas.
- [Living Reviews in Relativity (Journal)](https://link.springer.com/journal/41114) - Revisiones fundamentales sobre temas avanzados.
- Wikipedia: [Ecuaciones de campo de Einstein](https://es.wikipedia.org/wiki/Ecuaciones_del_campo_de_Einstein)
