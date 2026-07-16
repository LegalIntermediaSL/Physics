# [FLD-09] Ondas de Choque y Flujo Supersónico

## 1. El Límite de la Compresibilidad
A bajas velocidades (Mach $M < 0.3$), los gases se comportan como incompresibles. Sin embargo, a altas velocidades ($M > 1$), las variaciones de presión generan variaciones drásticas de densidad. Si un objeto viaja más rápido que la velocidad del sonido en el medio ($c_s$), las ondas de presión acústica no pueden preceder al objeto, colapsando en un frente discontinuo.

## 2. Relaciones de Rankine-Hugoniot
Una **Onda de Choque Normal** es una discontinuidad hiperdelgada (del orden del libre recorrido medio molecular) donde la presión, temperatura y densidad del gas aumentan abruptamente, mientras la velocidad cae a régimen subsónico. 

El choque debe obedecer las leyes de conservación masa, momento y energía a través del frente de la onda. Sean los estados $(1)$ antes del choque y $(2)$ después del choque:

$$
\rho_1 v_1 = \rho_2 v_2
$$

$$
p_1 + \rho_1 v_1^2 = p_2 + \rho_2 v_2^2
$$

$$
h_1 + \frac{1}{2}v_1^2 = h_2 + \frac{1}{2}v_2^2
$$

Resolviendo este sistema para un gas ideal (índice adiabático $\gamma$), obtenemos los saltos de las variables en función del Número de Mach incidente ($M_1$):

$$
\frac{p_2}{p_1} = 1 + \frac{2\gamma}{\gamma + 1}(M_1^2 - 1)
$$

$$
\frac{\rho_2}{\rho_1} = \frac{(\gamma + 1)M_1^2}{2 + (\gamma - 1)M_1^2}
$$

Es vital notar que la entropía del sistema aumenta irreversiblemente $s_2 > s_1$. El salto a través de un choque verdadero disipa energía cinética en calor extremo.

## 3. Ángulo de Mach y Cono de Choque
Para flujos supersónicos ($M > 1$) sobre cuerpos delgados o proyectiles en el aire, las perturbaciones infinitesimales se limitan al interior de un cono, cuyo semiángulo (Ángulo de Mach $\mu$) está dado puramente por la trigonometría balística:

$$
\sin \mu = \frac{1}{M}
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
