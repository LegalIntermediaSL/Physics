# [QM-08] Teoría de Dispersión (Scattering)

Si no podemos ver el interior de un átomo o de un núcleo, ¿cómo sabemos lo que hay dentro? La respuesta de la física desde Rutherford hasta el Gran Colisionador de Hadrones (LHC) es dispararle proyectiles a altas energías y observar cómo rebotan. Esta es la **Teoría Cuántica de Dispersión**.

## 1. El Paradigma Asintótico y la Sección Eficaz
En un experimento de colisión, lanzamos una onda plana cuántica libre (el proyectil $e^{ikz}$) desde el infinito hacia un potencial $V(r)$ localizado cerca del origen. Tras chocar, el proyectil emerge como una onda esférica dispersada en todas direcciones.
La función de onda completa lejos del centro de colisión tiene la forma asintótica:

$$
\psi(r, \theta) \approx e^{ikz} + f(\theta) \frac{e^{ikr}}{r}
$$

El Santo Grial es la **Amplitud de Dispersión $f(\theta)$**. Su módulo al cuadrado define la **Sección Eficaz Diferencial** ($d\sigma/d\Omega = |f(\theta)|^2$), que es exactamente lo que los físicos miden en los detectores del CERN: la probabilidad de que la partícula se desvíe en el ángulo sólido $\Omega$.

## 2. La Aproximación de Born
Si el potencial de dispersión $V(r)$ es "débil" (la partícula pasa tan rápido o el potencial es tan tenue que la onda apenas se altera de su trayectoria en línea recta), podemos usar la Teoría de Perturbaciones para calcular la Amplitud de Dispersión. 
La **Primera Aproximación de Born** demuestra maravillosamente que la Amplitud de Dispersión es simplemente la Transformada de Fourier 3D del Potencial espacal $V(r)$:

$$
f(\theta, \phi) = -\frac{m}{2\pi \hbar^2} \int e^{-i \mathbf{q} \cdot \mathbf{r}'} V(\mathbf{r}') d^3\mathbf{r}'
$$

Donde $\mathbf{q} = \mathbf{k}_f - \mathbf{k}_i$ es el momento transferido en el choque.

## 3. El Método de Ondas Parciales (Bajas Energías)
Si la energía del proyectil es muy baja, la Aproximación de Born falla espectacularmente. A baja energía (grandes longitudes de onda de De Broglie), la onda del proyectil siente todo el potencial lenta y esféricamente.
Descomponemos la onda incidente y esparcida en armónicos esféricos (ondas con momento angular definido $l$).
Cada "onda parcial $l$" sufre un retraso temporal al atravesar el potencial, emergiendo con un "Cambio de Fase" ($\delta_l$). La sección eficaz total es la suma de los desplazamientos de fase esféricos:

$$
\sigma = \frac{4\pi}{k^2} \sum_{l=0}^\infty (2l+1) \sin^2 \delta_l
$$

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.04: Quantum Physics I (Barton Zwiebach)](https://www.youtube.com/playlist?list=PLUl4u3cNGP61-9PEhRognw5vryrSEVLPr) - Excelente tratamiento riguroso de la mecánica ondulatoria y espinores.
- [Stanford: Theoretical Minimum - Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL701CD168D02FF56F) - El estándar de oro para entender el entrelazamiento y los espacios de Hilbert de forma intuitiva.
- [Perimeter Institute: Quantum Mechanics](https://www.youtube.com/user/PIOutreach) - Clases de nivel máster para investigadores.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Stanford: Quantum Mechanics](https://theoreticalminimum.com/courses/quantum-mechanics/2012/winter) - Leonard Susskind.
  - [MIT 8.04: Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/) - Allan Adams (Una de las mejores introducciones visuales y matemáticas del mundo).
- **Libros de Texto Canónicos:**
  - *Principles of Quantum Mechanics* - R. Shankar.
  - *Modern Quantum Mechanics* - J.J. Sakurai. (Estándar de posgrado).
  - *Quantum Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 3).
