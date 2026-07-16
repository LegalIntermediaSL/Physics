# [AMO-01] El Método de Hartree-Fock para Muchos Cuerpos

## 1. El Problema Imposible de los N-Electrones
La Ecuación de Schrödinger es analíticamente soluble y majestuosa para átomos de Hidrógeno (un protón, un electrón). Para cualquier átomo de la tabla periódica a partir del Helio ($N \ge 2$), las fuerzas de repulsión eléctrica cruzadas entre todos los electrones ($1/r_{ij}$) hacen la ecuación matemáticamente irresoluble.

La Ecuación Completa de $N$ electrones posee una función de onda hiperdimensional $\Psi(\vec{r}_1, \dots, \vec{r}_N)$.

## 2. La Aproximación de Campo Medio (Mean Field)
En la década de 1920, Douglas Hartree propuso una simplificación radical: Asumamos que cada electrón individual orbita el núcleo ignorando la presencia *puntual* explícita de sus vecinos. En lugar de interactuar con electrones discretos repulsivos, interactúa con una "Nube Promedio" global de carga esférica creada por el resto de los $N-1$ electrones.
Esto convierte una sola ecuación con miles de millones de interconexiones en $N$ ecuaciones uniparticulares aisladas, llamadas ecuaciones de Hartree.

## 3. Intercambio Cuántico (Determinante de Slater y Fock)
Vladimir Fock refinó el modelo forzando un rigor topológico fundamental: los electrones son Fermiones indistinguibles. Por el Principio de Exclusión de Pauli, su función de onda global debe ser anti-simétrica ante el intercambio de coordenadas de cualquier par de electrones ($\Psi(\dots \vec{r}_i \dots \vec{r}_j \dots) = -\Psi(\dots \vec{r}_j \dots \vec{r}_i \dots)$).

Fock construyó la función de onda de prueba no como un producto simple, sino como el **Determinante de Slater** de los orbitales individuales $\phi_k(\vec{r})$.

Al minimizar la energía mediante el Principio Variacional de Rayleigh-Ritz, se llega al sistema de Ecuaciones Íntegro-Diferenciales de **Hartree-Fock (HF)**:

$$
\left( -\frac{\hbar^2}{2m}\nabla^2 + V_{nuc}(\vec{r}) + V_{Hartree}(\vec{r}) \right) \phi_i(\vec{r}) - \sum_j \int \frac{\phi_j^*(\vec{r}') \phi_i(\vec{r}')}{|\vec{r} - \vec{r}'|} d^3r' \, \phi_j(\vec{r}) = \epsilon_i \phi_i(\vec{r})
$$

El último término negativo de la izquierda no tiene análogo clásico. Es el **Operador de Intercambio (Exchange)** y baja la energía del átomo al mantener a electrones del mismo espín alejados por la pura geometría de los números complejos, estabilizando la tabla periódica moderna.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.421: Atomic and Optical Physics I](https://ocw.mit.edu/courses/8-421-atomic-and-optical-physics-i-spring-2014/) - Prof. Wolfgang Ketterle (Premio Nobel por el condensado de Bose-Einstein).
  - [Oxford University: Atomic and Laser Physics](https://podcasts.ox.ac.uk/series/atomic-and-laser-physics).
- **Libros de Texto Canónicos:**
  - *Atomic Physics* - Christopher J. Foot.
  - *Physics of Atoms and Molecules* - B.H. Bransden & C.J. Joachain.
- **Lecturas Fundamentales:**
  - Artículos originales de Ketterle y Cornell sobre el enfriamiento láser y el BEC.
