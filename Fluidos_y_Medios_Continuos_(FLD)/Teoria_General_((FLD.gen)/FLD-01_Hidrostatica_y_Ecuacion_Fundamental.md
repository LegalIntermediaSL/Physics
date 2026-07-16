# [FLD-01] Hidrostática y Ecuación Fundamental

La Hidrostática estudia los fluidos en reposo mecánico (donde el tensor de esfuerzos viscosos es estrictamente cero). En este régimen estático, la única fuerza interna que actúa sobre un elemento de volumen es la presión isotrópica (normal a todas las superficies).

## 1. El Tensor de Esfuerzos en Reposo
En mecánica de medios continuos, el estado tensional de cualquier material se describe mediante el tensor de esfuerzos de Cauchy $\sigma_{ij}$.
Para un fluido en absoluto reposo, no puede haber esfuerzos cortantes (las capas no se deslizan unas sobre otras). Por lo tanto, el tensor es estrictamente diagonal e isótropo:

$$
\sigma_{ij} = -p \delta_{ij}
$$

El signo negativo indica que la presión $p$ es, por convención, un esfuerzo de compresión.

## 2. La Ecuación Fundamental de la Hidrostática
Consideremos un elemento de volumen de fluido en reposo bajo la influencia de un campo de fuerzas por unidad de masa $\mathbf{g}$ (típicamente la gravedad).
La suma de las fuerzas debidas al gradiente de presión y la fuerza másica debe ser cero (Primera Ley de Newton):

$$
-\nabla p + \rho \mathbf{g} = 0
$$

Si la gravedad es uniforme y apunta en la dirección $-z$ ($\mathbf{g} = -g \hat{k}$), obtenemos la ecuación diferencial ordinaria:

$$
\frac{dp}{dz} = -\rho g
$$

## 3. Fluido Incompresible (Líquidos)
Si la densidad $\rho$ es constante (aproximación excelente para el agua bajo presiones no extremas), la integración es trivial (El Principio de Stevin):

$$
p(z) = p_0 + \rho g (z_0 - z) = p_0 + \rho g h
$$

Esta ecuación contiene el Principio de Pascal: "Cualquier incremento de presión $p_0$ aplicado a la superficie se transmite íntegramente a todos los puntos del fluido incompresible".

## 4. Fluido Compresible (Gases y Atmósfera)
Para la atmósfera terrestre, la densidad no es constante; depende de la presión según la ecuación de los gases ideales ($p = \rho R T / M$).
Si asumimos un modelo isotérmico ($T$ constante), la ecuación diferencial de la hidrostática se convierte en:

$$
\frac{dp}{dz} = -\frac{p M g}{R T}
$$

Integrando, obtenemos la **Fórmula Barométrica** (decaimiento exponencial de la presión atmosférica):

$$
p(z) = p_0 \exp\left( -\frac{M g z}{R T} \right)
$$

## 5. El Principio de Arquímedes
Integrando el tensor de presión $-\oint p \mathbf{n} dS$ sobre la superficie cerrada de un cuerpo sumergido, y usando el Teorema de la Divergencia de Gauss, obtenemos la Fuerza de Empuje neta $\mathbf{E}$:

$$
\mathbf{E} = -\iiint (\nabla p) dV = \iiint (\rho_f \mathbf{g}) dV = M_{\text{fluido desalojado}} \mathbf{g}
$$


---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 2.006: Thermal-Fluids Engineering](https://ocw.mit.edu/courses/2-006-thermal-fluids-engineering-ii-spring-2004/).
  - [National Committee for Fluid Mechanics Films (NCFMF)](https://web.mit.edu/hml/ncfmf.html) - Serie histórica de vídeos del MIT (obligatorio para visualizar fluidos).
- **Libros de Texto Canónicos:**
  - *Fluid Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 6 del Curso de Física Teórica).
  - *An Introduction to Fluid Dynamics* - G.K. Batchelor.
  - *Turbulence: The Legacy of A.N. Kolmogorov* - Uriel Frisch.
