# La Ecuación de Transporte de Boltzmann

Para sistemas fuera del equilibrio termodinámico (como gases fluyendo, conductores sometidos a campos eléctricos, o plasmas), la mecánica estadística de ensambles estacionarios es insuficiente. Necesitamos describir cómo evoluciona la distribución de las partículas en el tiempo.
Ludwig Boltzmann desarrolló una ecuación íntegro-diferencial que describe la evolución de la función de distribución de las partículas.

## 1. La Función de Distribución en el Espacio de Fases
Consideremos un gas de partículas. Definimos $f(\vec{r}, \vec{p}, t)$ como la función de distribución espacial y de momentos. El valor $f(\vec{r}, \vec{p}, t) d^3r d^3p$ es el número de partículas dentro del elemento de volumen $d^3r$ y el elemento de momento $d^3p$ en el tiempo $t$.

## 2. Derivación de la Ecuación de Boltzmann
Si no hay colisiones entre las partículas, el flujo en el espacio de fases (fase espacial y de momento) debe conservarse. Siguiendo el teorema de Liouville de la mecánica clásica, la derivada total respecto al tiempo es cero:

$$
\frac{df}{dt} = \frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_r f + \vec{F} \cdot \nabla_p f = 0
$$

Donde $\vec{v} = d\vec{r}/dt$ es la velocidad de la partícula y $\vec{F} = d\vec{p}/dt$ es la fuerza externa neta aplicada (como gravedad o electromagnetismo).

Sin embargo, las partículas colisionan entre sí, alterando abruptamente sus momentos y dispersándolas fuera o dentro de la trayectoria analizada. Boltzmann incorporó este efecto añadiendo un **Término de Colisión** $\left(\frac{\partial f}{\partial t}\right)_{\text{col}}$ al lado derecho:

$$
\frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_r f + \vec{F} \cdot \nabla_p f = \left(\frac{\partial f}{\partial t}\right)_{\text{col}}
$$

## 3. El Término de Colisión (Stosszahlansatz)
La genialidad geométrica y física de Boltzmann consistió en modelar las colisiones asumiendo el **"Caos Molecular" (Stosszahlansatz)**: la suposición de que los momentos de las partículas antes de chocar no están correlacionados matemáticamente.
Para colisiones elásticas a dos cuerpos (partícula 1 de momento $p_1$ y partícula 2 de momento $p_2$, dispersándose a estados con momentos $p_1'$ y $p_2'$), la tasa de cambio neta de colisiones es la diferencia entre los procesos que dispersan partículas HASTA el estado de interés menos las que las dispersan FUERA de él:

$$
\left(\frac{\partial f}{\partial t}\right)_{\text{col}} = \int d^3p_2 \int d\Omega \, |v_1 - v_2| \frac{d\sigma}{d\Omega} [f(p_1') f(p_2') - f(p_1) f(p_2)]
$$

Donde $\frac{d\sigma}{d\Omega}$ es la sección eficaz diferencial de dispersión colisional.

## 4. Consecuencias Macroscópicas
La ecuación de Boltzmann es el fundamento de toda la teoría cinética de gases y fluidos. A través del cálculo de los "momentos" de esta ecuación (integrando $f$, $vf$, y $v^2f$ sobre todos los momentos), se deducen rigurosamente y desde primeros principios las ecuaciones de dinámica de fluidos macroscópicas:
- Conservación de masa (Ecuación de Continuidad).
- Conservación de momento (Ecuaciones de Navier-Stokes).
- Conservación de energía.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Statistical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtj_3l8x1k-D1H_cMB-x162) - Colectivos microcanónicos y fluctuaciones cuánticas.
- [MIT 8.044: Statistical Physics I (Thomas J. Greytak)](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Enfoque riguroso termodinámico (disponible en OCW/YouTube).
