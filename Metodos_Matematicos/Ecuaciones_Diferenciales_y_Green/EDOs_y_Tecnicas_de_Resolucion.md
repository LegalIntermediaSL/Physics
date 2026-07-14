# Ecuaciones Diferenciales Ordinarias (EDOs) y Funciones Especiales

En mecánica clásica y cuántica, a menudo reducimos la dinámica del sistema a una EDO lineal. Las técnicas para resolverlas originan toda la familia de "Funciones Especiales" de la física matemática.

## 1. El Método de Frobenius (Soluciones en Series)
Cuando los coeficientes de una EDO no son constantes, los métodos algebraicos fallan. Si la EDO tiene un "punto singular regular" en $x_0 = 0$, usamos el método de Frobenius.

Asumimos que la solución es una serie de potencias generalizada:

$$
y(x) = x^r \sum_{n=0}^{\infty} a_n x^n
$$

Al insertar esta serie en la EDO, obtenemos la **Ecuación Indicial** para determinar el exponente $r$, y una **Relación de Recurrencia** para hallar los coeficientes $a_{n+1}$ en función de $a_n$.

## 2. Funciones Especiales de la Física
El método de Frobenius, aplicado a las diferentes geometrías espaciales, produce soluciones tabuladas clásicas:

### A. Ecuación de Bessel (Simetría Cilíndrica)
Aparece al resolver membranas vibrantes circulares o guías de onda cilíndricas.

$$
x^2 y'' + x y' + (x^2 - \alpha^2) y = 0
$$

Soluciones: Funciones de Bessel de primera especie $J_\alpha(x)$ (que oscilan amortiguándose como ondas en un tambor) y de segunda especie $Y_\alpha(x)$ (que divergen en el origen).

### B. Ecuación de Legendre (Simetría Esférica)
Aparece al resolver potenciales gravitatorios o electrostáticos en coordenadas esféricas (independientes del ángulo azimutal).

$$
(1 - x^2) y'' - 2x y' + l(l+1) y = 0
$$

Soluciones: Polinomios de Legendre $P_l(x)$. Son ortogonales en el intervalo $[-1, 1]$ con función de peso $w(x)=1$. Conforman la parte angular de los orbitales atómicos $s, p, d$.

### C. Ecuación de Hermite (Oscilador Armónico Cuántico)

$$
y'' - 2x y' + 2n y = 0
$$

Soluciones: Polinomios de Hermite $H_n(x)$. Combinados con un decaimiento gaussiano $e^{-x^2/2}$, forman las funciones de onda ortogonales de un pozo de potencial cuadrático $V(x) = \frac{1}{2}kx^2$.
