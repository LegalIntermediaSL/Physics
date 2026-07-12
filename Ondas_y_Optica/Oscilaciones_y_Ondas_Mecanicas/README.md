# Oscilaciones y Ondas Mecánicas
Este apartado profundiza en los sistemas que presentan movimiento periódico y en cómo las perturbaciones se propagan a través de medios materiales, transportando energía sin transporte neto de materia.

## 📜 Contexto Histórico
El estudio del movimiento oscilatorio tiene raíces en las observaciones de Galileo Galilei sobre los péndulos en el siglo XVI. Christiaan Huygens posteriormente desarrolló el reloj de péndulo en 1656. La descripción matemática rigurosa de las ondas en cuerdas fue formulada por Jean le Rond d'Alembert en 1747, sentando las bases para la ecuación de onda clásica.

## 🧮 Desarrollo Teórico Profundo

El formalismo de las oscilaciones y ondas mecánicas es esencial para entender cómo la materia y la energía interactúan a través de fuerzas elásticas en sistemas físicos.

### 1. Oscilador Armónico: Formalismo Energético y Dinámico

El Movimiento Armónico Simple (MAS) puede derivarse de un potencial escalar alrededor de un punto de equilibrio estable $x_0$. Expandiendo en serie de Taylor la energía potencial $U(x)$:
$$ U(x) \approx U(x_0) + \frac{dU}{dx}\Big|_{x_0} (x - x_0) + \frac{1}{2} \frac{d^2U}{dx^2}\Big|_{x_0} (x - x_0)^2 + \dots $$
Si $x_0$ es un mínimo estable, $\frac{dU}{dx} = 0$, y absorbiendo $U(x_0)$ en el nivel cero, tenemos $U(x) \approx \frac{1}{2}k x^2$ donde la constante efectiva del resorte es $k = \frac{d^2U}{dx^2}$.
La fuerza conservativa es $F = -\nabla U = -kx$. Por la segunda ley de Newton:
$$ \frac{d^2x}{dt^2} + \omega_0^2 x = 0 \quad \text{con} \quad \omega_0 = \sqrt{\frac{k}{m}} $$
La energía mecánica total del oscilador es constante y es una métrica invariante del sistema:
$$ E = K + U = \frac{1}{2} m \dot{x}^2 + \frac{1}{2} k x^2 = \frac{1}{2} k A^2 $$

### 2. Ecuación de Onda en Cuerdas y Barras Sólidas

**Ondas Transversales (Cuerda):**
Como se derivó históricamente, una cuerda sometida a tensión $T$ y con masa por unidad de longitud $\mu$ presenta una fuerza restauradora perpendicular al equilibrio, resultando en:
$$ \frac{\partial^2 y}{\partial x^2} - \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} = 0 \quad \text{donde} \quad v = \sqrt{\frac{T}{\mu}} $$

**Ondas Longitudinales (Barra sólida):**
Si consideramos una barra elástica de densidad $\rho$, sección transversal $A$ y módulo de Young $Y$, un desplazamiento longitudinal $u(x,t)$ induce una deformación unitaria $\epsilon = \partial u/\partial x$. Por la Ley de Hooke, el esfuerzo es $\sigma = Y \epsilon$. La fuerza neta sobre un elemento $dx$ es $A \frac{\partial \sigma}{\partial x} dx = A Y \frac{\partial^2 u}{\partial x^2} dx$.
Igualando a la masa $(\rho A dx)$ por la aceleración $\frac{\partial^2 u}{\partial t^2}$, llegamos a la misma estructura matemática:
$$ \frac{\partial^2 u}{\partial x^2} - \frac{1}{c^2} \frac{\partial^2 u}{\partial t^2} = 0 \quad \text{donde la velocidad del sonido es} \quad c = \sqrt{\frac{Y}{\rho}} $$

### 3. Potencia y Flujo de Energía en la Onda

Una onda mecánica viajera transporta energía a través de la interfaz del medio material. La potencia $P$ transmitida por una onda transversal a lo largo de una cuerda es el producto de la componente transversal de la tensión y la velocidad transversal del elemento de cuerda:
$$ P(x,t) = F_y v_y \approx \left(-T \frac{\partial y}{\partial x}\right) \left(\frac{\partial y}{\partial t}\right) $$
Para una onda armónica $y(x,t) = A \sin(kx - \omega t)$, las derivadas son $\partial y/\partial x = kA \cos(kx-\omega t)$ y $\partial y/\partial t = -A\omega \cos(kx-\omega t)$. Sustituyendo, la potencia instantánea es:
$$ P(x,t) = T k \omega A^2 \cos^2(kx - \omega t) = \mu v \omega^2 A^2 \cos^2(kx - \omega t) $$
La **potencia promedio temporal** (promedio del coseno cuadrado es $1/2$) transmitida es:
$$ \langle P \rangle = \frac{1}{2} \mu v \omega^2 A^2 $$
Esto demuestra el teorema de conservación para el transporte de energía: la tasa de energía transmitida es estrictamente proporcional a la densidad del medio, la velocidad de onda, y fundamentalmente, al cuadrado de la amplitud y la frecuencia angular del movimiento.

