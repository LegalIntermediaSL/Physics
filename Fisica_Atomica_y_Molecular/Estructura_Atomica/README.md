# Estructura Atómica

La estructura atómica se ocupa de la organización de electrones, protones y neutrones dentro del átomo, utilizando la mecánica cuántica como herramienta principal para describir el comportamiento electrónico.

## 📜 Contexto Histórico

Desde el modelo planetario de Rutherford (1911) hasta la cuantización propuesta por Niels Bohr (1913), la estructura atómica revolucionó la física. En 1925-1926, Heisenberg y Schrödinger formularon la mecánica cuántica moderna. Posteriormente, Dirac introdujo la relatividad en 1928, prediciendo la existencia del espín del electrón y la antimateria.

## 🧮 Desarrollo Teórico Profundo

La formulación de la mecánica cuántica aplicada a la estructura atómica constituye uno de los pilares de la física moderna. Su abordaje riguroso comienza resolviendo exactamente el átomo hidrogenoide (un núcleo de carga $+Ze$ y un solo electrón) y luego empleando técnicas perturbativas y métodos variacionales para extender el tratamiento a sistemas multielectrónicos complejos.

### 1. El Hamiltoniano Central y la Separación de Variables

Para un átomo hidrogenoide no relativista, modelamos el sistema como dos masas interactuantes: un núcleo de masa $M$ y un electrón de masa $m_e$. Adoptando un marco de referencia en el centro de masa del sistema, el problema de dos cuerpos se reduce al movimiento de una sola partícula ficticia con una **masa reducida** $\mu = \frac{m_e M}{m_e + M}$. Dado que $M \gg m_e$, $\mu \approx m_e$.

El Hamiltoniano que rige el sistema cuántico sometido al potencial central electromagnético (fuerza de Coulomb) es:

$$
\hat{H} = - \frac{\hbar^2}{2\mu} \nabla^2 - \frac{Z e^2}{4 \pi \epsilon_0 r}
$$

La ecuación fundamental de Schrödinger independiente del tiempo es $\hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r})$. Aprovechando la simetría esférica intrínseca del potencial central, transformamos el laplaciano $\nabla^2$ a coordenadas esféricas $(r, \theta, \phi)$:

$$
\nabla^2 = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right) + \frac{1}{r^2 \sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial}{\partial \theta} \right) + \frac{1}{r^2 \sin^2\theta} \frac{\partial^2}{\partial \phi^2}
$$

Reconociendo que los últimos dos términos corresponden precisamente al operador cuadrado del momento angular orbital $\hat{L}^2$ dividido por $\hbar^2 r^2$, reescribimos:

$$
\hat{H} = -\frac{\hbar^2}{2\mu} \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right) + \frac{\hat{L}^2}{2\mu r^2} - \frac{Z e^2}{4\pi\epsilon_0 r}
$$

Al conmutar el Hamiltoniano central con el momento angular total $[\hat{H}, \hat{L}^2] = 0$ y su componente z $[\hat{H}, \hat{L}_z] = 0$, aseguramos la existencia de una base común de autoestados. Esto justifica invocar el método de separación de variables:

$$
\psi(r, \theta, \phi) = R(r) Y_{l}^{m_l}(\theta, \phi)
$$

Donde $Y_{l}^{m_l}(\theta, \phi)$ denota los **Armónicos Esféricos**. Al satisfacer la relación de valores propios:

$$
\hat{L}^2 Y_{l}^{m_l}(\theta, \phi) = \hbar^2 l(l+1) Y_{l}^{m_l}(\theta, \phi)
$$

Donde $l = 0, 1, 2, \dots$ es el número cuántico azimutal y $m_l = -l, -l+1, \dots, l$ es el número cuántico magnético.

### 2. Solución Analítica de la Ecuación Radial

Al reemplazar el *Ansatz* en la ecuación de Schrödinger y dividir por la función de onda, la contribución angular se desacopla enteramente, originando la **ecuación diferencial radial**:

