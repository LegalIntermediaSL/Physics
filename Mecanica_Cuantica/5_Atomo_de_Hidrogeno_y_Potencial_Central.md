# El Átomo de Hidrógeno y Fuerzas Centrales

El triunfo absoluto que consolidó la mecánica cuántica de Schrödinger fue derivar matemáticamente el espectro exacto del Átomo de Hidrógeno (electrón bajo el potencial de Coulomb del protón, $V(r) = -e^2/4\pi\epsilon_0 r$), explicando las extrañas líneas de emisión espectral vistas por Balmer y Rydberg.

## 1. Fuerzas Centrales y Separación de Variables
Dado que el potencial de Coulomb depende solo del radio $r$ y no de los ángulos (es esféricamente simétrico), el Hamiltoniano conmuta con $\hat{L}^2$ y $\hat{L}_z$. Esto nos permite separar la ecuación diferencial parcial 3D en tres ecuaciones diferenciales ordinarias independientes:

$$
\Psi(r, \theta, \phi) = R_{nl}(r) Y_l^m(\theta, \phi)
$$

La parte angular está resuelta genéricamente por los Armónicos Esféricos $Y_l^m$. Toda la física atómica reside en la función radial $R(r)$.

## 2. Ecuación Radial y los Polinomios de Laguerre
La ecuación para $R(r)$ incluye el potencial atractor eléctrico y un término repulsivo de "barrera centrífuga" proporcional a $l(l+1)/r^2$.
Para que las soluciones matemáticas no colapsen en el origen ni exploten en el infinito, se requiere que la serie matemática se trunque. Esta imposición de frontera genera un nuevo número cuántico principal $n$ ($n = 1, 2, 3...$).
Las soluciones exactas radican en los **Polinomios Asociados de Laguerre**.

## 3. Niveles de Energía y Degeneración
La condición de cuantización genera la famosísima fórmula de energía de Bohr (pero derivada rigurosamente de primeros principios ondulatorios):

$$
E_n = - \left( \frac{m_e e^4}{8 \epsilon_0^2 h^2} \right) \frac{1}{n^2} \approx - \frac{13.6 \text{ eV}}{n^2}
$$

Espectacularmente, la energía de un nivel en el Hidrógeno depende *únicamente* del número principal $n$, pero existen múltiples orbitales (diferentes $l$ y $m$) para la misma energía. Para un $n$ dado, la degeneración total (ignorando el espín) es exactamente $n^2$. (Por ejemplo, el nivel $n=2$ tiene 4 orbitales de misma energía: un 2s y tres 2p).

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
