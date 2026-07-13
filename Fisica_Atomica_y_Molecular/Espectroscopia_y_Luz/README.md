# Espectroscopia y Luz

La espectroscopia es el estudio de la interacción entre la radiación electromagnética y la materia, fundamental para determinar la estructura y la dinámica de átomos y moléculas.

## 📜 Contexto Histórico

En el siglo XIX, Fraunhofer descubrió líneas oscuras en el espectro solar (Líneas de Fraunhofer). Bunsen y Kirchhoff demostraron en 1859 que cada elemento emite y absorbe luz en longitudes de onda específicas. En 1916, Albert Einstein sentó las bases para el láser mediante su teoría de los coeficientes $A$ y $B$ para emisión espontánea y estimulada.

## 🧮 Desarrollo Teórico Profundo

### 1. El Hamiltoniano de Interacción Radiación-Materia

Para estudiar la interacción entre un átomo y un campo electromagnético, comenzamos desde la formulación clásica del electromagnetismo utilizando los potenciales vector $\mathbf{A}(\mathbf{r}, t)$ y escalar $\phi(\mathbf{r}, t)$. El campo eléctrico $\mathbf{E}$ y el campo magnético $\mathbf{B}$ se expresan como:

$$ \mathbf{E} = -\nabla \phi - \frac{\partial \mathbf{A}}{\partial t} $$
$$ \mathbf{B} = \nabla \times \mathbf{A} $$

En el **calibre de Coulomb** (o *gauge* de radiación), elegimos $\nabla \cdot \mathbf{A} = 0$ y $\phi = 0$ (en ausencia de fuentes de carga externas libres). Para un electrón de masa $m_e$ y carga $-e$ ligado a un núcleo por un potencial $V(\mathbf{r})$, el Hamiltoniano clásico se obtiene mediante la sustitución del momento canónico $\mathbf{p} \rightarrow \mathbf{p} + e\mathbf{A}$:

$$ H = \frac{1}{2m_e}(\mathbf{p} + e\mathbf{A})^2 + V(\mathbf{r}) $$

Al cuantizar el sistema, reemplazamos $\mathbf{p}$ por su operador mecano-cuántico $\hat{\mathbf{p}} = -i\hbar\nabla$. Expandiendo el término cinético:

$$ (\hat{\mathbf{p}} + e\mathbf{A})^2 = \hat{\mathbf{p}}^2 + e(\hat{\mathbf{p}} \cdot \mathbf{A} + \mathbf{A} \cdot \hat{\mathbf{p}}) + e^2\mathbf{A}^2 $$

Dado que estamos en el calibre de Coulomb, $\nabla \cdot \mathbf{A} = 0$, lo que implica que los operadores $\hat{\mathbf{p}}$ y $\mathbf{A}$ conmutan: $[\hat{\mathbf{p}}, \mathbf{A}] = -i\hbar (\nabla \cdot \mathbf{A}) = 0$. Por lo tanto, $\hat{\mathbf{p}} \cdot \mathbf{A} = \mathbf{A} \cdot \hat{\mathbf{p}}$. El Hamiltoniano total se puede dividir en un término no perturbado $\hat{H}_0$ y una perturbación dependiente del tiempo $\hat{H}'(t)$:

$$ \hat{H} = \underbrace{\frac{\hat{\mathbf{p}}^2}{2m_e} + V(\mathbf{r})}_{\hat{H}_0} + \underbrace{\frac{e}{m_e}\mathbf{A} \cdot \hat{\mathbf{p}} + \frac{e^2}{2m_e}\mathbf{A}^2}_{\hat{H}'(t)} $$

Para campos electromagnéticos de intensidad moderada, el término cuadrático $\mathbf{A}^2$ es despreciable en comparación con el término lineal, por lo que la perturbación se reduce a:

$$ \hat{H}'(t) \approx \frac{e}{m_e}\mathbf{A} \cdot \hat{\mathbf{p}} $$

### 2. La Aproximación Dipolar Eléctrica

Consideremos una onda plana electromagnética monocromática incidente, donde el potencial vector es de la forma:

$$ \mathbf{A}(\mathbf{r}, t) = \mathbf{A}_0 \cos(\mathbf{k} \cdot \mathbf{r} - \omega t) = \frac{\mathbf{A}_0}{2} \left[ e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)} + e^{-i(\mathbf{k} \cdot \mathbf{r} - \omega t)} \right] $$

