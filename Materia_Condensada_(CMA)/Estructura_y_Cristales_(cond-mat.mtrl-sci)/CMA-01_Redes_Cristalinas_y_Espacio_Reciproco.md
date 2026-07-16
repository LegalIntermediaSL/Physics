# [CMA-01] Redes Cristalinas y Espacio Recíproco

La Materia Condensada nace cuando $10^{23}$ átomos se enfrían e interactúan, rompiendo la simetría continua del espacio libre y adoptando configuraciones rígidas microscópicas periódicas.

## 1. Redes de Bravais (Espacio Real)
Una red cristalina ideal es un conjunto infinito de puntos discretos generados algebraicamente por vectores primitivos de traslación $(\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3)$:

$$
\mathbf{R} = n_1 \mathbf{a}_1 + n_2 \mathbf{a}_2 + n_3 \mathbf{a}_3
$$

Existen estrictamente 14 Redes de Bravais únicas en 3D (Cúbica Simple, FCC, BCC, Hexagonal, etc.). Cualquier estructura real de un sólido es simplemente una Red de Bravais genérica decorada con una "Base" (el átomo o grupo atómico colocado en cada punto $\mathbf{R}$).

## 2. La Celda de Wigner-Seitz
Dado que la red es periódica e infinita, la física de la estructura está enteramente contenida en la celda primitiva irreducible. La **Celda de Wigner-Seitz** se construye trazando líneas a los átomos más cercanos y cortándolas con planos mediatrices. Es el volumen del espacio que está más cerca del origen que de cualquier otro punto de la red.

## 3. La Red Recíproca (Espacio $k$)
Las propiedades electrónicas y acústicas se describen usando ondas mecánicas o cuánticas complejas ($e^{i \mathbf{k} \cdot \mathbf{r}}$).
Para que una onda posea la misma periodicidad exacta que la red del cristal, su vector de onda $\mathbf{K}$ debe satisfacer el axioma supremo:

$$
e^{i \mathbf{K} \cdot (\mathbf{r} + \mathbf{R})} = e^{i \mathbf{K} \cdot \mathbf{r}} \implies e^{i \mathbf{K} \cdot \mathbf{R}} = 1
$$

Esto ocurre si y solo si $\mathbf{K} \cdot \mathbf{R} = 2\pi m$.
Los vectores $\mathbf{K}$ que cumplen esto forman una red infinita en el "espacio de momentos". Esta es la mítica **Red Recíproca**.
Los vectores base de la red recíproca se generan combinando los del espacio real mediante el producto cruz:

$$
\mathbf{b}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

## 4. La Primera Zona de Brillouin
La celda de Wigner-Seitz de la Red Recíproca se denomina **Primera Zona de Brillouin**. Todas las teorías microscópicas de bandas y conducción electrónica asumen que los estados físicos y vectores de onda ($k$) están estrictamente restringidos al interior geométrico de esta zona sagrada.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Oxford University: The Oxford Solid State Basics](https://podcasts.ox.ac.uk/series/oxford-solid-state-basics) - Prof. Steven H. Simon.
  - [MIT 8.231: Physics of Solids I](https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/).
- **Libros de Texto Canónicos:**
  - *Solid State Physics* - Neil W. Ashcroft & N. David Mermin. (El estándar de oro).
  - *Introduction to Solid State Physics* - Charles Kittel.
  - *Condensed Matter Field Theory* - Alexander Altland & Ben Simons. (Avanzado, integrando QFT).
