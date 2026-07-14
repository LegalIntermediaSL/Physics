# Cosmología del Big Bang

La Cosmología del Big Bang es el modelo estándar sobre el origen y evolución del universo, que postula que este comenzó en un estado extremadamente caliente y denso hace unos 13.800 millones de años, y ha estado expandiéndose y enfriándose desde entonces.

## 📜 Contexto Histórico

En la década de 1920, las soluciones a las ecuaciones de la Relatividad General de Einstein por parte de Alexander Friedmann (1922) y Georges Lemaître (1927) sugerían que el universo no era estático, sino dinámico (pudiendo expandirse o contraerse). Einstein, prefiriendo un universo estático, introdujo la Constante Cosmológica para forzar esta quietud.

Sin embargo, en 1929, Edwin Hubble descubrió la **Ley de Hubble-Lemaître**: las galaxias se alejan de nosotros con una velocidad proporcional a su distancia, la primera prueba empírica de la expansión del universo. Lemaître propuso la teoría del "Átomo Primigenio", sugiriendo que si hoy el universo se expande, en el pasado debió estar concentrado en un punto.

El modelo rival de Estado Estacionario (Fred Hoyle, 1948) perdió apoyo definitivamente cuando en 1964 Arno Penzias y Robert Wilson descubrieron accidentalmente el **Fondo Cósmico de Microondas (CMB)**, el remanente térmico previsto por la teoría del Big Bang. En los 90s, el estudio de supernovas tipo Ia reveló que esta expansión está acelerada debido a la llamada **Energía Oscura**.

---

## 🧮 Desarrollo Teórico Profundo

El modelo cosmológico estándar, basado en la Relatividad General, se sustenta en el **Principio Cosmológico**, que establece que a gran escala, el universo es homogéneo e isótropo (igual en todas partes y en todas direcciones).

### 1. La Métrica FLRW

La única geometría del espacio-tiempo que satisface este principio es descrita por la **Métrica de Friedmann-Lemaître-Robertson-Walker (FLRW)**. En coordenadas comóviles $(t, r, \theta, \phi)$, el elemento de línea es:

$$
ds^2 = c^2 dt^2 - a^2(t) \left[ \frac{dr^2}{1 - kr^2} + r^2 (d\theta^2 + \sin^2\theta d\phi^2) \right]
$$

- $t$ es el tiempo cósmico, medido por un observador comóvil (en reposo respecto a la expansión local).
- $a(t)$ es el **factor de escala**, que parametriza la expansión del universo (usualmente normalizado para que $a(t_0) = 1$ en el presente).
- $k$ es la constante de curvatura espacial:
  - $k = +1$: Geometría esférica (universo cerrado).
  - $k = 0$: Geometría euclidiana (universo plano).
  - $k = -1$: Geometría hiperbólica (universo abierto).

```mermaid
graph TD
    A[Métrica FLRW] --> B{Parámetro de Curvatura k}
    B -->|k = +1| C(Universo Cerrado: Finita, sin fronteras)
    B -->|k = 0| D(Universo Plano: Infinito, expansión crítica)
    B -->|k = -1| E(Universo Abierto: Infinito, expansión eterna)
    A --> F[Factor de Escala a]
    F --> G(Expansión Temporal)
```

### 2. Las Ecuaciones de Friedmann

Al insertar la métrica FLRW y un tensor de energía-impulso para un fluido perfecto ($T^\mu_\nu = \text{diag}(\rho c^2, -P, -P, -P)$) en las ecuaciones de campo de Einstein, obtenemos las dos **Ecuaciones de Friedmann**.

**Primera Ecuación de Friedmann (Ecuación de la Expansión):**
Derivada de la componente temporal de las ecuaciones de Einstein, gobierna la tasa de expansión:

$$
H^2 \equiv \left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}
$$

Donde $H(t)$ es el Parámetro de Hubble, $\rho$ es la densidad total de materia/radiación y $\Lambda$ es la constante cosmológica.

**Segunda Ecuación de Friedmann (Ecuación de Aceleración o de Raychaudhuri):**
Derivada de las componentes espaciales:

$$
\frac{\ddot{a}}{a} = -\frac{4\pi G}{3} \left( \rho + \frac{3P}{c^2} \right) + \frac{\Lambda c^2}{3}
$$

