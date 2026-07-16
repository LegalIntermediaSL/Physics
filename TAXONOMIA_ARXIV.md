# El Estándar Taxonómico del Repositorio y su Relación con ArXiv

Para gestionar la inmensa cantidad de tratados teóricos, simulaciones matemáticas y literatura contenida en este repositorio, se ha adoptado una **Codificación Taxonómica Global** basada en los estándares de la Universidad de Cornell (arXiv) y la Sociedad Americana de Física (APS).

Tal y como es la convención universal en la comunidad científica, **hemos utilizado siglas en Inglés** para clasificar todas las áreas.

## 1. ¿Qué es arXiv y por qué dicta el estándar?
[arXiv](https://arxiv.org/) (pronunciado *arkive*) es el repositorio global por excelencia de artículos científicos (*preprints*). Fundado en 1991 por Paul Ginsparg, alberga más de dos millones de publicaciones de física, matemáticas y computación. 

Cuando los físicos teóricos publican un descubrimiento (desde el Bosón de Higgs hasta la primera detección de Ondas Gravitacionales), suben su artículo a arXiv utilizando un sistema de etiquetas estrictas para categorizar el campo. Estas etiquetas (ej. `hep-th` para física de altas energías teórica, o `gr-qc` para relatividad general) son el lenguaje universal mediante el cual los científicos navegan el conocimiento.

## 2. La Codificación de 3 Letras del Repositorio
Inspirados por las divisiones oficiales de arXiv, hemos asignado un **Prefijo de 3 Letras en Inglés** único a cada macro-área de la física. Cada archivo en este repositorio, ya sea un tratado teórico en Markdown o un simulador en Jupyter Notebook, está forjado con este código en su ADN (en su nombre de archivo y en su encabezado interno).

Este sistema te permite localizar ecuaciones de forma cruzada. Si lees "Ver fórmula en [QFT-04]", sabrás de forma instintiva a dónde dirigirte.

### Índice Taxonómico Oficial (Siglas en Inglés)
| Código | Acrónimo en Inglés | Traducción / Área | Etiqueta ArXiv | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| **[AST]** | **AST**rophysics | Astrofísica | `astro-ph` | Evolución estelar, galaxias, agujeros negros, límite de Chandrasekhar. |
| **[COS]** | **COS**mology | Cosmología | `gr-qc` / `astro-ph.CO` | Big Bang, Métrica FLRW, Energía Oscura, Inflación, Multiverso. |
| **[AMO]** | **A**tomic, **M**olecular & **O**ptical | Física Atómica y Molecular | `physics.atom-ph` | Condensados BEC, espectroscopia, estructura fina. |
| **[BSM]** | **B**eyond **S**tandard **M**odel | Física Más Allá del Modelo Estándar | `hep-ph` / `hep-th` | Supersimetría (SUSY), Materia Oscura, Axiones. |
| **[CMA]** | **C**ondensed **MA**tter | Materia Condensada | `cond-mat` | Redes de Bravais, superconductividad, fermiones pesados. |
| **[CLM]** | **CL**assical **M**echanics | Mecánica Clásica | `physics.class-ph` | Lagrangianos, Hamiltonianos, caos determinista. |
| **[ELM]** | **EL**ectro**M**agnetism | Electromagnetismo | `physics.class-ph` | Ecuaciones de Maxwell, radiación sincrotrón. |
| **[FLD]** | **FL**uid **D**ynamics | Fluidos y Medios Continuos | `physics.flu-dyn` | Navier-Stokes, turbulencia de Kolmogorov, MHD. |
| **[FUN]** | **FUN**damentals | Ecuaciones Fundamentales | `physics.gen-ph` | Leyes de Newton, principios de conservación. |
| **[HEP]** | **H**igh **E**nergy **P**hysics | Física Nuclear y de Partículas | `hep-ex` / `nucl-th` | Modelo estándar, quarks, desintegración radiactiva. |
| **[MTH]** | **M**a**TH**ematical Physics | Métodos Matemáticos | `math-ph` | Tensores, geometría diferencial, álgebra de Lie. |
| **[NLD]** | **N**on-**L**inear **D**ynamics | Física No Lineal y Sistemas Complejos | `nlin` | Atractores extraños, fractales, dinámica de poblaciones. |
| **[OPT]** | **OPT**ics & Waves | Ondas y Óptica | `physics.optics` | Láseres, óptica cuántica, fotones squeezed. |
| **[PLA]** | **PLA**sma Physics | Física de Plasmas y Fusión | `physics.plasm-ph` | Ecuación de Vlasov, Tokamaks, amortiguamiento de Landau. |
| **[QG]**  | **Q**uantum **G**ravity & Strings | Gravedad Cuántica y Cuerdas | `gr-qc` / `hep-th` | M-Theory, gravedad cuántica de lazos, branas. |
| **[QFT]** | **Q**uantum **F**ield **T**heory | Teoría Cuántica de Campos | `hep-th` | Diagramas de Feynman, renormalización, ecuación de Dirac. |
| **[QIC]** | **Q**uantum **I**nformation & **C**omputation | Información Cuántica | `quant-ph` | Qubits, teletransporte, algoritmo de Shor. |
| **[QM]**  | **Q**uantum **M**echanics | Mecánica Cuántica | `quant-ph` | Ecuación de Schrödinger, espaciotiempo de Hilbert. |
| **[REL]** | **REL**ativity | Relatividad | `gr-qc` | Tensor de Einstein, métrica de Schwarzschild, agujeros de gusano. |
| **[THD]** | **TH**ermo**D**ynamics | Termodinámica y Estadística | `cond-mat.stat-mech` | Entropía, colectivos de Gibbs, transiciones de fase. |

## 3. Sub-Categorías Oficiales de arXiv (Implementadas en Subcarpetas)
Para reflejar la extrema especialización de la física moderna, las macro-áreas se dividen internamente en subcarpetas que coinciden con las sub-etiquetas oficiales de arXiv. Algunos ejemplos notables implementados en el repositorio son:

*   `astro-ph` (Astrofísica)
    *   `astro-ph.GA`: Astrofísica de Galaxias
    *   `astro-ph.CO`: Cosmología y Astrofísica Extragaláctica
    *   `astro-ph.SR`: Física Solar y Estelar
*   `cond-mat` (Materia Condensada)
    *   `cond-mat.mes-hall`: Física Mesoscópica y Efecto Hall
    *   `cond-mat.stat-mech`: Mecánica Estadística
    *   `cond-mat.str-el`: Electrones Fuertemente Correlacionados
*   `hep` (Física de Altas Energías)
    *   `hep-th`: Teoría (Gravedad Cuántica, Cuerdas)
    *   `hep-ph`: Fenomenología (Materia Oscura, SUSY)
    *   `hep-lat`: Lattice QCD

## 4. Ejemplo de Uso Práctico
Supongamos que estás desarrollando un simulador de agujeros negros. Necesitas consultar el comportamiento del giro (*spin*) del agujero negro.
1. Reconoces que los agujeros negros giratorios (Kerr) son terreno de la Relatividad General (**Relativity**).
2. Buscas la etiqueta **[REL]** y navegas a la carpeta `Relatividad_(REL)`.
3. Encuentras el artículo `REL-04_Relatividad_Kerr_Ray_Tracing.md`.
4. Sabrás inmediatamente que el cuaderno Jupyter correspondiente se llamará `REL-04_Relatividad_Kerr_Ray_Tracing.ipynb` y estará en `Simulaciones_Jupyter/Relatividad_(REL)`.

Este puente taxonómico no solo mantiene el repositorio impecable, sino que te entrena visualmente para leer *papers* internacionales y reconocer la jerga oficial.
