# Elasticidad de Materiales
La teoría de la elasticidad es la parte de la mecánica de medios continuos que estudia cómo los objetos sólidos se deforman cuando se les aplican fuerzas (esfuerzos) y cómo recuperan su forma original (si no superan el límite elástico).

## 📜 Contexto Histórico
En 1660, Robert Hooke descubrió empíricamente la ley que lleva su nombre ("Ut tensio, sic vis" - Como la extensión, así es la fuerza). Augustin-Louis Cauchy, en la década de 1820, formalizó el concepto de tensión (esfuerzo) y deformación mediante un formalismo tensorial que sentó las bases matemáticas de la mecánica de sólidos moderna.

## 🧮 Desarrollo Teórico Profundo
**Ley de Hooke (1D):**
El esfuerzo normal $ \sigma $ es proporcional a la deformación unitaria $ \epsilon $:
$ \sigma = E \epsilon $
donde $ \sigma = \frac{F}{A} $ (fuerza por unidad de área), $ \epsilon = \frac{\Delta L}{L_0} $ (cambio fraccional de longitud) y $ E $ es el Módulo de Young.

**Coeficiente de Poisson ($ \nu $):**
Mide el efecto de estrechamiento lateral cuando un material es estirado longitudinalmente:
$ \nu = -\frac{\epsilon_{\text{transversal}}}{\epsilon_{\text{longitudinal}}} $

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

## 📚 Recursos Específicos
- **Cursos:** "Mechanics of Materials" (Coursera/edX).
- **Artículos/Textos:** *Theory of Elasticity* (Timoshenko), *Mechanics of Materials* (Hibbeler).
- **Simulaciones:** Calculadoras de tensión-deformación, análisis de elementos finitos básico (FEA).
