# Fundamentos y Dualidad Onda-Partícula

En esta sección exploramos los orígenes de la mecánica cuántica, donde la física clásica (newtoniana y maxwelliana) fracasó al intentar explicar fenómenos a escala atómica, dando lugar a una nueva descripción de la naturaleza en términos de cuantos de energía y el comportamiento dual onda-partícula.

## 📜 Contexto Histórico
A finales del siglo XIX y principios del XX, una serie de experimentos inexplicables para la física clásica iniciaron la revolución cuántica:
* **Max Planck (1900)**: Para resolver la "catástrofe ultravioleta" en la radiación del cuerpo negro, propuso que la energía electromagnética se emite y absorbe en "cuantos" discretos.
* **Albert Einstein (1905)**: Explicó el efecto fotoeléctrico postulando que la luz en sí misma está cuantizada en fotones.
* **Arthur Compton (1923)**: Demostró que los fotones tienen momento y pueden colisionar con electrones como si fueran partículas (Efecto Compton).
* **Louis de Broglie (1924)**: Extendió la idea de la dualidad luz-partícula a la materia, sugiriendo que las partículas masivas, como los electrones, también tienen propiedades ondulatorias.

---

## 🧮 Desarrollo Teórico Profundo

### Radiación del Cuerpo Negro
La ley de Rayleigh-Jeans predecía que la radiancia espectral divergía a altas frecuencias ($\nu$):
$$ \rho(\nu, T) = \frac{8\pi \nu^2 k_B T}{c^3} $$
Planck modificó esto asumiendo que la energía de los osciladores en las paredes de la cavidad está cuantizada, $E = nh\nu$. La distribución de Planck resultante es:
$$ \rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu/k_B T} - 1} $$
Esto evita la catástrofe ultravioleta para $\nu \to \infty$.

### El Efecto Fotoeléctrico
La energía máxima de los electrones emitidos por un metal iluminado por luz depende de la frecuencia $\nu$ y no de la intensidad. Einstein propuso que la luz está formada por cuantos (fotones) de energía $E = h\nu$.
$$ K_{\max} = h\nu - \Phi $$
Donde $\Phi$ es la función de trabajo del metal y $h$ es la constante de Planck ($6.626 \times 10^{-34} \text{ J}\cdot\text{s}$).

### Hipótesis de de Broglie
De Broglie propuso que cualquier partícula con momento $p$ tiene asociada una longitud de onda $\lambda$:
$$ \lambda = \frac{h}{p} = \frac{h}{mv} $$
Esto introdujo formalmente la dualidad onda-partícula para electrones, protones y átomos enteros, confirmada más tarde por el experimento de difracción de electrones de Davisson y Germer (1927).

---

## 🛠 Ejemplo Práctico
**Problema:** Calcula la longitud de onda de de Broglie de un electrón acelerado desde el reposo a través de una diferencia de potencial de $V = 100 \text{ V}$.

**Solución paso a paso:**
1. La energía cinética ganada por el electrón es $K = eV$, donde $e = 1.6 \times 10^{-19} \text{ C}$.
$$ K = (1.6 \times 10^{-19} \text{ C})(100 \text{ V}) = 1.6 \times 10^{-17} \text{ J} $$
2. Relacionamos la energía cinética (no relativista) con el momento:
$$ K = \frac{p^2}{2m_e} \implies p = \sqrt{2m_e K} $$
3. Sustituimos la masa del electrón $m_e = 9.11 \times 10^{-31} \text{ kg}$:
$$ p = \sqrt{2 (9.11 \times 10^{-31}) (1.6 \times 10^{-17})} \approx 5.4 \times 10^{-24} \text{ kg}\cdot\text{m/s} $$
4. Usamos la relación de de Broglie:
$$ \lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{5.4 \times 10^{-24}} \approx 1.23 \times 10^{-10} \text{ m} = 0.123 \text{ nm} $$
La longitud de onda está en el rango de los rayos X, adecuada para difracción cristalina.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
* **MIT 8.04 Quantum Physics I (Prof. Allan Adams):** Clase 1 y 2, excelentes para motivación histórica y el fallo de la física clásica.
* **Stanford - Quantum Mechanics (Leonard Susskind):** Introducción a la rareza cuántica y el experimento de la doble rendija.
* **Física Cuántica Básica (Universidad de Colorado):** Clases teóricas sobre orígenes de la cuántica.

### 📝 Artículos e Interactivos Interesantes
* **PhET Interactive Simulations:** *Photoelectric Effect* (Excelente simulación visual del experimento de Einstein).
* **PhET Interactive Simulations:** *Blackbody Spectrum* (Visualiza cómo cambia la curva de Planck con la temperatura).
* **Artículo Histórico (Wikipedia):** [Experimento de Davisson-Germer](https://es.wikipedia.org/wiki/Experimento_de_Davisson-Germer) (Evidencia experimental de de Broglie).
