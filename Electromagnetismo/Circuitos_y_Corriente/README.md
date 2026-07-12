# Circuitos y Corriente

El estudio de circuitos y corriente eléctrica se ocupa del movimiento macroscópico continuo de cargas eléctricas a través de conductores y componentes pasivos o activos. Es la base tecnológica de toda la electrónica moderna.

## 📜 Contexto Histórico
A finales del siglo XVIII, Luigi Galvani descubrió la "electricidad animal" en patas de rana, lo cual inspiró a Alessandro Volta a inventar en 1800 la primera pila eléctrica (pila voltaica), proporcionando una fuente de corriente continua y estable. En 1827, el físico alemán Georg Simon Ohm publicó su famosa ley que relaciona voltaje y corriente, basándose en analogías con el flujo de calor de Fourier. En 1845, Gustav Kirchhoff generalizó el análisis de topologías de circuitos complejos al deducir sus famosas leyes (Leyes de Kirchhoff) basadas en la conservación de carga y energía. 

---

## 🧮 Desarrollo Teórico Profundo

### Corriente y Densidad de Corriente
La corriente eléctrica $I$ es la tasa de flujo de carga neta que cruza un área transversal en un tiempo $dt$:
$$ I = \frac{dq}{dt} $$
Microscópicamente, se define mediante el vector densidad de corriente $\vec{J}$:
$$ I = \int_S \vec{J} \cdot d\vec{A} $$
donde $\vec{J} = n q \vec{v}_d$, siendo $n$ la densidad de portadores, $q$ la carga de cada portador y $\vec{v}_d$ la velocidad de deriva.

### Ley de Ohm
En muchos materiales, la densidad de corriente es proporcional al campo eléctrico local:
$$ \vec{J} = \sigma \vec{E} $$
donde $\sigma$ es la conductividad. En forma macroscópica para un hilo conductor uniforme de longitud $L$, área $A$ y resistividad $\rho = 1/\sigma$, esto se convierte en la Ley de Ohm:
$$ V = I R $$
con la resistencia definida como $R = \rho \frac{L}{A}$.

### Potencia Eléctrica
La tasa a la que la energía eléctrica es transferida por un circuito es:
$$ P = V I $$
Para una resistencia óhmica, esto resulta en calentamiento por efecto Joule:
$$ P = I^2 R = \frac{V^2}{R} $$

### Leyes de Kirchhoff
Las leyes de Kirchhoff permiten resolver redes eléctricas complejas:
1. **Ley de Nodos (KCL - Conservación de la carga):** La suma algebraica de las corrientes que entran y salen de un nodo es cero:
   $$ \sum_{k} I_k = 0 $$
2. **Ley de Mallas (KVL - Conservación de la energía):** La suma algebraica de las diferencias de potencial en un camino cerrado es cero:
   $$ \sum_{k} \Delta V_k = 0 $$

---

## 🛠 Ejemplo Práctico
**Problema:** Un circuito RC en serie consta de una fuente de voltaje continuo $\mathcal{E}$, una resistencia $R$, y un condensador de capacitancia $C$, inicialmente descargado. El circuito se cierra mediante un interruptor en $t=0$. Encontrar la carga del condensador $q(t)$ como función del tiempo.

**Solución paso a paso:**
1. **Aplicar la Ley de Mallas de Kirchhoff:**
   Al recorrer el circuito, tenemos el aumento de la fuente, la caída en el resistor y la caída en el condensador:
   $$ \mathcal{E} - I R - \frac{q}{C} = 0 $$
2. **Expresar la corriente:** Sabemos que $I = \frac{dq}{dt}$, luego:
   $$ R \frac{dq}{dt} + \frac{q}{C} = \mathcal{E} $$
3. **Resolver la ecuación diferencial:**
   Esta es una ecuación diferencial lineal de primer orden separable:
   $$ \frac{dq}{dt} = \frac{\mathcal{E} C - q}{R C} \implies \frac{dq}{q - \mathcal{E} C} = -\frac{dt}{R C} $$
   Integrando desde $t=0$ (con $q(0)=0$) hasta $t$:
   $$ \ln \left( \frac{q(t) - \mathcal{E} C}{-\mathcal{E} C} \right) = -\frac{t}{R C} $$
4. **Despejar $q(t)$:**
   $$ q(t) - \mathcal{E} C = -\mathcal{E} C e^{-t/(RC)} $$
   $$ q(t) = C \mathcal{E} \left( 1 - e^{-t/\tau} \right) $$
   Donde $\tau = R C$ es la constante de tiempo del circuito. La carga crece asintóticamente hasta el valor máximo $Q_{\max} = C \mathcal{E}$.

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
* **MIT 6.002 (Circuits and Electronics):** Excelente para llevar el análisis de circuitos a nivel de ingeniería.
* **Feynman Lectures on Physics:** Volumen II, Capítulos 22 y 23 (Circuitos de CA y cavidades).
* **Khan Academy - Ingeniería Eléctrica:** Análisis de circuitos (resistencias, divisores de tensión, Thevenin).

### 📝 Artículos e Interactivos Interesantes
* **PhET Interactive Simulations - Circuit Construction Kit (DC/AC):** Una herramienta magnífica para construir circuitos virtuales y ver el flujo de electrones en tiempo real.
* **Falstad Circuit Simulator:** Un emulador de circuitos en el navegador altamente avanzado y visual.
* **Biografía de Volta y Galvani (Wikipedia):** El fascinante debate histórico sobre la "electricidad animal" versus la electricidad química.
