# Galaxias

El estudio de las Galaxias comprende la dinámica, formación, evolución y morfología de las estructuras masivas unidas gravitacionalmente que contienen estrellas, gas estelar, polvo cósmico y materia oscura.

## 📜 Contexto Histórico

Hasta principios del siglo XX, muchos astrónomos creían que la Vía Láctea constituía la totalidad del universo, y que las "nebulosas espirales" observadas eran sistemas solares en formación dentro de nuestra galaxia. Este debate culminó en 1920 con el "Gran Debate" entre Harlow Shapley y Heber Curtis.

En 1924, Edwin Hubble resolvió el debate al utilizar estrellas variables Cefeidas en la galaxia de Andrómeda para medir su distancia. Hubble demostró que Andrómeda estaba mucho más allá de los límites de la Vía Láctea, probando que el universo contiene múltiples "universos islas" o galaxias. En 1926, Hubble creó el sistema de **Clasificación Morfológica de Galaxias** (el "Diapasón de Hubble"), clasificándolas en Elípticas, Espirales y Lenticulares.

Posteriormente, en la década de 1970, Vera Rubin observó las curvas de rotación de las galaxias espirales. Encontró que las estrellas en los bordes de la galaxia se movían demasiado rápido para ser contenidas por la masa visible, proporcionando una de las evidencias más fuertes de la existencia del **Halo de Materia Oscura**.

---

## 🧮 Desarrollo Teórico Profundo

La dinámica galáctica no puede entenderse únicamente en base a la materia luminosa visible (estrellas y gas). El modelado riguroso del movimiento estelar requiere la formulación teórica de los potenciales gravitatorios y la inclusión de la materia oscura.

### 1. Ecuación de Boltzmann sin Colisiones

A diferencia de las moléculas en un gas, el tiempo entre colisiones físicas directas de estrellas en una galaxia es mucho mayor que la edad del universo (son sistemas no colisionales). Por tanto, modelamos la galaxia como un fluido en el espacio de fases (posición $\mathbf{x}$ y velocidad $\mathbf{v}$), descrito por una función de distribución de densidad $f(\mathbf{x}, \mathbf{v}, t)$.

La evolución de este fluido está regida por la **Ecuación de Boltzmann sin Colisiones** (o ecuación de Vlasov):

$$ \frac{\partial f}{\partial t} + \mathbf{v} \cdot \nabla_{\mathbf{x}} f - \nabla_{\mathbf{x}} \Phi \cdot \nabla_{\mathbf{v}} f = 0 $$

Donde $\Phi(\mathbf{x}, t)$ es el potencial gravitatorio medio suave generado por todas las estrellas y la materia oscura juntas. Este potencial, a su vez, debe satisfacer la Ecuación de Poisson:

$$ \nabla^2 \Phi = 4\pi G \int f(\mathbf{x}, \mathbf{v}, t) d^3\mathbf{v} = 4\pi G \rho(\mathbf{x}, t) $$

El acoplamiento de estas dos ecuaciones gobierna la estructura y evolución de los sistemas estelares masivos.

### 2. Teorema del Virial y Masas Galácticas

Para un sistema galáctico autogravitante en estado estacionario, el Teorema del Virial relaciona la energía cinética total $K$ con la energía potencial gravitatoria total $U$:

$$ 2K + U = 0 $$

Dado que $K = \frac{1}{2} M \langle v^2 \rangle$ (donde $\langle v^2 \rangle$ es la dispersión de velocidades cuadrática media) y $U \approx -\frac{GM^2}{R}$ (donde $R$ es un radio característico), podemos estimar la "masa dinámica" total $M$ de la galaxia midiendo la dispersión de velocidades estelar:

$$ M \approx \frac{R \langle v^2 \rangle}{G} $$

Al aplicar esto a cúmulos de galaxias (como hizo Fritz Zwicky en 1933) o a galaxias individuales (Vera Rubin en los 70s), se descubrió que la masa dinámica superaba masivamente (de 5 a 50 veces) a la masa luminosa observada.

### 3. Curvas de Rotación y Halos de Materia Oscura

