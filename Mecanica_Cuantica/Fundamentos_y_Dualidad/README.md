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

### Teoría Cuántica de la Radiación del Cuerpo Negro

El inicio del formalismo cuántico surgió al analizar la densidad de energía de la radiación electromagnética en una cavidad en equilibrio térmico. Clásicamente, la física estadística y el electromagnetismo (ley de Rayleigh-Jeans) asumen que la energía térmica se reparte equitativamente en todos los modos vibracionales. Como el número de modos por unidad de frecuencia escala con $\nu^2$, la densidad de energía sería:
$$ \rho_{RJ}(\nu, T) = \frac{8\pi \nu^2 k_B T}{c^3} $$
Esto predice que un objeto a temperatura constante radiará una cantidad infinita de energía en altas frecuencias ($\nu \to \infty$), un absurdo físico bautizado como la "Catástrofe Ultravioleta".

Para resolver esto, Max Planck propuso una hipótesis ad hoc (1900): los osciladores materiales en las paredes de la cavidad no pueden emitir o absorber energía de manera continua, sino en paquetes discretos o "cuantos". La energía de un oscilador de frecuencia $\nu$ se cuantiza en múltiplos enteros:
$$ E_n = nh\nu, \quad n = 0, 1, 2, \dots $$
donde $h$ es la constante de Planck ($6.62607015 \times 10^{-34} \text{ J}\cdot\text{s}$). Calculando el valor esperado estadístico de la energía de los osciladores usando la distribución de Boltzmann:
$$ \langle E \rangle = \frac{\sum_{n=0}^{\infty} (nh\nu) e^{-nh\nu / k_B T}}{\sum_{n=0}^{\infty} e^{-nh\nu / k_B T}} = \frac{h\nu}{e^{h\nu / k_B T} - 1} $$
Multiplicando por la densidad de modos $\frac{8\pi \nu^2}{c^3}$, surge la **Ley de Radiación de Planck**:
$$ \rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu / k_B T} - 1} $$
Esta fórmula coincide perfectamente con los espectros observados y decae exponencialmente a altas frecuencias, resolviendo la divergencia clásica.

```mermaid
graph TD
    A[Problema Clásico] --> B(Ley de Rayleigh-Jeans)
    B -->|Predice| C[Divergencia Infinita de Energía a altas frecuencias]
    A --> D(Hipótesis de Cuantización de Planck: E = nhv)
    D -->|Estadística de Boltzmann| E[Energía Media Cuantizada]
    E --> F[Ley de Planck]
    F -->|Resuelve| G[Ajuste Experimental Perfecto]
```

### Efecto Fotoeléctrico y la Naturaleza Corpuscular de la Luz

En 1905, Einstein fue más allá: la cuantización no era un artefacto de los osciladores de las paredes, sino una propiedad fundamental del campo electromagnético en sí. La luz está compuesta por partículas inseparables (luego llamadas fotones) de energía $E = h\nu$.

En el efecto fotoeléctrico, cuando una placa de metal es iluminada, emite electrones. Clásicamente se esperaba que una luz más intensa aumentara la energía de estos electrones y que existiera un retardo temporal. Sin embargo, la energía de los electrones resultaba ser independiente de la intensidad, pero linealmente dependiente de la frecuencia. 
Einstein modeló el proceso como colisiones uno-a-uno entre fotones y electrones. La conservación de la energía en la extracción de un electrón dicta:
$$ h\nu = K_{\max} + \Phi $$
$$ K_{\max} = h\nu - \Phi $$
donde $\Phi$ (función de trabajo) es la energía mínima necesaria para arrancar un electrón, dependiente del material. Si $h\nu < \Phi$, ningún electrón es emitido, explicando el efecto del umbral de frecuencia.

### Dualidad Onda-Partícula y Momento del Fotón

El fotón viaja a la velocidad de la luz $c$, por lo que su masa invariante es nula. Por relatividad especial, la relación energía-momento es $E^2 = (pc)^2 + (m_0 c^2)^2$. Para $m_0 = 0$:
$$ E = pc \implies p = \frac{E}{c} = \frac{h\nu}{c} = \frac{h}{\lambda} $$
Arthur Compton (1923) confirmó que los fotones portan este momento $p = h/\lambda$ colisionándolos con electrones y verificando la conservación del momento (Dispersión Compton):
$$ \Delta \lambda = \lambda' - \lambda = \frac{h}{m_e c} (1 - \cos\theta) $$

### Hipótesis de de Broglie: Ondas de Materia

Si las ondas de luz presentan comportamiento de partícula (fotón), Louis de Broglie propuso (1924) la simetría opuesta: las partículas materiales (como los electrones) deberían exhibir comportamiento de onda. A toda partícula con momento $p$ se le asocia una onda de materia de longitud:
$$ \lambda_{dB} = \frac{h}{p} = \frac{h}{mv} $$
Esta relación revolucionaria fue confirmada cuando se observó difracción cristalina en haces de electrones (Davisson-Germer, 1927). A partir de la hipótesis de de Broglie, la condición de cuantización del átomo de Bohr ($mvr = n\hbar$) emerge naturalmente al exigir que la onda electrónica forme una onda estacionaria estable en la órbita atómica:
$$ 2\pi r = n\lambda_{dB} = n\frac{h}{p} \implies pr = n\frac{h}{2\pi} = n\hbar $$
Este salto conceptual prepararía el terreno para la formulación completa de la función de onda de Schrödinger.

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
