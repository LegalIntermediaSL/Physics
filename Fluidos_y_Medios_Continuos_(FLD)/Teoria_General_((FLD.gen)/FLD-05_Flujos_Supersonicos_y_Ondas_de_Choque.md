# [FLD-05] Flujos Supersónicos y Ondas de Choque

Cuando la velocidad del flujo se aproxima a la velocidad de la luz, entra la Relatividad. Cuando la velocidad del fluido se aproxima a la velocidad a la que la información de presión viaja en ese medio (la Velocidad del Sonido $c$), entra la Dinámica de Gases Compresibles.

## 1. El Número de Mach ($Ma$)
El factor decisivo de compresibilidad térmica y cinética es la ratio de velocidades:

$$
Ma = \frac{v}{c} = \frac{v}{\sqrt{\gamma R T}}
$$

- **Incompresible ($Ma < 0.3$)**: La densidad apenas varía. Es el régimen de los fluidos cotidianos.
- **Transónico/Supersónico ($Ma > 1$)**: La densidad y temperatura de las parcelas de gas varían masivamente debido a la inmensa compresión dinámica.

## 2. Conos de Mach y el Silencio Adelantado
En régimen subsónico, las ondas sonoras (perturbaciones de presión) viajan hacia adelante más rápido que el objeto que las crea, avisando al fluido de que el avión se acerca, permitiendo que el aire se aparte suavemente de la trayectoria.
En régimen supersónico, el objeto viaja literalmente más rápido que su propio ruido. El fluido frente al morro está completamente "ciego", sordo, y quieto, hasta que el avión se estampa físicamente contra él de manera repentina y violenta, formando un Cono de Mach.

## 3. Ondas de Choque (Las Discontinuidades Matemáticas)
Para reajustar el flujo supersónico violento, la naturaleza crea discontinuidades abruptas llamadas Ondas de Choque: frentes físicos de un grosor nanométrico (el libre recorrido medio molecular) donde la Presión, Densidad y Temperatura se disparan discontinuamente casi al infinito de forma instantánea.

La física a través del choque ignora las derivadas y se rige por saltos algebraicos de conservación de masa, momento y energía total (Las **Relaciones de Salto de Rankine-Hugoniot**):

$$
\rho_1 u_1 = \rho_2 u_2
$$

$$
p_1 + \rho_1 u_1^2 = p_2 + \rho_2 u_2^2
$$

$$
h_1 + \frac{1}{2}u_1^2 = h_2 + \frac{1}{2}u_2^2
$$

La segunda ley de la termodinámica dicta que las Ondas de Choque son irreversibles; la entropía siempre salta hacia arriba ($\Delta S > 0$), y por ende, solo pueden existir choques compresivos (un flujo supersónico frenando a subsónico de golpe).

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 2.006: Thermal-Fluids Engineering](https://ocw.mit.edu/courses/2-006-thermal-fluids-engineering-ii-spring-2004/).
  - [National Committee for Fluid Mechanics Films (NCFMF)](https://web.mit.edu/hml/ncfmf.html) - Serie histórica de vídeos del MIT (obligatorio para visualizar fluidos).
- **Libros de Texto Canónicos:**
  - *Fluid Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 6 del Curso de Física Teórica).
  - *An Introduction to Fluid Dynamics* - G.K. Batchelor.
  - *Turbulence: The Legacy of A.N. Kolmogorov* - Uriel Frisch.