Esta ecuación muestra que tanto la masa-energía ($\rho$) como la presión ($P$) contribuyen a frenar la expansión cósmica (de ahí el signo menos), a menos que predomine el término $\Lambda$.

### 3. Ecuación de Continuidad y Evolución de las Especies Cósmicas

Por conservación de la energía ($\nabla_\mu T^{\mu 0} = 0$), obtenemos la ecuación termodinámica del fluido cósmico:

$$
\dot{\rho} + 3\frac{\dot{a}}{a}\left(\rho + \frac{P}{c^2}\right) = 0
$$

El comportamiento de $\rho(a)$ depende de la **Ecuación de Estado** termodinámica $P = w \rho c^2$, donde $w$ es un parámetro adimensional:

- **Materia no relativista (Polvo):** Partículas moviéndose muy por debajo de $c$, como galaxias y materia oscura. Tienen $w = 0 \implies P = 0$.
  Integrando la ecuación de continuidad: $\rho_m \propto a^{-3}$ (se diluye con el volumen).
- **Radiación (y materia ultra-relativista):** Tienen $w = 1/3$.
  Integrando: $\rho_r \propto a^{-4}$. Cae más rápido que la materia debido a que el factor de escala no solo diluye la densidad numérica, sino que estira la longitud de onda de cada fotón (desplazamiento al rojo cosmológico $E \propto 1/a$).
- **Energía Oscura (Constante Cosmológica):** Tiene presión negativa $w = -1 \implies P = -\rho_\Lambda c^2$.
  Integrando: $\rho_\Lambda = \text{constante}$. La densidad no cambia a pesar de la expansión cósmica.

### 4. Parámetros de Densidad y el Universo Concordante

Es útil dividir la densidad por la **Densidad Crítica** $\rho_c$, que es la densidad exacta necesaria para un universo plano ($k=0, \Lambda=0$):

$$
\rho_c(t) = \frac{3H(t)^2}{8\pi G}
$$

Definimos los parámetros de densidad adimensionales $\Omega_i = \rho_i / \rho_c$. La primera ecuación de Friedmann puede escribirse como una regla de suma:

$$
\Omega_m + \Omega_r + \Omega_\Lambda + \Omega_k = 1
$$

Donde $\Omega_k = -kc^2 / (a^2 H^2)$. Las observaciones actuales (como la misión Planck) indican que nuestro universo es plano ($\Omega_k \approx 0$), compuesto aproximadamente por $\Omega_\Lambda \approx 0.68$, $\Omega_m \approx 0.32$ (materia oscura + bariónica), y una cantidad insignificante de radiación $\Omega_r \sim 10^{-4}$ en la era actual.

---

## 🛠 Ejemplo Práctico

**Problema:** Calcula la edad del Universo asumiendo un modelo plano ($k=0$) dominado únicamente por materia ($\Omega_m = 1$). Si la constante de Hubble actual es $H_0 \approx 70 \text{ km s}^{-1} \text{ Mpc}^{-1}$, ¿cuál es la edad en años?

**Solución paso a paso:**
1. En un universo dominado por la materia, $\rho(t) \propto a^{-3}$. Específicamente, $\rho = \rho_0 a^{-3}$ asumiendo $a_0 = 1$.
2. La ecuación de Friedmann es:

   

$$
\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3} \frac{\rho_0}{a^3} \implies \dot{a}^2 = \frac{H_0^2}{a}
$$

   Donde hemos usado que en $t_0$, $H_0^2 = \frac{8\pi G}{3} \rho_0$.
3. Despejamos $dt$:

   

$$
\dot{a} = \frac{da}{dt} = H_0 a^{-1/2} \implies dt = \frac{1}{H_0} a^{1/2} da
$$

4. Integramos desde el Big Bang ($t=0, a=0$) hasta hoy ($t=t_0, a=1$):

   

$$
\int_0^{t_0} dt = \frac{1}{H_0} \int_0^1 a^{1/2} da
$$

   

$$
t_0 = \frac{1}{H_0} \left[ \frac{2}{3} a^{3/2} \right]_0^1 = \frac{2}{3 H_0}
$$

5. Convertimos $H_0$ a unidades SI ($s^{-1}$). Sabemos que $1 \text{ Mpc} = 3.086 \times 10^{19} \text{ km}$.

   

