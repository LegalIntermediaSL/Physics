# Dinámica de Fluidos

La dinámica de fluidos estudia cómo se mueven líquidos y gases bajo la acción de fuerzas, gradientes de presión y condiciones de contorno. Es esencial para describir el flujo sanguíneo, la atmósfera, la aerodinámica, las tuberías, la oceanografía y una enorme cantidad de sistemas naturales y tecnológicos.

## Conceptos Fundamentales

- **Campo de velocidad**: Cada punto del fluido tiene asociada una velocidad $\vec{v}(\vec{r},t)$.
- **Descripción euleriana**: Observa el flujo desde puntos fijos en el espacio.
- **Descripción lagrangiana**: Sigue el movimiento de partículas del fluido.
- **Caudal**: Cantidad de fluido que cruza una sección por unidad de tiempo.

## Ecuaciones Clave

- **Conservación de masa**:
  $\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0$
- **Fluido incompresible**:
  $\nabla \cdot \vec{v} = 0$
- **Bernoulli**:
  $p + \frac{1}{2}\rho v^2 + \rho g z = \text{cte}$
- **Balance de momento**:
  Base para llegar a las ecuaciones de Euler y Navier-Stokes.

## Temas Importantes

### 1. Flujo ideal vs viscoso
El modelo ideal es muy útil, pero los efectos viscosos suelen dominar cerca de superficies y en conductos.

### 2. Vorticidad
Permite entender rotación local, remolinos y circulación.

### 3. Números adimensionales
El número de Reynolds, entre otros, ayuda a comparar regímenes físicos muy distintos.
