# Derivación Tensorial de las Ecuaciones de Einstein

## 1. Componentes Geométricos
Para formular las leyes de la gravedad, Einstein necesitaba un tensor que resumiera la curvatura espacial y obedeciera la conservación de la energía.

- **Tensor de Ricci ($R_{\mu\nu}$):** Es la contracción del Tensor de Riemann. Mide cómo el volumen de un cúmulo de partículas geodesicas cambia mientras cae. $R_{\mu\nu} = R^\lambda_{\mu\lambda\nu}$
- **Escalar de Ricci ($R$):** Contracción del Tensor de Ricci ($R = g^{\mu\nu} R_{\mu\nu}$). Representa la curvatura escalar local (desviación de volumen respecto al espacio plano).

## 2. El Tensor de Einstein ($G_{\mu\nu}$)
Einstein estructuró un nuevo tensor que, por las *Identidades de Bianchi*, su derivada covariante (divergencia) es estrictamente cero ($\nabla^\mu G_{\mu\nu} = 0$).

$$
G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu}
$$

## 3. Las Ecuaciones de Campo
El Principio de Equivalencia establece que la masa/energía dobla el espacio-tiempo. El contenido material del universo es descrito por el **Tensor de Energía-Impulso $T_{\mu\nu}$**.
Al igualar la Geometría ($G_{\mu\nu}$) con la Materia ($T_{\mu\nu}$), obtenemos la obra maestra de Einstein:

$$
R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

Donde:
- $G$ es la constante de Newton.
- $c$ es la velocidad de la luz.
- $\Lambda$ es la Constante Cosmológica (Energía Oscura).

*John Wheeler lo resumió:* **"El espacio-tiempo le dice a la materia cómo moverse; la materia le dice al espacio-tiempo cómo curvarse."**
