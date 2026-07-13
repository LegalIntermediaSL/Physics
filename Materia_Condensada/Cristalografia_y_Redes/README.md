# Cristalografía y Redes

La cristalografía estudia cómo se ordenan los átomos en sólidos. Esta estructura microscópica determina muchas propiedades macroscópicas: dureza, conductividad, anisotropía, respuesta magnética y comportamiento óptico.

## 🧮 Desarrollo Teórico Profundo

La cristalografía proporciona el marco matemático estricto para describir el arreglo periódico de los átomos en el espacio tridimensional. Esta periodicidad es la razón subyacente de fenómenos como las bandas de energía electrónica y la difracción de rayos X.

### 1. La Red de Bravais y la Red Recíproca

Un cristal ideal está definido por una **Red de Bravais** y una **Base**. La red de Bravais es un conjunto infinito de puntos generados por un grupo de traslaciones discretas:

$$ \mathbf{R} = n_1 \mathbf{a}_1 + n_2 \mathbf{a}_2 + n_3 \mathbf{a}_3 $$

donde $\mathbf{a}_i$ son tres vectores primitivos linealmente independientes, y $n_i$ son enteros ($\mathbb{Z}$). Existen exactamente 14 redes de Bravais tridimensionales agrupadas en 7 sistemas cristalinos (cúbico, tetragonal, ortorrómbico, hexagonal, trigonal, monoclínico y triclínico).

Para analizar ondas en medios periódicos (como funciones de onda de electrones o rayos X incidentes), la representación de Fourier de la red directa es indispensable. Esto se denomina **Red Recíproca**, definida como el conjunto de todos los vectores de onda $\mathbf{G}$ que rinden ondas planas periódicas respecto a la red de Bravais directa:

$$ e^{i \mathbf{G} \cdot \mathbf{R}} = 1 \quad \forall \mathbf{R} \in \text{Red de Bravais} $$

Esto implica que $\mathbf{G} \cdot \mathbf{R} = 2\pi m$, con $m \in \mathbb{Z}$. Los vectores primitivos de la red recíproca ($\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3$) se construyen como:

$$ \mathbf{b}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}, \quad \mathbf{b}_2 = 2\pi \frac{\mathbf{a}_3 \times \mathbf{a}_1}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}, \quad \mathbf{b}_3 = 2\pi \frac{\mathbf{a}_1 \times \mathbf{a}_2}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} $$

El denominador $\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3) = V_c$ es el volumen de la celda unitaria primitiva directa. De estas definiciones se deduce inmediatamente que $\mathbf{b}_i \cdot \mathbf{a}_j = 2\pi \delta_{ij}$, garantizando la condición de periodicidad.

### 2. Teoría de la Difracción: Von Laue y Bragg

Cuando una onda de rayos X plana $e^{i\mathbf{k}\cdot\mathbf{r}}$ incide sobre un cristal, el potencial dispersor es periódico $U(\mathbf{r}) = U(\mathbf{r} + \mathbf{R})$. Podemos expandir la densidad electrónica local $n(\mathbf{r})$ en serie de Fourier sobre los vectores de la red recíproca:

$$ n(\mathbf{r}) = \sum_{\mathbf{G}} n_{\mathbf{G}} e^{i\mathbf{G}\cdot\mathbf{r}} $$

La amplitud de dispersión en la dirección del vector de onda reflejado $\mathbf{k}'$ está determinada por el cambio en el momento de onda $\Delta \mathbf{k} = \mathbf{k}' - \mathbf{k}$. Evaluando la integral de dispersión sobre todo el cristal:

$$ F = \int d^3r \, n(\mathbf{r}) e^{-i\Delta\mathbf{k}\cdot\mathbf{r}} = \sum_{\mathbf{G}} n_{\mathbf{G}} \int d^3r \, e^{i(\mathbf{G} - \Delta\mathbf{k})\cdot\mathbf{r}} $$

La integral exponencial oscila rápidamente a cero a menos que el argumento se anule idénticamente, resultando en la **Condición de Difracción de von Laue**:

$$ \Delta \mathbf{k} = \mathbf{k}' - \mathbf{k} = \mathbf{G} $$

