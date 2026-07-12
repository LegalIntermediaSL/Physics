# Laboratorio y Medición

La física es fundamentalmente una ciencia experimental. Los conceptos de precisión, exactitud, propagación de errores, instrumentación, y estadística de datos son críticos para validar o refutar hipótesis teóricas. La capacidad de discernir entre la "señal verdadera" y el "ruido instrumental" es el corazón de la ciencia física real.

## 📜 Contexto Histórico

El auge de la física experimental moderna se le atribuye a Galileo Galilei por su uso sistemático del experimento para entender el plano inclinado y el péndulo, contrastando la filosofía natural especulativa aristotélica. El desarrollo de instrumentos ópticos (microscopios, telescopios) expandió enormemente las fronteras de medición en el siglo XVII. Hacia el siglo XIX, el refinamiento en la medición electromagnética liderado por Faraday y Maxwell, y más tarde los precisos experimentos interferométricos de Michelson-Morley, abrieron las puertas a la relatividad y la cuántica. Hoy, experimentos como LIGO o el LHC operan en los límites absolutos de lo que tecnológicamente puede medirse.

## 🧮 Desarrollo Teórico Profundo

**Teoría de Errores y Estadística:**

Ninguna medición es absolutamente exacta. Una medida se reporta como:
$ x = \bar{x} \pm \delta x $

La **media muestral** para $N$ mediciones es la mejor estimación del valor real:
$ \bar{x} = \frac{1}{N} \sum_{i=1}^N x_i $

El error estándar de la media está ligado a la **desviación estándar** $\sigma$:
$ \sigma_x = \sqrt{ \frac{1}{N-1} \sum_{i=1}^N (x_i - \bar{x})^2 } \quad \implies \quad \delta \bar{x} = \frac{\sigma_x}{\sqrt{N}} $

**Propagación de Errores:**
Si calculamos una magnitud $q = f(x, y, z)$ a partir de mediciones independientes, la incertidumbre resultante se obtiene expandiendo $f$ en serie de Taylor de primer orden (asumiendo variables no correlacionadas):
$ \delta q = \sqrt{ \left( \frac{\partial f}{\partial x} \delta x \right)^2 + \left( \frac{\partial f}{\partial y} \delta y \right)^2 + \left( \frac{\partial f}{\partial z} \delta z \right)^2 } $

En mediciones que siguen estadística de conteo (como fotomultiplicadores o decaimientos radiactivos), la fluctuación estadística sigue la **distribución de Poisson**, donde la varianza es igual a la media, por lo que el error inherente para $N$ conteos es:
$ \sigma_N = \sqrt{N} $

## 🛠 Ejemplo Práctico

**Problema:** Medición de la gravedad y propagación de incertidumbre.

Un estudiante mide el período $T$ de un péndulo simple de longitud $L$ para determinar $g$. La relación es $g = 4\pi^2 L / T^2$.
Mide:
- $L = 1.000 \pm 0.005$ m.
- $T = 2.00 \pm 0.02$ s.
Determinar $g$ y su incertidumbre $\delta g$.

**Solución paso a paso:**
1. Calculamos el valor central de $g$:
   $ g = 4 \pi^2 \frac{1.000}{(2.00)^2} = 4 \pi^2 \frac{1.000}{4.00} = \pi^2 \approx 9.8696 \, \text{m/s}^2 $
2. Para una función multiplicativa $g = C L T^{-2}$, la fórmula de propagación de error relativo simplificada es:
   $ \left( \frac{\delta g}{g} \right)^2 = \left( \frac{\delta L}{L} \right)^2 + \left( -2 \frac{\delta T}{T} \right)^2 $
3. Evaluamos los errores relativos individuales:
   - Para $L$: $\frac{\delta L}{L} = \frac{0.005}{1.000} = 0.005 = 0.5\%$
   - Para $T$: $\frac{\delta T}{T} = \frac{0.02}{2.00} = 0.01 = 1.0\%$
4. Propagamos el error relativo al cuadrado:
   $ \left( \frac{\delta g}{g} \right)^2 = (0.005)^2 + (2 \times 0.01)^2 = 0.000025 + 0.0004 = 0.000425 $
5. Extraemos la raíz cuadrada para obtener el error relativo de $g$:
   $ \frac{\delta g}{g} = \sqrt{0.000425} \approx 0.0206 \, (2.06\%) $
6. Obtenemos la incertidumbre absoluta:
   $ \delta g = 0.0206 \times 9.8696 \approx 0.203 \, \text{m/s}^2 $
**Conclusión:** El resultado final de la medición se reporta (redondeando al primer dígito incierto) como $g = 9.87 \pm 0.20 \, \text{m/s}^2$. Notar que el error en $T$ domina ampliamente la incertidumbre total porque su contribución se cuadriplica al estar al cuadrado en la fórmula.

## 📚 Recursos Específicos
- **Cursos:** Physics Laboratory Courses (MIT OCW, serie 8.13/8.14), MOOCs sobre Data Analysis and Statistics in Physics.
- **Artículos/Textos:** *An Introduction to Error Analysis* de John R. Taylor (el libro definitivo para estudiantes); *Practical Physics* de G.L. Squires; Entornos interactivos de simulación de circuitos y laboratorios virtuales (PhET).
