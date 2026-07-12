# Leyes de la Termodinámica

La termodinámica clásica estudia las transferencias de calor, la realización de trabajo y las propiedades macroscópicas de los sistemas en equilibrio. Todo el marco teórico descansa sobre cuatro postulados fundamentales empíricamente validados, conocidos como las Leyes de la Termodinámica.

## 📜 Contexto Histórico
El desarrollo de la termodinámica fue fuertemente motivado por la Revolución Industrial y la necesidad de mejorar la eficiencia de las máquinas de vapor. En 1824, Nicolas Léonard Sadi Carnot publicó un tratado sobre el calor, sentando las bases teóricas de la eficiencia térmica. Julius Robert von Mayer y James Prescott Joule, en la década de 1840, demostraron experimentalmente la equivalencia entre el calor y el trabajo mecánico. Lord Kelvin (William Thomson) y Rudolf Clausius formularon luego las primeras y segundas leyes de la termodinámica en la década de 1850, y Clausius acuñó el término "entropía" en 1865. Finalmente, Walther Nernst propuso la tercera ley a principios del siglo XX.

---

## 🧮 Desarrollo Teórico Profundo

### Ley Cero de la Termodinámica
Establece el concepto de temperatura: *Si dos sistemas A y B están en equilibrio térmico con un tercer sistema C, entonces A y B están en equilibrio térmico entre sí.*
Esto permite la construcción de termómetros.

### Primera Ley de la Termodinámica (Conservación de la Energía)
La energía total de un sistema aislado se conserva. La variación de la energía interna $dU$ de un sistema es igual al calor $dQ$ añadido al sistema menos el trabajo $dW$ realizado por el sistema sobre su entorno:
$$ dU = \delta Q - \delta W $$
En procesos reversibles de un gas, el trabajo mecánico es $\delta W = P \, dV$, por lo que:
$$ dU = \delta Q - P \, dV $$
Como la energía interna $U$ es una función de estado, su integral a través de un ciclo cerrado es nula: $\oint dU = 0$.

### Segunda Ley de la Termodinámica (Entropía)
Existen varias formulaciones equivalentes:
* **Enunciado de Clausius:** Es imposible construir un dispositivo que opere en un ciclo y cuyo único efecto sea la transferencia de calor de un cuerpo más frío a un cuerpo más caliente.
* **Enunciado de Kelvin-Planck:** Es imposible construir una máquina térmica que, operando en un ciclo, extraiga calor de una sola fuente y realice una cantidad equivalente de trabajo.
Matemáticamente, para un proceso infinitesimal reversible, el cambio de entropía se define como:
$$ dS = \frac{\delta Q_{\text{rev}}}{T} $$
Para cualquier proceso en un sistema aislado:
$$ \Delta S \ge 0 $$

### Tercera Ley de la Termodinámica
A medida que la temperatura de un sistema se aproxima al cero absoluto ($T \to 0$), su entropía se aproxima a un valor mínimo constante. Para un cristal perfecto, este valor es cero.
$$ \lim_{T \to 0} S = 0 $$

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular el trabajo, calor y cambio de energía interna de un mol de gas ideal monoatómico que sufre una expansión isotérmica reversible desde un volumen $V_1$ hasta $V_2$ a una temperatura constante $T$.

**Solución paso a paso:**
1. **Energía Interna:** Para un gas ideal, la energía interna depende únicamente de la temperatura. Puesto que el proceso es isotérmico ($\Delta T = 0$):
   $$ \Delta U = 0 $$
2. **Trabajo Realizado ($W$):**
   El trabajo viene dado por la integral de presión respecto al volumen:
   $$ W = \int_{V_1}^{V_2} P \, dV $$
   Usando la ecuación de los gases ideales $P = \frac{nRT}{V}$:
   $$ W = \int_{V_1}^{V_2} \frac{nRT}{V} dV = nRT \ln\left(\frac{V_2}{V_1}\right) $$
