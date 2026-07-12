# Estructura Cristalina y Redes

La estructura cristalina se refiere a la disposición ordenada, periódica y simétrica de los átomos, iones o moléculas en un sólido. Es la base para comprender la mayoría de las propiedades mecánicas, térmicas y electrónicas de los materiales, desde los metales simples hasta los semiconductores complejos.

## 📜 Contexto Histórico

El estudio sistemático de las estructuras cristalinas comenzó con la formulación de las leyes de la cristalografía macroscópica por René Just Haüy en el siglo XVIII. Sin embargo, el verdadero avance se produjo en 1912 cuando Max von Laue descubrió la difracción de rayos X por los cristales, lo que demostró la naturaleza ondulatoria de los rayos X y la disposición periódica de los átomos. Posteriormente, William Henry Bragg y William Lawrence Bragg desarrollaron la ley de difracción que lleva su nombre, permitiendo la determinación directa de la estructura atómica de los cristales, lo cual les valió el Premio Nobel en 1915.

## 🧮 Desarrollo Teórico Profundo

Un cristal ideal se describe matemáticamente mediante una **red de Bravais** combinada con una **base** (el conjunto de átomos asociado a cada punto de la red).

Una red de Bravais se define por los vectores de traslación espacial:
$$ \mathbf{R} = n_1 \mathbf{a}_1 + n_2 \mathbf{a}_2 + n_3 \mathbf{a}_3 $$
donde $ \mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3 $ son los vectores primitivos y $ n_1, n_2, n_3 $ son enteros.

Para analizar la difracción y las propiedades electrónicas, es crucial definir la **red recíproca**. Los vectores de la red recíproca $\mathbf{G}$ satisfacen la condición:
$$ e^{i \mathbf{G} \cdot \mathbf{R}} = 1 $$
Los vectores primitivos de la red recíproca, $\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3$, se construyen a partir de la red directa como:
$$ \mathbf{b}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} $$
$$ \mathbf{b}_2 = 2\pi \frac{\mathbf{a}_3 \times \mathbf{a}_1}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} $$
$$ \mathbf{b}_3 = 2\pi \frac{\mathbf{a}_1 \times \mathbf{a}_2}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} $$

La condición para la difracción constructiva se da por la **Ley de Bragg** formulada en el espacio recíproco (condición de Laue):
$$ \Delta \mathbf{k} = \mathbf{k}' - \mathbf{k} = \mathbf{G} $$
que es equivalente a $ 2d \sin(\theta) = n\lambda $.

## 🛠 Ejemplo Práctico

**Problema:** Calcula los vectores primitivos de la red recíproca para una red Cúbica Centrada en las Caras (FCC).

**Solución paso a paso:**
1. Los vectores primitivos de la red FCC (con parámetro de red $a$) se pueden elegir como:
   $$ \mathbf{a}_1 = \frac{a}{2}(\hat{y} + \hat{z}) $$
   $$ \mathbf{a}_2 = \frac{a}{2}(\hat{x} + \hat{z}) $$
   $$ \mathbf{a}_3 = \frac{a}{2}(\hat{x} + \hat{y}) $$
2. Calculamos el volumen de la celda unitaria primitiva $V_c = \mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)$:
   $$ \mathbf{a}_2 \times \mathbf{a}_3 = \frac{a^2}{4} [(\hat{x} + \hat{z}) \times (\hat{x} + \hat{y})] = \frac{a^2}{4} (\hat{x}\times\hat{x} + \hat{x}\times\hat{y} + \hat{z}\times\hat{x} + \hat{z}\times\hat{y}) = \frac{a^2}{4}(\hat{z} + \hat{y} - \hat{x}) $$
   $$ V_c = \frac{a}{2}(\hat{y} + \hat{z}) \cdot \frac{a^2}{4}(-\hat{x} + \hat{y} + \hat{z}) = \frac{a^3}{8}(1 + 1) = \frac{a^3}{4} $$
3. Ahora calculamos $\mathbf{b}_1$:
   $$ \mathbf{b}_1 = 2\pi \frac{\frac{a^2}{4}(-\hat{x} + \hat{y} + \hat{z})}{\frac{a^3}{4}} = \frac{2\pi}{a} (-\hat{x} + \hat{y} + \hat{z}) $$
4. Por simetría cíclica, obtenemos $\mathbf{b}_2$ y $\mathbf{b}_3$:
   $$ \mathbf{b}_2 = \frac{2\pi}{a} (\hat{x} - \hat{y} + \hat{z}) $$
   $$ \mathbf{b}_3 = \frac{2\pi}{a} (\hat{x} + \hat{y} - \hat{z}) $$
**Conclusión:** Estos vectores definen una red Cúbica Centrada en el Cuerpo (BCC). Por lo tanto, la red recíproca de una FCC es una BCC.

## 📚 Recursos Específicos

### Cursos
1. **[MIT OCW 8.231 - Physics of Solids](https://ocw.mit.edu):** Explora la estructura de la red recíproca con gran detalle matemático.
2. **[Cristalografía y Simetría (Coursera)](https://www.coursera.org):** Para aprender a identificar grupos espaciales.
3. **[Solid State Physics (NPTEL)](https://nptel.ac.in):** Excelentes clases magistrales enfocadas en difracción de rayos X y redes de Bravais.
4. **[X-Ray Diffraction in Crystals (edX)](https://www.edx.org):** Técnicas experimentales e interpretación de difractogramas.
5. **[Introduction to Crystallography (Oxford online materials)](https://www.ox.ac.uk):** Recursos interactivos y visuales para entender índices de Miller.
6. **[Symmetry in Condensed Matter (Cambridge)](https://www.cam.ac.uk):** Un curso avanzado para usar la teoría de grupos aplicada a las redes.

### Artículos y Simulaciones
1. **[PhET Interactive Simulations - "Crystal Lattice"](https://phet.colorado.edu):** Simulación visual básica para ver arreglos atómicos.
2. **[VESTA (Visualization for Electronic and STructural Analysis)](https://jp-minerals.org/vesta/en/):** Software indispensable para visualizar redes y densidades electrónicas.
3. **[O-PTIR and X-Ray Scattering (Article)](https://pubs.acs.org):** Ejemplos recientes en caracterización estructural.
4. **["The Discovery of X-Ray Diffraction" (W.L. Bragg, original papers)](https://www.nobelprize.org):** La historia y fundamentos físicos desde la fuente.
5. **[Bilbao Crystallographic Server](https://www.cryst.ehu.es/):** Una herramienta online esencial para estudiar simetrías espaciales.
6. **[Mercury (CSD)](https://www.ccdc.cam.ac.uk):** Simulación y exploración estructural de moléculas en redes cristalinas.
7. **[Jmol / JSmol](https://jmol.sourceforge.net/):** Simuladores en el navegador para estudiar estructuras empaquetadas.
8. **["A periodic table of crystal structures" (Nature Review Materials)](https://www.nature.com):** Un resumen visual muy útil para estructuras complejas.

### 📖 Referencias Útiles y Bibliografía
1. [Ashcroft, N. W., & Mermin, N. D. (1976). *Solid State Physics*](https://archive.org). (Capítulos 1-5).
2. [Kittel, C. (2004). *Introduction to Solid State Physics*](https://archive.org). (Capítulos iniciales sobre redes).
3. [Hammond, C. (2015). *The Basics of Crystallography and Diffraction*](https://global.oup.com). Oxford University Press.
4. [Cullity, B. D. (1978). *Elements of X-Ray Diffraction*](https://archive.org). Addison-Wesley.