$$
H_0 = \frac{70 \text{ km/s}}{1 \text{ Mpc}} = \frac{70}{3.086 \times 10^{19}} \text{ s}^{-1} \approx 2.268 \times 10^{-18} \text{ s}^{-1}
$$

6. El inverso de la constante de Hubble, conocido como el *Tiempo de Hubble*, es:

   

$$
t_H = \frac{1}{H_0} \approx \frac{1}{2.268 \times 10^{-18} \text{ s}^{-1}} \approx 4.409 \times 10^{17} \text{ s}
$$

7. Convertimos a años ($1 \text{ año} \approx 3.154 \times 10^7 \text{ s}$):

   

$$
t_H = \frac{4.409 \times 10^{17}}{3.154 \times 10^7} \approx 13.98 \times 10^9 \text{ años} = 13.98 \text{ mil millones de años}
$$

8. La edad para un universo puramente dominado por materia es $t_0 = \frac{2}{3} t_H$:

   

$$
t_0 = \frac{2}{3} \times 13.98 \times 10^9 \approx 9.32 \text{ mil millones de años}
$$

9. **Conclusión:** Este resultado ($9.32 \times 10^9$ años) es notablemente inferior a la edad observada de los cúmulos estelares más antiguos ($\sim 13$ mil millones). Fue la adición de la energía oscura (que cambia la relación integral de $t_0$) la que resolvió el "problema de la edad", arrojando el valor exacto de $13.8$ mil millones de años.

---

## 📝 Guía de Ejercicios Resueltos

**Problema 1: Temperatura del fondo cósmico y factor de escala**
Sabiendo que el fondo cósmico de microondas (CMB) sigue un espectro de cuerpo negro, demuestre cómo varía la temperatura del CMB $T$ con el factor de escala cósmico $a(t)$. Calcule a qué factor de escala se formó el CMB si la temperatura de recombinación fue de $3000\text{ K}$ y hoy es de $2.725\text{ K}$.

**Solución paso a paso:**
1. **Conservación del número de fotones:**
   En un volumen comóvil en expansión $V \propto a^3$, el número de fotones es constante. La densidad numérica de fotones de un cuerpo negro es $n_\gamma \propto T^3$.
   Por tanto, $n_\gamma a^3 = \text{constante} \implies T^3 a^3 = \text{constante} \implies T \propto 1/a$.
   Alternativamente, el corrimiento al rojo $1+z = \lambda_0/\lambda = a_0/a$. La energía de un fotón $E \propto 1/\lambda \propto a^{-1}$. Como $E \sim k_B T$, tenemos que $T(a) = T_0 / a$ (con $a_0 = 1$).
2. **Cálculo del factor de escala:**
   Sabiendo que $T(a) = \frac{T_0}{a}$:
   $a_{rec} = \frac{T_0}{T_{rec}} = \frac{2.725}{3000} \approx 9.08 \times 10^{-4}$.
   Esto corresponde a un corrimiento al rojo $z = \frac{1}{a} - 1 \approx 1100$.

**Problema 2: Distancia Luminosa vs Distancia Comóvil**
Derive la relación matemática general entre la distancia de luminosidad $d_L$ y la distancia comóvil radial $\chi$ en función del factor de escala de emisión $a_e$ (o corrimiento al rojo $z$).

**Solución paso a paso:**
1. **Flujo y luminosidad:**
   La distancia luminosa se define mediante la conservación del flujo medido: $F = \frac{L_{int}}{4\pi d_L^2}$.
2. **Propagación en el espacio en expansión:**
   Supongamos una fuente cosmológica con luminosidad intrínseca $L_{int}$ (energía / tiempo en el emisor).
   El número de fotones emitidos cruza una esfera de radio comóvil actual $d_c$. El área de esta esfera es $4\pi d_c^2$ (asumiendo universo plano, $k=0$, por lo que $d_c = \chi$).
3. **Pérdida de energía y dilatación temporal:**
   Cada fotón recibido pierde energía por el redshift cosmológico: $E_{rec} = E_{em} / (1+z) = E_{em} \cdot a_e$.
   El intervalo de tiempo de emisión y recepción se dilata: $dt_{rec} = dt_{em} (1+z) = dt_{em} / a_e$.
   El flujo observado es $F = \frac{L_{rec}}{\text{Área}} = \frac{E_{rec}/dt_{rec}}{4\pi d_c^2} = \frac{ (E_{em} / (1+z)) / (dt_{em} (1+z)) }{4\pi d_c^2} = \frac{L_{int}}{4\pi d_c^2 (1+z)^2}$.
