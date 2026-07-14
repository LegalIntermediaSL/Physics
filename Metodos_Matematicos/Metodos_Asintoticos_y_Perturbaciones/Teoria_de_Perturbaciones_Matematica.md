# Teoría de Perturbaciones: Series Convergentes vs Asintóticas

En física teórica, solo podemos resolver exactamente un puñado vergonzosamente pequeño de problemas analíticos (el átomo de Hidrógeno, el Oscilador Armónico cuadrático libre, el campo libre). 
El momento en que los electrones interactúan entre sí, la ecuación diferencial de la naturaleza se rompe para nuestras matemáticas exactas. La solución universal a esto es la **Teoría de Perturbaciones**.

## 1. El Paradigma Perturbativo
Supón un operador (Hamiltoniano) $\hat{H} = \hat{H}_0 + \lambda \hat{V}$.
Donde $\hat{H}_0$ es el sistema ideal (con soluciones conocidas $\phi_n$), $\hat{V}$ es una pequeña interacción compleja, y $\lambda$ es un parámetro numérico infinitesimal muy pequeño que controla la fuerza de la interacción ($\lambda \ll 1$).

Buscamos las verdaderas energías $\mathcal{E}_n$ del sistema complejo como una Serie de Taylor abstracta en potencias infinitas de $\lambda$:

$$
\mathcal{E}_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \lambda^3 E_n^{(3)} + ...
$$

Calculamos los términos usando el formalismo de Rayleigh-Schrödinger, evaluando integrales de matriz.

## 2. El Horror de Dyson (Series Asintóticas)
En 1952, Freeman Dyson comprendió un hecho terrorífico sobre la Electrodinámica Cuántica (QED) y la física perturbativa general.

Esperaríamos que calculando infinitos diagramas de Feynman (infinitos términos $n$), llegaríamos al valor real exacto. Pero Dyson mostró que la serie matemática perturbativa fundamental de la física **no es convergente**, sino **Asintótica**. 
El factor numérico de combinaciones y multiplicidades que acompaña a los términos de orden alto crece como un factorial $n!$. En un momento dado (alcanzando el término $N \sim 137$ en QED), $\lambda^n n!$ empieza a dispararse al infinito absoluto.

Las matemáticas nos dictaminan que si calculas unos pocos términos mejoras astronómicamente la precisión. Pero si intentas calcular la "precisión absoluta" con diagramas teóricos infinitos, la matemática te escupirá infinito y la teoría explotará. (Esto ha obligado a la física moderna a crear técnicas potentes No-Perturbativas como Lattice QCD y D-Branas).
