# Formulación Hamiltoniana y el Espacio Fásico

Mientras que la mecánica lagrangiana opera en el "Espacio de Configuración" coordenado por $(q_i, \dot{q}_i)$, la formulación hamiltoniana abandona las velocidades a favor de los momentos, operando en el **Espacio Fásico** de $2N$ dimensiones coordinado estrictamente por posiciones y momentos conjugados $(q_i, p_i)$ tratados como variables independientes.

## 1. La Transformada de Legendre
Para cambiar la dependencia funcional del Lagrangiano $L(q, \dot{q}, t)$ a una nueva función que dependa de $p$, ejecutamos una Transformada de Legendre. 
Definimos la función **Hamiltoniana ($H$)**:

$$
H(q, p, t) = \sum_i p_i \dot{q}_i - L(q, \dot{q}, t)
$$

Tomando el diferencial total de esta definición matemática:

$$
dH = \sum_i (\dot{q}_i dp_i + p_i d\dot{q}_i) - dL
$$

Sabiendo que $dL = \sum_i \left(\frac{\partial L}{\partial q_i} dq_i + \frac{\partial L}{\partial \dot{q}_i} d\dot{q}_i\right) + \frac{\partial L}{\partial t} dt$ y usando las definiciones $p_i = \frac{\partial L}{\partial \dot{q}_i}$ y $\dot{p}_i = \frac{\partial L}{\partial q_i}$, obtenemos:

$$
dH = \sum_i (\dot{q}_i dp_i - \dot{p}_i dq_i) - \frac{\partial L}{\partial t} dt
$$

## 2. Las Ecuaciones Canónicas de Hamilton
Igualando el diferencial obtenido $dH$ con el diferencial natural de la función $H(q, p, t)$, obtenemos las **Ecuaciones Canónicas de Hamilton**, que reemplazan las $N$ ecuaciones de segundo orden de Lagrange por $2N$ ecuaciones diferenciales de primer orden:

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

Adicionalmente, se demuestra que $\frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}$. Si $H$ no depende explícitamente de $t$, su valor es una constante de movimiento (la Energía Total).

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Classical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL47F408D36D615022) - El Lagrangiano, Hamiltoniano y el Principio de Mínima Acción desmitificados.
- [MIT 8.01: Classical Mechanics (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e) - Física newtoniana icónica.
