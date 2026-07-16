# [FLD-02] Dinámica Ideal (Euler y Bernoulli)

Para analizar el movimiento, pasamos de la Hidrostática a la Dinámica. Históricamente, el primer gran avance fue asumir fluidos "Ideales" (Inviscidos o no viscosos). Aunque ignora la fricción, describe extraordinariamente bien el flujo lejos de las fronteras sólidas.

## 1. Descripciones de Lagrange vs Euler
- **Enfoque Lagrangiano**: Seguir a una partícula de fluido específica $\mathbf{r}(t)$ mientras se mueve por el espacio (como seguir un coche en una autopista).
- **Enfoque Euleriano**: Colocarse en un punto fijo del espacio $\mathbf{x}$ y observar el campo de velocidades del fluido $\mathbf{u}(\mathbf{x}, t)$ que pasa por ese punto (como mirar una cámara de tráfico). Este es el enfoque dominante en la física de fluidos.

## 2. La Derivada Material (Advectiva)
Dado que observamos un campo, la aceleración de una partícula de fluido requiere la "Derivada Material" o "Sustancial" $D/Dt$. Un cambio en una propiedad surge no solo porque cambie en el tiempo en un punto fijo ($\partial/\partial t$), sino porque la partícula ha sido *transportada* (advectada) a una nueva región:

$$
\frac{D\mathbf{u}}{Dt} = \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u}
$$

El término convectivo no-lineal $(\mathbf{u} \cdot \nabla)\mathbf{u}$ es el monstruo matemático que genera toda la complejidad (y el caos) de los fluidos.

## 3. Conservación de la Masa (Ecuación de Continuidad)
La materia no se crea ni se destruye. Matemáticamente, la divergencia del flujo de masa iguala la tasa de disminución de la densidad local:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0
$$

Para fluidos incompresibles ($\rho$ constante), esto se simplifica a la condición de divergencia nula: $\nabla \cdot \mathbf{u} = 0$.

## 4. La Ecuación de Euler (Conservación del Momento Ideal)
Aplicando $F = ma$ a un elemento de fluido ideal (sin fuerzas viscosas), usando la derivada material:

$$
\rho \left( \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} \right) = -\nabla p + \rho \mathbf{g}
$$

## 5. El Teorema de Bernoulli
Integrando la Ecuación de Euler a lo largo de una línea de corriente (para flujo estacionario, incompresible e invíscido), obtenemos una expresión de conservación de la energía mecánica total por unidad de volumen:

$$
\frac{1}{2} \rho v^2 + \rho g z + p = \text{constante}
$$

Esta mágica y sencilla ecuación es la que explica el efecto Venturi, el funcionamiento del tubo de Pitot en los aviones y, fundamentalmente, que donde el fluido se acelera, la presión debe caer trágicamente.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 2.006: Thermal-Fluids Engineering](https://ocw.mit.edu/courses/2-006-thermal-fluids-engineering-ii-spring-2004/).
  - [National Committee for Fluid Mechanics Films (NCFMF)](https://web.mit.edu/hml/ncfmf.html) - Serie histórica de vídeos del MIT (obligatorio para visualizar fluidos).
- **Libros de Texto Canónicos:**
  - *Fluid Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 6 del Curso de Física Teórica).
  - *An Introduction to Fluid Dynamics* - G.K. Batchelor.
  - *Turbulence: The Legacy of A.N. Kolmogorov* - Uriel Frisch.
