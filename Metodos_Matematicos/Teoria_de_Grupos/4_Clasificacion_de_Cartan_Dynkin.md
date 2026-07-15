# La Clasificación de Cartan-Dynkin (Raíces y Pesos)

Si la naturaleza de las fuerzas fundamentales del universo se reduce a Álgebras de Lie (campos de Yang-Mills), entonces clasificar todas las álgebras de Lie posibles equivale a enlistar los universos físicamente posibles. Afortunadamente, Élie Cartan (y luego Eugene Dynkin) resolvieron este colosal problema matemático: lograron clasificar absolutamente todas las **Álgebras de Lie Simples Finitas sobre los Complejos**.

## 1. La Subálgebra de Cartan (CSA)
El algoritmo de clasificación comienza buscando dentro del álgebra de Lie $\mathfrak{g}$ el conjunto máximo de generadores que *conmutan entre sí*. Este conjunto se denomina **Subálgebra de Cartan** ($\mathfrak{h}$).
Su dimensión se denomina el **Rango ($r$)** del álgebra.
En física, estos son los generadores observables simultáneamente. En $SU(3)$ de la QCD, el rango es 2: el Isospín $T_3$ y la Hipercarga $Y$, correspondientes a los 2 colores medibles simultáneamente de los gluones.

## 2. Raíces y Vectores de Peso
Dado que los elementos de $\mathfrak{h}$ conmutan, pueden ser diagonalizados simultáneamente. Los autovectores (los estados cuánticos base) para la representación adjunta (el álgebra misma) se asocian a tuplas de $r$ autovalores, llamados **Vectores Raíz** $\vec{\alpha}$.
Cada vector raíz indica la "carga" bajo los operadores de Cartan del generador paso correspondiente. Estos vectores forman celosías geométricas ultra-rígidas en el espacio euclídeo $\mathbb{R}^r$.
La simetría hiper-estricta de este sistema de raíces está dictada por las reflexiones del **Grupo de Weyl**.

## 3. Los Diagramas de Dynkin
Eugene Dynkin codificó toda la geometría multidimensional del sistema de raíces en simples dibujos rupestres (Diagramas de Dynkin). Cada círculo (nodo) representa una raíz simple, y las líneas entre círculos dictan el ángulo estricto entre ellas:
- **0 líneas**: Ángulo de 90°
- **1 línea**: Ángulo de 120°
- **2 líneas**: Ángulo de 135° (una raíz es más larga que la otra por un factor $\sqrt{2}$)
- **3 líneas**: Ángulo de 150° (factor $\sqrt{3}$)

## 4. La Tabla Periódica de la Física Teórica
El teorema de Cartan-Dynkin demuestra que solo existen las siguientes Álgebras de Lie simples (y nada más puede existir):
-   **4 Familias Clásicas (Infinitas)**:
    -   $A_n \cong \mathfrak{su}(n+1)$ (Grupos Unitarios Especiales, bases de las fuerzas cuánticas).
    -   $B_n \cong \mathfrak{so}(2n+1)$ (Rotaciones ortogonales en dimensión impar).
    -   $C_n \cong \mathfrak{sp}(2n)$ (Grupos Simplécticos, asociados a la mecánica hamiltoniana fásica).
    -   $D_n \cong \mathfrak{so}(2n)$ (Rotaciones ortogonales en dimensión par).
-   **5 Álgebras Excepcionales**:
    -   $G_2, F_4, E_6, E_7, E_8$.
    -   $E_8$ (con dimensión 248) es el rey de la matemática pura y la pieza central de la Teoría de Cuerdas Heterótica, el mejor candidato para una Teoría del Todo matemática.