Esto establece que sólo habrá interferencia constructiva masiva (picos de difracción) si el cambio de vector de onda de los fotones coincide exactamente con un vector de la red recíproca. Asumiendo dispersión elástica ($|\mathbf{k}'| = |\mathbf{k}|$), cuadramos ambos lados de la condición $\mathbf{k}' = \mathbf{k} + \mathbf{G}$:

$$ |\mathbf{k}'|^2 = |\mathbf{k}|^2 + |\mathbf{G}|^2 + 2\mathbf{k}\cdot\mathbf{G} \implies |\mathbf{G}|^2 = -2\mathbf{k}\cdot\mathbf{G} $$

Dado que la red recíproca es invariante bajo inversión ($\mathbf{G} \to -\mathbf{G}$ es también un vector), podemos escribir de forma equivalente $2\mathbf{k}\cdot\mathbf{G} = G^2$.

Podemos reescribir esta condición en términos de la formulación original de W.L. Bragg. Las familias de planos cristalinos se designan por sus índices de Miller $(hkl)$, y se puede demostrar que el vector $\mathbf{G}_{hkl} = h\mathbf{b}_1 + k\mathbf{b}_2 + l\mathbf{b}_3$ es ortogonal a dichos planos, y que la separación interplanar es $d = 2\pi / |\mathbf{G}|$.
Sustituyendo $\mathbf{k}\cdot\mathbf{G} = k G \cos(90^\circ - \theta) = k G \sin\theta$ (donde $\theta$ es el ángulo rasante respecto al plano, y $k = 2\pi/\lambda$), la condición de Laue se simplifica a la **Ley de Bragg**:

$$ 2 \left( \frac{2\pi}{\lambda} \right) \left( \frac{2\pi}{d} \right) \sin\theta = \left( \frac{2\pi}{d} \right)^2 \implies 2d\sin\theta = \lambda $$

Para difracciones de orden superior simplemente escalamos $\mathbf{G}$ por un entero $n$, resultando en $2d\sin\theta = n\lambda$.

### Diagrama: Geometría de Dispersión en Espacio k

```mermaid
graph TD
    A[Cristal Cúbico Directo] --> B{Transformada de Fourier}
    B --> C[Red Recíproca <br> Puntos G]
    C --> D[Esfera de Ewald <br> Radio |k| = 2&pi;/&lambda;]
    D -- Vector k incidente --> E[Origen Espacio k]
    D -- Vector k' dispersado --> F[Intersección con nodo G]
    E -.->|Condición &Delta;k = G| F
    
    style C fill:#0077b6,stroke:#fff,color:#fff
    style D fill:#00b4d8,stroke:#fff,color:#fff
```

### 3. Factor de Estructura y Reglas de Extinción

La condición geométrica de Laue nos dice dónde puede haber picos, pero no qué tan intensos serán. La intensidad está dada por el **Factor de Estructura Geométrico**, que evalúa la interferencia debida a la base de átomos dentro de la celda unitaria. Si la base contiene átomos $j$ en posiciones $\mathbf{d}_j = x_j \mathbf{a}_1 + y_j \mathbf{a}_2 + z_j \mathbf{a}_3$ con factor de forma atómico $f_j$:

$$ S_{\mathbf{G}} = \sum_j f_j e^{-i \mathbf{G} \cdot \mathbf{d}_j} $$

Para $\mathbf{G} = h\mathbf{b}_1 + k\mathbf{b}_2 + l\mathbf{b}_3$, el producto $\mathbf{G}\cdot\mathbf{d}_j = 2\pi(h x_j + k y_j + l z_j)$. Por lo tanto:

$$ S_{hkl} = \sum_j f_j e^{-2\pi i (h x_j + k y_j + l z_j)} $$

Si $S_{hkl} = 0$, el pico de difracción predicho geométricamente por la red de Bravais desaparece físicamente. A esto se le conoce como **extinción sistemática**.

## 🛠 Ejemplo Práctico

**Problema:** Una muestra de Hierro metálico cristaliza en una red cúbica centrada en el cuerpo (BCC). Asumiendo átomos idénticos, demuestre matemáticamente la regla de extinción sistemática para este tipo de red utilizando el factor de estructura geométrico, y determine si se observará el pico de difracción correspondiente al plano (1 0 0).

**Solución paso a paso:**

1. **Definición de la celda:**
   La estructura BCC se puede describir como una red de Bravais Cúbica Simple (SC) con una celda unitaria que contiene una base de **dos átomos idénticos**:
   - Átomo 1 en el origen: $(x_1, y_1, z_1) = (0, 0, 0)$
   - Átomo 2 en el centro del cubo: $(x_2, y_2, z_2) = (1/2, 1/2, 1/2)$

2. **Cálculo del Factor de Estructura:**
   Sustituimos estas posiciones en la ecuación de $S_{hkl}$ asumiendo $f_1 = f_2 = f$ (mismo tipo de átomo):
   $$ S_{hkl} = f \left( e^{-2\pi i (0)} + e^{-2\pi i (h(1/2) + k(1/2) + l(1/2))} \right) $$
   $$ S_{hkl} = f \left( 1 + e^{-i\pi (h + k + l)} \right) $$

3. **Análisis de la paridad:**
   Sabemos por identidad de Euler que $e^{-i\pi n} = (-1)^n$ para cualquier número entero $n$.
   Por lo tanto, $e^{-i\pi (h+k+l)} = (-1)^{h+k+l}$.
   
   Esto nos da dos casos fundamentales:
   - **Caso A (suma par):** Si $h+k+l = \text{número par}$, entonces $(-1)^{h+k+l} = 1$.
     $$ S_{hkl} = f (1 + 1) = 2f $$
     (La intensidad es proporcional a $|S|^2 = 4f^2$, el pico es **observable**).
   - **Caso B (suma impar):** Si $h+k+l = \text{número impar}$, entonces $(-1)^{h+k+l} = -1$.
     $$ S_{hkl} = f (1 - 1) = 0 $$
     (La intensidad es cero, el pico sufre **extinción sistemática**).

4. **Aplicación al plano (1 0 0):**
   Para el pico de Miller $(h=1, k=0, l=0)$, la suma es $1 + 0 + 0 = 1$.
   Dado que $1$ es un número impar, el factor de estructura es $S_{100} = 0$.
   
**Conclusión:** En una red BCC de átomos idénticos (como el hierro $\alpha$), todos los planos cuya suma de índices de Miller sea impar se extinguen debido a interferencia destructiva perfecta del átomo central con los átomos de los vértices. En consecuencia, **el pico (1 0 0) no se observará en el difractograma de rayos X**. El primer pico visible corresponderá al (1 1 0).

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Factor de Estructura de la Red FCC
Calcule el factor de estructura $S_{hkl}$ para una red cúbica centrada en las caras (FCC) formada por átomos idénticos con factor de dispersión atómica $f$. Determine las reglas de extinción.

**Solución paso a paso:**
La celda unitaria convencional FCC contiene 4 átomos en las siguientes posiciones relativas $(x,y,z)$:
1) $(0,0,0)$
2) $(1/2, 1/2, 0)$
3) $(1/2, 0, 1/2)$
4) $(0, 1/2, 1/2)$
El factor de estructura geométrico es $S_{hkl} = \sum_{j=1}^4 f e^{-2\pi i (hx_j + ky_j + lz_j)}$.
Sustituyendo las posiciones:
$$ S_{hkl} = f \left[ 1 + e^{-i\pi(h+k)} + e^{-i\pi(h+l)} + e^{-i\pi(k+l)} \right] $$
Usando la propiedad $e^{-i\pi n} = (-1)^n$:
$$ S_{hkl} = f \left[ 1 + (-1)^{h+k} + (-1)^{h+l} + (-1)^{k+l} \right] $$
Analizamos la paridad de los índices $(h,k,l)$:
- Si $h,k,l$ son todos pares o todos impares (ej. 111, 200, 220), la suma de cualquier par será par. Entonces $(-1)^{\text{par}} = 1$.
  $$ S_{hkl} = f [1 + 1 + 1 + 1] = 4f $$
