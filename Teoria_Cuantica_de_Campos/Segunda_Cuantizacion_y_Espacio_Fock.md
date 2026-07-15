# Segunda Cuantización y el Espacio de Fock

La mecánica cuántica ordinaria ("primera cuantización") trata la posición y el momento de un número *fijo* de partículas como operadores. Sin embargo, en procesos relativistas donde la energía puede convertirse en masa ($E=mc^2$), el número de partículas no se conserva (se crean y se aniquilan fotones, pares electrón-positrón, etc.).

## 1. El Campo como Entidad Fundamental
Para resolver esto, la QFT cuantiza el *campo* mismo ("segunda cuantización"). Si tomamos el campo electromagnético clásico o la función de onda de Schrödinger/Klein-Gordon y los promovemos a operadores, obtenemos un **Campo Cuántico**.

El campo cuántico $\hat{\phi}(x)$ puede expresarse como una expansión de Fourier en términos de operadores de creación y aniquilación cuánticos de osciladores armónicos:

$$
\hat{\phi}(x) = \int \frac{d^3p}{(2\pi)^3 \sqrt{2E_p}} \left( \hat{a}_p e^{-ip \cdot x} + \hat{a}^\dagger_p e^{ip \cdot x} \right)
$$

## 2. Operadores de Creación y Aniquilación
- $\hat{a}^\dagger_p$: Es el **operador de creación**. Al actuar sobre el estado de vacío $|0\rangle$, "crea" una partícula (un cuanto del campo) con momento exacto $p$.
- $\hat{a}_p$: Es el **operador de aniquilación**. "Destruye" una partícula de momento $p$. Si actúa sobre el vacío, el resultado es nulo ($\hat{a}_p |0\rangle = 0$).

## 3. El Espacio de Fock
Puesto que en QFT podemos tener cualquier cantidad arbitraria de partículas $N$, el espacio de Hilbert estándar es insuficiente. Necesitamos el **Espacio de Fock** ($\mathcal{F}$), que es la suma directa de los espacios de Hilbert para $0, 1, 2, ...$ partículas:

$$
\mathcal{F} = \bigoplus_{n=0}^{\infty} \mathcal{H}^{\otimes n}
$$

El estado de $n$ partículas con momentos $p_1, ..., p_n$ se genera simplemente aplicando el operador de creación repetidas veces sobre el vacío:

$$
|p_1, p_2, ..., p_n\rangle = \hat{a}^\dagger_{p_1} \hat{a}^\dagger_{p_2} ... \hat{a}^\dagger_{p_n} |0\rangle
$$

