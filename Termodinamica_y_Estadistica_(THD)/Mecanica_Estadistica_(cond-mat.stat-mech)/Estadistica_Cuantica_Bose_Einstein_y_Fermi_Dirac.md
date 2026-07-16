# Estadísticas Cuánticas: Fermiones y Bosones

A temperaturas muy bajas o densidades muy altas, la mecánica estadística clásica de Maxwell-Boltzmann ($p_i \propto e^{-\beta E_i}$) fracasa. La indistinguibilidad intrínseca de las partículas cuánticas y el espín obligan al uso de estadísticas especializadas.

## 1. El Problema de la Indistinguibilidad
En mecánica cuántica, si intercambiamos dos partículas idénticas, la densidad de probabilidad del estado no debe cambiar. Esto implica que la función de onda total $\Psi$ solo puede ser simétrica o antisimétrica bajo el intercambio de partículas.
- **Bosones** (Espín entero: 0, 1, 2...): La función de onda es simétrica. Múltiples bosones pueden ocupar el mismo estado cuántico simultáneamente.
- **Fermiones** (Espín semientero: 1/2, 3/2...): La función de onda es antisimétrica. Debido a la anulación de la función de onda si los estados coinciden, dos fermiones idénticos no pueden ocupar el mismo estado cuántico simultáneamente (**Principio de Exclusión de Pauli**).

## 2. Derivación de las Distribuciones Cuánticas
Consideremos un estado cuántico individual con energía $\epsilon$. Asumimos que este estado es en sí mismo un sistema termodinámico abierto en contacto con el resto de partículas (baño). Usamos la Gran Función de Partición $\mathcal{Z}$.

Para **Fermiones**, el número de ocupación del estado cuántico solo puede ser $n = 0$ o $n = 1$.

$$
\mathcal{Z}_{FD} = \sum_{n=0}^{1} e^{-\beta(\epsilon - \mu)n} = 1 + e^{-\beta(\epsilon - \mu)}
$$

El número medio de ocupación térmica de este nivel de energía es la **Distribución de Fermi-Dirac**:

$$
\langle n \rangle_{FD} = - \frac{1}{\beta} \frac{\partial \ln \mathcal{Z}}{\partial \epsilon} = \frac{1}{e^{\beta(\epsilon - \mu)} + 1}
$$

Para **Bosones**, el estado cuántico puede ser ocupado por cualquier número de partículas, $n = 0, 1, 2, \dots, \infty$.

$$
\mathcal{Z}_{BE} = \sum_{n=0}^{\infty} e^{-\beta(\epsilon - \mu)n} = \frac{1}{1 - e^{-\beta(\epsilon - \mu)}}
$$

La convergencia exige que $\mu < \epsilon$ para el estado fundamental. El número medio de ocupación es la **Distribución de Bose-Einstein**:

$$
\langle n \rangle_{BE} = \frac{1}{e^{\beta(\epsilon - \mu)} - 1}
$$

## 3. Aplicaciones Físicas y Degeneración
- **Gas de Fermi Degenerado**: A temperatura cercana al cero absoluto ($T \to 0$), la distribución de Fermi-Dirac se convierte en una función escalón. Todos los niveles de energía hasta la "Energía de Fermi" ($E_F$) están llenos, y los superiores vacíos. Este empaquetamiento genera una tremenda presión puramente cuántica, la **Presión de Degeneración Electrónica**, que es la fuerza física responsable de sostener la gravedad e impedir el colapso de las estrellas Enanas Blancas.
- **Condensado de Bose-Einstein**: Al acercarse al cero absoluto, el potencial químico de un gas de bosones $\mu$ se aproxima por debajo a la energía del estado fundamental $\epsilon_0$. El denominador de la distribución diverge, provocando que una fracción macroscópica de las partículas del gas "caiga" y se acumule colectivamente en el estado cuántico fundamental. El gas se comporta entonces como un único super-átomo mecánico-cuántico.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Statistical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtj_3l8x1k-D1H_cMB-x162) - Colectivos microcanónicos y fluctuaciones cuánticas.
- [MIT 8.044: Statistical Physics I (Thomas J. Greytak)](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Enfoque riguroso termodinámico (disponible en OCW/YouTube).
