# Termalización y la Ecuación de Fokker-Planck

## 1. El Retorno de las Colisiones (Régimen de Fusión)
Aunque el Vlasov sin colisiones domina fenómenos oscilatorios rápidos, para encender un reactor de fusión necesitamos calcular cómo un ión "bala" (partícula alfa generada en la reacción) se frena cediendo todo su calor al plasma de fondo más frío. Este es un proceso cinético irreversible dominado por las colisiones de ángulo pequeño causadas por las fuerzas eléctricas de largo alcance.

## 2. Derivación a través de Cadenas de Markov
A diferencia de un gas neutral denso (esferas duras descritas por la Integral de Colisión de Boltzmann discreta), las partículas en un plasma sienten sutiles atracciones y repulsiones electromagnéticas simultáneas de un millón de partículas a la vez dentro de la Esfera de Debye. Sus velocidades cambian de forma continua como un "Caminar Aleatorio" en el espacio de momento.

Al expandir en Taylor la probabilidad estocástica continua, obtenemos la Ecuación diferencial de Dispersión de **Fokker-Planck**:

$$
\frac{\partial f}{\partial t} = -\nabla_{\vec{v}} \cdot (\vec{A} f) + \frac{1}{2} \sum_{i,j} \frac{\partial^2}{\partial v_i \partial v_j} (D_{ij} f)
$$

## 3. Coeficientes de Fricción y Difusión
Físicamente, la evolución temporal de la temperatura o velocidad estocástica está dominada por dos tensores:
- El Vector Fricción Dinámica $\vec{A}$ (el arrastre térmico que ralentiza un haz inyectado).
- El Tensor de Difusión Velocimetral $D_{ij}$ (el ensanchamiento estocástico y esparcimiento).
Esta ecuación permite calcular tiempos de confinamiento críticos ($\tau_E$) y potencias de calentamiento NBI (*Neutral Beam Injection*) en ITER.
