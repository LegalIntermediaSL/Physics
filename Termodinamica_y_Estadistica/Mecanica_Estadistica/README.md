# Mecánica Estadística

La mecánica estadística es la formulación matemática que deduce todas las leyes de la termodinámica clásica partiendo del estudio probabilístico de los incontables microestados (configuraciones atómicas o cuánticas) compatibles con un macroestado dado (como energía, volumen y temperatura fijas).

## 📜 Contexto Histórico
A finales del siglo XIX, Ludwig Boltzmann y Josiah Willard Gibbs sentaron las bases fundacionales de esta disciplina. Boltzmann propuso que la entropía es una medida del número de microestados disponibles (expresado en su famosa lápida $S = k \log W$). Gibbs, por su parte, desarrolló la noción de los "colectivos" o "ensembles" (microcanónico, canónico, macrocanónico). Con el advenimiento de la mecánica cuántica, Albert Einstein, Satyendra Nath Bose, Enrico Fermi y Paul Dirac ampliaron la teoría a los bosones y fermiones en la década de 1920, lo que permitió explicar fenómenos que escapaban a la física clásica (como el cuerpo negro, la conducción en metales y la superfluidez).

---

## 🧮 Desarrollo Teórico Profundo

### Colectivo Microcanónico (Sistema Aislado)
Describe un sistema aislado con número de partículas $N$, volumen $V$, y energía total $E$ fijos. El postulado fundamental afirma que todos los microestados accesibles $\Omega(N,V,E)$ son igualmente probables.
La entropía $S$ se define como:
$$ S = k_B \ln \Omega $$

### Colectivo Canónico (Sistema en Contacto Térmico)
Describe un sistema con $N$ y $V$ fijos, pero que puede intercambiar energía con un baño térmico inmenso a temperatura constante $T$. La probabilidad de encontrar al sistema en un microestado $r$ con energía $E_r$ está dada por la distribución de Boltzmann:
$$ P_r = \frac{e^{-\beta E_r}}{Z} $$
donde $\beta = \frac{1}{k_B T}$ y $Z$ es la **función de partición canónica**:
$$ Z(N,V,T) = \sum_r e^{-\beta E_r} $$
A partir de $Z$ se deducen todas las variables termodinámicas. Por ejemplo, la Energía Libre de Helmholtz $F$ es:
$$ F = -k_B T \ln Z $$
Y la energía interna media $U$:
$$ U = \langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} $$

### Estadísticas Cuánticas
A bajas temperaturas o altas densidades, la naturaleza indistinguible de las partículas cuánticas es crucial.
* **Estadística de Bose-Einstein (Bosones):** Partículas de espín entero, sin restricción de ocupación. El número de ocupación medio por estado de energía $\epsilon_i$ es:
  $$ \langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$
* **Estadística de Fermi-Dirac (Fermiones):** Partículas de espín semientero (e.g., electrones), sujetas al principio de exclusión de Pauli (a lo sumo 1 partícula por estado):
  $$ \langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} + 1} $$
donde $\mu$ es el potencial químico.

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular la energía interna promedio y la capacidad calorífica de un paramagneto de espín $1/2$ que consta de $N$ átomos fijos y no interactuantes, en presencia de un campo magnético externo $B$, a temperatura $T$.

**Solución paso a paso:**
1. **Identificar los microestados de un átomo:**
   Cada espín puede apuntar "arriba" (energía $\epsilon_{\uparrow} = -\mu_B B$) o "abajo" (energía $\epsilon_{\downarrow} = +\mu_B B$), donde $\mu_B$ es el magnetón de Bohr.
2. **Calcular la función de partición de una sola partícula ($z$):**
   $$ z = e^{-\beta(-\mu_B B)} + e^{-\beta(+\mu_B B)} = e^{\beta \mu_B B} + e^{-\beta \mu_B B} = 2 \cosh(\beta \mu_B B) $$
3. **Calcular la función de partición total ($Z$):**
   Como las partículas son distinguibles por estar fijas en la red cristalina:
   $$ Z = z^N = \left[ 2 \cosh(\beta \mu_B B) \right]^N $$
4. **Calcular la energía interna ($U$):**
   $$ U = -\frac{\partial \ln Z}{\partial \beta} = -N \frac{\partial}{\partial \beta} \ln[2 \cosh(\beta \mu_B B)] $$
   $$ U = -N \frac{2 \mu_B B \sinh(\beta \mu_B B)}{2 \cosh(\beta \mu_B B)} = -N \mu_B B \tanh(\beta \mu_B B) $$
5. **Calcular la capacidad calorífica ($C$):**
   $$ C = \frac{\partial U}{\partial T} = \frac{\partial U}{\partial \beta} \frac{\partial \beta}{\partial T} $$
   Como $\frac{\partial \beta}{\partial T} = -\frac{1}{k_B T^2}$:
   $$ C = N k_B (\beta \mu_B B)^2 \operatorname{sech}^2(\beta \mu_B B) $$
   Este resultado demuestra de forma teórica la "anomalía de Schottky", un pico en la capacidad calorífica a bajas temperaturas típico de sistemas de dos niveles.

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
* **Stanford - Statistical Mechanics (Leonard Susskind):** Esencial, se adentra directamente en la lógica matemática subyacente y la física de la información.
* **MIT 8.044 (Statistical Physics I):** Excelente enfoque formal desde sistemas discretos a gases cuánticos.
* **Perimeter Institute - Statistical Physics:** Clases de maestría con nivel avanzado, ideal para física de materia condensada.

### 📝 Artículos e Interactivos Interesantes
* **Simulación Ising Model (Varios en la web):** Visualizar el ferromagnetismo y las transiciones de fase críticas desde un ensamble de espines en interacción.
* **Catástrofe Ultravioleta e Historia de Planck:** Leer sobre cómo el conteo estadístico de fotones inició la revolución cuántica.
* **Bose-Einstein Condensation (PhET / Videos):** Animaciones y artículos detallando el fenómeno macroscópico que ocurre cuando la ocupación cuántica diverge hacia el estado fundamental.