4. **Identificación de $d_L$:**
   Comparando con la definición, obtenemos $d_L^2 = d_c^2 (1+z)^2$, de donde resulta:
   $d_L = d_c (1+z) = \frac{d_c}{a_e}$.
   En un universo plano, $d_c = c \int_0^z \frac{dz'}{H(z')}$, lo que permite vincular observables fotométricos a la historia de la expansión.

**Problema 3: Edad del universo con Materia y Constante Cosmológica**
Calcule la edad de un universo plano compuesto sólo de materia no relativista $\Omega_m$ y energía oscura (constante cosmológica $\Omega_\Lambda = 1 - \Omega_m$). Determine el límite de $t(a)$ cuando $a \rightarrow 0$ y expréselo en función de $H_0$.

**Solución paso a paso:**
1. La ecuación de Friedmann es:
   $H^2 = H_0^2 \left( \Omega_m a^{-3} + \Omega_\Lambda \right)$.
2. Sustituyendo $H = \frac{\dot{a}}{a}$:
   $\dot{a} = H_0 \sqrt{\Omega_m a^{-1} + \Omega_\Lambda a^2}$.
   $dt = \frac{1}{H_0} \frac{da}{\sqrt{\Omega_m a^{-1} + \Omega_\Lambda a^2}} = \frac{1}{H_0} \frac{\sqrt{a} da}{\sqrt{\Omega_m + \Omega_\Lambda a^3}}$.
3. Para hallar la edad a un factor de escala $a$:
   $t(a) = \frac{1}{H_0} \int_0^a \frac{x^{1/2} dx}{\sqrt{\Omega_m + \Omega_\Lambda x^3}}$.
4. Hacemos el cambio de variable $u = \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} x^{3/2} \implies du = \frac{3}{2} \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} x^{1/2} dx$.
   El integrando se transforma en:
   $t(a) = \frac{2}{3H_0 \sqrt{\Omega_\Lambda}} \int \frac{du}{\sqrt{1 + u^2}}$.
5. La primitiva es $\text{arsinh}(u)$, evaluada de 0 a $u(a)$:
   $t(a) = \frac{2}{3H_0 \sqrt{\Omega_\Lambda}} \text{arsinh} \left( \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} a^{3/2} \right)$.
   Para el tiempo actual $a=1$:
   $t_0 = \frac{2}{3H_0 \sqrt{\Omega_\Lambda}} \text{ln} \left( \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} + \sqrt{\frac{\Omega_\Lambda}{\Omega_m} + 1} \right)$.
   Con $\Omega_m \approx 0.3, \Omega_\Lambda \approx 0.7$, arroja el valor exacto $\sim 13.8$ Gyr.

## 💻 Simulaciones Computacionales

Esta simulación resuelve numéricamente la Ecuación de Friedmann utilizando `scipy.integrate.odeint` para rastrear el factor de escala $a(t)$ del universo bajo diferentes composiciones cosmológicas (materia, radiación y energía oscura).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constante de Hubble actual (normalizada a 1 para tiempo cósmico t_H)
H0 = 1.0 

def friedmann_eq(a, t, Omega_m, Omega_r, Omega_L):
    # da/dt = H0 * sqrt(Omega_m/a + Omega_r/a^2 + Omega_L*a^2 + Omega_k)
    # Asumimos universo plano: Omega_k = 1 - (Omega_m + Omega_r + Omega_L)
    Omega_k = 1.0 - (Omega_m + Omega_r + Omega_L)
    
    # Evitar singularidad en a=0
    if a < 1e-5:
        a = 1e-5
        
    dadt = H0 * np.sqrt(Omega_m / a + Omega_r / (a**2) + Omega_L * (a**2) + Omega_k)
    return dadt

# Tiempos cósmicos (en unidades de 1/H0)
t = np.linspace(0, 2.0, 500)
a0 = 1e-4 # Factor de escala inicial pequeño

# Diferentes modelos de universo
models = {
    'Materia ($\\Omega_m=1$)': (1.0, 0.0, 0.0),
    'Radiación ($\\Omega_r=1$)': (0.0, 1.0, 0.0),
    'Energía Oscura ($\\Omega_\\Lambda=1$)': (0.0, 0.0, 1.0),
    'LCDM (Concordancia)': (0.3, 0.0, 0.7)
}

