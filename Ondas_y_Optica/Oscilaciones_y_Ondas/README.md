# Oscilaciones y Ondas

Las oscilaciones describen sistemas que evolucionan alrededor de un equilibrio estable. Cuando ese comportamiento se transmite en el espacio, aparecen las ondas: perturbaciones que transportan energía e información sin transportar materia de manera neta.

## 🧮 Desarrollo Teórico Profundo

El estudio de las oscilaciones y ondas constituye uno de los pilares de la física teórica y aplicada. Comienza con el análisis dinámico de sistemas perturbados alrededor de un equilibrio estable y se extiende a la propagación de esta energía en medios continuos.

### 1. El Oscilador Armónico Simple, Amortiguado y Forzado

Un sistema de masa $m$ sujeto a una fuerza restauradora lineal (Ley de Hooke) $F = -kx$ obedece la ecuación diferencial:
$$ m \frac{d^2 x}{dt^2} + kx = 0 $$
Definiendo la frecuencia angular natural $\omega_0 = \sqrt{k/m}$, la solución general es $x(t) = A \cos(\omega_0 t + \phi)$. 

**Oscilador Amortiguado:** Si consideramos una fuerza disipativa proporcional a la velocidad, $F_d = -b v$, la ecuación se convierte en:
$$ m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + kx = 0 \implies \frac{d^2 x}{dt^2} + 2\gamma \frac{dx}{dt} + \omega_0^2 x = 0 $$
donde $\gamma = b/2m$. En el caso subamortiguado ($\gamma < \omega_0$), la solución es:
$$ x(t) = A e^{-\gamma t} \cos(\omega_d t + \phi) \quad \text{con} \quad \omega_d = \sqrt{\omega_0^2 - \gamma^2} $$
La amplitud decrece exponencialmente, perdiendo energía cinética y potencial en forma de calor.

**Oscilador Forzado y Resonancia:** Al aplicar una fuerza armónica externa $F_{ext}(t) = F_0 \cos(\omega t)$, el estado estacionario adopta la frecuencia de la fuerza externa:
$$ x(t) = A(\omega) \cos(\omega t - \delta) $$
donde la amplitud $A(\omega)$ tiene un máximo absoluto (resonancia) cuando $\omega \approx \omega_0$:
$$ A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\gamma\omega)^2}} $$

### 2. La Ecuación de Onda Clásica

Cuando conectamos una infinidad de osciladores acoplados, pasamos del dominio discreto al continuo. Consideremos una cuerda bajo tensión $T$ y con densidad lineal de masa $\mu$. Aplicando la Segunda Ley de Newton a un segmento infinitesimal $dx$, y asumiendo ángulos pequeños $\theta \approx \partial y/\partial x$, la componente vertical de la fuerza neta es:
$$ dF_y = T \left( \frac{\partial y}{\partial x}\Big|_{x+dx} - \frac{\partial y}{\partial x}\Big|_{x} \right) \approx T \frac{\partial^2 y}{\partial x^2} dx $$
Igualando esto a la masa $(\mu dx)$ por la aceleración $(\partial^2 y/\partial t^2)$, obtenemos la **Ecuación de Onda de d'Alembert**:
$$ \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} $$
donde la velocidad de propagación es $v = \sqrt{T/\mu}$. 

### 3. Soluciones de la Ecuación de Onda

La solución de d'Alembert demuestra que cualquier función dos veces diferenciable de la forma $y(x,t) = f(x - vt) + g(x + vt)$ satisface la ecuación de onda.
Para ondas armónicas, usamos el método de separación de variables $y(x,t) = X(x)T(t)$, que nos lleva a:
$$ y(x,t) = A \cos(kx \pm \omega t + \phi) $$
donde el número de onda $k = 2\pi/\lambda$ y $\omega = 2\pi/T = 2\pi f$. La velocidad de fase está dada por la relación de dispersión $v_p = \omega / k$.

### 4. Interferencia y Ondas Estacionarias

