# [ELM-04] Ondas Electromagnéticas y Teoría de Radiación

Si limpiamos el espacio de materia ($\rho=0, \vec{J}=0$), las leyes acopladas de Maxwell exhiben el espectro más hermoso de la física: Tomando el rotacional del rotacional, obtenemos Ecuaciones Diferenciales de Onda Puras para $\vec{E}$ y $\vec{B}$, viajando a la brutal y exótica velocidad absoluta $c = 1/\sqrt{\mu_0\varepsilon_0}$.

## 1. Ondas Planas Monocromáticas
En el vacío lejano, la energía lumínica radiada viaja asintóticamente como ondas transversales exactas (TEM).

$$
\vec{E}(z,t) = E_0 \cos(kz - \omega t) \hat{x}
$$

$$
\vec{B}(z,t) = \frac{E_0}{c} \cos(kz - \omega t) \hat{y}
$$

La energía oscila perfectamente en fase, con los vectores Eléctrico, Magnético y de Propagación conformando una tétrada dextrógira mutuamente ortogonal $\vec{k} \propto \vec{E} \times \vec{B}$.

## 2. Potenciales Retardados
Si la distribución de corriente de las antenas origen depende estocásticamente del tiempo $\vec{J}(\vec{r}', t)$, las fórmulas de Poisson del potencial abstracto en la estática colapsan porque "la luz tarda tiempo en viajar la distancia de separación $\Delta r$".
Se debe reescribir integralmente reemplazando el tiempo local por el "Tiempo Retardado" de Liénard ($t_r = t - |\vec{r}-\vec{r}'|/c$):

$$
\Phi(\vec{r}, t) = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\vec{r}', t_r)}{|\vec{r} - \vec{r}'|} d\tau'
$$

## 3. Radiación de Larmor y Dipolo
Para que una partícula física real desprenda energía que escape permanentemente hacia el infinito absoluto irrecuperable ($U \propto 1/r^2$ y área $\propto r^2$), el Campo Eléctrico radiado debe decaer suavemente como $1/r$ (no como el campo de Coulomb $1/r^2$).
La **Fórmula de Larmor** establece que esto solo sucede si, y solo si, la partícula está Acelerada. El poder total (Watts) irradiado al cosmos es:

$$
P = \frac{\mu_0 q^2 a^2}{6\pi c}
$$

El Bremsstrahlung ("Radiación de frenado") en sincrotrones es la manifestación relativista violenta de este poder.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.02: Electricity and Magnetism (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro2314mKyUiALIcyEP7uHTy1I) - Experimentos magistrales y derivaciones desde cero.
- [Yale PHYS 201: Fundamentals of Physics II (Ramamurti Shankar)](https://www.youtube.com/playlist?list=PLD07B2225BBFA0681) - Énfasis matemático riguroso en electrostática y radiación.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.02: Physics II: Electricity and Magnetism](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/) - Walter Lewin.
  - [Stanford: Special Relativity and Electrodynamics](https://theoreticalminimum.com/courses/special-relativity-and-electrodynamics/2012/spring) - Leonard Susskind.
- **Libros de Texto Canónicos:**
  - *Classical Electrodynamics* - John David Jackson. (El texto definitivo a nivel posgrado).
  - *Introduction to Electrodynamics* - David J. Griffiths. (El texto estándar a nivel pregrado).
  - *The Feynman Lectures on Physics (Vol. II)*.