$$
\left[ -\frac{\hbar^2}{2\mu} \frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{d}{dr} \right) + \frac{\hbar^2 l(l+1)}{2\mu r^2} - \frac{Z e^2}{4 \pi \epsilon_0 r} \right] R(r) = E R(r)
$$

Podemos transformar esta ecuación a la forma unidimensional estándar introduciendo la función radial auxiliar $u(r) = r R(r)$. Las derivadas radiales se reducen de $\frac{1}{r^2}\frac{d}{dr}\left(r^2 \frac{dR}{dr}\right)$ a simplemente $\frac{1}{r}\frac{d^2u}{dr^2}$, obteniendo:

$$
- \frac{\hbar^2}{2\mu} \frac{d^2 u}{dr^2} + \underbrace{ \left[ - \frac{Z e^2}{4 \pi \epsilon_0 r} + \frac{\hbar^2 l(l+1)}{2\mu r^2} \right] }_{V_{\text{efectivo}}(r)} u(r) = E u(r)
$$

El potencial efectivo posee un *término centrífugo* positivo que crea una repulsión prohibitiva en el origen para órbitas con $l > 0$. Para encontrar los estados ligados, analizamos los regímenes asintóticos:
- **Para $r \to \infty$**: El potencial se desvanece, obteniendo $\frac{d^2 u}{dr^2} = -\frac{2\mu E}{\hbar^2} u$. Para estados con $E < 0$, definimos un factor de decaimiento real $\kappa = \frac{\sqrt{-2\mu E}}{\hbar}$, resultando en la caída exponencial normalizable $u(r) \sim e^{-\kappa r}$.
- **Para $r \to 0$**: El término de momento angular domina la barrera centrífuga, dictando la condición en el origen de que $u(r) \sim r^{l+1}$.

Motivados por estas dos condiciones asintóticas extremas, realizamos un cambio de variable adimensional introduciendo $\rho = 2 \kappa r$. Buscamos entonces una solución que contemple ambos comportamientos asintóticos factorizados por una serie de potencias desconocida $v(\rho)$:

$$
u(\rho) = \rho^{l+1} e^{-\rho/2} v(\rho)
$$

Sustituyendo esto en la ecuación radial adimendional, obtenemos para $v(\rho)$ la **ecuación diferencial de Laguerre asociada**. Para evitar que la función de onda diverja y pierda la interpretabilidad de probabilidad finita, la serie de Frobenius empleada para hallar $v(\rho)$ debe truncarse tras un determinado polinomio de grado $n_r \ge 0$. 
Esta severa condición matemática para el truncamiento fuerza la emergencia de un nuevo número entero conocido como el **número cuántico principal**, definido como:

$$
n = n_r + l + 1 \quad \text{con} \quad n = 1, 2, 3, \dots
$$

Este criterio de contorno de Dirichlet que exige la normalización es lo que verdaderamente "cuantiza" la energía.

#### Cuantización Energética de Bohr

La energía impuesta por el truncamiento de la serie depende puramente del número cuántico $n$ (una notable degeneración temporal y espacial conocida como "degeneración accidental" dictada por la simetría extra de Lenz-Runge). La serie de energías del átomo de hidrógeno es:

$$
E_n = - \left[ \frac{\mu e^4}{32 \pi^2 \epsilon_0^2 \hbar^2} \right] \frac{Z^2}{n^2} = - \frac{13.6 \, \text{eV} \cdot Z^2}{n^2}
$$

```mermaid
graph TD
    A[Hamiltoniano Central Átomo de Hidrógeno] --> B[Separación de Variables]
    B --> C[Ecuación Angular]
    B --> D[Ecuación Radial u=rR]
    C --> E[Armónicos Esféricos Y_lm]
    C --> F[Valores propios L^2 y L_z]
    D --> G[Análisis Asintótico y Serie de Frobenius]
    G --> H[Ecuación Diferencial de Laguerre]
    H --> I[Condición de Normalización L^2]
    I --> J[Cuantización de la Energía E_n]
    J --> K[Espectro Discreto no Degenerado en E_n]
```