- Si hay una mezcla de pares e impares (ej. 100, 210, 211), al menos dos sumas serán impares y una par (o viceversa).
  $$ S_{hkl} = f [1 - 1 - 1 + 1] = 0 $$
Por lo tanto, la red FCC solo presenta picos de difracción cuando los índices $h,k,l$ tienen todos la misma paridad.

### Problema 2: Volumen de la Red Recíproca
Demuestre que el volumen de la celda primitiva en el espacio recíproco $V_{rec}$ está relacionado con el volumen de la celda primitiva directa $V_c$ por la relación $V_{rec} = (2\pi)^3 / V_c$.

**Solución paso a paso:**
El volumen de la celda en el espacio recíproco es el producto triple escalar de sus vectores base:
$$ V_{rec} = \mathbf{b}_1 \cdot (\mathbf{b}_2 \times \mathbf{b}_3) $$
Usando las definiciones de los vectores de la red recíproca:
$$ \mathbf{b}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{V_c}, \quad \mathbf{b}_2 = 2\pi \frac{\mathbf{a}_3 \times \mathbf{a}_1}{V_c}, \quad \mathbf{b}_3 = 2\pi \frac{\mathbf{a}_1 \times \mathbf{a}_2}{V_c} $$
Sustituyendo $\mathbf{b}_2$ y $\mathbf{b}_3$ en el producto vectorial:
$$ \mathbf{b}_2 \times \mathbf{b}_3 = \frac{(2\pi)^2}{V_c^2} [(\mathbf{a}_3 \times \mathbf{a}_1) \times (\mathbf{a}_1 \times \mathbf{a}_2)] $$
Aplicando la identidad del vector cuádruple $(\mathbf{A} \times \mathbf{B}) \times \mathbf{C} = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{A}(\mathbf{B}\cdot\mathbf{C})$ con $\mathbf{C} = \mathbf{a}_1 \times \mathbf{a}_2$:
$$ (\mathbf{a}_3 \times \mathbf{a}_1) \times \mathbf{C} = \mathbf{a}_1 (\mathbf{a}_3 \cdot \mathbf{C}) - \mathbf{a}_3 (\mathbf{a}_1 \cdot \mathbf{C}) $$
Sabemos que $\mathbf{a}_3 \cdot (\mathbf{a}_1 \times \mathbf{a}_2) = V_c$ y $\mathbf{a}_1 \cdot (\mathbf{a}_1 \times \mathbf{a}_2) = 0$. Entonces:
$$ \mathbf{b}_2 \times \mathbf{b}_3 = \frac{(2\pi)^2}{V_c^2} [\mathbf{a}_1 (V_c)] = \frac{(2\pi)^2}{V_c} \mathbf{a}_1 $$
Ahora multiplicamos escalarmente por $\mathbf{b}_1$:
$$ V_{rec} = \mathbf{b}_1 \cdot \left( \frac{(2\pi)^2}{V_c} \mathbf{a}_1 \right) = \frac{(2\pi)^2}{V_c} (\mathbf{b}_1 \cdot \mathbf{a}_1) $$
Sabiendo que por definición $\mathbf{b}_1 \cdot \mathbf{a}_1 = 2\pi$:
$$ V_{rec} = \frac{(2\pi)^3}{V_c} $$