plt.figure(figsize=(10, 6))

for name, (Om, Or, OL) in models.items():
    a = odeint(friedmann_eq, a0, t, args=(Om, Or, OL))
    plt.plot(t, a, label=name, lw=2)

plt.axhline(1.0, color='k', linestyle='--', alpha=0.5, label='Hoy ($a=1$)')
plt.title('Evolución del Factor de Escala Cósmico $a(t)$')
plt.xlabel('Tiempo Cósmico (Unidades $1/H_0$)')
plt.ylabel('Factor de Escala $a$')
plt.ylim(0, 3)
plt.legend()
plt.grid(True)
plt.show()
```

## 🚀 Fronteras de Investigación y Problemas Abiertos

La cosmología en 2026 se encuentra en una fase de "crisis fértil" debido a las precisiones observacionales que han puesto a prueba el modelo estándar $\Lambda$CDM. El problema más candente es la "Tensión de $H_0$", una discrepancia estadísticamente insalvable (>5$\sigma$) entre la constante de Hubble medida localmente (mediante Cefeidas y supernovas) y la deducida de la radiación de fondo de microondas (CMB) en el universo temprano. Esta tensión sugiere nueva física: energía oscura temprana (Early Dark Energy), interacciones oscuras, o especies de neutrinos ligeros estériles. Al mismo tiempo, la búsqueda incansable de la señal de los **modos B primordiales** en la polarización del CMB (por satélites y telescopios terrestres de próxima generación como el Simons Observatory y CMB-S4) pretende ofrecer la confirmación definitiva de la época inflacionaria y fijar la escala de energía de la gravedad cuántica, mediante la detección de ondas gravitacionales tensor-a-escalar. La asimetría bariónica del universo (por qué hay más materia que antimateria) sigue siendo otro de los misterios insondables que une la cosmología y la física de partículas.

## 📐 Formalismo Matemático Avanzado (Nivel Posgrado/Doctorado)

La cosmología moderna se fundamenta en la **Teoría de Perturbaciones Cosmológicas Relativistas**, crucial para entender cómo las fluctuaciones cuánticas del vacío se expandieron inflacionariamente para formar la estructura cósmica a gran escala. Partimos de la métrica de Friedmann-Lemaître-Robertson-Walker (FLRW) perturbada. En el calibre longitudinal (o calibre conforme newtoniano), la métrica perturbada con perturbaciones escalares se escribe usando el tiempo conforme $\eta$:

$$
ds^2 = a^2(\eta) \left[ -(1 + 2\Phi)d\eta^2 + (1 - 2\Psi)\gamma_{ij} dx^i dx^j \right]
$$

donde $a(\eta)$ es el factor de escala, y $\Phi$ y $\Psi$ son los potenciales métricos de Bardeen (que son invariantes gauge).

La dinámica del universo temprano está dominada por un campo escalar inflatón $\varphi = \varphi_0(\eta) + \delta\varphi(x, \eta)$. Expandiendo las ecuaciones de Einstein y la ecuación de Klein-Gordon a primer orden, introducimos la variable conjugada invariante de Mukhanov-Sasaki $v = a \left( \delta\varphi + \frac{\varphi_0'}{\mathcal{H}}\Phi \right)$, donde $\mathcal{H} = a'/a$. La cuantización de las perturbaciones se realiza promoviendo $v$ a un operador que satisface la **Ecuación de Mukhanov-Sasaki**:

$$
v_k'' + \left( k^2 - \frac{z''}{z} \right) v_k = 0
$$

con $z = a\varphi_0' / \mathcal{H}$. 

El estado de vacío de Bunch-Davies proporciona las condiciones iniciales en el límite asintótico $k \gg \mathcal{H}$ (modos sub-horizonte) con $v_k(\eta) \simeq e^{-ik\eta} / \sqrt{2k}$. Al evolucionar estos modos fuera del horizonte de Hubble durante la inflación cósmica ($k \ll \mathcal{H}$), sus amplitudes se "congelan". El espectro de potencia adimensional primordial $\mathcal{P}_\mathcal{R}(k)$ para la curvatura comóvil $\mathcal{R} = v/z$ evaluado a la salida del horizonte es:

$$
\mathcal{P}_\mathcal{R}(k) = \frac{k^3}{2\pi^2} |\mathcal{R}_k|^2 \approx \frac{H^2}{8\pi^2 M_{Pl}^2 \epsilon}
$$

donde $\epsilon = -\dot{H}/H^2$ es el parámetro de slow-roll (rodadura lenta) de la inflación. Este formalismo riguroso es el que predice el espectro de Harrison-Zel'dovich casi invariante de escala ($n_s \approx 0.965$) que ha sido confirmado con asombrosa precisión por el satélite Planck.

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **[MIT OpenCourseWare: 8.286 The Early Universe (Alan Guth)](https://ocw.mit.edu/courses/8-286-the-early-universe-fall-2013/)** - Un curso magistral en video dictado por el mismísimo arquitecto de la teoría de la inflación cósmica. Cubre métricas FLRW, materia oscura, bariogénesis y radiación primordial sin requerir cálculo tensorial previo en RG extrema.
2. **[Stanford University: Cosmology (Leonard Susskind)](https://theoreticalminimum.com/courses/cosmology/2013/winter)** - Parte del ciclo "The Theoretical Minimum", desarrolla de manera precisa y amena las matemáticas de las Ecuaciones de Friedmann y la evolución del factor de escala.
3. **[UC Irvine: Physics 20B - Cosmology (James Bullock)](https://www.youtube.com/playlist?list=PLqOZ6FD_RQ7nwb-mX-Z6G5fFv9yO-F18i)** - Destacada serie de clases de pregrado que detalla la historia térmica del universo temprano, Big Bang Nucleosynthesis (BBN) y la formación del CMB.
4. **[Perimeter Institute: Cosmology (PSI Lectures)](https://pirsa.org/)** - Charlas y seminarios avanzados que discuten la física teórica contemporánea de la inflación (teoría de perturbaciones) y el problema moderno de la tensión de Hubble.

### 📝 Artículos Científicos Históricos y Avanzados

1. **A Relation between Distance and Radial Velocity among Extra-Galactic Nebulae (Una relación entre la distancia y la velocidad radial entre nebulosas extragalácticas)**  
   *Edwin Hubble (1929)*. [Proceedings of the National Academy of Sciences, 15(3), 168-173](https://www.pnas.org/doi/10.1073/pnas.15.3.168).  
   **Importancia Teórica:** El hito observacional fundacional de la cosmología moderna. Utilizando Cefeidas para medir distancias, Hubble demostró de forma concluyente que las galaxias ("nebulosas espirales") no solo están fuera de la Vía Láctea, sino que se alejan sistemáticamente, probando la expansión métrica del espacio.  
   **Fondo Matemático:** Establece empíricamente la Ley de Hubble (hoy Hubble-Lemaître), relacionando la velocidad de recesión aparente $v$ (obtenida del corrimiento al rojo $z$ estelar) con la distancia propia $D$:

   

$$
v = H_0 D
$$

   **Implicaciones Físicas:** Demolió el modelo del "Universo Estático" propuesto inicialmente por Einstein y condujo directamente a la formulación empírica del origen del universo a partir de un punto concentrado: el "Átomo Primigenio" (Big Bang).

2. **A Measurement of Excess Antenna Temperature at 4080 Mc/s (Una medida del exceso de temperatura de antena a 4080 Mc/s)**  
   *Arno Penzias & Robert Wilson (1965)*. [The Astrophysical Journal, 142, 419-421](https://ui.adsabs.harvard.edu/abs/1965ApJ...142..419P/abstract).  
   **Importancia Teórica:** Confirma de forma accidental pero decisiva el Fondo Cósmico de Microondas (CMB), la radiación térmica isotrópica fósil predicha teóricamente por Gamow, Alpher y Herman para un universo que comenzó en un estado extremadamente caliente y se ha enfriado por expansión.  
   **Fondo Matemático:** Observan un ruido de fondo que corresponde a un espectro de cuerpo negro perfecto no direccional, validando la ley del desplazamiento de Wien termodinámica en cosmología:

   

$$
T(z) = T_0 (1 + z)
$$

   A un $z \approx 1100$ (era de la recombinación atómica), la temperatura cayó por debajo del límite de ionización del hidrógeno (unos $3000\text{ K}$), liberando para siempre el baño de fotones al universo, que hoy medimos enfriado astronómicamente a $T_0 = 2.725\text{ K}$.  
   **Implicaciones Físicas:** Hizo descartar por completo el Modelo del Estado Estacionario (Steady State) en cosmología, consolidando al Big Bang como la única teoría aceptada de la evolución cósmica general.

3. **Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant (Evidencia observacional con supernovas de un universo en aceleración y una constante cosmológica)**  
   *A. Riess et al. (High-Z Supernova Search Team) & S. Perlmutter et al. (Supernova Cosmology Project) (1998/1999)*. [The Astronomical Journal, 116(3), 1009-1038](https://iopscience.iop.org/article/10.1086/300499).  
   **Importancia Teórica:** El descubrimiento más revolucionario en astrofísica de finales del s. XX, demostrando que la expansión del universo no se está frenando por la gravedad mutua de la materia, sino que está acelerando positivamente.  
   **Fondo Matemático:** Midiendo explosiones de Supernovas Tipo Ia lejanas como candelas estándar (determinando así su distancia luminosa $d_L$), hallaron que están mucho más tenues de lo esperado en un universo dominado por la materia. Esto obliga a incluir un término positivo dominante de "Energía Oscura" ($\Omega_\Lambda$) en la Ecuación de Aceleración de Friedmann-Raychaudhuri:

   

$$
\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\rho_m + \frac{\Lambda c^2}{3} > 0
$$

   **Implicaciones Físicas:** Llevó a la adopción formal del modelo Concordante Lambda-CDM ($\Lambda$CDM), donde el ~68% del cosmos se compone de una repulsión de vacío inexplicable, sellando el destino de un "Big Freeze" (muerte térmica) eterna e insalvable para nuestro universo.

### 📖 Referencias Útiles y Bibliografía
1. **Barbara Ryden - [Introduction to Cosmology (Cambridge University Press)](https://www.cambridge.org/highereducation/books/introduction-to-cosmology/A7080DA9D6A9C5D089E4670DAB5259B2)** - Posiblemente el libro de introducción pedagógica más claro y ameno a nivel de pregrado, excepcional para derivar y aplicar en ejercicios prácticos la métrica FLRW y las ecuaciones de Friedmann.
2. **Steven Weinberg - [Cosmology (Oxford University Press)](https://global.oup.com/academic/product/cosmology-9780198526827)** - Una joya moderna e implacablemente rigurosa firmada por un físico ganador del Premio Nobel, enfocada explícitamente en el desarrollo avanzado de tensores y perturbaciones cosmológicas inflacionarias (posgrado).
3. **Scott Dodelson & Fabian Schmidt - [Modern Cosmology (Academic Press, 2da Ed)](https://shop.elsevier.com/books/modern-cosmology/dodelson/978-0-12-815948-4)** - El estándar contemporáneo indispensable y avanzado que enseña explícitamente cómo interpretar analíticamente el espectro de potencias del CMB y analizar numéricamente las anisotropías térmicas cósmicas.

## 🌐 Seminarios Avanzados y Literatura de Frontera

### Seminarios y Cursos Avanzados
1. [Perimeter Institute Recorded Seminars (PIRSA) - Cosmology](https://pirsa.org/) - Conferencias teóricas y experimentales en la frontera del Big Bang y el universo temprano.
2. [CERN Theoretical Physics Department Seminars](https://theory.cern/) - Discusiones sobre la física de partículas en el universo primordial y modelos inflacionarios.
3. [Kavli Institute for Cosmological Physics (KICP) Seminars](https://kicp.uchicago.edu/) - Charlas en profundidad sobre radiación cósmica de fondo y energía oscura.

### Literatura de Frontera
1. [Planck 2018 results. VI. Cosmological parameters (Astronomy & Astrophysics)](https://www.aanda.org/articles/aa/full_html/2020/08/aa33910-18/aa33910-18.html) - Resultados cruciales de la misión Planck que definen el modelo estándar de la cosmología $\Lambda$CDM moderno.
2. [Inflationary cosmology: Exploring the Universe from the smallest to the largest scales (Physics Reports)](https://www.sciencedirect.com/science/article/pii/S037015731500196X) - Una revisión extensiva de los modelos inflacionarios y sus firmas observacionales.
3. [Observation of Gravitational Waves from a Binary Black Hole Merger (Physical Review Letters)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102) - El descubrimiento fundamental de ondas gravitacionales, abriendo una nueva era para estudiar el universo distante.
