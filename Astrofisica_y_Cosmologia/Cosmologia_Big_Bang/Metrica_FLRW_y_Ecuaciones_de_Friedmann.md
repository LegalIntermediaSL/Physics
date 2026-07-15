# Métrica de FLRW y Ecuaciones de Friedmann

El Principio Cosmológico establece que, a escalas suficientemente grandes, el Universo es espacialmente homogéneo e isotrópico. Matemáticamente, esto restringe la forma que puede adoptar la métrica del espaciotiempo general relativista.

## 1. Métrica de Friedmann-Lemaître-Robertson-Walker (FLRW)
La única métrica que satisface matemáticamente homogeneidad e isotropía espaciales exactas en cuatro dimensiones es la métrica FLRW. Utilizando coordenadas comóviles $(t, r, \theta, \phi)$, se escribe como:

$$
ds^2 = -c^2 dt^2 + a^2(t) \left[ \frac{dr^2}{1 - kr^2} + r^2(d\theta^2 + \sin^2\theta \, d\phi^2) \right]
$$

Donde:
- $a(t)$ es el **factor de escala cósmico** dinámico, que describe la expansión relativa del espacio en función del tiempo cósmico $t$.
- $k$ es el **parámetro de curvatura espacial** ($+1$ cerrado esférico, $0$ plano euclidiano, $-1$ abierto hiperbólico).

## 2. Derivación de las Ecuaciones de Friedmann
Para deducir la evolución dinámica del universo $a(t)$, introducimos la métrica FLRW en las Ecuaciones de Campo de Einstein de la Relatividad General:

$$
R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

El Universo a gran escala se modela como un fluido perfecto estático respecto al marco comóvil. Su tensor de energía-momento es:

$$
T^\mu_\nu = \text{diag}(-\rho c^2, P, P, P)
$$

Donde $\rho(t)$ es la densidad de energía masiva total y $P(t)$ es la presión macroscópica.

Evaluando la componente temporal-temporal ($\mu=\nu=0$) de las ecuaciones de Einstein, obtenemos la **Primera Ecuación de Friedmann** (Ecuación de restricción de densidad):

$$
\left( \frac{\dot{a}}{a} \right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}
$$

El término $H = \dot{a}/a$ se define como el **Parámetro de Hubble**.

Evaluando la traza o combinando las componentes espaciales ($\mu=\nu=i$), obtenemos la **Segunda Ecuación de Friedmann** (Ecuación de aceleración):

$$
\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\left(\rho + \frac{3P}{c^2}\right) + \frac{\Lambda c^2}{3}
$$

## 3. Consecuencias Dinámicas
La Segunda Ecuación muestra un aspecto físico crucial de la Relatividad General frente a la gravedad newtoniana: la presión $P$ también contribuye activamente a la fuente gravitatoria atractiva.
Para que el universo acelere su expansión ($\ddot{a} > 0$) en ausencia de una constante cosmológica ($\Lambda = 0$), debe existir una materia con una ecuación de estado exótica $P = w\rho c^2$ tal que $w < -1/3$. Esto fundamenta la necesidad teórica de la **Energía Oscura**.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.286: The Early Universe (Alan Guth)](https://www.youtube.com/playlist?list=PLUl4u3cNGP61BjmEhhzEDqLq0B7k7Uon-) - Impartido por el propio creador de la Teoría Inflacionaria.
- [Stanford: Cosmology (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAvM2BvGzD9L9v_EwR04QzZl) - Métrica FLRW, Expansión Cósmica y Fondo de Microondas.
