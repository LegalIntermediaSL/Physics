# Ecuaciones de Maxwell y Ondas Electromagnéticas

Las Ecuaciones de Maxwell representan la obra magna del electromagnetismo clásico, unificando la electricidad, el magnetismo y la óptica en un marco teórico elegante y autoconsistente. Son el equivalente en electromagnetismo a las Leyes de Newton en mecánica clásica.

## 📜 Contexto Histórico
A mediados del siglo XIX, las leyes de Gauss, Ampère y Faraday existían como principios empíricos desconectados o parcialmente incompatibles. James Clerk Maxwell, inspirado en las intuiciones visuales de Faraday sobre las "líneas de fuerza", desarrolló un modelo matemático unificado en la década de 1860. Maxwell descubrió una inconsistencia en la Ley de Ampère al aplicarla a condensadores, y añadió la "corriente de desplazamiento". Esto no solo salvó la conservación de la carga, sino que predijo la existencia de ondas electromagnéticas que viajaban a la velocidad de la luz. En 1887, Heinrich Hertz demostró experimentalmente la existencia de estas ondas. Oliver Heaviside fue quien reformuló matemáticamente las 20 ecuaciones de Maxwell originales en la notación vectorial (gradiente, divergencia, rotacional) que usamos hoy.

---

## 🧮 Desarrollo Teórico Profundo

Las ecuaciones de Maxwell en el vacío, en su forma diferencial e integral, son:

### 1. Ley de Gauss para el Campo Eléctrico
Las cargas eléctricas son las fuentes del campo eléctrico.
* **Diferencial:** $\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$
* **Integral:** $\oint_S \vec{E} \cdot d\vec{A} = \frac{Q}{\varepsilon_0}$

### 2. Ley de Gauss para el Campo Magnético
No existen los monopolos magnéticos; las líneas de campo son cerradas.
* **Diferencial:** $\nabla \cdot \vec{B} = 0$
* **Integral:** $\oint_S \vec{B} \cdot d\vec{A} = 0$

### 3. Ley de Faraday-Lenz
Un campo magnético variable en el tiempo induce un campo eléctrico rotacional.
* **Diferencial:** $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$
* **Integral:** $\oint_C \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}$

### 4. Ley de Ampère-Maxwell
Un campo magnético es generado tanto por corrientes eléctricas de conducción como por campos eléctricos variables en el tiempo (corriente de desplazamiento).
* **Diferencial:** $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$
* **Integral:** $\oint_C \vec{B} \cdot d\vec{l} = \mu_0 I + \mu_0 \varepsilon_0 \frac{d\Phi_E}{dt}$

### Derivación de la Ecuación de Onda
En el vacío (sin cargas ni corrientes, $\rho=0, \vec{J}=0$), tomamos el rotacional de la ley de Faraday:
$$ \nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) $$
Usando la identidad vectorial $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$, y sabiendo que $\nabla \cdot \vec{E} = 0$:
$$ -\nabla^2 \vec{E} = -\frac{\partial}{\partial t} \left( \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t} \right) \implies \nabla^2 \vec{E} = \mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2} $$
Esta es una ecuación de onda cuya velocidad de propagación es $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, que coincide exactamente con la velocidad de la luz.

---

## 🛠 Ejemplo Práctico
**Problema:** Una onda electromagnética plana viaja en el vacío en la dirección $+z$. Si el campo eléctrico está dado por $\vec{E}(z,t) = E_0 \cos(kz - \omega t) \hat{i}$, deducir el vector campo magnético $\vec{B}(z,t)$.

**Solución paso a paso:**
1. **Usar la Ley de Faraday en el vacío:** $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$
2. **Calcular el rotacional de $\vec{E}$:**
   Como $\vec{E}$ solo tiene componente $x$ y solo depende de $z$ y $t$:
   $$ \nabla \times \vec{E} = \left| \begin{matrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ E_x & 0 & 0 \end{matrix} \right| = \frac{\partial E_x}{\partial z} \hat{j} $$
   Derivando $E_x(z,t) = E_0 \cos(kz - \omega t)$ respecto a $z$:
   $$ \frac{\partial E_x}{\partial z} = -k E_0 \sin(kz - \omega t) $$
   Por tanto, $\nabla \times \vec{E} = -k E_0 \sin(kz - \omega t) \hat{j}$.
3. **Igualar y resolver para $\vec{B}$:**
   $$ -\frac{\partial \vec{B}}{\partial t} = -k E_0 \sin(kz - \omega t) \hat{j} \implies \frac{\partial \vec{B}}{\partial t} = k E_0 \sin(kz - \omega t) \hat{j} $$
   Integrando con respecto al tiempo:
   $$ \vec{B}(z,t) = \int k E_0 \sin(kz - \omega t) dt \, \hat{j} = \frac{k}{\omega} E_0 \cos(kz - \omega t) \hat{j} $$
4. **Relación entre $E_0$ y $B_0$:**
   Sabiendo que $c = \frac{\omega}{k}$, el campo magnético resulta:
   $$ \vec{B}(z,t) = \frac{E_0}{c} \cos(kz - \omega t) \hat{j} $$
   Note que $\vec{E}$ y $\vec{B}$ oscilan en fase y son ortogonales entre sí y ortogonales a la dirección de propagación.

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
* **MIT 8.02 (Electricity and Magnetism):** Últimas clases del curso, donde se revela la corriente de desplazamiento y las ondas electromagnéticas.
* **Stanford - Special Relativity (Leonard Susskind):** Explica la invariancia Lorentziana de las Ecuaciones de Maxwell, vital para la relatividad.
* **Feynman Lectures on Physics:** Volumen II, Capítulo 18 (Las Ecuaciones de Maxwell).

### 📝 Artículos e Interactivos Interesantes
* **PhET - Radiating Charge:** Simulador que muestra cómo una carga acelerada genera ondas electromagnéticas.
* **"A Dynamical Theory of the Electromagnetic Field" (1865):** El artículo histórico de Maxwell (recomendado revisar en un contexto histórico).
* **Demostración de Ondas de Hertz (Video en YouTube):** Documentales históricos de cómo Hertz produjo ondas de radio mediante chispas eléctricas.
