# [QIC-09] Matemática del Algoritmo de Shor (Factorización)

## 1. El Problema de Factorización
El algoritmo de Shor, propuesto por Peter Shor en 1994, resuelve el problema de factorización de enteros en tiempo polinómico $O((\log N)^3)$, destrozando los esquemas de criptografía RSA que dependen de que la factorización clásica sea exponencialmente dura.

El algoritmo reduce el problema de factorizar $N$ al problema de encontrar el **período** (u orden) de una función.

## 2. Reducción a la Búsqueda de Período
1. Elige un número aleatorio $a < N$ tal que el máximo común divisor $\text{mcd}(a, N) = 1$.
2. Define la función modular $f(x) = a^x \pmod N$.
3. Esta función es periódica. Existe un entero $r$ (el período) tal que $f(x+r) = f(x)$, o lo que es lo mismo, $a^r \equiv 1 \pmod N$.
4. Si $r$ es par y $a^{r/2} \not\equiv -1 \pmod N$, entonces los factores de $N$ se pueden encontrar calculando $\text{mcd}(a^{r/2} \pm 1, N)$.

## 3. La Subrutina Cuántica (Quantum Period Finding)
La magia ocurre porque un ordenador cuántico puede evaluar $f(x)$ para *todos* los posibles valores de $x$ simultáneamente usando superposición, e interferir los resultados usando la Transformada de Fourier Cuántica (QFT) para revelar la periodicidad global $r$.

El circuito tiene dos registros:
1.  Registro $X$: Se pone en una superposición uniforme $\frac{1}{\sqrt{Q}} \sum_{x=0}^{Q-1} |x\rangle$.
2.  Registro $Y$: En este registro se computa la función $f(x)$ usando un oráculo cuántico (exponenciación modular controlada), entrelazando el registro $X$ e $Y$:
    $$ \sum_x |x\rangle |a^x \bmod N\rangle $$
3.  Se mide el registro $Y$. Esto colapsa el registro $X$ a una superposición de solo aquellos $x$ que dan el mismo valor en $f(x)$. Es decir, $X$ colapsa a $|x_0\rangle + |x_0+r\rangle + |x_0+2r\rangle + \dots$
4.  Se aplica la **Transformada de Fourier Cuántica Inversa (IQFT)** al registro $X$. La interferencia destructiva cancela todas las amplitudes excepto aquellas cercanas a los múltiplos de $Q/r$.
5.  Se mide el registro $X$. El resultado de la medición con altísima probabilidad es un número $c$ tal que $c/Q \approx d/r$.
6.  Usando el algoritmo de fracciones continuas clásico, extraemos $r$ a partir del valor medido.