### 3. Estructura Fina: Relatividad y el Espín

El modelo anterior es fenomenal para el modelado a primer orden del átomo, pero falla bajo instrumentación espectroscópica fina. Las discrepancias teóricas requirieron la incorporación empírica del espín electrónico introducido por Goudsmit y Uhlenbeck, formalizado posteriormente mediante la ecuación del electrón relativista de **Paul Dirac**. 

Tomando el límite no relativista de la Ecuación de Dirac se recupera el Hamiltoniano de Schrödinger, adicionando un operador de perturbaciones de *estructura fina* $\hat{H}_{fs}$ formado por tres aportes sutiles:

$$
\hat{H}_{fs} = \hat{H}_{rel} + \hat{H}_{SO} + \hat{H}_{Darwin}
$$

1. **Corrección Relativista de la Energía Cinética ($\hat{H}_{rel}$):**
   La expansión de la energía en relatividad especial se escribe como:

   

$$
T = \sqrt{p^2 c^2 + (mc^2)^2} - mc^2 = \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2} + \dots
$$

   El término perturbativo es $\hat{H}_{rel} = - \frac{\hat{p}^4}{8m^3 c^2}$. En el esquema de perturbaciones independientes del tiempo de primer orden, su contribución a la energía rompe la degeneración en $l$:

   

$$
\Delta E_{rel} = \langle nlm | \hat{H}_{rel} | nlm \rangle = - \frac{E_n^2}{2mc^2} \left[ \frac{4n}{l + 1/2} - 3 \right]
$$

2. **Acoplamiento Espín-Órbita ($\hat{H}_{SO}$):**
   Un electrón orbitando experimenta, desde su marco inercial de referencia en reposo, un protón en órbita alrededor de él, originando un campo magnético aparente de Biot-Savart proporcional al momento angular orbital $\mathbf{L}$. El momento magnético intrínseco del espín $\mathbf{S}$ interacciona con dicho campo. Tomando en consideración la corrección cinemática relativista de precesión de Thomas, se obtiene el hamiltoniano de interacción perturbativo:

   