En una galaxia espiral, asumimos órbitas circulares para el gas y las estrellas en el disco galáctico. La velocidad de rotación $v_c(r)$ se iguala centrípetamente al campo gravitacional:

$$ \frac{v_c^2(r)}{r} = \frac{d\Phi}{dr} = \frac{G M(r)}{r^2} \implies v_c(r) = \sqrt{\frac{G M(r)}{r}} $$

Donde $M(r)$ es la masa encerrada en la esfera de radio $r$. Si asumimos que la masa está solo en el disco luminoso y el bulto central, $M(r)$ se volvería constante fuera del centro visible ($M(r) \approx M_{\text{tot}}$), por lo que esperaríamos un declive kepleriano en la velocidad:
$$ v_c(r) \propto \frac{1}{\sqrt{r}} $$

Sin embargo, las curvas de rotación observadas son característicamente planas ($v_c(r) \approx \text{constante} = V_0$) para radios grandes. Esto requiere que matemáticamente:
$$ M(r) = \frac{V_0^2 r}{G} \implies M(r) \propto r $$

Para que la masa aumente linealmente con el radio, debe existir un vasto componente esférico no luminoso, el **halo de materia oscura**, con un perfil de densidad que se asintotiza como la *esfera isoterma singular*:
$$ \rho_{\text{DM}}(r) = \frac{1}{4\pi r^2} \frac{dM(r)}{dr} = \frac{V_0^2}{4\pi G r^2} \propto r^{-2} $$

Este halo domina el potencial gravitacional en las regiones exteriores, asegurando la estabilidad del disco galáctico visible (evitando inestabilidades de barra que de otro modo lo destruirían rápidamente, según el criterio de Ostriker-Peebles).

```mermaid
graph LR
    A[Masa Luminosa] -->|Estrellas / Gas| B[Potencial Visible]
    C[Materia Oscura] -->|Halo Esférico r^-2| D[Potencial Oscuro]
    B --> E(Potencial Total Gravitatorio)
    D --> E
    E -->|Dinámica Newtoniana / Boltzmann| F[Curva de Rotación Plana Observada]
```

### 4. Relaciones de Escala (Tully-Fisher y Faber-Jackson)

Existen relaciones empíricas profundas que vinculan las propiedades dinámicas de las galaxias con su luminosidad intrínseca $L$:

- **Relación de Tully-Fisher (para Espirales):** Relaciona la luminosidad total con la amplitud máxima de la velocidad de rotación plana $V_{\text{max}}$.
  $$ L \propto V_{\text{max}}^\alpha \quad (\text{con } \alpha \approx 3 \text{ a } 4) $$
- **Relación de Faber-Jackson (para Elípticas):** Relaciona la luminosidad intrínseca con la dispersión de velocidades central $\sigma$.
  $$ L \propto \sigma^4 $$

Estas leyes son fundamentales como "candelas estándar" secundarias para medir distancias cosmológicas a galaxias lejanas independientes de su desplazamiento al rojo.

---

## 🛠 Ejemplo Práctico

**Problema:** Una galaxia elíptica gigante tiene una dispersión de velocidades estelar $\sigma = 300 \text{ km/s}$ y un radio efectivo (radio que contiene la mitad de la luz) $R_e = 10 \text{ kpc}$. Utilizando una aproximación del Teorema del Virial estelar, calcule su masa dinámica en masas solares ($M_\odot$).

**Solución paso a paso:**
1. Datos conocidos:
   - $\sigma = 300 \text{ km/s} = 3 \times 10^5 \text{ m/s}$
   - $R_e = 10 \text{ kpc} = 10 \times (3.086 \times 10^{19}) \text{ m} = 3.086 \times 10^{20} \text{ m}$
   - $G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$
2. La masa viríal estimada se relaciona con la dispersión de la línea de visión unidimensional ($\sigma$) usando un factor geométrico que para sistemas esféricos isótropos suele tomarse como $k \approx 5$ de forma aproximada en el radio medio de la masa:
   $$ M_{dyn} \approx \frac{5 R_e \sigma^2}{G} $$
   *(Nota: Dependiendo del perfil de densidad exacto, la constante varía entre 3 y 5. Utilizaremos 5 para esta aproximación)*.