### Problema 3: Separación Interplanar $d_{hkl}$ en Sistema Cúbico
Demuestre que la distancia interplanar $d_{hkl}$ para una red ortogonal (incluyendo la cúbica de lado $a$) está dada por $1/d^2 = (h/a)^2 + (k/b)^2 + (l/c)^2$. Evalúe para la red cúbica.

**Solución paso a paso:**
El vector de la red recíproca asociado al plano $(hkl)$ es:
$$ \mathbf{G}_{hkl} = h\mathbf{b}_1 + k\mathbf{b}_2 + l\mathbf{b}_3 $$
La distancia interplanar se define como $d_{hkl} = 2\pi / |\mathbf{G}_{hkl}|$. Por lo tanto, $1/d_{hkl}^2 = |\mathbf{G}_{hkl}|^2 / (2\pi)^2$.
Para una red ortogonal pura con parámetros de red $a, b, c$:
$$ \mathbf{a}_1 = a\mathbf{\hat{i}}, \quad \mathbf{a}_2 = b\mathbf{\hat{j}}, \quad \mathbf{a}_3 = c\mathbf{\hat{k}} $$
Los vectores recíprocos son:
$$ \mathbf{b}_1 = \frac{2\pi}{a}\mathbf{\hat{i}}, \quad \mathbf{b}_2 = \frac{2\pi}{b}\mathbf{\hat{j}}, \quad \mathbf{b}_3 = \frac{2\pi}{c}\mathbf{\hat{k}} $$
Por lo tanto, $\mathbf{G}_{hkl} = \frac{2\pi h}{a}\mathbf{\hat{i}} + \frac{2\pi k}{b}\mathbf{\hat{j}} + \frac{2\pi l}{c}\mathbf{\hat{k}}$.
El módulo al cuadrado es:
$$ |\mathbf{G}_{hkl}|^2 = 4\pi^2 \left[ \left(\frac{h}{a}\right)^2 + \left(\frac{k}{b}\right)^2 + \left(\frac{l}{c}\right)^2 \right] $$
Sustituyendo en la ecuación de la distancia interplanar:
$$ \frac{1}{d_{hkl}^2} = \left(\frac{h}{a}\right)^2 + \left(\frac{k}{b}\right)^2 + \left(\frac{l}{c}\right)^2 $$
Para una red cúbica, $a = b = c$, lo que simplifica la expresión a:
$$ d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}} $$

