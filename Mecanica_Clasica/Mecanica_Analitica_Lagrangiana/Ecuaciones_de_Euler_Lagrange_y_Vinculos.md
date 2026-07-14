# Ecuaciones de Euler-Lagrange y Multiplicadores

Aplicando el Cálculo de Variaciones al Principio de Hamilton ($\delta \mathcal{S} = 0$) e integrando por partes, llegamos a las ecuaciones maestras de la dinámica clásica.

## 1. Las Ecuaciones de Euler-Lagrange
Para cada coordenada generalizada $q_i$ y su velocidad generalizada $\dot{q}_i$, la trayectoria real del universo obedece ciegamente:

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

La magia monumental de estas ecuaciones es que son **invariantes de forma**. No importa si usas coordenadas esféricas, cilíndricas, ángulos de péndulos, o coordenadas en una variedad curva tetradimensional: la ecuación luce exactamente igual, algo que NO es cierto para $F=ma$, donde en coordenadas esféricas aparecen horribles términos de fuerzas ficticias (Coriolis, centrífugas) que en Lagrange salen automáticamente y gratis.

## 2. Momento Conjugado y Fuerzas Generalizadas
El término $p_i = \frac{\partial L}{\partial \dot{q}_i}$ se denomina **Momento Conjugado** (o canónico). Si $q$ es una posición lineal $x$, el momento conjugado es la cantidad de movimiento $mv$. Pero si $q$ es un ángulo $\theta$, su momento conjugado es el Momento Angular ($L = I\omega$).
El término $F_i = \frac{\partial L}{\partial q_i}$ se denomina **Fuerza Generalizada**.

Por tanto, Euler-Lagrange simplemente dicta: $\frac{d p_i}{dt} = F_i$. (El cambio del momento canónico es la fuerza generalizada).

## 3. Vínculos Holónomos y Multiplicadores de Lagrange
En la vida real, los cuerpos no se mueven libremente. Un tren debe ir por la vía; un péndulo no puede estirar su hilo. Estos son **vínculos holónomos**, representados por ecuaciones algebraicas $f_k(q_1, ... q_n, t) = 0$.

Para incluir vínculos sin necesidad de rompernos la cabeza calculando las fuerzas de tensión a mano, introducimos los **Multiplicadores de Lagrange** ($\lambda_k$):

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = \sum_{k} \lambda_k \frac{\partial f_k}{\partial q_i}
$$

El término de la derecha escupe directamente las "fuerzas de restricción" (ej. la tensión de la cuerda o la fuerza normal del suelo) necesarias para mantener a la partícula atada al vínculo geométrico, ¡y todo sin dibujar ni un solo diagrama vectorial de cuerpo libre!
