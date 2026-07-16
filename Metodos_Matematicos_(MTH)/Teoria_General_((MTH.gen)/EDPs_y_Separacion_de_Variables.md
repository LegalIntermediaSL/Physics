# Ecuaciones en Derivadas Parciales (EDPs)

El universo macroscópico está gobernado por tres EDPs fundamentales de segundo orden, clasificadas según su discriminante $B^2 - 4AC$ (como las cónicas geométricas):

## 1. Clasificación de las EDPs de la Física

### A. Ecuación de Laplace / Poisson (Elíptica)

$$
\nabla^2 \Phi = -\frac{\rho}{\epsilon_0}
$$

Describe campos estáticos (Electrostática, Gravedad Newtoniana, Termostática). El potencial en una región sin cargas ($\rho=0$) no tiene máximos ni mínimos locales (Teorema de Gauss).

### B. Ecuación de Difusión o Calor (Parabólica)

$$
\alpha \nabla^2 T = \frac{\partial T}{\partial t}
$$

Describe procesos irreversibles que rompen la simetría temporal (aumento de entropía). Las distribuciones de calor se difuminan exponencialmente con el tiempo. La Ecuación de Schrödinger es, matemáticamente, una ecuación de difusión en "tiempo imaginario" ($t \to \tau = it$).

### C. Ecuación de Onda (Hiperbólica)

$$
c^2 \nabla^2 \Psi = \frac{\partial^2 \Psi}{\partial t^2}
$$

Describe procesos dinámicos con simetría temporal (reversible) que se propagan a una velocidad finita $c$. (Fotones, sonido, ondas gravitacionales).

## 2. Método de Separación de Variables
La técnica maestra para resolver EDPs lineales en geometrías simétricas (cajas, cilindros, esferas) es la Separación de Variables.

Postulamos que la función multidimensional se puede factorizar en un producto de funciones de una sola variable. Para la Ecuación de Schrödinger en 3D (esférica) $\Psi(r, \theta, \phi)$:

$$
\Psi(r, \theta, \phi) = R(r) \Theta(\theta) \Phi(\phi)
$$

Al sustituir en la EDP y dividir por la función total, cada término dependerá exclusivamente de una variable independiente. Puesto que las variables pueden variar libremente pero la suma es constante, **cada término debe ser igual a una constante de separación**.

Esto convierte la terrorífica EDP 3D en **3 EDOs separadas**.

## 3. Armónicos Esféricos ($Y_l^m$)
Al separar la parte angular $(\theta, \phi)$ en coordenadas esféricas, obtenemos las soluciones armónicas sobre la superficie de una esfera.

$$
Y_l^m(\theta, \phi) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!}} P_l^m(\cos \theta) e^{im\phi}
$$

Donde $P_l^m$ son los polinomios asociados de Legendre. Los armónicos esféricos son los autovectores del operador del Momento Angular Cuántico ($L^2$ y $L_z$). Son los "ladrillos de construcción" visuales de todos los orbitales atómicos del universo y del fondo cósmico de microondas (CMB).

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Carl Bender: Mathematical Physics (Washington University)](https://www.youtube.com/playlist?list=PL1B1123DDB9DD4668) - Brillantes clases de perturbaciones, asintóticos y WKB impartidas por un genio del análisis.
- [ICTP: Mathematics for Physicists](https://www.youtube.com/user/ictp) - Herramientas analíticas puras desde Trieste.