```mermaid
graph LR
    A(Equilibrio Estable) --> B(Fuerza Restauradora)
    B --> C(Expansión de Taylor Potencial U)
    C --> D[Ley de Hooke F = -kx]
    D --> E[Ecuación del MAS]
    E --> F{Medio Extendido}
    F --> |Acoplamiento| G[Ecuación de Onda]
    G --> H[Propagación Longitudinal v = √Y/ρ]
    G --> I[Propagación Transversal v = √T/μ]
    I --> J(Transporte de Potencia ~ A²ω²)
```

## 🛠 Ejemplo Práctico
**Problema:** Una cuerda de $ 2 \text{ m} $ de longitud y masa de $ 0.01 \text{ kg} $ está sometida a una tensión de $ 200 \text{ N} $. Se genera una onda armónica con una frecuencia de $ 50 \text{ Hz} $ y amplitud $ 0.05 \text{ m} $. Calcula la velocidad de la onda, la longitud de onda y la ecuación de la onda asumiendo que viaja en la dirección positiva de x y $ \phi = 0 $.

**Solución paso a paso:**
1. Densidad lineal de masa: $ \mu = \frac{m}{L} = \frac{0.01 \text{ kg}}{2 \text{ m}} = 0.005 \text{ kg/m} $.
2. Velocidad de la onda: $ v = \sqrt{\frac{T}{\mu}} = \sqrt{\frac{200}{0.005}} = \sqrt{40000} = 200 \text{ m/s} $.
3. Longitud de onda: $ v = \lambda f \implies \lambda = \frac{v}{f} = \frac{200 \text{ m/s}}{50 \text{ Hz}} = 4 \text{ m} $.
4. Parámetros angulares:
   - $ k = \frac{2\pi}{\lambda} = \frac{2\pi}{4} = \frac{\pi}{2} \text{ rad/m} $.
   - $ \omega = 2\pi f = 2\pi(50) = 100\pi \text{ rad/s} $.
5. Ecuación de la onda: $ y(x,t) = 0.05 \sin\left(\frac{\pi}{2} x - 100\pi t\right) \text{ m} $.

## 📚 Recursos Específicos
### Cursos
1. ["Vibrations and Waves" - MIT OpenCourseWare (Walter Lewin)](https://ocw.mit.edu/courses/8-03-physics-iii-vibrations-and-waves-fall-2004/)
2. ["Physics of Waves" - edX](https://www.edx.org/course/waves-and-optics)
3. ["Mechanical Waves" - Khan Academy](https://www.khanacademy.org/science/physics/mechanical-waves-and-sound)
4. ["Introduction to Oscillations and Waves" - Coursera](https://www.coursera.org/learn/physics-101)
5. ["Vibrations and Waves" - NPTEL (IIT Bombay)](https://nptel.ac.in/courses/115101011)

### Artículos y Simulaciones
1. ["Wave on a String" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/wave-on-a-string)
2. ["Masses and Springs" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/masses-and-springs)
3. ["Normal Modes" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/normal-modes)
4. ["Longitudinal vs Transverse Waves" - oPhysics](https://ophysics.com/w7.html)
5. ["Standing Waves Simulation" - oPhysics](https://ophysics.com/w8.html)
6. ["Beat Frequency" - oPhysics](https://ophysics.com/w10.html)
7. ["Resonance in a Tube" - oPhysics](https://ophysics.com/w9.html)
8. ["Wave Interference" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/wave-interference)
9. ["Simple Harmonic Motion" - oPhysics](https://ophysics.com/w1.html)

### 📖 Referencias Útiles y Bibliografía
1. [*Vibrations and Waves* por A.P. French](https://www.routledge.com/Vibrations-and-Waves/French/p/book/9780393099362)
2. [*Physics of Waves* por William C. Elmore y Mark A. Heald](https://store.doverpublications.com/products/9780486649269)
3. ["The Feynman Lectures on Physics, Vol. I"](https://www.feynmanlectures.caltech.edu/I_toc.html)
4. [*Fundamentals of Physics* por Halliday & Resnick](https://www.wiley.com/en-us/Fundamentals+of+Physics%2C+12th+Edition-p-9781119773511)
