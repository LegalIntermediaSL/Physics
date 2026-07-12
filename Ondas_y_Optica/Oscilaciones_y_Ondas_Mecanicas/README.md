# Oscilaciones y Ondas Mecánicas
Este apartado profundiza en los sistemas que presentan movimiento periódico y en cómo las perturbaciones se propagan a través de medios materiales, transportando energía sin transporte neto de materia.

## 📜 Contexto Histórico
El estudio del movimiento oscilatorio tiene raíces en las observaciones de Galileo Galilei sobre los péndulos en el siglo XVI. Christiaan Huygens posteriormente desarrolló el reloj de péndulo en 1656. La descripción matemática rigurosa de las ondas en cuerdas fue formulada por Jean le Rond d'Alembert en 1747, sentando las bases para la ecuación de onda clásica.

## 🧮 Desarrollo Teórico Profundo
El modelo más básico de oscilación es el Movimiento Armónico Simple (MAS), descrito por la ecuación diferencial:
$ \frac{d^2x}{dt^2} + \omega^2 x = 0 $
donde $ \omega = \sqrt{\frac{k}{m}} $ es la frecuencia angular natural.
La solución general es:
$ x(t) = A \cos(\omega t + \phi) $

Para ondas unidimensionales propagándose en un medio, la ecuación de onda de d'Alembert es:
$ \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} $
donde $ v = \sqrt{\frac{T}{\mu}} $ es la velocidad de la onda en una cuerda (con tensión $ T $ y densidad lineal de masa $ \mu $).

La solución para una onda armónica viajera es:
$ y(x,t) = A \sin(kx \pm \omega t) $
donde el número de onda es $ k = \frac{2\pi}{\lambda} $ y la frecuencia angular $ \omega = \frac{2\pi}{T} = 2\pi f $.

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
- **Cursos:** "Vibrations and Waves" (MIT OCW, Lewin), "Physics of Waves" (edX).
- **Artículos/Textos:** *Vibrations and Waves* (A.P. French), *Physics of Waves* (Elmore & Heald).
- **Simulaciones:** "Wave on a String" (PhET Interactive Simulations).
