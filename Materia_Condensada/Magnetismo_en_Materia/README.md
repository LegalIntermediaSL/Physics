# Magnetismo en Materia

El magnetismo en la materia es el estudio de cómo los materiales responden a los campos magnéticos y cómo los momentos magnéticos intrínsecos de sus partículas elementales (principalmente electrones) interactúan entre sí. Esta rama abarca desde el diamagnetismo y paramagnetismo débil hasta fenómenos cooperativos fuertes como el ferromagnetismo, el antiferromagnetismo y el ferrimagnetismo.

## 📜 Contexto Histórico

El conocimiento del magnetismo se remonta a la antigüedad con el descubrimiento de la magnetita (piedra imán). El entendimiento moderno comenzó con los trabajos de Oersted, Ampère y Faraday en el siglo XIX, unificando electricidad y magnetismo. Sin embargo, la explicación del ferromagnetismo requirió de la mecánica cuántica. En 1907, Pierre Weiss introdujo la idea de un "campo molecular" para explicar el alineamiento espontáneo de los espines. Más tarde, en 1928, Werner Heisenberg explicó que este campo molecular era una consecuencia directa del **principio de exclusión de Pauli** y la **interacción de intercambio** culombiana, sentando las bases del magnetismo cuántico.

## 🧮 Desarrollo Teórico Profundo

A nivel microscópico, el momento magnético de un átomo proviene del momento angular orbital y del espín electrónico. El hamiltoniano básico para un átomo en un campo magnético externo $\mathbf{B}$ incluye el efecto Zeeman:
$ H = -\boldsymbol{\mu} \cdot \mathbf{B} = \frac{e}{2m} (\mathbf{L} + g_0 \mathbf{S}) \cdot \mathbf{B} $

El **Ferromagnetismo** se describe fundamentalmente mediante el modelo de Heisenberg. El Hamiltoniano de intercambio entre momentos magnéticos (espines) en una red está dado por:
$ H_{Heis} = -2 \sum_{\langle i,j \rangle} J_{ij} \mathbf{S}_i \cdot \mathbf{S}_j $
donde $J_{ij}$ es la integral de intercambio y la suma es sobre pares de vecinos más cercanos.
- Si $J > 0$, el estado de menor energía favorece espines paralelos (ferromagnetismo).
- Si $J < 0$, favorece espines antiparalelos (antiferromagnetismo).

En el modelo de Weiss de campo medio, reemplazamos la interacción con los vecinos por un campo magnético efectivo (el campo molecular):
$ \mathbf{B}_{eff} = \mathbf{B}_{ext} + \lambda \mathbf{M} $
Esto lleva a la predicción de una temperatura crítica (Temperatura de Curie, $T_C$), por encima de la cual se destruye el orden ferromagnético debido a las fluctuaciones térmicas:
$ M \propto \left( T_C - T \right)^\beta \quad \text{para } T < T_C $
y una susceptibilidad magnética que sigue la ley de Curie-Weiss para $T > T_C$:
$ \chi = \frac{C}{T - T_C} $

## 🛠 Ejemplo Práctico

**Problema:** Obtener la ley de Curie para un gas ideal de iones paramagnéticos con espín $S=1/2$ bajo un campo magnético $B$.

**Solución paso a paso:**
1. Para $S=1/2$, los dos posibles estados del espín a lo largo del campo magnético (dirección $z$) tienen energías de Zeeman:
   $ E_\uparrow = -\mu_B B $ y $ E_\downarrow = +\mu_B B $
   (asumiendo $g \approx 2$, $\mu_z = \pm \mu_B$).
2. La probabilidad térmica de estar en cada estado sigue la distribución de Boltzmann:
   $ p_\uparrow = \frac{1}{Z} e^{\mu_B B / k_B T} $
   $ p_\downarrow = \frac{1}{Z} e^{-\mu_B B / k_B T} $
   donde la función de partición es $Z = e^{\mu_B B / k_B T} + e^{-\mu_B B / k_B T} = 2 \cosh\left(\frac{\mu_B B}{k_B T}\right)$.
3. El momento magnético promedio de un ion es:
   $ \langle \mu_z \rangle = \mu_B p_\uparrow + (-\mu_B) p_\downarrow = \mu_B \frac{e^{\mu_B B / k_B T} - e^{-\mu_B B / k_B T}}{e^{\mu_B B / k_B T} + e^{-\mu_B B / k_B T}} = \mu_B \tanh\left(\frac{\mu_B B}{k_B T}\right) $
4. Para altas temperaturas o campos débiles ($k_B T \gg \mu_B B$), aproximamos $\tanh(x) \approx x$:
   $ \langle \mu_z \rangle \approx \mu_B \left( \frac{\mu_B B}{k_B T} \right) = \frac{\mu_B^2 B}{k_B T} $
5. La magnetización $M$ para $N$ iones por unidad de volumen es:
   $ M = N \langle \mu_z \rangle = \frac{N \mu_B^2}{k_B T} B $
**Conclusión:** La susceptibilidad magnética $\chi = \mu_0 \frac{M}{B} = \frac{\mu_0 N \mu_B^2}{k_B T}$, lo que demuestra la **Ley de Curie** $\chi = C/T$.

## 📚 Recursos Específicos
- **Cursos:** Magnetism and Magnetic Materials (NPTEL), Spintronics and Magnetism en EdX.
- **Artículos/Simulaciones:** *Magnetism and Magnetic Materials* de J. M. D. Coey; *Introduction to Magnetic Materials* de B.D. Cullity; Simulador de Ising Model para observar transiciones de fase (disponible en plataformas de física computacional).
