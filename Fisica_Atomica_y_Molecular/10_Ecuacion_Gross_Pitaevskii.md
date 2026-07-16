# Ecuación de Gross-Pitaevskii (Superfluidos)

## 1. Dinámica del Campo Mean-Field
Un Condensado de Bose-Einstein (BEC) a cero grados, compuesto de miles de átomos interactuantes ligeramente repulsivos, no se modela intentando rastrear $10^5$ ondas entrelazadas. Se modela mediante la **Aproximación de Bogoliubov** donde la abrumadora mayoría de los átomos ocupan el mismo estado orbital coherente macroscópico $\Psi(\vec{r}, t)$.

El formalismo físico es una versión de campo medio de la teoría de campo cuántico bosónica que se reduce a la Ecuación no-lineal de **Gross-Pitaevskii** (GPE).

## 2. La Ecuación de Schrödinger No Lineal
La GPE es estructuralmente idéntica a la Ecuación de Schrödinger convencional uniparticular, pero con un término diabólico de auto-interacción no lineal que depende del cuadrado módulo de la función de onda misma $|\Psi|^2$ (la densidad local del condensado $\rho$):

$$
i\hbar \frac{\partial \Psi(\vec{r}, t)}{\partial t} = \left( -\frac{\hbar^2}{2m}\nabla^2 + V_{ext}(\vec{r}) + g |\Psi(\vec{r}, t)|^2 \right) \Psi(\vec{r}, t)
$$

Donde $V_{ext}$ es el potencial de la trampa magnética de laboratorio que sostiene a los átomos, y $g = \frac{4\pi \hbar^2 a_s}{m}$ mide la potencia de la repulsión de contacto interatómica ($a_s$ longitud de scattering).
Es conocida como *Ecuación de Schrödinger No Lineal (NLSE)* en física matemática.

## 3. Superfluidez y Vórtices Cuantizados
El término no-lineal repulsivo confiere "rigidez" a la función de onda fluida. Si rotas ligeramente el recipiente del condensado, en vez de rotar de forma continua solidaria, el fluido rechaza el movimiento demostrando **Superfluidez** (viscosidad cero estricta).
Si rotas el recipiente lo suficientemente rápido, aparecen agujeros y singularidades topológicas en la red: **Vórtices Cuantizados**. La circulación de la velocidad alrededor de estos vórtices no puede tomar valores arbitrarios en $R$, está hipercuantizada de forma estricta en pasos enteros de constante de Planck ($\kappa = \frac{nh}{m}$), idéntico a las líneas de flujo en un superconductor magnético de Tipo-II.

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
