# Hidrostática y Principio de Pascal
La hidrostática estudia los fluidos en estado de reposo. Se basa en principios fundamentales como las variaciones de presión con la profundidad, el principio de Pascal y el principio de flotación de Arquímedes.

## 📜 Contexto Histórico
El principio de flotabilidad fue descubierto por Arquímedes de Siracusa en el siglo III a.C. Siglos después, en 1647, Blaise Pascal formuló la ley que lleva su nombre, afirmando que un cambio de presión aplicado a un fluido encerrado se transmite sin disminución a todas las partes del fluido, lo cual es la base de la hidráulica moderna.

## 🧮 Desarrollo Teórico Profundo
**Ecuación Fundamental de la Hidrostática:**
Para un fluido incompresible en reposo sometido a gravedad constante, la variación de la presión $ p $ respecto a la altura $ z $ es:
$$ \frac{dp}{dz} = -\rho g $$
Al integrar entre dos puntos, obtenemos la presión absoluta a una profundidad $ h $:
$$ P = P_0 + \rho g h $$
donde $ P_0 $ es la presión en la superficie (usualmente presión atmosférica), $ \rho $ es la densidad del fluido y $ g $ es la aceleración gravitacional.

**Principio de Pascal:**
$$ \Delta P_1 = \Delta P_2 \implies \frac{F_1}{A_1} = \frac{F_2}{A_2} $$
Este principio permite multiplicar la fuerza en las prensas hidráulicas.

**Fuerza de Flotación (Principio de Arquímedes):**
La fuerza de empuje $ E $ o $ F_b $ hacia arriba es igual al peso del fluido desplazado:
$$ E = \rho_{\text{fluido}} V_{\text{sumergido}} g $$

## 🛠 Ejemplo Práctico
**Problema:** Una corona supuestamente de oro ($ \rho_{\text{oro}} = 19.3 \text{ g/cm}^3 $) tiene una masa de $ 1.5 \text{ kg} $ en el aire. Al sumergirla completamente en agua ($ \rho_{\text{agua}} = 1000 \text{ kg/m}^3 $), su peso aparente es de $ 13.5 \text{ N} $. ¿Es la corona de oro puro? ($ g = 9.8 \text{ m/s}^2 $).

**Solución paso a paso:**
1. Peso real en el aire: $ W = m g = 1.5 \times 9.8 = 14.7 \text{ N} $.
2. La fuerza de flotación $ E $ es la diferencia entre el peso real y el peso aparente:
   $ E = 14.7 \text{ N} - 13.5 \text{ N} = 1.2 \text{ N} $.
3. Relacionamos $ E $ con el volumen de la corona:
   $$ E = \rho_{\text{agua}} V g \implies V = \frac{E}{\rho_{\text{agua}} g} $$
   $ V = \frac{1.2}{1000 \times 9.8} = \frac{1.2}{9800} \approx 1.224 \times 10^{-4} \text{ m}^3 $.
4. Calculamos la densidad de la corona:
   $ \rho = \frac{m}{V} = \frac{1.5}{1.224 \times 10^{-4}} \approx 12250 \text{ kg/m}^3 = 12.25 \text{ g/cm}^3 $.
5. **Conclusión:** Como la densidad $ 12.25 \text{ g/cm}^3 $ es mucho menor que la del oro puro ($ 19.3 \text{ g/cm}^3 $), la corona no es de oro puro (el joyero intentó estafar al rey).

## 📚 Recursos
### Cursos Específicos
1. ["Physics 101: Fluid Statics and Pascal's Principle" - Coursera](https://www.coursera.org/learn/physics-101)
2. ["Fluid Mechanics: Statics and Kinematics" - edX](https://www.edx.org/learn/fluid-mechanics)
3. ["Hydraulics and Pneumatics Systems" - NPTEL](https://nptel.ac.in/courses/112105047)
4. ["Introductory Physics: Fluids" - MIT OCW](https://ocw.mit.edu/courses/physics/8-01sc-classical-mechanics-fall-2016/fluid-mechanics/)
5. ["Engineering Mechanics: Statics" - Coursera](https://www.coursera.org/learn/engineering-mechanics-statics)
6. ["Applied Hydrostatics" - Udemy](https://www.udemy.com/topic/fluid-mechanics/)

### Artículos y Simulaciones
1. [PhET Interactive Simulations: "Under Pressure"](https://phet.colorado.edu/en/simulations/under-pressure)
2. [PhET Interactive Simulations: "Buoyancy"](https://phet.colorado.edu/en/simulations/buoyancy)
3. ["The Treatise on the Equilibrium of Liquids" - Blaise Pascal](https://archive.org/details/physicaltreatise00pasc)
4. [Capítulos de Estática de Fluidos en Fox & McDonald](https://www.amazon.com/Fox-McDonalds-Introduction-Fluid-Mechanics/dp/1119616175)
5. ["Archimedes to Hawking: Laws of Science" - Clifford Pickover](https://www.amazon.com/Archimedes-Hawking-Laws-Science-Behind/dp/0195336119)
6. [Simulación de Prensas Hidráulicas (Virtual Lab)](https://vlab.amrita.edu/?sub=1&brch=74&sim=1521&cnt=1)
7. ["Pascal's Principle and Hydraulic Brakes" - Automotive Engineering Journals](https://www.sae.org/publications/journals)
8. ["Stability of Submarines and Floating Vessels" - Naval Architecture Papers](https://www.rina.org.uk/publications.html)
9. [Experimentos de tubo en U y barómetros virtuales](https://www.physicsclassroom.com/class/fluids)

### 📖 Referencias Útiles y Bibliografía
1. [*Fluid Mechanics* - L.D. Landau y E.M. Lifshitz](https://www.amazon.com/Fluid-Mechanics-Second-Theoretical-Physics/dp/0080339336)
2. [*Fluid Mechanics* - Pijush K. Kundu y Ira M. Cohen](https://www.amazon.com/Fluid-Mechanics-Pijush-K-Kundu/dp/012405935X)
3. [*Introduction to Fluid Mechanics* - R.W. Fox, A.T. McDonald](https://www.amazon.com/Fox-McDonalds-Introduction-Fluid-Mechanics/dp/1119616175)
4. [*Fluid Mechanics* - Frank M. White](https://www.amazon.com/Fluid-Mechanics-Frank-White/dp/0073398276)