Si una onda viajera incidente $y_1 = A \sin(kx - \omega t)$ se refleja en un extremo fijo, produce una onda reflejada $y_2 = A \sin(kx + \omega t)$. La superposición $y = y_1 + y_2$ resulta en una **onda estacionaria**:
$$ y(x,t) = [2A \sin(kx)] \cos(\omega t) $$
El término espacial $\sin(kx)$ obliga a la cuerda a tener nodos inmóviles en los puntos $x = n\pi/k = n\lambda/2$. Si la cuerda está fija en sus dos extremos (longitud $L$), se imponen las condiciones de frontera de Dirichlet $y(0,t)=y(L,t)=0$. Esto restringe las longitudes de onda permitidas (cuantización):
$$ \lambda_n = \frac{2L}{n} \implies f_n = \frac{nv}{2L} = n f_1 $$
Estos $f_n$ representan los modos normales de vibración o armónicos del sistema.

```mermaid
graph TD
    Oscilador[Oscilador Armónico Simple] --> Acoplamiento[Osciladores Acoplados]
    Acoplamiento --> Continuo[Medio Continuo Múltiples Grados Libertad]
    Continuo --> Ecuacion[Ecuación Diferencial de Onda]
    Ecuacion --> Viajeras[Ondas Viajeras: Energía se propaga]
    Ecuacion --> Estacionarias[Ondas Estacionarias: Interferencia Espacial]
    Viajeras --> Dispersion[Dispersión y Velocidad de Grupo]
    Estacionarias --> ModosNormales[Modos Normales y Cuantización]
```

## Aplicaciones

- Cuerdas vibrantes e instrumentos musicales.
- Circuitos eléctricos oscilantes.
- Sismología y ondas en sólidos.
- Ondas electromagnéticas y cuánticas.

## 📝 Guía de Ejercicios Resueltos

**Problema 1: Oscilador Armónico Amortiguado No Lineal**
Un oscilador de masa $m$ y constante elástica $k$ está sujeto a una fuerza de amortiguamiento $F_v = -c v^2 \text{sgn}(v)$. Plantee la ecuación de movimiento diferencial y resuelva la pérdida de energía mecánica por ciclo asumiendo baja disipación.

**Solución paso a paso:**
1. La ecuación de movimiento es $m\ddot{x} + c\dot{x}^2\text{sgn}(\dot{x}) + kx = 0$.
2. Para baja disipación, asumimos una solución aproximada de un ciclo: $x(t) = A \cos(\omega t)$ con $\omega = \sqrt{k/m}$.
3. La velocidad es $v(t) = -A\omega \sin(\omega t)$.
4. El trabajo realizado por la fuerza disipativa en un ciclo es $\Delta E = \int_0^T F_v v \, dt$.
5. Sustituyendo: $F_v v = (-c v^2 \text{sgn}(v)) v = -c |v|^3 = -c A^3 \omega^3 |\sin(\omega t)|^3$.
6. $\Delta E = -c A^3 \omega^3 \int_0^{2\pi/\omega} |\sin(\omega t)|^3 \, dt$.
7. Haciendo $\theta = \omega t$, $dt = d\theta/\omega$: $\Delta E = -c A^3 \omega^2 \int_0^{2\pi} |\sin \theta|^3 \, d\theta$.
8. $\int_0^{2\pi} |\sin \theta|^3 \, d\theta = 4 \int_0^{\pi/2} \sin^3 \theta \, d\theta = 4 \left( \frac{2}{3} \right) = \frac{8}{3}$.
9. Entonces, $\Delta E = -\frac{8}{3} c A^3 \omega^2 = -\frac{8}{3} \frac{ck}{m} A^3$. La pérdida de energía por ciclo es proporcional al cubo de la amplitud.

**Problema 2: Ecuación de Onda en Cuerda con Masa Variable**
Una cuerda de longitud $L$ cuelga verticalmente desde un soporte en $z = L$. La masa por unidad de longitud es constante $\mu$. Encuentre el tiempo que tarda un pulso transversal en viajar desde $z = 0$ (extremo inferior libre) hasta $z = L$.

