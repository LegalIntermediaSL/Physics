# Superconductividad

La superconductividad es un estado cuántico macroscópico de la materia que ocurre en ciertos materiales a muy bajas temperaturas. Se caracteriza por dos fenómenos fundamentales: una resistencia eléctrica exactamente igual a cero y la expulsión del campo magnético de su interior (Efecto Meissner).

## 📜 Contexto Histórico

La superconductividad fue descubierta en 1911 por Heike Kamerlingh Onnes en Leiden al observar que la resistencia del mercurio sólido caía abruptamente a cero al enfriarse a 4.2 K mediante helio líquido. En 1933, Walther Meissner y Robert Ochsenfeld descubrieron el diamagnetismo perfecto en los superconductores. El gran avance teórico se dio en 1957 con la teoría BCS (Bardeen, Cooper y Schrieffer), la cual demostró que los electrones interactuando a través de la red (fonones) pueden formar "pares de Cooper" y condensarse en un estado base colectivo. En 1986, Bednorz y Müller descubrieron los superconductores de alta temperatura (cupratos), un enigma teórico que aún no tiene una explicación completa.

## 🧮 Desarrollo Teórico Profundo

La **Teoría Ginzburg-Landau** (1950) es un enfoque fenomenológico usando un parámetro de orden complejo $\psi(\mathbf{r})$ donde $|\psi|^2$ representa la densidad de pares superconductores. La energía libre cerca de la temperatura crítica $T_c$ se expande como:
$ F = F_n + \alpha |\psi|^2 + \frac{\beta}{2} |\psi|^4 + \frac{1}{2m^*} \left| \left( -i\hbar\nabla - \frac{e^*}{c}\mathbf{A} \right) \psi \right|^2 + \frac{|\mathbf{B}|^2}{2\mu_0} $
Minimizar esta energía libre respecto a $\psi$ y $\mathbf{A}$ lleva a las dos ecuaciones de Ginzburg-Landau, que explican la longitud de coherencia $\xi$ y la longitud de penetración $\lambda$, dando origen a superconductores Tipo I y Tipo II.

A nivel microscópico, la **Teoría BCS** propone que existe una atracción débil entre electrones en la superficie de Fermi, mediada por el intercambio de fonones. El estado de pares de Cooper $(+\mathbf{k}\uparrow, -\mathbf{k}\downarrow)$ tiene una energía menor que el gas de Fermi. La brecha de energía de excitación $\Delta$ depende de la temperatura y cerca de $T=0$ resulta en:
$ \Delta(0) \approx 1.76 k_B T_c $
El Hamiltoniano reducido de BCS se puede resolver mediante las transformaciones de Bogoliubov para obtener los cuasipárticulas de excitación.

## 🛠 Ejemplo Práctico

**Problema:** Deducir el Efecto Meissner usando la ecuación de London.

**Solución paso a paso:**
1. Fritz y Heinz London propusieron (en 1935) una ecuación fenomenológica para la densidad de supercorriente $\mathbf{J}_s$:
   $ \nabla \times \mathbf{J}_s = - \frac{n_s e^2}{m} \mathbf{B} $
   donde $n_s$ es la densidad de electrones superconductores.
2. Usamos la ley de Ampère de Maxwell en el caso estático ($\nabla \times \mathbf{B} = \mu_0 \mathbf{J}_s$).
3. Aplicamos el rotor a ambos lados de la ley de Ampère:
   $ \nabla \times (\nabla \times \mathbf{B}) = \mu_0 (\nabla \times \mathbf{J}_s) $
4. Usamos la identidad vectorial $\nabla \times (\nabla \times \mathbf{B}) = \nabla(\nabla \cdot \mathbf{B}) - \nabla^2 \mathbf{B}$. Dado que por la ley de Gauss para el magnetismo $\nabla \cdot \mathbf{B} = 0$:
   $ - \nabla^2 \mathbf{B} = \mu_0 \left( - \frac{n_s e^2}{m} \mathbf{B} \right) $
5. Reagrupando términos obtenemos:
   $ \nabla^2 \mathbf{B} = \frac{1}{\lambda_L^2} \mathbf{B} \quad \text{donde} \quad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}} $
6. En una geometría 1D donde la superficie del superconductor está en $x=0$ y ocupa $x>0$, la solución a esta ecuación diferencial (con la condición $\mathbf{B} \to 0$ en el infinito) es:
   $ \mathbf{B}(x) = \mathbf{B}(0) e^{-x/\lambda_L} $
**Conclusión:** El campo magnético decae exponencialmente en el interior del superconductor en una escala de longitud $\lambda_L$ (longitud de penetración de London). Esto demuestra que el campo magnético no puede penetrar en volumen al material, explicando el **Efecto Meissner**.

## 📚 Recursos Específicos
- **Cursos:** Introducción a la Superconductividad (Coursera), Solid State Physics 2 (MIT OCW).
- **Artículos/Simulaciones:** *Introduction to Superconductivity* por Michael Tinkham; *Theory of Superconductivity* (Schrieffer). Documentales sobre la levitación magnética y el tren Maglev.