## 💻 Simulaciones Computacionales

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_bcc_lattice():
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # BCC Unit Cell points
    r = [-0.5, 0.5]
    X, Y, Z = np.meshgrid(r, r, r)
    
    ax.scatter(X, Y, Z, color='blue', s=100, label='Esquinas')
    ax.scatter([0], [0], [0], color='red', s=150, label='Centro (BCC)')
    
    # Draw unit cell edges
    for x in r:
        for y in r:
            ax.plot([x, x], [y, y], [-0.5, 0.5], 'k-', alpha=0.3)
            ax.plot([x, x], [-0.5, 0.5], [y, y], 'k-', alpha=0.3)
            ax.plot([-0.5, 0.5], [x, x], [y, y], 'k-', alpha=0.3)
            
    ax.set_title("Simulación: Celda Unitaria BCC")
    ax.legend()
    plt.show()

if __name__ == '__main__':
    plot_bcc_lattice()
```

## 📚 Recursos Específicos

### Cursos
1. **[Introduction to Crystallography (MIT OCW)](https://ocw.mit.edu):** Conceptos básicos y notación.
2. **[Solid State Chemistry (edX)](https://www.edx.org):** Para entender cómo se forman los cristales.
3. **[Diffraction and Symmetry (Coursera)](https://www.coursera.org):** Enfoque práctico sobre simetrías y grupos puntuales.
4. **[NPTEL Crystallography](https://nptel.ac.in):** Estudio riguroso de índices de Miller y redes de Bravais.
5. **[Advanced Structural Analysis (Stanford online)](https://online.stanford.edu):** Profundización en difracción de electrones y neutrones.

### Artículos y Simulaciones
1. **[VESTA Software](https://jp-minerals.org/vesta/en/):** Simulador y visualizador de estructuras cristalinas en 3D.
2. **[PhET Crystal Structures](https://phet.colorado.edu):** Simulaciones interactivas para entender empaquetamiento compacto.
3. **[Bilbao Crystallographic Server](https://www.cryst.ehu.es/):** Base de datos y herramientas de simetría.
4. **["Crystallography of Quasicrystals" (Steinhardt)](https://arxiv.org):** Artículo seminal sobre cristales no periódicos.
5. **[Crystallography Open Database (COD)](http://www.crystallography.net/cod/):** Catálogo de estructuras cristalinas reales.
6. **[Materials Project](https://nextgen.materialsproject.org/):** Base de datos para ver celdas unitarias calculadas con DFT.
7. **["Bragg's Law in 21st Century" (Physics Today)](https://physicstoday.scitation.org):** Artículo moderno sobre el impacto de la cristalografía.
8. **[CrystalMaker](https://www.crystalmaker.com/):** Software (con versiones demo) para construir y visualizar redes animadas.

### 📖 Referencias Útiles y Bibliografía
1. [Kittel, C. *Introduction to Solid State Physics*](https://archive.org) (Capítulos 1 y 2).
2. [Ashcroft, N. W., & Mermin, N. D. *Solid State Physics*](https://archive.org).
3. [Hammond, C. *The Basics of Crystallography and Diffraction*](https://global.oup.com).