**Solución paso a paso:**
1. La tensión en la cuerda a una altura $z$ se debe al peso de la porción debajo de $z$: $T(z) = \mu g z$.
2. La velocidad de propagación de la onda transversal localmente es $v(z) = \sqrt{\frac{T(z)}{\mu}} = \sqrt{\frac{\mu g z}{\mu}} = \sqrt{gz}$.
3. El tiempo de propagación es $t = \int_0^L \frac{dz}{v(z)} = \int_0^L \frac{dz}{\sqrt{gz}}$.
4. Evaluamos la integral: $t = \frac{1}{\sqrt{g}} \int_0^L z^{-1/2} \, dz = \frac{1}{\sqrt{g}} \left[ 2z^{1/2} \right]_0^L = 2\sqrt{\frac{L}{g}}$.
5. Curiosamente, este tiempo es el mismo que el período de oscilación de un péndulo de longitud $L$ o el doble del tiempo de caída libre desde una altura $L$.

**Problema 3: Osciladores Acoplados**
Dos masas idénticas $m$ están conectadas entre sí y a paredes rígidas mediante tres resortes idénticos de constante $k$. Determine las frecuencias normales del sistema (modos normales).

**Solución paso a paso:**
1. Sean $x_1$ y $x_2$ los desplazamientos desde el equilibrio. Ecuaciones:
   $m\ddot{x}_1 = -k x_1 + k(x_2 - x_1)$
   $m\ddot{x}_2 = -k x_2 - k(x_2 - x_1)$
2. Reordenando matricialmente: $m \begin{pmatrix} \ddot{x}_1 \\ \ddot{x}_2 \end{pmatrix} = \begin{pmatrix} -2k & k \\ k & -2k \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$.
3. Buscamos soluciones oscilatorias $x_j(t) = A_j e^{i\omega t}$, lo que da el problema de autovalores:
   $\det \begin{pmatrix} -2k + m\omega^2 & k \\ k & -2k + m\omega^2 \end{pmatrix} = 0$.
4. $(-2k + m\omega^2)^2 - k^2 = 0 \implies m\omega^2 - 2k = \pm k$.
5. Las frecuencias son $m\omega_1^2 = 2k - k = k \implies \omega_1 = \sqrt{k/m}$ (modo simétrico).
6. $m\omega_2^2 = 2k + k = 3k \implies \omega_2 = \sqrt{3k/m}$ (modo antisimétrico).

## 💻 Simulaciones Computacionales