$$
\hat{H}_{SO} = \frac{1}{2 m^2 c^2} \left( \frac{1}{r} \frac{dV}{dr} \right) \hat{\mathbf{S}} \cdot \hat{\mathbf{L}}
$$

   El producto escalar de operadores requiere usar la base de acoplamiento del **Momento Angular Total** $\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}$. Elevando al cuadrado para eliminar el término de cruce obtenemos la famosa identidad $\hat{\mathbf{S}} \cdot \hat{\mathbf{L}} = \frac{1}{2} (\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$. Al evaluar su valor propio:

   

$$
\langle \hat{\mathbf{S}} \cdot \hat{\mathbf{L}} \rangle = \frac{\hbar^2}{2} \left[ j(j+1) - l(l+1) - s(s+1) \right]
$$

   Esta corrección vincula el espectro energético finamente a una combinación inseparable de números orbitales y de espín intrínseco.

3. **Corrección de Darwin ($\hat{H}_{Darwin}$):**
   Una peculiaridad rigurosamente derivada de la mecánica relativista cuántica de Dirac es el temblor o agitación subyacente de la partícula (Zitterbewegung). Esta fluctuación posicional implica que el electrón no puede confinarse a volúmenes puramente puntuales, suavizando el potencial en torno al origen. Solo aplica a órbitas con presencia no nula en el núcleo central, restringiéndose casi puramente a estados *s* ($l=0$).

La energía atómica de estructura fina reensambla los tres términos proporcionando un ajuste preciso dependiente tanto de $n$ como de $j$:

$$
E_{nj} = E_n \left[ 1 + \frac{(Z\alpha)^2}{n} \left( \frac{1}{j+1/2} - \frac{3}{4n} \right) \right]
$$

Donde $\alpha = \frac{e^2}{4\pi \epsilon_0 \hbar c} \approx \frac{1}{137}$ es la legendaria **Constante de Estructura Fina**.

### 4. Átomos Multielectrónicos y la Teoría de Hartre-Fock

Para un átomo arbitrario con carga nuclear $Z$ y albergando un enjambre de $N$ electrones, la simple aditividad de términos de momento angular se quiebra debido al campo eléctrico de repulsión correlacionado electrón-electrón:

$$
\hat{H} = \underbrace{ \sum_{i=1}^{N} \left( -\frac{\hbar^2}{2m} \nabla_i^2 - \frac{Z e^2}{4\pi\epsilon_0 r_i} \right) }_{\hat{H}_{\text{núcleo}}} + \underbrace{ \sum_{i=1}^{N} \sum_{j > i}^{N} \frac{e^2}{4\pi\epsilon_0 | \mathbf{r}_i - \mathbf{r}_j |} }_{\hat{H}_{\text{repulsión}}}
$$

Dado que la función de potencial de repulsión mezcla implícitamente las coordenadas conjuntas de múltiples partículas interdependientes, la imposibilidad generalizada de alcanzar una solución analítica dio lugar a los formidables cimientos de los métodos computacionales algebraicos cuánticos.

#### El Principio de Pauli y Los Determinantes de Slater

Como requerimiento intrínseco del postulado de simetrización fermiónico impuesto en mecánica cuántica, la **Función de Onda Polielectrónica** total debe ser estrictamente antisimétrica ante la permutación y cruce arbitrario de las variables espaciales y de espín de cualquier par de electrones constituyentes:

$$
\Psi(\dots, \mathbf{x}_i, \dots, \mathbf{x}_j, \dots) = - \Psi(\dots, \mathbf{x}_j, \dots, \mathbf{x}_i, \dots)
$$

Con el objeto de satisfacer tal restricción, la aproximación orbital expresa la función a partir del **Determinante de Slater**. Un determinante nulo emana de poseer dos columnas idénticas correspondientes al mismo estado cuántico; la manifestación rigurosa del **Principio de Exclusión de Pauli**:

$$
\Psi(\mathbf{x}_1, \dots, \mathbf{x}_N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} \phi_1(\mathbf{x}_1) & \phi_2(\mathbf{x}_1) & \dots & \phi_N(\mathbf{x}_1) \\ \phi_1(\mathbf{x}_2) & \phi_2(\mathbf{x}_2) & \dots & \phi_N(\mathbf{x}_2) \\ \vdots & \vdots & \ddots & \vdots \\ \phi_1(\mathbf{x}_N) & \phi_2(\mathbf{x}_N) & \dots & \phi_N(\mathbf{x}_N) \end{vmatrix}
$$

#### La Aproximación de Hartree-Fock

El método fundacional propuesto para deducir los estados estacionarios de mínima energía es el **Método de Hartree-Fock**, el cual invoca explícitamente el teorema variacional. Minimizar el funcional de la energía sujeta a constricciones de ortonormalidad de las funciones de espín-orbitales bases genera un arreglo acoplado de ecuaciones integro-diferenciales. En ellas se manifiesta el operador de interacciones de Coulomb y un nuevo operador de intercambio. El marco requiere una solución cíclica recursiva denominada **Campo Autoconsistente (SCF)**.

### 5. Configuración Electrónica en Terminos de Russell-Saunders

En el dominio atómico ligero y de mediana masa, el acoplamiento magnético LS o de Russell-Saunders predomina asumiendo la suma vectorial estricta orbital $\mathbf{L} = \sum \mathbf{l}_i$ así como de la correlación angular intrínseca de espines totales $\mathbf{S} = \sum \mathbf{s}_i$. Los subniveles originan agrupamientos denominados términos espectroscópicos:

$$
^{2S+1}L_{J}
$$

La energía preferida fundamental es inferida deductivamente recurriendo a las **Reglas de Hund**.

---

## 🛠 Ejemplo Computacional Práctico

**Problema:** Un átomo de hidrógeno, estimulado en el sistema de transición de Balmer, emite la línea espectral ultra característica Alpha de Hidrógeno ($H_\alpha$). Derivemos matemáticamente la magnitud ondulatoria de propagación transversal de su longitud de onda ($\lambda$), al desescalar desde la capa $n=3$ al nivel transitorio $n=2$.

**Demostración y Solución Formal paso a paso:**

1. **Fronteras de energía:**
   Las capas degeneradas arrojan una cuantificación energética discrecional:

   

$$
E_n = -\frac{13.60569 \, \text{eV}}{n^2}
$$

2. **Evaluación de Eigen-energías para el Estado Inicial ($n_i = 3$) y Final ($n_f = 2$):**

   

$$
E_3 = -\frac{13.60569}{3^2} = -1.51174 \, \text{eV}
$$

   

$$
E_2 = -\frac{13.60569}{2^2} = -3.40142 \, \text{eV}
$$

3. **Emisión de Fotones:**
   Evaluamos la energía desprendida cuantificada de la fluctuación electromagnética:

   

$$
\Delta E = E_3 - E_2 = -1.51174 - (-3.40142) = 1.88968 \, \text{eV}
$$

4. **Conversión MKS para Joules ($J$):**
   Aprovechando $1 \text{ eV} = 1.602176634 \times 10^{-19} \, \text{J}$:

   

$$
\Delta E = (1.88968) \times (1.602176634 \times 10^{-19}) = 3.0276 \times 10^{-19} \, \text{J}
$$

5. **Derivación de Longitud de Onda Fundacional ($\lambda$):**
   Usando $E = h \nu$ y $\nu = c / \lambda \implies \lambda = \frac{hc}{\Delta E}$:

   

$$
\lambda = \frac{(6.626070 \times 10^{-34}) (2.99792458 \times 10^8)}{3.0276 \times 10^{-19}}
$$

   

$$
\lambda \approx \frac{1.986445 \times 10^{-25}}{3.0276 \times 10^{-19}} \approx 6.561 \times 10^{-7} \, \text{m} = 656.1 \, \text{nm}
$$

**(Nota Científica:)** La corrección marginal experimentada de la línea analítica $H_\alpha = 656.3 \, \text{nm}$ (en vacío) reside principalmente debido a los minúsculos efectos estructurales acoplados y al ensanchamiento Doppler de las correcciones de estructura fina discutidas teóricamente arriba.

## 📝 Guía de Ejercicios Resueltos

### Ejercicio 1: Efecto Stark Lineal en el Átomo de Hidrógeno
Considere un átomo de hidrógeno en el primer estado excitado ($n=2$) sometido a un campo eléctrico externo uniforme $\vec{\mathcal{E}} = \mathcal{E}_0 \hat{z}$. Calcule el corrimiento de los niveles de energía utilizando la teoría de perturbaciones degenerada de primer orden.

**Solución paso a paso:**
1. Los estados degenerados para $n=2$ son $|2,0,0\rangle$, $|2,1,0\rangle$, $|2,1,1\rangle$, y $|2,1,-1\rangle$ en la base $|n,l,m\rangle$.
2. El Hamiltoniano de perturbación es $H' = e \mathcal{E}_0 z = e \mathcal{E}_0 r \cos\theta$.
3. Los elementos de matriz de $H'$ solo son no nulos si $\Delta m = 0$ y $\Delta l = \pm 1$ debido a las reglas de selección.
4. Por lo tanto, el único elemento no diagonal no nulo es entre $|2,0,0\rangle$ y $|2,1,0\rangle$:

   

$$
\langle 2,0,0 | H' | 2,1,0 \rangle = e \mathcal{E}_0 \int d^3r \psi_{200}^* z \psi_{210} = -3 e \mathcal{E}_0 a_0
$$

   donde $a_0$ es el radio de Bohr.
5. La matriz de perturbación en la sub-base $\{|2,0,0\rangle, |2,1,0\rangle, |2,1,1\rangle, |2,1,-1\rangle\}$ es:

   

$$
H' = \begin{pmatrix} 0 & -3ea_0\mathcal{E}_0 & 0 & 0 \\ -3ea_0\mathcal{E}_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

6. Los autovalores son $\Delta E = \pm 3 e a_0 \mathcal{E}_0$ y $0$ (doblemente degenerado).

### Ejercicio 2: Espectro Rotovibracional de la Molécula de Diatómica
Derive la expresión para los niveles de energía rotovibracionales de una molécula diatómica tratada como un oscilador armónico y rotor rígido acoplados, incluyendo la corrección de distorsión centrífuga. 

**Solución paso a paso:**
1. El Hamiltoniano molecular efectivo es $H = \frac{P^2}{2\mu} + \frac{L^2}{2\mu R^2} + V(R)$.
2. Expandiendo el potencial alrededor del mínimo $R_e$: $V(R) \approx \frac{1}{2} k (R - R_e)^2$.
3. La energía a orden cero es $E_{v,J} = \hbar \omega \left(v + \frac{1}{2}\right) + B_e J(J+1)$, donde $B_e = \frac{\hbar^2}{2\mu R_e^2}$.
4. Para la distorsión centrífuga, el mínimo efectivo de la energía potencial efectiva $V_{\text{eff}}(R) = V(R) + \frac{\hbar^2 J(J+1)}{2\mu R^2}$ se desplaza.
5. Minimizando $V_{\text{eff}}$: $k(R_c - R_e) - \frac{\hbar^2 J(J+1)}{\mu R_c^3} = 0 \implies \Delta R \approx \frac{\hbar^2 J(J+1)}{k \mu R_e^3}$.
6. Sustituyendo de nuevo en la energía, el término de corrección es $-D_e J^2(J+1)^2$, donde $D_e = \frac{4B_e^3}{\hbar^2 \omega^2}$.
7. La energía final es $E_{v,J} = \hbar \omega \left(v + \frac{1}{2}\right) + B_e J(J+1) - D_e J^2(J+1)^2$.

### Ejercicio 3: Condensación de Bose-Einstein en una Trampa Armónica
Determine la temperatura crítica $T_c$ para la condensación de Bose-Einstein de un gas ideal de $N$ bosones atrapados en un potencial armónico tridimensional isotrópico $V(r) = \frac{1}{2} m \omega^2 r^2$.

**Solución paso a paso:**
1. La densidad de estados para un oscilador armónico 3D es $g(E) = \frac{E^2}{2(\hbar\omega)^3}$.
2. El número total de partículas en estados excitados viene dado por la integral:

   

$$
N_{ex} = \int_0^\infty \frac{g(E)}{e^{\beta (E-\mu)} - 1} dE
$$

3. En la temperatura crítica $T_c$, el potencial químico $\mu \to 0$ y $N_{ex} = N$.
4. Reemplazando $g(E)$ e introduciendo $x = E/k_B T_c$:

   

$$
N = \frac{(k_B T_c)^3}{2(\hbar\omega)^3} \int_0^\infty \frac{x^2}{e^x - 1} dx
$$

5. La integral es conocida como $\Gamma(3)\zeta(3) = 2 \times 1.202$.
6. Resolviendo para $T_c$:

   

$$
N = \left( \frac{k_B T_c}{\hbar\omega} \right)^3 \zeta(3) \implies T_c = \frac{\hbar\omega}{k_B} \left( \frac{N}{\zeta(3)} \right)^{1/3}
$$

## 💻 Simulaciones Computacionales

Este script computa y visualiza la densidad de probabilidad radial de los orbitales del átomo de hidrógeno, implementando analíticamente los polinomios asociados de Laguerre derivados de la ecuación de Schrödinger central.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
from math import factorial

def R_nl(n, l, r):
    """Función de onda radial para el átomo de hidrógeno (Z=1).
    r está en unidades de radio de Bohr (a0)."""
    rho = 2.0 * r / n
    # Factor de normalización
    norm_term = np.sqrt((2.0/n)**3 * factorial(n - l - 1) / (2.0 * n * factorial(n + l)))
    # Polinomio de Laguerre generalizado L_{n-l-1}^{2l+1}(rho)
    L_poly = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    return norm_term * np.exp(-rho / 2.0) * (rho**l) * L_poly

r_vals = np.linspace(0, 30, 1000)

# Casos de orbitales a plotear (n, l)
orbitals = [(1, 0, '1s'), (2, 0, '2s'), (2, 1, '2p'), (3, 0, '3s'), (3, 1, '3p'), (3, 2, '3d')]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

plt.figure(figsize=(12, 6))

for (n, l, name), color in zip(orbitals, colors):
    # Función de densidad de probabilidad radial P(r) = r^2 * |R(r)|^2
    R = R_nl(n, l, r_vals)
    P_r = r_vals**2 * R**2
    plt.plot(r_vals, P_r, label=f'Orbital {name}', lw=2, color=color)

plt.title("Densidad de Probabilidad Radial Atómica del Hidrógeno")
plt.xlabel("Distancia al Núcleo $r$ (en radios de Bohr $a_0$)")
plt.ylabel("Densidad Radial $P(r) = r^2 |R_{nl}(r)|^2$")
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.xlim(0, 25)
plt.tight_layout()
# plt.show()
```

## 🚀 Fronteras de Investigación y Problemas Abiertos

La física de Estructura Atómica para 2026 lidia con los límites absolutos de la Tabla Periódica. La búsqueda de la "Isla de Estabilidad" en elementos superpesados (Elemento 114, 120+) enfrenta el hecho de que en regímenes de alta $Z$ (donde $Z\alpha \approx 1$), los electrones $1s$ alcanzan velocidades cercanas a la de la luz. Esto genera un colapso de la aproximación de Dirac-Coulomb y efectos cuánticos electrodinámicos (QED) no-perturbativos que reorganizan por completo las valencias químicas, al punto de que los elementos superpesados no respetan la periodicidad de sus grupos. Asimismo, el uso de Iones Altamente Cargados (HCIs), donde casi todos los electrones han sido despojados (ej. $Ar^{13+}$), proporciona la base para la próxima generación de Relojes Ópticos, gracias a su extrema insensibilidad a perturbaciones electromagnéticas externas. Por último, la espectroscopía de precisión del Desplazamiento Isotópico (Isotope Shift) en cadenas largas de isótopos se utiliza para establecer límites en el acoplamiento de "Nuevas Fuerzas" de corto alcance mediadas por bosones oscuros hipotéticos.

## 📐 Formalismo Matemático Avanzado (Nivel Posgrado/Doctorado)

Para tratar átomos pesados, se abandona la ecuación de Schrödinger en favor de la **Teoría Cuántica de Muchos Cuerpos Relativista**. La estructura algebraica base son las **Álgebras de Clifford** asociadas a la Ecuación de Dirac, actuando sobre un fibrado espinorial. El problema central radica en el tratamiento riguroso de la repulsión interelectrónica acoplada a la electrodinámica.

En lugar de modelos fenomenológicos, se utiliza el **Formalismo de Espacio de Fock** (Segunda Cuantización). Para abordar la correlación electrónica post-Hartree-Fock, el estándar de oro matemático es la **Teoría de Clústeres Acoplados (Coupled Cluster, CC)**. El estado base exacto interactuante $|\Psi\rangle$ se asume gobernado por un operador de clúster exponencial sobre el determinante de Slater de referencia $|\Phi_0\rangle$:

$$
|\Psi\rangle = e^{\hat{T}} |\Phi_0\rangle
$$

$$
\hat{T} = \hat{T}_1 + \hat{T}_2 + \dots + \hat{T}_N
$$

Donde $\hat{T}_n$ crea excitaciones de $n$ partículas y $n$ huecos. El mapeo del problema de valores propios original $e^{-\hat{T}}\hat{H}e^{\hat{T}} |\Phi_0\rangle = E|\Phi_0\rangle$ usa el lema de Baker-Campbell-Hausdorff. Esta serie conmuta y termina en el cuarto conmutador debido a que el Hamiltoniano cuántico contiene solo interacciones de hasta dos cuerpos, derivando en un sistema riguroso acoplado de ecuaciones no lineales algebraicas. En el límite $Z \to 137$, el operador de Dirac deja de ser esencialmente autoadjunto para núcleos puntuales, requiriendo un análisis funcional riguroso de los índices de deficiencia de von Neumann para aplicar las extensiones autoadjuntas físicamente motivadas por el radio nuclear finito.

## 📚 Recursos Específicos
5. [Schrödinger, E. (1926). *An Undulatory Theory of the Mechanics of Atoms and Molecules*. Phys. Rev.](https://journals.aps.org/pr/abstract/10.1103/PhysRev.28.1049)
6. [Pauli, W. (1925). *On the Connexion between the Completion of Electron Groups in an Atom with the Complex Structure of Spectra*.](https://link.springer.com/article/10.1007/BF02980631)
7. [PhET Simulation: Rutherford Scattering](https://phet.colorado.edu/en/simulations/rutherford-scattering)
8. [PhET Simulation: Neon Lights & Other Discharge Lamps](https://phet.colorado.edu/en/simulations/neon-lights-and-other-discharge-lamps)
9. [Dirac, P. A. M. (1928). *The Quantum Theory of the Electron*. Proc. R. Soc. Lond.](https://royalsocietypublishing.org/doi/10.1098/rspa.1928.0023)
10. [Slater, J. C. (1929). *The Theory of Complex Spectra*. Phys. Rev.](https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.1293)

### 📖 Referencias Útiles y Bibliografía
- [Foot, C. J. (2005). *Atomic Physics*. Oxford University Press.](https://global.oup.com/academic/product/atomic-physics-9780198506966)
- [Bransden, B. H., & Joachain, C. J. (2003). *Physics of Atoms and Molecules*. Pearson Education.](https://www.pearson.com/en-us/subject-catalog/p/physics-of-atoms-and-molecules/P200000005739)
- [Woodgate, G. K. (1980). *Elementary Atomic Structure*. Oxford University Press.](https://global.oup.com/academic/product/elementary-atomic-structure-9780198511564)
- [Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra*. University of California Press.](https://www.ucpress.edu/book/9780520038219/the-theory-of-atomic-structure-and-spectra)

## 🌐 Seminarios Avanzados y Literatura de Frontera

### Seminarios y Cursos Avanzados
1. [Perimeter Institute Recorded Seminars (PIRSA) - Quantum Physics](https://pirsa.org/) - Exploración profunda sobre los fundamentos cuánticos de la estructura atómica y molecular.
2. [CERN ISOLDE Seminars](https://isolde.cern/seminars) - Estudios experimentales y espectroscopía de precisión sobre estructuras atómicas en isótopos exóticos.
3. [Max Planck Institute for Nuclear Physics Seminars](https://www.mpi-hd.mpg.de/) - Dinámica de electrones atómicos, procesos iónicos y metrología.

### Literatura de Frontera
1. [Precision Measurement of the Fine-Structure Constant (Science)](https://www.science.org/doi/10.1126/science.aap7706) - Un hito en la espectroscopía atómica que pone a prueba la electrodinámica cuántica y el Modelo Estándar con precisión abismal.
2. [Rydberg Atoms for Quantum Information (Reviews of Modern Physics)](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.82.2313) - Un estado del arte de cómo las propiedades extremas de átomos en estados altamente excitados habilitan computación cuántica de nueva era.
3. [Atomic parity violation in cesium (Science)](https://www.science.org/doi/10.1126/science.275.5307.1759) - Medición altamente precisa que investiga la física de partículas débil directamente a través de interacciones en un átomo pesado.