La longitud de onda $\lambda = 2\pi / |\mathbf{k}|$ de la luz visible o ultravioleta ($\sim 10^{-7}$ m) es mucho mayor que las dimensiones típicas de un átomo ($a_0 \sim 10^{-10}$ m). Esto nos permite realizar la **aproximación dipolar eléctrica**, en la cual expandimos la exponencial en serie de Taylor alrededor del núcleo (situado en $\mathbf{r}=0$):

$$ e^{i\mathbf{k} \cdot \mathbf{r}} = 1 + i\mathbf{k} \cdot \mathbf{r} - \frac{1}{2}(\mathbf{k} \cdot \mathbf{r})^2 + \dots \approx 1 $$

Bajo esta aproximación, el campo se vuelve espacialmente uniforme sobre el átomo, es decir, $\mathbf{A}(\mathbf{r}, t) \approx \mathbf{A}(0, t)$. Es posible demostrar, a través de una transformación de *gauge* de Göppert-Mayer, que esta interacción equivale a la forma más familiar e intuitiva que acopla el **momento dipolar eléctrico** $\hat{\mathbf{d}} = -e\hat{\mathbf{r}}$ con el campo eléctrico $\mathbf{E}(t) = -\frac{\partial \mathbf{A}}{\partial t}$:

$$ \hat{H}'(t) = -\hat{\mathbf{d}} \cdot \mathbf{E}(t) = e \hat{\mathbf{r}} \cdot \mathbf{E}_0 \cos(\omega t) $$

### 3. Teoría de Perturbaciones Dependiente del Tiempo

Para determinar cómo este Hamiltoniano dependiente del tiempo induce transiciones entre un estado inicial $|i\rangle$ y un estado final $|f\rangle$ (soluciones estacionarias de $\hat{H}_0$), empleamos la ecuación de Schrödinger dependiente del tiempo:

$$ i\hbar \frac{\partial |\Psi(t)\rangle}{\partial t} = (\hat{H}_0 + \hat{H}'(t)) |\Psi(t)\rangle $$

Expandimos la función de onda en la base de autoestados imperturbados $|n\rangle$ con autovalores $E_n$:

$$ |\Psi(t)\rangle = \sum_n c_n(t) e^{-iE_n t / \hbar} |n\rangle $$

Sustituyendo esta expansión en la ecuación de Schrödinger, multiplicando por $\langle f|$ e integrando sobre todo el espacio, obtenemos un sistema acoplado de ecuaciones diferenciales para los coeficientes de probabilidad $c_f(t)$:

$$ i\hbar \frac{dc_f(t)}{dt} = \sum_n c_n(t) \langle f | \hat{H}'(t) | n \rangle e^{i\omega_{fn} t} $$

Donde $\omega_{fn} = (E_f - E_n)/\hbar$ es la frecuencia de Bohr para la transición. A tiempo $t=0$, asumimos que el sistema se encuentra en el estado inicial exacto, es decir, $c_n(0) = \delta_{ni}$. En primer orden de perturbación, consideramos $c_n(t) \approx \delta_{ni}$ en el lado derecho de la ecuación. Así, la tasa de cambio de $c_f$ (para $f \neq i$) es:

$$ i\hbar \frac{dc_f^{(1)}(t)}{dt} \approx \langle f | \hat{H}'(t) | i \rangle e^{i\omega_{fi} t} $$

Para nuestra perturbación armónica $\hat{H}'(t) = \hat{V} e^{-i\omega t} + \hat{V}^\dagger e^{i\omega t}$ (donde $\hat{V} = e \hat{\mathbf{r}} \cdot \mathbf{E}_0 / 2$), la integración directa resulta en:

$$ c_f^{(1)}(t) = -\frac{i}{\hbar} \int_0^t \langle f | \hat{H}'(t') | i \rangle e^{i\omega_{fi} t'} dt' $$
$$ c_f^{(1)}(t) = -\frac{1}{\hbar} \left[ \langle f | \hat{V} | i \rangle \frac{e^{i(\omega_{fi}-\omega)t}-1}{\omega_{fi}-\omega} + \langle f | \hat{V}^\dagger | i \rangle \frac{e^{i(\omega_{fi}+\omega)t}-1}{\omega_{fi}+\omega} \right] $$

En el régimen de resonancia ($\omega \approx \omega_{fi}$ para absorción), el primer término domina drásticamente. Ignorando el segundo término (aproximación de onda rotatoria), la probabilidad de transición $P_{i \rightarrow f}(t) = |c_f^{(1)}(t)|^2$ resulta:

$$ P_{i \rightarrow f}(t) = \frac{|\langle f | \hat{V} | i \rangle|^2}{\hbar^2} \left[ \frac{\sin((\omega_{fi}-\omega)t/2)}{(\omega_{fi}-\omega)/2} \right]^2 $$

### 4. La Regla de Oro de Fermi

En la práctica, los estados finales en un continuo (o expuestos a radiación electromagnética que cubre un continuo de frecuencias) están descritos por una densidad de estados $\rho(E)$. La tasa de transición total $W_{i \rightarrow f}$ requiere integrar la probabilidad sobre este continuo:

$$ W_{i \rightarrow f} = \frac{d}{dt} \int P_{i \rightarrow f}(t) \rho(E_f) dE_f $$

En el límite de tiempos largos ($t \rightarrow \infty$), la función $[\sin(xt/2)/(x/2)]^2$ se vuelve extremadamente afilada alrededor de $x=0$, comportándose como la función delta de Dirac $2\pi t \delta(x)$. Reemplazando esto en la integral, derivamos la célebre **Regla de Oro de Fermi**:

$$ W_{i \rightarrow f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2 \rho(E_f) \delta(E_f - E_i \pm \hbar\omega) $$

Esta expresión captura la esencia de la espectroscopia: las transiciones están gobernadas estrictamente por la superposición mecano-cuántica del estado inicial, el estado final y el operador del campo.

### 5. Reglas de Selección (Transiciones Dipolares)

La probabilidad de transición depende del **elemento de matriz del dipolo** $\mathbf{M}_{fi} = \langle f | -e\hat{\mathbf{r}} | i \rangle$. Si esta integral de volumen es nula, la transición está "prohibida" (en primer orden).
Para un átomo hidrogenoide, las funciones de onda se separan en partes radiales y angulares: $\psi_{n,l,m}(\mathbf{r}) = R_{nl}(r) Y_l^m(\theta, \phi)$. El vector de posición $\mathbf{r}$ puede expresarse en términos de los armónicos esféricos de orden 1, $Y_1^\mu$.
Para que la integral angular $\int (Y_{l'}^{m'})^* Y_1^\mu Y_l^m d\Omega$ no se anule, deben cumplirse condiciones estrictas relacionadas con el teorema de Wigner-Eckart y la conservación del momento angular:

1. **Regla del cambio de paridad ($\Delta l$):** El momento dipolar es impar bajo inversión espacial ($\mathbf{r} \rightarrow -\mathbf{r}$). Para que la integral de todo el espacio sea simétrica, el estado final debe tener diferente paridad que el inicial:
   $$ \Delta l = l_f - l_i = \pm 1 $$
2. **Regla del número cuántico magnético ($\Delta m_l$):** Correspondiente a la conservación de la componente z del momento angular cuando se absorbe un fotón (que tiene espín 1):
   $$ \Delta m_l = m_f - m_i = 0, \pm 1 $$

### 6. Desdoblamiento de Niveles y Perturbaciones Estáticas

Más allá de la interacción dinámica con campos oscilantes, la espectroscopia también abarca el estudio de perturbaciones estáticas.

**El Efecto Zeeman:**
La aplicación de un campo magnético estático $\mathbf{B} = B\hat{\mathbf{z}}$ rompe la degeneración de los niveles atómicos. Un electrón con momento angular orbital $\mathbf{L}$ y momento angular de espín $\mathbf{S}$ posee un momento magnético $\boldsymbol{\mu} = -\frac{\mu_B}{\hbar}(\mathbf{L} + g_s\mathbf{S})$, donde $\mu_B = \frac{e\hbar}{2m_e}$ es el magnetón de Bohr y $g_s \approx 2$. El Hamiltoniano de perturbación es:

$$ \hat{H}_B = -\boldsymbol{\mu} \cdot \mathbf{B} = \frac{\mu_B B}{\hbar}(L_z + g_s S_z) $$

En el límite de campo débil (Efecto Zeeman Anómalo), donde el acoplamiento espín-órbita es mayor que la perturbación magnética, $\mathbf{J} = \mathbf{L} + \mathbf{S}$ es un buen número cuántico. La corrección de energía de primer orden usa el teorema de Wigner-Eckart (factor de Landé $g_J$):

$$ \Delta E_{m_J} = \langle J, m_J | \hat{H}_B | J, m_J \rangle = \mu_B g_J m_J B $$

donde el factor g de Landé se define matemáticamente como:

$$ g_J = 1 + \frac{J(J+1) - L(L+1) + S(S+1)}{2J(J+1)} $$

### 7. Diagrama de Procesos Espectroscópicos

```mermaid
graph TD
    classDef state fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef photon fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    classDef process fill:#f1f8e9,stroke:#33691e,stroke-width:2px;

    S1(Estado Base |i⟩):::state
    S2(Estado Excitado |f⟩):::state
    Ph1([Fotón Incidente ℏω]):::photon
    Ph2([Fotón Emitido ℏω]):::photon
    Ph3([Fotón Estimulado ℏω]):::photon
    
    Ph1 --> Abs(Absorción):::process
    S1 --> Abs
    Abs --> S2
    
    S2 --> SpE(Emisión Espontánea):::process
    SpE --> S1
    SpE --> Ph2
    
    S2 --> StE(Emisión Estimulada):::process
    Ph1 -.-> StE
    StE --> S1
    StE --> Ph3
    StE --> Ph1
```

### 8. Ejemplo Analítico Riguroso

**Problema:** Determinar el desdoblamiento de las líneas espectrales en un experimento del Efecto Zeeman Normal para la transición de un estado $nd$ ($L=2$, $S=0$) a un estado $np$ ($L=1$, $S=0$) sometido a un campo magnético $\mathbf{B} = B \hat{\mathbf{z}}$.

**Solución Demostrativa:**
1. Dado que $S=0$, estamos en un estado singlete. Consecuentemente, $\mathbf{J} = \mathbf{L}$ y el factor g de Landé se simplifica a $g_J = 1$.
2. Los desplazamientos de energía de los niveles individuales son $\Delta E = \mu_B m_L B$.
3. Para el nivel superior $nd$ ($L=2$), las proyecciones magnéticas son $m_{L_i} \in \{-2, -1, 0, 1, 2\}$.
4. Para el nivel inferior $np$ ($L=1$), las proyecciones son $m_{L_f} \in \{-1, 0, 1\}$.
5. La frecuencia original de la transición en ausencia de campo es $\nu_0 = \frac{E_{nd} - E_{np}}{h}$. Con el campo activado, las energías de transición modificadas se expresan como:
   $$ h\nu = (E_{nd} + \mu_B m_{L_i} B) - (E_{np} + \mu_B m_{L_f} B) = h\nu_0 + \mu_B B (m_{L_i} - m_{L_f}) $$
6. Aplicando la regla de selección dipolar $\Delta m_L = m_{L_f} - m_{L_i} \in \{0, \pm 1\}$:
   - Para $\Delta m_L = 0$ (transiciones $\pi$), el cambio de energía es cero: $h\nu = h\nu_0$.
   - Para $\Delta m_L = +1$ (transiciones $\sigma^+$), $h\nu = h\nu_0 - \mu_B B$.
   - Para $\Delta m_L = -1$ (transiciones $\sigma^-$), $h\nu = h\nu_0 + \mu_B B$.
7. **Conclusión:** Aunque haya $5 \times 3 = 15$ posibles pares de estados inicial-final, las estrictas reglas de selección limitan los decaimientos permitidos, observándose exactamente un triplete de Lorentz en el espectro: tres componentes polarizadas separadas energéticamente por una cantidad discreta y exacta de $\mu_B B$.

## 📝 Guía de Ejercicios Resueltos

### Ejercicio 1: Efecto Stark Lineal en el Átomo de Hidrógeno
Considere un átomo de hidrógeno en el primer estado excitado ($n=2$) sometido a un campo eléctrico externo uniforme $\vec{\mathcal{E}} = \mathcal{E}_0 \hat{z}$. Calcule el corrimiento de los niveles de energía utilizando la teoría de perturbaciones degenerada de primer orden.

**Solución paso a paso:**
1. Los estados degenerados para $n=2$ son $|2,0,0\rangle$, $|2,1,0\rangle$, $|2,1,1\rangle$, y $|2,1,-1\rangle$ en la base $|n,l,m\rangle$.
2. El Hamiltoniano de perturbación es $H' = e \mathcal{E}_0 z = e \mathcal{E}_0 r \cos\theta$.
3. Los elementos de matriz de $H'$ solo son no nulos si $\Delta m = 0$ y $\Delta l = \pm 1$ debido a las reglas de selección.
4. Por lo tanto, el único elemento no diagonal no nulo es entre $|2,0,0\rangle$ y $|2,1,0\rangle$:
   $$ \langle 2,0,0 | H' | 2,1,0 \rangle = e \mathcal{E}_0 \int d^3r \psi_{200}^* z \psi_{210} = -3 e \mathcal{E}_0 a_0 $$
   donde $a_0$ es el radio de Bohr.
5. La matriz de perturbación en la sub-base $\{|2,0,0\rangle, |2,1,0\rangle, |2,1,1\rangle, |2,1,-1\rangle\}$ es:
   $$ H' = \begin{pmatrix} 0 & -3ea_0\mathcal{E}_0 & 0 & 0 \\ -3ea_0\mathcal{E}_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} $$
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
   $$ N_{ex} = \int_0^\infty \frac{g(E)}{e^{\beta (E-\mu)} - 1} dE $$
3. En la temperatura crítica $T_c$, el potencial químico $\mu \to 0$ y $N_{ex} = N$.
4. Reemplazando $g(E)$ e introduciendo $x = E/k_B T_c$:
   $$ N = \frac{(k_B T_c)^3}{2(\hbar\omega)^3} \int_0^\infty \frac{x^2}{e^x - 1} dx $$
5. La integral es conocida como $\Gamma(3)\zeta(3) = 2 \times 1.202$.
6. Resolviendo para $T_c$:
   $$ N = \left( \frac{k_B T_c}{\hbar\omega} \right)^3 \zeta(3) \implies T_c = \frac{\hbar\omega}{k_B} \left( \frac{N}{\zeta(3)} \right)^{1/3} $$

## 💻 Simulaciones Computacionales

Esta simulación analiza cómo responde un sistema cuántico de dos niveles ante un pulso láser aplicando teoría dependiente del tiempo. Se simulan las Oscilaciones de Rabi bajo distintas desintonizaciones (detunings), observando cómo la absorción pierde eficiencia fuera de resonancia.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rabi_dynamics(state, t, Omega, Delta):
    """
    Ecuaciones diferenciales acopladas para los coeficientes de amplitud
    de un sistema de dos niveles (aproximación RWA).
    state = [Re(c_g), Im(c_g), Re(c_e), Im(c_e)]
    """
    cg_r, cg_i, ce_r, ce_i = state
    cg = cg_r + 1j*cg_i
    ce = ce_r + 1j*ce_i
    
    # Ecuaciones de Schrödinger con RWA
    dcg_dt = 1j * (Omega / 2.0) * ce * np.exp(1j * Delta * t)
    dce_dt = 1j * (Omega / 2.0) * cg * np.exp(-1j * Delta * t)
    
    return [np.real(dcg_dt), np.imag(dcg_dt), np.real(dce_dt), np.imag(dce_dt)]

t_span = np.linspace(0, 10, 500)
Omega_0 = 2.0 * np.pi  # Frecuencia de Rabi (Resonante)

# Condiciones iniciales: Población entera en el estado base |g>
initial_state = [1.0, 0.0, 0.0, 0.0]

# Diferentes valores de Desintonización (Detuning Delta)
detunings = [0.0, 1.0 * np.pi, 2.0 * np.pi]
colors = ['#d62728', '#2ca02c', '#1f77b4']

plt.figure(figsize=(9, 5))

for Delta, color in zip(detunings, colors):
    solution = odeint(rabi_dynamics, initial_state, t_span, args=(Omega_0, Delta))
    
    # Probabilidad de estar en el estado excitado |e>
    ce_real = solution[:, 2]
    ce_imag = solution[:, 3]
    prob_e = ce_real**2 + ce_imag**2
    
    label_str = 'Resonante ($\\Delta = 0$)' if Delta == 0 else f'Desintonizado ($\\Delta = {Delta/np.pi:.1f}\\pi$)'
    plt.plot(t_span, prob_e, lw=2, color=color, label=label_str)

plt.title("Oscilaciones de Rabi en un Sistema de Dos Niveles (Interacción Luz-Materia)")
plt.xlabel("Tiempo (Unidades Arbitrarias)")
plt.ylabel("Probabilidad de Excitación $P_e(t)$")
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.ylim(0, 1.05)
plt.tight_layout()
# plt.show()
```

## 📚 Recursos Específicos

### Cursos Específicos
1. [Light and Matter - MIT OCW](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/)
2. [Spectroscopy - Coursera](https://www.coursera.org/learn/spectroscopy)
3. [Atomic and Optical Physics - MIT (YouTube)](https://www.youtube.com/playlist?list=PLUl4u3cNGP62FPGcyFJkzhZZpaQTOuFI7)
4. [Quantum Optics - edX](https://www.edx.org/course/quantum-optics)
5. [Molecular Spectroscopy - University of Manchester](https://www.coursera.org/learn/spectroscopy)

### Artículos y Simulaciones
1. [Einstein, A. (1916). *Strahlungs-emission und -absorption nach der Quantentheorie*.](https://onlinelibrary.wiley.com/doi/abs/10.1002/andp.19163561702)
2. [PhET Simulation: Molecules and Light](https://phet.colorado.edu/en/simulations/molecules-and-light)
3. [PhET Simulation: Lasers](https://phet.colorado.edu/en/simulations/lasers)
4. [Townes, C. H., & Schawlow, A. L. (1955). *Microwave Spectroscopy*. McGraw-Hill.](https://store.doverpublications.com/048661798x.html)
5. [Bloembergen, N. (1982). *Nonlinear optics and spectroscopy*. Rev. Mod. Phys.](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.54.685)
6. [Schawlow, A. L. (1982). *Spectroscopy in a new light*. Rev. Mod. Phys.](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.54.697)
7. [PhET Simulation: Color Vision](https://phet.colorado.edu/en/simulations/color-vision)
8. [PhET Simulation: Blackbody Spectrum](https://phet.colorado.edu/en/simulations/blackbody-spectrum)
9. [Lamb, W. E., & Retherford, R. C. (1947). *Fine Structure of the Hydrogen Atom by a Microwave Method*.](https://journals.aps.org/pr/abstract/10.1103/PhysRev.72.241)
10. [Purcell, E. M. (1946). *Spontaneous Emission Probabilities at Radio Frequencies*.](https://journals.aps.org/pr/abstract/10.1103/PhysRev.69.37)

### 📖 Referencias Útiles y Bibliografía
- [Hollas, J. M. (2004). *Modern Spectroscopy*. John Wiley & Sons.](https://www.wiley.com/en-us/Modern+Spectroscopy%2C+4th+Edition-p-9780470844168)
- [Demtröder, W. (2014). *Laser Spectroscopy: Basic Concepts and Instrumentation*. Springer.](https://link.springer.com/book/10.1007/978-3-662-44641-6)
- [Bernath, P. F. (2015). *Spectra of Atoms and Molecules*. Oxford University Press.](https://global.oup.com/academic/product/spectra-of-atoms-and-molecules-9780190252215)
- [Loudon, R. (2000). *The Quantum Theory of Light*. Oxford University Press.](https://global.oup.com/academic/product/the-quantum-theory-of-light-9780198501763)
