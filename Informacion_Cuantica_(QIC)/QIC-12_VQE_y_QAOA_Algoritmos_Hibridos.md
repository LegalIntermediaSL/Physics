# [QIC-12] Variational Quantum Eigensolver (VQE) y QAOA

## 1. La Era NISQ (Noisy Intermediate-Scale Quantum)
Hasta que dispongamos de ordenadores cuánticos tolerantes a fallos (con millones de qubits de corrección de errores), nos encontramos en la era NISQ. Los dispositivos NISQ tienen docenas o cientos de qubits ruidosos. Los algoritmos como Shor son inviables debido al ruido.
Para aprovechar las máquinas NISQ, surgieron los **Algoritmos Cuántico-Clásicos Híbridos**.

## 2. VQE: Variational Quantum Eigensolver
El VQE se utiliza principalmente en química cuántica para encontrar la energía del estado fundamental de una molécula (el autovalor mínimo de su Hamiltoniano $H$).

Se basa en el principio variacional de la mecánica cuántica:
$$
\langle \psi(\theta) | H | \psi(\theta) \rangle \ge E_{min}
$$

El algoritmo funciona en un bucle cerrado:
1.  **Circuito Cuántico (Ansatz):** Un circuito parametrizado prepara un estado de prueba $|\psi(\theta)\rangle$, donde $\theta$ son ángulos de las puertas lógicas (ej. rotaciones RX).
2.  **Medición Cuántica:** Se mide el valor esperado de la energía $\langle H \rangle$ en el ordenador cuántico.
3.  **Optimizador Clásico:** Un ordenador clásico (con algoritmos como Gradiente Descendiente o COBYLA) toma el valor de energía y ajusta los parámetros $\theta$ para minimizarla.
4.  El bucle se repite hasta la convergencia.

## 3. QAOA: Quantum Approximate Optimization Algorithm
Similar al VQE, QAOA resuelve problemas de optimización combinatoria clásica (ej. Max-Cut en grafos).
Codifica el problema clásico en un Hamiltoniano de coste $H_C$. Alterna la aplicación de este Hamiltoniano con un Hamiltoniano de mezcla $H_M$:

$$
|\psi(\gamma, \beta)\rangle = e^{-i \beta_p H_M} e^{-i \gamma_p H_C} \dots e^{-i \beta_1 H_M} e^{-i \gamma_1 H_C} |+\rangle^{\otimes n}
$$

Un optimizador clásico busca los parámetros $\gamma$ y $\beta$ que maximicen el valor esperado de la solución óptima.
