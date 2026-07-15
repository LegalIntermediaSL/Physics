# El Teorema de Noether y Leyes de Conservación

En 1915, Emmy Noether demostró el que es, posiblemente, el teorema más profundo de toda la física teórica: Toda simetría diferenciable continua de la Acción de un sistema físico tiene asociada una única ley de conservación estricta.

## 1. Demostración del Teorema de Noether
Consideremos una transformación infinitesimal continua paramétrizada por $\epsilon$:

$$
q_i \to q_i + \epsilon \delta q_i
$$

Si esta transformación es una simetría, la Lagrangiana debe ser invariante (salvo, como máximo, una derivada total respecto al tiempo de una función $F$). 
La variación total del Lagrangiano bajo el cambio es:

$$
\Delta L = \sum_i \left( \frac{\partial L}{\partial q_i} \delta q_i + \frac{\partial L}{\partial \dot{q}_i} \delta \dot{q}_i \right) = \frac{dF}{dt}
$$

Sustituyendo $\frac{\partial L}{\partial q_i}$ mediante las ecuaciones de movimiento de Euler-Lagrange:

$$
\sum_i \left( \left[\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i}\right] \delta q_i + \frac{\partial L}{\partial \dot{q}_i} \frac{d}{dt}(\delta q_i) \right) = \frac{dF}{dt}
$$

Aplicando la regla del producto, obtenemos:

$$
\frac{d}{dt} \left( \sum_i \frac{\partial L}{\partial \dot{q}_i} \delta q_i \right) = \frac{dF}{dt}
$$

Agrupando, derivamos matemáticamente la corriente o **Carga Conservada ($Q$)**:

$$
\frac{d}{dt} \left( \sum_i p_i \delta q_i - F \right) = 0 \implies Q = \sum_i p_i \delta q_i - F = \text{Constante}
$$

## 2. Consecuencias Fundamentales
Las leyes de conservación más importantes de la naturaleza no son empíricas, sino consecuencias de la geometría del espacio-tiempo:
- **Traslaciones Espaciales**: Si $L$ es invariante bajo el desplazamiento espacial, el momento lineal total se conserva ($\vec{P} = \text{cte}$).
- **Rotaciones Espaciales**: Si $L$ es invariante bajo una rotación angular, el momento angular total se conserva ($\vec{L} = \text{cte}$).
- **Traslaciones Temporales**: Si $L$ no depende explícitamente del tiempo ($\frac{\partial L}{\partial t} = 0$), el **Hamiltoniano ($H$)** (la Energía) se conserva.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Classical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL47F408D36D615022) - El Lagrangiano, Hamiltoniano y el Principio de Mínima Acción desmitificados.
- [MIT 8.01: Classical Mechanics (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e) - Física newtoniana icónica.