3. Sustituimos valores:
   $$ M_{dyn} = \frac{5 \times (3.086 \times 10^{20}) \times (3 \times 10^5)^2}{6.674 \times 10^{-11}} $$
   $$ M_{dyn} = \frac{15.43 \times 10^{20} \times 9 \times 10^{10}}{6.674 \times 10^{-11}} $$
   $$ M_{dyn} = \frac{138.87 \times 10^{30}}{6.674 \times 10^{-11}} \approx 20.81 \times 10^{41} \text{ kg} $$
4. Convertimos a masas solares ($1 M_\odot \approx 1.989 \times 10^{30} \text{ kg}$):
   $$ M_{dyn} \approx \frac{20.81 \times 10^{41}}{1.989 \times 10^{30}} \approx 10.46 \times 10^{11} M_\odot $$
5. **Conclusión:** La masa dinámica de la galaxia es superior a 1 billón de masas solares ($> 10^{12} M_\odot$), lo cual supera ampliamente la masa que se estimaría sólo contabilizando el brillo de sus estrellas, confirmando la presencia sustancial de materia oscura en el sistema.

---

## 📝 Guía de Ejercicios Resueltos

**Problema 1: Perfil de Densidad de un Halo Isotermo de Materia Oscura**
Demuestre, a partir de la ecuación de Jeans, que el perfil de densidad de una esfera isoterma singular de materia oscura sin colisiones escala exactamente como $\rho(r) \propto r^{-2}$ y deduzca la velocidad constante de la curva de rotación en función de la dispersión de velocidad unidimensional $\sigma$.

**Solución paso a paso:**
1. **Ecuación de Jeans esférica y estacionaria:**
   Para un sistema con isotropía de velocidad radial y tangencial, y sin rotación neta, la ecuación de Jeans hidrostática análoga es:
   $\frac{d(\rho \sigma^2)}{dr} = -\rho \frac{GM(r)}{r^2}$.
2. **Hipótesis Isoterma:**
   La dispersión de velocidades $\sigma$ (el "análogo de la temperatura") es constante en todo el radio.
   $\sigma^2 \frac{d\rho}{dr} = -\rho \frac{GM(r)}{r^2} \implies \frac{1}{\rho} \frac{d\rho}{dr} = -\frac{GM(r)}{\sigma^2 r^2}$.
3. **Solución tipo ley de potencia:**
   Suponemos una solución del tipo $\rho(r) = C r^{-\alpha}$.
   La masa encerrada es $M(r) = \int_0^r 4\pi x^2 (C x^{-\alpha}) dx = \frac{4\pi C}{3-\alpha} r^{3-\alpha}$ (asumiendo $\alpha < 3$).
   Sustituyendo $\rho$ y $M(r)$ en la ecuación de Jeans:
   $\frac{d}{dr}(\ln \rho) = \frac{-\alpha}{r} = -\frac{G}{\sigma^2 r^2} \frac{4\pi C}{3-\alpha} r^{3-\alpha} = -\frac{4\pi G C}{\sigma^2(3-\alpha)} r^{1-\alpha}$.
4. **Igualación de exponentes:**
   Para que la igualdad se sostenga para todo $r$, la potencia de $r$ debe coincidir:
   $-1 = 1 - \alpha \implies \alpha = 2$.
5. **Valor de la constante $C$:**
   Sustituyendo $\alpha = 2$ en el coeficiente:
   $\frac{-2}{r} = -\frac{4\pi G C}{\sigma^2 (1)} \frac{1}{r} \implies C = \frac{\sigma^2}{2\pi G}$.
   Por lo tanto, $\rho(r) = \frac{\sigma^2}{2\pi G r^2}$.
