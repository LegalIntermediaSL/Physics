# Equilibrio Hidrostático y la Ecuación de Lane-Emden

Una estrella estable en la secuencia principal es el escenario de un equilibrio prolongado: la masa de la estrella trata de colapsar sobre su centro por gravedad, pero el gradiente de presión interno y la energía liberada por fusión termonuclear resisten el colapso.

## 1. Ecuaciones Básicas de Estructura Estelar
El equilibrio se describe asumiendo simetría esférica. La presión $P(r)$ requerida para soportar el peso de las capas externas en una cáscara radial $r$ es la **Ecuación de Equilibrio Hidrostático**:

$$
\frac{dP}{dr} = -\frac{G M(r) \rho(r)}{r^2}
$$

Junto con la Ecuación de Conservación de Masa:

$$
\frac{dM}{dr} = 4\pi r^2 \rho(r)
$$

## 2. Modelos Polítropos y la Ecuación de Lane-Emden
Para resolver este sistema, requerimos una ecuación de estado que relacione presión y densidad.
Para obtener modelos analíticos matemáticos, utilizamos un gas **polítropo**, donde la presión obedece directamente:

$$
P = K \rho^{1 + 1/n}
$$

Donde $K$ es la constante de proporcionalidad y $n$ es el **índice del polítropo**.

Introduciendo esta relación y realizando un cambio de variable no-dimensional a $\xi$ (radio rescalado) y $\theta$ (densidad adimensional, donde $\rho = \rho_c \theta^n$), las ecuaciones hidrostáticas se fusionan en una única ecuación diferencial no lineal de segundo orden, la **Ecuación de Lane-Emden**:

$$
\frac{1}{\xi^2} \frac{d}{d\xi} \left( \xi^2 \frac{d\theta}{d\xi} \right) = -\theta^n
$$

## 3. Resoluciones Analíticas de Lane-Emden
La ecuación debe integrarse desde el centro estelar $\theta(0) = 1$ y $\theta'(0) = 0$. Solo admite soluciones algebraicas cerradas explícitas para tres valores del índice $n$:
- **$n = 0$ (Fluido incompresible de densidad constante)**: $\theta(\xi) = 1 - \frac{\xi^2}{6}$.
- **$n = 1$**: $\theta(\xi) = \frac{\sin(\xi)}{\xi}$.
- **$n = 5$ (Radio extendido al infinito asintótico)**: $\theta(\xi) = \left( 1 + \frac{\xi^2}{3} \right)^{-1/2}$.

En Astrofísica, el modelo de una Enana Blanca masiva, compuesta por un gas de electrones degenerados relativistas, corresponde al caso físico del polítropo con $n = 3$.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.286: The Early Universe (Alan Guth)](https://www.youtube.com/playlist?list=PLUl4u3cNGP61BjmEhhzEDqLq0B7k7Uon-) - Impartido por el propio creador de la Teoría Inflacionaria.
- [Stanford: Cosmology (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAvM2BvGzD9L9v_EwR04QzZl) - Métrica FLRW, Expansión Cósmica y Fondo de Microondas.
