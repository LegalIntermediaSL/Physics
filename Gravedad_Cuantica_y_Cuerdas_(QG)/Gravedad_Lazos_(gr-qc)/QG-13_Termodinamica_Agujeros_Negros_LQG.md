# [QG-13] Termodinamica de Agujeros Negros en LQG

## 1. La Fórmula de Bekenstein-Hawking
Desde los años 70, sabemos por Bekenstein y Hawking que un agujero negro tiene una entropía proporcional a su área $A$:

$$
S_{BH} = \frac{k_B A}{4 l_P^2}
$$

Donde $l_P$ es la longitud de Planck. Sin embargo, la relatividad general clásica no proporciona los "microestados" estadísticos que justifiquen esta entropía térmica. Encontrar estos microestados es la prueba de fuego de cualquier teoría de gravedad cuántica.

## 2. Microestados en LQG
La Gravedad Cuántica de Lazos (LQG) ofrece una derivación directa e intuitiva de la entropía de los agujeros negros.

Imaginemos el horizonte de eventos de un agujero negro. El espacio interior y exterior está descrito por una red de espín. Los enlaces (*links*) de la red de espín atraviesan el horizonte de eventos, perforando la superficie 2D.

Cada perforación dota al horizonte de un "cuanto de área". El área macroscópica $A$ del agujero negro restringe la suma total de estos cuantos.
Los microestados del agujero negro son las posibles configuraciones de espín $j_i$ (y sus proyecciones $m_i$) en los bordes que perforan el horizonte, tales que el área total coincida con $A$.

## 3. El Cálculo de la Entropía
Usando la fórmula de Rovelli-Smolin para el área, la teoría de Chern-Simons para los grados de libertad en el horizonte (horizonte aislado), y contando combinatoriamente el número de microestados $\Omega(A)$, LQG obtiene que la entropía es:

$$
S = \frac{\gamma_0}{\gamma} \frac{A}{4 l_P^2}
$$

Donde $\gamma$ es el parámetro de Immirzi de la teoría.

## 4. El Parámetro de Immirzi
Para que el resultado de LQG coincida exactamente con la predicción semiclásica de Hawking, debe cumplirse que $\gamma = \gamma_0$.
Cálculos detallados demostraron que si se fija el parámetro de Immirzi a un valor específico (relacionado con raíces de ecuaciones logarítmicas, aproximadamente $\gamma pprox 0.2375$), LQG reproduce la entropía de Bekenstein-Hawking no solo para agujeros negros de Schwarzschild, sino para Reissner-Nordström y agujeros de Kerr simultáneamente.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Stanford: String Theory and M-Theory](https://theoreticalminimum.com/courses/string-theory/2010/fall) - Leonard Susskind.
  - [Perimeter Institute: String Theory (PIRSA)](https://pirsa.org/) - Cursos de posgrado.
  - [Cambridge DAMTP: String Theory Lectures](http://www.damtp.cam.ac.uk/user/tong/string.html) - David Tong.
- **Libros de Texto Canónicos:**
  - *String Theory* (Vol 1 y 2) - Joseph Polchinski. (La Biblia moderna de Cuerdas).
  - *A First Course in String Theory* - Barton Zwiebach. (Excelente para nivel grado).
  - *Quantum Gravity* - Carlo Rovelli. (Para la perspectiva de Loop Quantum Gravity).
