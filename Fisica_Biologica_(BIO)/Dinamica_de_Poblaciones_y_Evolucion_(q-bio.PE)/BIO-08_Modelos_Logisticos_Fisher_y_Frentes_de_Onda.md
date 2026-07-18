# [BIO-08] Modelos Logísticos, Fisher y Frentes de Onda

## 1. Crecimiento con Recursos Limitados
El modelo logístico corrige el crecimiento exponencial incorporando saturación ambiental:

$$
\frac{dN}{dt} = rN\left(1-\frac{N}{K}\right)
$$

donde $r$ es la tasa intrínseca de crecimiento y $K$ la capacidad de carga. Este modelo aparece en ecología, epidemiología simple y dinámica de colonización.

## 2. Espacio y Difusión
Cuando la población se dispersa espacialmente, el paso natural es la ecuación de Fisher-KPP:

$$
\frac{\partial u}{\partial t}
=
D \nabla^2 u + ru(1-u)
$$

La difusión $D$ suaviza gradientes y el término reactivo reproduce competencia o reproducción local.

## 3. Frentes de Propagación
La ecuación admite ondas viajeras que describen invasiones biológicas, expansión de una mutación ventajosa o propagación de una especie invasora. La velocidad mínima del frente es

$$
c_{min} = 2\sqrt{Dr}
$$

lo que une dispersión microscópica y velocidad macroscópica de avance.

## 4. Generalizaciones
Versiones más realistas incluyen heterogeneidad espacial, ruido demográfico, Allee effect, competencia entre especies y acoplamiento con advección.

## 5. Valor Conceptual
Estos modelos son un puente excelente entre ecuaciones diferenciales, teoría de reacción-difusión y evolución darwiniana cuantitativa.