6. **Velocidad de rotación $V_c$:**
   La velocidad de una órbita circular es $V_c^2(r) = \frac{GM(r)}{r}$.
   Con $\alpha=2$, $M(r) = \frac{4\pi (\sigma^2/2\pi G)}{1} r = \frac{2\sigma^2 r}{G}$.
   $V_c^2(r) = \frac{G (\frac{2\sigma^2 r}{G})}{r} = 2\sigma^2 \implies V_c = \sqrt{2}\sigma$. (La curva de rotación es perfectamente plana).

**Problema 2: Relación de Tully-Fisher Dinámica**
Usando el equilibrio rotacional (fuerza centrípeta gravitatoria) y asumiendo una relación teórica constante entre la masa y la luminosidad de las galaxias ($M/L = \text{const}$), derive una relación analítica entre la luminosidad intrínseca de una galaxia espiral y su velocidad máxima de rotación plana, deduciendo el valor del exponente.

**Solución paso a paso:**
1. **Base Dinámica:**
   Para una galaxia cuyo componente dominante es un disco luminoso con masa $M$ contenida en un radio $R$, la velocidad de rotación es aproximadamente $V^2 \propto \frac{GM}{R}$.
2. **Brillo Superficial Central Constante:**
   Una propiedad observacional importante de las galaxias de disco es que su brillo superficial central intrínseco, denotado frecuentemente como $I_0 \propto L/R^2$, es sorprendentemente constante para diversas espirales (Ley de Freeman).
   De aquí despejamos el radio $R$:
   $R^2 \propto \frac{L}{I_0} \implies R \propto L^{1/2}$.
3. **Masa Constante y Relación $M/L$:**
   Si la relación $M/L = \Upsilon$ es constante en esta población de galaxias:
   $M \propto L$.
4. **Combinando las ecuaciones:**
   Insertamos las proporcionalidades en la ley de la velocidad circular:
   $V^2 \propto \frac{M}{R} \propto \frac{L}{L^{1/2}} = L^{1/2}$.
   Elevando ambos lados al cuadrado:
   $V^4 \propto L \implies L \propto V^4$.
5. **Conclusión:**
   El resultado predice un exponente de Tully-Fisher $\alpha \approx 4$. Observacionalmente se obtienen valores de $\alpha \approx 3.5 - 4$ (dependiendo de la banda fotométrica espectral). Las desviaciones revelan que $M/L$ no es estrictamente constante y que la masa total se ve fuertemente influenciada por la materia oscura de halo, no puramente estelar.

**Problema 3: Tiempo de Fricción Dinámica (Chandrasekhar)**
Estime de forma simplificada cómo depende el tiempo de vida (antes de fusionarse con el núcleo galáctico) de un cúmulo globular o una pequeña galaxia satélite de masa $m$, que orbita en un halo de galaxia masiva de fondo isótropo con densidad $\rho$.

**Solución paso a paso:**
1. **Ecuación de Fricción Dinámica:**
   Una masa $m$ que se mueve a velocidad $v$ por un 'mar' de partículas pequeñas de masa $m_a$ y densidad total $\rho$, atrae partículas formando una 'estela' gravitatoria detrás. Esto causa un frenado neto:
   $\frac{d\mathbf{v}}{dt} \approx -\frac{4\pi G^2 m \rho \ln \Lambda}{v^3} \mathbf{v}$. (Aproximación de Chandrasekhar para velocidad $v$ mayor a la dispersión de fondo).
2. **Pérdida de Energía Angular:**
   La aceleración paralela es $a = \frac{dv}{dt} \approx -\frac{C \cdot m}{v^2}$, donde $C = 4\pi G^2 \rho \ln \Lambda$.
   La pérdida de energía orbital específica (por unidad de masa) o torque causará que la órbita (asumida casi circular) se encoja. Su momento angular específico $j \approx v r$ cae drásticamente.
   Para mantener $V_c \approx$ const (curva plana galáctica), $\frac{dr}{dt} = \frac{1}{v_c} \frac{dj}{dt} = \frac{a \cdot r}{v_c}$.
3. **Integración del tiempo de hundimiento:**
   $\frac{dr}{dt} = - \frac{C \cdot m}{V_c^3} r$. (Para un pozo isotermo).
   Integrando de un radio inicial $r_i$ a 0:
   El tiempo de fricción dinámica $t_{fric} \propto \frac{V_c^3 r_i^2}{G^2 m \rho \ln \Lambda}$.
