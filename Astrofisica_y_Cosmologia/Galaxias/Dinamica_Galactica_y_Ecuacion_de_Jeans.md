# Dinámica Galáctica y la Ecuación de Jeans

Al estar constituidas por billones de estrellas, una galaxia puede modelarse como un fluido de partículas continuas donde, debido a las inmensas distancias, las colisiones directas estelares son virtualmente nulas.

## 1. La Ecuación Estática de Vlasov
En la estadística de un sistema galáctico libre de colisiones locales (dinámica no colisional), el término de interacción de colisión en la teoría del transporte se anula de forma precisa. 
La distribución estelar $f(\vec{r}, \vec{v}, t)$ en el espacio de fases evoluciona por tanto según la **Ecuación de Vlasov** (la ecuación de Boltzmann sin colisiones):

$$
\frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_r f - \nabla \Phi \cdot \nabla_v f = 0
$$

Donde $\Phi(\vec{r}, t)$ es el potencial gravitacional liso macroscópico generado por toda la masa colectiva de la galaxia y la materia oscura contenida.

## 2. Ecuación Hidrodinámica de Movimiento de Jeans
Al integrar los momentos cinemáticos de la ecuación de Vlasov, deducimos las ecuaciones fluidas efectivas de transporte de momento macroscópico de la galaxia. El resultado es el conjunto formal y analítico de las **Ecuaciones de Jeans**:

$$
\frac{\partial(\rho \langle v_i \rangle)}{\partial t} + \sum_j \frac{\partial(\rho \langle v_i v_j \rangle)}{\partial x_j} = -\rho \frac{\partial \Phi}{\partial x_i}
$$

Aquí, $\rho(\vec{r})$ es la densidad de masa espacial, y el término $\langle v_i v_j \rangle$ representa la dispersión isotrópica térmica del tensor de velocidades (similar a un tensor anisotrópico de presión estelar).
Aplicando suposiciones de simetría esférica (como en halos oscuros galácticos), podemos utilizar directamente el perfil de dispersión de velocidades para deducir inversamente y observar el pozo de potencial gravitacional subyacente de toda la masa no visible.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.286: The Early Universe (Alan Guth)](https://www.youtube.com/playlist?list=PLUl4u3cNGP61BjmEhhzEDqLq0B7k7Uon-) - Impartido por el propio creador de la Teoría Inflacionaria.
- [Stanford: Cosmology (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAvM2BvGzD9L9v_EwR04QzZl) - Métrica FLRW, Expansión Cósmica y Fondo de Microondas.