A continuación, se presenta un script en Python que simula la dinámica de dos osciladores armónicos acoplados débilmente. Se utiliza `scipy.integrate.solve_ivp` para resolver el sistema de ecuaciones diferenciales, permitiendo observar cómo la energía se transfiere periódicamente entre ambas masas, generando un patrón de batido (modos normales mezclados).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def simular_osciladores_acoplados():
    """
    Simula el movimiento de dos masas acopladas por resortes utilizando
    integración numérica, mostrando la transferencia de energía (batido).
    """
    # Parámetros del sistema
    m1, m2 = 1.0, 1.0    # Masas (kg)
    k1, k3 = 20.0, 20.0  # Resortes extremos (N/m)
    k2 = 1.0             # Resorte de acoplamiento central débil (N/m)
    
    # Definición del sistema de EDOs (Ecuaciones Diferenciales Ordinarias)
    # y = [x1, v1, x2, v2]
    def sistema(t, y):
        x1, v1, x2, v2 = y
        
        # Ecuaciones de movimiento (Segunda Ley de Newton)
        dx1_dt = v1
        dv1_dt = (-k1 * x1 + k2 * (x2 - x1)) / m1
        
        dx2_dt = v2
        dv2_dt = (-k3 * x2 - k2 * (x2 - x1)) / m2
        
        return [dx1_dt, dv1_dt, dx2_dt, dv2_dt]

    # Condiciones iniciales: Masa 1 desplazada, Masa 2 en reposo
    # Esto excitará una superposición de los modos simétrico y antisimétrico
    y0 = [1.0, 0.0, 0.0, 0.0]
    
    # Intervalo de tiempo
    t_span = (0, 30)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)
    
    # Resolución numérica
    sol = solve_ivp(sistema, t_span, y0, t_eval=t_eval, method='RK45')
    
    t = sol.t
    x1 = sol.y[0]
    x2 = sol.y[2]
    
    # Energías cinéticas (para ilustrar la transferencia de energía)
    E1 = 0.5 * m1 * sol.y[1]**2 + 0.5 * k1 * x1**2 + 0.25 * k2 * (x1 - x2)**2
    E2 = 0.5 * m2 * sol.y[3]**2 + 0.5 * k3 * x2**2 + 0.25 * k2 * (x1 - x2)**2
    # El término del resorte central se divide para visualizar aproximada/ la energía "perteneciente" a cada masa
    
    # Visualización
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfica de posiciones
    ax1.plot(t, x1, label='Posición Masa 1 (x1)', color='b', linewidth=2)
    ax1.plot(t, x2, label='Posición Masa 2 (x2)', color='r', linewidth=2, alpha=0.8)
    ax1.set_title('Desplazamiento de Masas Acopladas (Efecto Batido)')
    ax1.set_ylabel('Posición (m)')
    ax1.grid(True)
    ax1.legend(loc='upper right')
    
    # Gráfica de energías
    ax1_e = ax2.plot(t, E1, label='Energía Aprox. Masa 1', color='b', alpha=0.7)
    ax2_e = ax2.plot(t, E2, label='Energía Aprox. Masa 2', color='r', alpha=0.7)
    ax2.plot(t, E1 + E2, 'k--', label='Energía Total Conservada')
    ax2.set_title('Transferencia de Energía Mecánica')
    ax2.set_xlabel('Tiempo (s)')
    ax2.set_ylabel('Energía (J)')
    ax2.grid(True)
    ax2.legend(loc='center right')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    simular_osciladores_acoplados()
```

## 📚 Recursos
### Cursos
1. ["Vibrations and Waves" - MIT OpenCourseWare (Walter Lewin)](https://ocw.mit.edu/courses/8-03-physics-iii-vibrations-and-waves-fall-2004/)
2. ["Waves and Optics" - edX (Rice University)](https://www.edx.org/course/waves-and-optics)
3. ["Oscillations and Waves" - Khan Academy](https://www.khanacademy.org/science/physics/mechanical-waves-and-sound)
4. ["Vibrations and Waves" - NPTEL (IIT Bombay)](https://nptel.ac.in/courses/115101011)
5. ["Physics 101: Simple Harmonic Motion" - Coursera](https://www.coursera.org/learn/physics-101)

### Artículos y Simulaciones
1. ["Masses and Springs" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/masses-and-springs)
2. ["Wave on a String" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/wave-on-a-string)
3. ["Pendulum Lab" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/pendulum-lab)
4. ["Coupled Oscillators Simulation" - oPhysics](https://ophysics.com/w2.html)
5. ["Resonance Simulator" - PhET](https://phet.colorado.edu/en/simulations/resonance)
6. ["Harmonic Motion and Circular Motion" - oPhysics](https://ophysics.com/k6.html)
7. ["Lissajous Figures Simulation" - oPhysics](https://ophysics.com/w3.html)
8. ["Standing Waves on a String" - oPhysics](https://ophysics.com/w8.html)
9. ["Fourier: Making Waves" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/fourier-making-waves)

### 📖 Referencias Útiles y Bibliografía
1. [*Vibrations and Waves* por A.P. French](https://www.routledge.com/Vibrations-and-Waves/French/p/book/9780393099362)
2. [*Physics of Waves* por William C. Elmore y Mark A. Heald](https://store.doverpublications.com/products/9780486649269)
3. ["The Feynman Lectures on Physics, Vol. I" (Capítulos 21-31)](https://www.feynmanlectures.caltech.edu/I_toc.html)
4. [*Vibrations and Waves in Physics* por Iain G. Main](https://www.cambridge.org/core/books/vibrations-and-waves-in-physics/B1E1E6B9E93C3852DF39634B0B9D65E1)
