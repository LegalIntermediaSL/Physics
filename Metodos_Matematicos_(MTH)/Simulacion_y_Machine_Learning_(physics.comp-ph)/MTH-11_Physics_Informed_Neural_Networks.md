# [MTH-11] Fundamentos de PINNs (Physics-Informed Neural Networks)

## 1. Machine Learning Físicamente Restringido
A diferencia del Deep Learning clásico basado enteramente en datos tabulares, las PINNs integran las Ecuaciones en Derivadas Parciales (EDPs) directamente en la función de pérdida (Loss Function) de la red neuronal.

## 2. La Función de Pérdida Híbrida
Para una EDP residual $\mathcal{R}(\mathbf{x}, t) = 0$, entrenamos una red $\hat{u}(\mathbf{x}, t; \theta)$. La función de pérdida penaliza tanto las desviaciones de los datos iniciales/frontera como el incumplimiento de la ley física:

$$
\mathcal{L}(\theta) = \omega_{data} \mathcal{L}_{data} + \omega_{fisica} \frac{1}{N} \sum_{i=1}^N \left| \mathcal{R}(\mathbf{x}_i, t_i; \theta) \right|^2
$$

Las derivadas parciales exactas (ej. espaciales y temporales de $\hat{u}$) se obtienen sin mallas, utilizando *Automatic Differentiation* (Autograd).
