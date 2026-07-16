# Solitones y Ecuación de Korteweg-de Vries

## 1. El Fenómeno del Solitón
Un solitón es un paquete de ondas solapadas (un pulso solitario) que mantiene su forma y velocidad constante a lo largo de propagación. Surge del equilibrio perfecto entre los efectos no lineales (que tienden a escarpar la ola) y la dispersión (que tiende a ensancharla). Tras una colisión entre dos solitones, ambos emergen inalterados, comportándose como partículas interactuantes.

## 2. Ecuación de Korteweg-de Vries (KdV)
Modeliza solitones de aguas poco profundas, plasmones iónicos y acústicos. Es una Ecuación en Derivadas Parciales no lineal e integrable:

$$
\frac{\partial u}{\partial t} + 6u \frac{\partial u}{\partial x} + \frac{\partial^3 u}{\partial x^3} = 0
$$

Donde:
- $6u \frac{\partial u}{\partial x}$ es el término convectivo no lineal (escarpamiento).
- $\frac{\partial^3 u}{\partial x^3}$ es el término dispersivo.

## 3. Solución Exacta del Solitón de 1 Polo
Buscamos una solución viajera de la forma $u(x,t) = f(x - ct)$ donde $c$ es la velocidad de fase. La solución es un solitón secante-hiperbólico:

$$
u(x,t) = \frac{c}{2} \text{sech}^2 \left( \frac{\sqrt{c}}{2} (x - ct - x_0) \right)
$$

¡La amplitud ($c/2$) es directamente proporcional a la velocidad ($c$) y el ancho inversamente proporcional! Los solitones más altos viajan más rápido y son más agudos.

## 4. Transformada de Dispersión Inversa (IST)
La ecuación KdV se resuelve exactamente formulando un problema de autovalores de Schrödinger donde $u(x,t)$ actúa como un potencial. La evolución topológica del solitón obedece los pares de Lax, garantizando infinitas cantidades conservadas.