4. **Relación masa y fricción:**
   La observación clave es $t_{fric} \propto \frac{1}{m}$.
   Las galaxias satélites más grandes y masivas sufren una fricción dinámica mucho mayor (la magnitud del frenado proporcional a su propia atracción gravitatoria). Caen rápidamente al núcleo de la galaxia huésped, mientras los pequeños cúmulos globulares pueden subsistir en el halo por un tiempo mayor a la edad de Hubble.

## 💻 Simulaciones Computacionales

Esta simulación en Python utiliza la ecuación de masa de un perfil de halo isoterma (materia oscura) combinado con un disco estelar (exponencial) para modelar y graficar la descomposición de la curva de rotación galáctica, demostrando la necesidad de la materia oscura.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parámetros (Unidades arbitrarias: R en kpc, V en km/s)
r = np.linspace(0.1, 30.0, 300)

# 1. Componente de Disco Estelar (Aproximación de disco Freeman)
# V_disk^2(r) se aproxima cualitativamente para alcanzar un pico y luego caer (Kepleriano en exterior)
R_d = 3.0 # Longitud de escala del disco
Sigma_0 = 100.0 # Densidad superficial central
# Fórmula analítica simplificada para la forma del disco
v_disk = 150.0 * (r / R_d) * np.exp(-r / (2 * R_d)) 

# 2. Componente de Bulbo Central (Aproximación esférica de masa concentrada)
M_bulge = 1e9 # masa
r_bulge = 1.0 # radio de escala
v_bulge = 80.0 * np.sqrt(r_bulge / (r + 0.1)) * np.exp(-r/10) # decae rápidamente

# 3. Componente de Halo de Materia Oscura (Esfera isoterma)
# V_halo^2 = G M(r)/r. Si M(r) propto r, V_halo = cte asintóticamente.
# Utilizamos un halo de núcleo (pseudo-isoterma)
r_c = 5.0 # radio del núcleo del halo
v_halo_inf = 200.0 # velocidad asintótica
v_halo = v_halo_inf * np.sqrt(1 - (r_c / r) * np.arctan(r / r_c))

# 4. Curva de Rotación Total
# Suma en cuadratura de las velocidades
v_total = np.sqrt(v_disk**2 + v_bulge**2 + v_halo**2)

plt.figure(figsize=(10, 6))
plt.plot(r, v_total, 'k-', lw=3, label='Curva de Rotación Total Observada')
plt.plot(r, v_halo, 'b--', lw=2, label='Contribución: Halo Materia Oscura')
plt.plot(r, v_disk, 'r-.', lw=2, label='Contribución: Disco Estelar Luminoso')
plt.plot(r, v_bulge, 'g:', lw=2, label='Contribución: Bulbo Central')

