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
* **MIT 8.044 (Statistical Physics I):** Las primeras clases de este curso brindan una recapitulación muy rigurosa de las leyes macroscópicas.
* **Yale Fundamentals of Physics (PHYS 200):** Prof. Ramamurti Shankar, excelentes analogías para comprender la Segunda Ley.
* **The Theoretical Minimum (Thermodynamics):** Curso por Leonard Susskind, muy enfocado a físicos teóricos.

### 📝 Artículos e Interactivos Interesantes
* **PhET - Propiedades de los Gases:** Para ver en tiempo real cómo cambia la presión y el trabajo al modificar volúmenes y temperaturas.
* **"Reflections on the Motive Power of Fire" (1824):** El clásico de Sadi Carnot donde plantea el concepto de la máquina térmica ideal.
* **Artículo sobre el Demonio de Maxwell:** Un experimento mental fundamental sobre la entropía y la información.
