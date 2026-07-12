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
1. [MIT 8.04 Quantum Physics I (Allan Adams)](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/): Clases 1 y 2, absolutamente excelentes para motivación histórica, relatando paso a paso el fallo espectacular de la física clásica.
2. [Stanford - Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtWCAh1E_yT1eF82k7bFepf): Introducción magistral a la "rareza cuántica" utilizando la fenomenología del experimento de la doble rendija.
3. [Física Cuántica Básica (Universidad de Colorado)](https://www.coursera.org/learn/quantum-mechanics): Clases teóricas (Coursera/edX) que cubren exhaustivamente los orígenes históricos de la teoría de los cuantos.
4. [Yale PHYS 201 (Ramamurti Shankar)](https://oyc.yale.edu/physics/phys-201): Las primeras conferencias de este curso brindan una transición inigualable entre la óptica de ondas clásica y el fotón cuántico.
5. [Khan Academy - Quantum Physics](https://es.khanacademy.org/science/physics/quantum-physics): Módulos cortos enfocados en comprender cualitativamente y cuantitativamente la radiación de cuerpo negro y el efecto fotoeléctrico.

### 📝 Artículos e Interactivos Interesantes
1. **PhET Interactive Simulations:** [Photoelectric Effect](https://phet.colorado.edu/en/simulations/photoelectric) - Excelente simulación visual del experimento que le dio el Nobel a Einstein.
2. **PhET Interactive Simulations:** [Blackbody Spectrum](https://phet.colorado.edu/en/simulations/blackbody-spectrum) - Visualiza cómo cambia la curva de emisión de Planck en función de la temperatura del objeto.
3. **HyperPhysics:** [Wave-Particle Duality](http://hyperphysics.phy-astr.gsu.edu/hbase/mod1.html) - Mapa conceptual interactivo que conecta la fórmula de De Broglie, el fotón y los experimentos.
4. **Wikipedia:** [Experimento de Davisson-Germer](https://es.wikipedia.org/wiki/Experimento_de_Davisson-Germer) - Descripción de la primera evidencia experimental firme de la difracción de electrones predicha por de Broglie.
5. **Wikipedia:** [Catástrofe Ultravioleta](https://es.wikipedia.org/wiki/Cat%C3%A1strofe_ultravioleta) - Explicación matemática del fallo de la ley de Rayleigh-Jeans.
6. **Stanford Encyclopedia of Philosophy:** [The Equivalence of Mass and Energy & Quantum Early Origins](https://plato.stanford.edu/entries/equivME/) - Contexto filosófico sobre la materia y la energía a la luz de los descubrimientos de 1905.
7. **Artículo Original:** [A Heuristic Point of View Concerning the Production and Transformation of Light](https://einsteinpapers.press.princeton.edu/vol2-trans/100) - Traducción al inglés del artículo original de Einstein de 1905.
8. **PhysicsWorld:** [Quantum Physics Early History](https://physicsworld.com/c/quantum/) - Artículos sobre el centenario del modelo de Bohr y la relevancia del átomo de hidrógeno.

### 📖 Referencias Útiles y Bibliografía
1. **Libro**: [Quantum Physics of Atoms, Molecules, Solids, Nuclei, and Particles - Eisberg & Resnick](https://www.wiley.com/en-us/Quantum+Physics+of+Atoms%2C+Molecules%2C+Solids%2C+Nuclei%2C+and+Particles%2C+2nd+Edition-p-9780471873730). Un texto fantástico sobre la física moderna y los experimentos fundamentales.
2. **Libro**: [Introduction to Quantum Mechanics - David J. Griffiths](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799252758F46C8765A2C3946C342C) (Introduction). Repaso de la fenomenología antes de entrar a Schrödinger.
3. **Libro**: [Quantum Physics - Stephen Gasiorowicz](https://www.wiley.com/en-us/Quantum+Physics%2C+3rd+Edition-p-9780471057000) (Capítulo 1). Detalles numéricos y experimentales sobre el cuerpo negro y el efecto Compton.
4. **Libro**: [Concepts of Modern Physics - Arthur Beiser](https://www.mheducation.com/highered/product/concepts-modern-physics-beiser/M9780072448481.html). Ideal para una base conceptual firme en los fenómenos relativistas y cuánticos pioneros.
