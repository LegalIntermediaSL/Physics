# [FLD-03] Las Ecuaciones de Navier-Stokes

Claude-Louis Navier (1822) y George Gabriel Stokes (1845) añadieron la fricción interna (Viscosidad) a las ecuaciones ideales de Euler. El resultado es el conjunto de ecuaciones diferenciales más famosas y temidas de la física clásica: Las Ecuaciones de Navier-Stokes.

## 1. El Tensor de Esfuerzos Viscosos
En un fluido real, las capas adyacentes que se mueven a distintas velocidades frotan entre sí. Stokes postuló matemáticamente que el tensor de esfuerzos totales $\sigma_{ij}$ se compone de la presión isotrópica termodinámica y un tensor viscoso dependiente del gradiente de velocidad (Tensor Tasa de Deformación $e_{ij}$):

$$
\sigma_{ij} = -p \delta_{ij} + 2\mu \left( e_{ij} - \frac{1}{3}(\nabla \cdot \mathbf{u})\delta_{ij} \right) + \zeta (\nabla \cdot \mathbf{u})\delta_{ij}
$$

Donde $\mu$ es la viscosidad dinámica (cizalla) y $e_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)$.
Esta hipótesis lineal define a los **Fluidos Newtonianos** (como el agua y el aire).

## 2. Derivación de la Ecuación Completa
Sustituyendo el tensor en la ecuación general de conservación de momento ($\rho \frac{D\mathbf{u}}{Dt} = \nabla \cdot \boldsymbol{\sigma} + \mathbf{f}$), asumiendo un fluido incompresible ($\nabla \cdot \mathbf{u} = 0$) con viscosidad $\mu$ constante, se obtiene la forma clásica:

$$
\rho \left( \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} \right) = -\nabla p + \mu \nabla^2 \mathbf{u} + \rho \mathbf{g}
$$

Término a término:
- **Inercia Local**: $\rho \frac{\partial \mathbf{u}}{\partial t}$ (Aceleración temporal).
- **Advección No-Lineal**: $\rho (\mathbf{u} \cdot \nabla)\mathbf{u}$ (La aceleración espacial causante del caos).
- **Gradiente de Presión**: $-\nabla p$ (Fuerza impulsora).
- **Difusión Viscosa**: $\mu \nabla^2 \mathbf{u}$ (Fuerza de amortiguación/fricción).
- **Fuerzas de Cuerpo**: $\rho \mathbf{g}$ (Gravedad).

## 3. El Problema del Milenio
Junto con la condición incompresible ($\nabla \cdot \mathbf{u} = 0$), estas ecuaciones modelan desde el flujo sanguíneo en el corazón hasta la Gran Mancha Roja de Júpiter.
Sin embargo, su no-linealidad matemática extrema las hace analíticamente irresolubles (excepto en casos simétricos triviales como Poiseuille).
El Clay Mathematics Institute ofrece un millón de dólares al que demuestre que, dadas unas condiciones iniciales suaves, siempre existe una solución suave, continua y globalmente definida para Navier-Stokes en 3D (Demostración de Existencia y Suavidad). Hasta hoy, no sabemos matemáticamente si la ecuación desarrolla singularidades de "velocidad infinita" o "cortes topológicos" a tiempos finitos.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 2.006: Thermal-Fluids Engineering](https://ocw.mit.edu/courses/2-006-thermal-fluids-engineering-ii-spring-2004/).
  - [National Committee for Fluid Mechanics Films (NCFMF)](https://web.mit.edu/hml/ncfmf.html) - Serie histórica de vídeos del MIT (obligatorio para visualizar fluidos).
- **Libros de Texto Canónicos:**
  - *Fluid Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 6 del Curso de Física Teórica).
  - *An Introduction to Fluid Dynamics* - G.K. Batchelor.
  - *Turbulence: The Legacy of A.N. Kolmogorov* - Uriel Frisch.