plt.title('Descomposición de la Curva de Rotación Galáctica')
plt.xlabel('Radio Galactocéntrico (kpc)')
plt.ylabel('Velocidad de Rotación $V_c$ (km/s)')
plt.legend()
plt.grid(True)
plt.ylim(0, 300)
plt.xlim(0, 30)
plt.show()
```

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **[UC Irvine: Physics 20B Cosmology (James Bullock)](https://www.youtube.com/playlist?list=PLqOZ6FD_RQ7nwb-mX-Z6G5fFv9yO-F18i)** - Aborda profundamente halos de materia oscura, rotación galáctica y modelos de formación jerárquica.
2. **[MIT 8.286 The Early Universe](https://ocw.mit.edu/courses/8-286-the-early-universe-fall-2013/)** - Incluye aspectos de la estructura a gran escala del universo y cómo las fluctuaciones primordiales dieron lugar a las galaxias.
3. **[Canal de YouTube Dr. Becky](https://www.youtube.com/c/DrBecky)** - Becky Smethurst es una destacada investigadora de galaxias y agujeros negros supermasivos que explica fenomenalmente la evolución galáctica en video.
4. **[Caltech - Ay 127: Cosmology and Galaxy Formation](http://www.astro.caltech.edu/~george/ay127/)** - Material avanzado (a menudo disponible de forma gratuita por profesores) sobre los detalles finos del medio intergaláctico y simulaciones N-body.
5. **[Coursera: Galaxies and Cosmology (Caltech / varios)](https://www.coursera.org/learn/astro)** - Módulos introductorios que explican las formas galácticas, el grupo local, colisiones y la historia temprana del universo galáctico.

### 📝 Artículos e Interactivos Interesantes
1. [Galaxy Zoo (Zooniverse)](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/) - Un proyecto de ciencia ciudadana famosísimo donde puedes ayudar a astrónomos a clasificar millones de galaxias según su morfología.
2. [Sloan Digital Sky Survey (SDSS)](https://www.sdss.org/) - Una de las cartografías digitales más grandes del cielo nocturno. Permite explorar la estructura a gran escala, agrupaciones y el espectro de millones de galaxias.
3. [Vera Rubin's 1970 Paper en The Astrophysical Journal](https://ui.adsabs.harvard.edu/abs/1970ApJ...159..379R/abstract) - Artículo original donde establece de forma robusta las curvas de rotación de galaxias espirales (Andrómeda).
4. [Illustris Project / IllustrisTNG](https://www.illustris-project.org/) - Simulaciones computacionales masivas de formación galáctica desde el Big Bang hasta hoy. Tienen espectaculares visualizaciones y videos.
5. [Hubble Ultra Deep Field (NASA)](https://esahubble.org/images/heic0611b/) - La histórica imagen que capturó miles de galaxias muy lejanas en un parche aparentemente vacío del cielo.
6. [Scholarpedia: Galaxy Formation](http://www.scholarpedia.org/article/Galaxy_formation) - Explicaciones detalladas de la disipación de gas, halos de materia oscura y retroalimentación de supernovas/agujeros negros.
7. [NASA/IPAC Extragalactic Database (NED)](https://ned.ipac.caltech.edu/) - La base de datos definitiva de objetos extragalácticos para investigadores y aficionados serios.
8. [Space Telescope Science Institute: Galaxies](https://www.stsci.edu/) - Investigaciones recientes impulsadas por el James Webb Space Telescope (JWST) sobre las primeras galaxias del universo.

### 📖 Referencias Útiles y Bibliografía
- **["Galactic Dynamics" - James Binney y Scott Tremaine](https://press.princeton.edu/books/paperback/9780691130279/galactic-dynamics)**: El tratado definitivo y avanzado (nivel de posgrado) sobre cómo se mueven las estrellas y el gas dentro del campo gravitacional galáctico.
- **["Galaxies in the Universe: An Introduction" - Linda S. Sparke y John S. Gallagher III](https://www.cambridge.org/highereducation/books/galaxies-in-the-universe/6F045A9524584288C00F7A598F6B928E)**: Un texto excepcional para niveles de pregrado y posgrado temprano, que conecta observaciones con las teorías físicas.
- **["Extragalactic Astronomy and Cosmology: An Introduction" - Peter Schneider](https://link.springer.com/book/10.1007/978-3-642-54083-7)**: Cubre todo lo que está más allá de la Vía Láctea, incluyendo núcleos galácticos activos y cuásares.
- **["Galaxy Formation and Evolution" - Houjun Mo, Frank van den Bosch, y Simon White](https://www.cambridge.org/highereducation/books/galaxy-formation-and-evolution/8C4A731F75B26E9528D8E9F6A24D3D52)**: Una referencia moderna monumental para entender la física completa (gas, enfriamiento, fusión) que forma el zoológico galáctico.
- **["An Introduction to Modern Astrophysics" - B. Carroll y D. Ostlie](https://www.cambridge.org/highereducation/books/an-introduction-to-modern-astrophysics/8C2B3C2B3A6C5B3E6B4A6C8D8E9F6B5C)**: También provee capítulos robustos en su sección extragaláctica, ideales como primer encuentro formal con las ecuaciones de galaxias espirales y elípticas.