3. **Calor Intercambiado ($Q$):**
   De la Primera Ley, $\Delta U = Q - W$. Puesto que $\Delta U = 0$:
   $$ Q = W = nRT \ln\left(\frac{V_2}{V_1}\right) $$
   Si $V_2 > V_1$, $W > 0$ y $Q > 0$, lo que significa que el gas absorbe calor para expandirse manteniendo su temperatura.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **MIT 8.044 (Statistical Physics I):** [Página del Curso OCW](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Las primeras clases de este curso brindan una recapitulación muy rigurosa de las leyes macroscópicas.
2. **Yale Fundamentals of Physics (PHYS 200):** [Sesiones de Termodinámica](https://oyc.yale.edu/physics/phys-200) - Prof. Ramamurti Shankar, excelentes analogías para comprender la Segunda Ley y el ciclo de Carnot.
3. **The Theoretical Minimum (Thermodynamics):** [Curso Completo](https://theoreticalminimum.com/courses/statistical-mechanics/2013/spring) - Curso por Leonard Susskind, muy enfocado a físicos teóricos.
4. **Coursera - Introduction to Thermodynamics:** [Enlace a Coursera](https://www.coursera.org/learn/thermodynamics-intro) - Universidad de Míchigan, curso profundo sobre la conservación de energía.
5. **NPTEL - Classical Thermodynamics:** [Curso de NPTEL](https://nptel.ac.in/courses/112/105/112105123/) - Curso avanzado sobre equilibrio y estabilidad termodinámica.

### 📝 Artículos e Interactivos Interesantes
1. **PhET - Propiedades de los Gases:** [Simulación Interactiva](https://phet.colorado.edu/es/simulation/gas-properties) - Para ver en tiempo real cómo cambia la presión y el trabajo al modificar volúmenes y temperaturas.
2. **"Reflections on the Motive Power of Fire" (1824):** [Sadi Carnot's Book](https://en.wikipedia.org/wiki/Reflections_on_the_Motive_Power_of_Fire) - El clásico de Sadi Carnot donde plantea el concepto de la máquina térmica ideal y la eficiencia máxima.
3. **Artículo sobre el Demonio de Maxwell:** [Maxwell's Demon](https://en.wikipedia.org/wiki/Maxwell%27s_demon) - Un experimento mental fundamental sobre la entropía y la información de la naturaleza.
4. **Wikipedia - Leyes de la Termodinámica:** [Leyes de la Termodinámica](https://es.wikipedia.org/wiki/Leyes_de_la_termodin%C3%A1mica) - Excelente resumen de los cuatro postulados fundamentales.
5. **HyperPhysics - Primera Ley:** [Primera Ley](http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/firlaw.html) - Detalles sobre procesos isobáricos, isocóricos e isotérmicos.
6. **HyperPhysics - Segunda Ley:** [Segunda Ley](http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/seclaw.html) - Entropía y los enunciados de Kelvin y Clausius.
7. **Feynman Lectures - Ch. 44:** [The Laws of Thermodynamics](https://www.feynmanlectures.caltech.edu/I_44.html) - Una explicación brillante del concepto de máquinas reversibles.
8. **Wolfram Demonstrations - Carnot Cycle:** [Simulación del Ciclo Carnot](https://demonstrations.wolfram.com/CarnotCycleOnIdealGas/) - Simulaciones interactivas del ciclo de Carnot.

### 📖 Referencias Útiles y Bibliografía
* [Fundamentals of Statistical and Thermal Physics - Reif, F.](https://books.google.com/books?id=0sM4DgAAQBAJ) - Un estándar indispensable que detalla cómo la termodinámica emerge de las leyes estadísticas, ideal para entender las leyes clásicas en profundidad.
* [An Introduction to Thermal Physics - Schroeder, D. V.](https://physics.weber.edu/thermal/) - Texto excelente e intuitivo, muy claro en sus explicaciones de calor y trabajo.
* [Statistical Mechanics - Pathria, R. K.](https://www.elsevier.com/books/statistical-mechanics/pathria/978-0-12-382188-1) - Aunque más estadístico, sus primeros capítulos sobre las leyes termodinámicas son profundos.
* [Heat and Thermodynamics - Zemansky, M. W. & Dittman, R. H.](https://www.mheducation.com/highered/product/heat-thermodynamics-zemansky-dittman/M9780070170599.html) - Un texto puramente termodinámico y muy completo para las leyes clásicas.
* [Thermodynamics and an Introduction to Thermostatistics - Callen, H. B.](https://books.google.com/books/about/Thermodynamics_and_an_Introduction_to_Th.html?id=R2s_AQAAIAAJ) - Uno de los mejores textos formales sobre el enfoque axiomático de la termodinámica.
