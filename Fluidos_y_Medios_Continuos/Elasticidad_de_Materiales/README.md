# Elasticidad de Materiales
La teoría de la elasticidad es la parte de la mecánica de medios continuos que estudia cómo los objetos sólidos se deforman cuando se les aplican fuerzas (esfuerzos) y cómo recuperan su forma original (si no superan el límite elástico).

## 📜 Contexto Histórico
En 1660, Robert Hooke descubrió empíricamente la ley que lleva su nombre ("Ut tensio, sic vis" - Como la extensión, así es la fuerza). Augustin-Louis Cauchy, en la década de 1820, formalizó el concepto de tensión (esfuerzo) y deformación mediante un formalismo tensorial que sentó las bases matemáticas de la mecánica de sólidos moderna.

## 🧮 Desarrollo Teórico Profundo
**Ley de Hooke (1D):**
El esfuerzo normal $ \sigma $ es proporcional a la deformación unitaria $ \epsilon $:
$$ \sigma = E \epsilon $$
donde $ \sigma = \frac{F}{A} $ (fuerza por unidad de área), $ \epsilon = \frac{\Delta L}{L_0} $ (cambio fraccional de longitud) y $ E $ es el Módulo de Young.

**Coeficiente de Poisson ($ \nu $):**
Mide el efecto de estrechamiento lateral cuando un material es estirado longitudinalmente:
$$ \nu = -\frac{\epsilon_{\text{transversal}}}{\epsilon_{\text{longitudinal}}} $$

**Módulo de Cizalladura ($ G $) y Módulo Volumétrico ($ K $):**
Para esfuerzos cortantes: $ \tau = G \gamma $, donde $ \gamma $ es la deformación angular.
Para compresión uniforme: $ P = -K \frac{\Delta V}{V_0} $.
Relación isotrópica: $ G = \frac{E}{2(1+\nu)} $ y $ K = \frac{E}{3(1-2\nu)} $.

**Tensor de Esfuerzos de Cauchy ($ \sigma_{ij} $):**
En 3D, el estado de esfuerzos se describe por una matriz simétrica $ 3 \times 3 $. La Ley de Hooke generalizada es:
$ \sigma_{ij} = C_{ijkl} \epsilon_{kl} $ (donde $ C $ es el tensor de rigidez de cuarto orden).

## 🛠 Ejemplo Práctico
**Problema:** Un cable de acero cilíndrico ($ E = 200 \text{ GPa} $) de $ 2 \text{ m} $ de longitud y $ 5 \text{ mm} $ de radio se usa para colgar una carga de $ 1000 \text{ kg} $. Calcula el esfuerzo longitudinal y cuánto se alarga el cable. ($ g = 9.8 \text{ m/s}^2 $).

**Solución paso a paso:**
1. Fuerza aplicada (Peso): $ F = mg = 1000 \times 9.8 = 9800 \text{ N} $.
2. Área transversal del cable: $ A = \pi r^2 = \pi (0.005 \text{ m})^2 = 7.854 \times 10^{-5} \text{ m}^2 $.
3. Esfuerzo longitudinal $ \sigma $:
   $ \sigma = \frac{F}{A} = \frac{9800}{7.854 \times 10^{-5}} = 1.248 \times 10^8 \text{ Pa} = 124.8 \text{ MPa} $.
4. Deformación unitaria $ \epsilon $ usando la Ley de Hooke:
   $ \epsilon = \frac{\sigma}{E} = \frac{124.8 \times 10^6 \text{ Pa}}{200 \times 10^9 \text{ Pa}} = 6.24 \times 10^{-4} $.
5. Alargamiento $ \Delta L $:
   $ \epsilon = \frac{\Delta L}{L_0} \implies \Delta L = \epsilon L_0 = (6.24 \times 10^{-4}) \times 2 = 1.248 \times 10^{-3} \text{ m} = 1.248 \text{ mm} $.

## 📚 Recursos
### Cursos Específicos
1. ["Mechanics of Materials I & II" - Coursera (Georgia Tech)](https://www.coursera.org/learn/mechanics-1)
2. ["Theory of Elasticity" - NPTEL](https://nptel.ac.in/courses/112105159)
3. ["Solid Mechanics" - MIT OCW](https://ocw.mit.edu/courses/mechanical-engineering/2-001-mechanics-materials-i-fall-2006/)
4. ["Introduction to Finite Element Analysis" - edX](https://www.edx.org/course/introduction-to-finite-element-analysis)
5. ["Advanced Mechanics of Deformable Solids" - Coursera](https://www.coursera.org/learn/solid-mechanics)
6. ["Continuum Mechanics of Solids" - NPTEL](https://nptel.ac.in/courses/112105166)

### Artículos y Simulaciones
1. [Calculadoras de Tensión-Deformación y Círculo de Mohr](https://www.efunda.com/formulae/solid_mechanics/mat_mechanics/mohr_circle.cfm)
2. [SimScale: Finite Element Analysis (FEA) Basic Tutorials](https://www.simscale.com/blog/2014/10/finite-element-analysis/)
3. [Ansys Student: Structural Mechanics Simulations](https://www.ansys.com/academic/students)
4. ["On the Mathematical Foundations of Elasticity" - A.L. Cauchy](https://en.wikipedia.org/wiki/Linear_elasticity)
5. ["Ut tensio, sic vis" - Robert Hooke (Historical reference)](https://en.wikipedia.org/wiki/Hooke%27s_law)
6. ["The Mathematical Theory of Elasticity" - A.E.H. Love (Classic text)](https://archive.org/details/mathematicaltheo00loveuoft)
7. [SolidWorks Simulation Express Tutorials](https://my.solidworks.com/training/path/17/solidworks-simulation)
8. [PhET Simulations on Hooke's Law and Springs](https://phet.colorado.edu/en/simulations/hookes-law)
9. [*Mechanics of Materials* - R.C. Hibbeler (Selected chapters)](https://www.amazon.com/Mechanics-Materials-10th-Russell-Hibbeler/dp/0134319656)

### 📖 Referencias Útiles y Bibliografía
1. [*Theory of Elasticity* - S.P. Timoshenko y J.N. Goodier](https://www.amazon.com/Theory-Elasticity-Stephen-P-Timoshenko/dp/0070858055)
2. [*Theory of Elasticity* - L.D. Landau y E.M. Lifshitz](https://www.amazon.com/Theory-Elasticity-Course-Theoretical-Physics/dp/075062633X)
3. [*Continuum Mechanics* - A.J.M. Spencer](https://www.amazon.com/Continuum-Mechanics-Dover-Books-Physics/dp/0486435946)
4. [*Advanced Mechanics of Materials* - A.P. Boresi](https://www.amazon.com/Advanced-Mechanics-Materials-Arthur-Boresi/dp/0471438812)
