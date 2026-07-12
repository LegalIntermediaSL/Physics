# Dinámica de Fluidos y Ecuación de Bernoulli
La dinámica de fluidos estudia los fluidos en movimiento. Analiza magnitudes como velocidad, presión, densidad y temperatura en función de la posición y el tiempo, basándose en leyes de conservación (masa, energía, momento).

## 📜 Contexto Histórico
Leonhard Euler formuló las ecuaciones básicas del movimiento de los fluidos no viscosos en el siglo XVIII. Daniel Bernoulli, en su obra "Hydrodynamica" de 1738, estableció el famoso principio que lleva su nombre. Posteriormente, Navier y Stokes agregaron términos de fricción viscosa para formar las Ecuaciones de Navier-Stokes en el siglo XIX.

## 🧮 Desarrollo Teórico Profundo
**Ecuación de Continuidad (Conservación de la masa):**
Para un fluido incompresible fluyendo por un tubo, el caudal volumétrico $ Q $ es constante:
$ A_1 v_1 = A_2 v_2 = Q $

**Ecuación de Bernoulli (Conservación de energía):**
Válida para flujo estacionario, incompresible, no viscoso (ideal) y a lo largo de una línea de corriente:
$ P + \frac{1}{2} \rho v^2 + \rho g z = \text{constante} $
$ P_1 + \frac{1}{2} \rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2} \rho v_2^2 + \rho g z_2 $
Donde $ P $ es la presión estática, $ \frac{1}{2} \rho v^2 $ es la presión dinámica y $ \rho g z $ la presión hidrostática.

**Efecto Venturi y Tubo de Pitot:**
Aplicaciones directas de la ecuación de Bernoulli para medir velocidades y caídas de presión en conductos.

## 🛠 Ejemplo Práctico
**Problema:** Por una tubería horizontal fluye agua. En la sección ancha, el diámetro es de $ 10 \text{ cm} $, la presión es de $ 1.5 \times 10^5 \text{ Pa} $ y la velocidad es de $ 2 \text{ m/s} $. La tubería se estrecha a un diámetro de $ 5 \text{ cm} $. Calcula la velocidad y la presión en la sección estrecha. ($ \rho_{\text{agua}} = 1000 \text{ kg/m}^3 $).

**Solución paso a paso:**
1. Áreas de las secciones:
   $ A_1 = \pi (0.05 \text{ m})^2 = 0.0025\pi \text{ m}^2 $
   $ A_2 = \pi (0.025 \text{ m})^2 = 0.000625\pi \text{ m}^2 $
2. Usamos la ecuación de continuidad para hallar $ v_2 $:
   $ v_2 = v_1 \frac{A_1}{A_2} = 2 \frac{0.0025\pi}{0.000625\pi} = 2 \times 4 = 8 \text{ m/s} $.
3. Aplicamos Bernoulli. Como es horizontal, $ z_1 = z_2 $, por lo que el término $ \rho g z $ se cancela:
   $ P_1 + \frac{1}{2} \rho v_1^2 = P_2 + \frac{1}{2} \rho v_2^2 $
4. Despejamos $ P_2 $:
   $ P_2 = P_1 + \frac{1}{2} \rho (v_1^2 - v_2^2) $
   $ P_2 = 1.5 \times 10^5 + \frac{1}{2} (1000) (2^2 - 8^2) $
   $ P_2 = 150000 + 500 (4 - 64) = 150000 + 500 (-60) $
   $ P_2 = 150000 - 30000 = 120000 \text{ Pa} $ (O $ 1.2 \times 10^5 \text{ Pa} $).

## 📚 Recursos Específicos
- **Cursos:** "Introduction to Fluid Mechanics" (Coursera).
- **Artículos/Textos:** *Fluid Mechanics* (Frank M. White), "Hydrodynamica" de Daniel Bernoulli.
- **Simulaciones:** "Fluid Pressure and Flow" (PhET Interactive Simulations).
