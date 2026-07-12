# Hidrostática y Principio de Pascal
La hidrostática estudia los fluidos en estado de reposo. Se basa en principios fundamentales como las variaciones de presión con la profundidad, el principio de Pascal y el principio de flotación de Arquímedes.

## 📜 Contexto Histórico
El principio de flotabilidad fue descubierto por Arquímedes de Siracusa en el siglo III a.C. Siglos después, en 1647, Blaise Pascal formuló la ley que lleva su nombre, afirmando que un cambio de presión aplicado a un fluido encerrado se transmite sin disminución a todas las partes del fluido, lo cual es la base de la hidráulica moderna.

## 🧮 Desarrollo Teórico Profundo
**Ecuación Fundamental de la Hidrostática:**
Para un fluido incompresible en reposo sometido a gravedad constante, la variación de la presión $ p $ respecto a la altura $ z $ es:
$ \frac{dp}{dz} = -\rho g $
Al integrar entre dos puntos, obtenemos la presión absoluta a una profundidad $ h $:
$ P = P_0 + \rho g h $
donde $ P_0 $ es la presión en la superficie (usualmente presión atmosférica), $ \rho $ es la densidad del fluido y $ g $ es la aceleración gravitacional.

**Principio de Pascal:**
$ \Delta P_1 = \Delta P_2 \implies \frac{F_1}{A_1} = \frac{F_2}{A_2} $
Este principio permite multiplicar la fuerza en las prensas hidráulicas.

**Fuerza de Flotación (Principio de Arquímedes):**
La fuerza de empuje $ E $ o $ F_b $ hacia arriba es igual al peso del fluido desplazado:
$ E = \rho_{\text{fluido}} V_{\text{sumergido}} g $

## 🛠 Ejemplo Práctico
**Problema:** Una corona supuestamente de oro ($ \rho_{\text{oro}} = 19.3 \text{ g/cm}^3 $) tiene una masa de $ 1.5 \text{ kg} $ en el aire. Al sumergirla completamente en agua ($ \rho_{\text{agua}} = 1000 \text{ kg/m}^3 $), su peso aparente es de $ 13.5 \text{ N} $. ¿Es la corona de oro puro? ($ g = 9.8 \text{ m/s}^2 $).

**Solución paso a paso:**
1. Peso real en el aire: $ W = m g = 1.5 \times 9.8 = 14.7 \text{ N} $.
2. La fuerza de flotación $ E $ es la diferencia entre el peso real y el peso aparente:
   $ E = 14.7 \text{ N} - 13.5 \text{ N} = 1.2 \text{ N} $.
3. Relacionamos $ E $ con el volumen de la corona:
   $ E = \rho_{\text{agua}} V g \implies V = \frac{E}{\rho_{\text{agua}} g} $
   $ V = \frac{1.2}{1000 \times 9.8} = \frac{1.2}{9800} \approx 1.224 \times 10^{-4} \text{ m}^3 $.
4. Calculamos la densidad de la corona:
   $ \rho = \frac{m}{V} = \frac{1.5}{1.224 \times 10^{-4}} \approx 12250 \text{ kg/m}^3 = 12.25 \text{ g/cm}^3 $.
5. **Conclusión:** Como la densidad $ 12.25 \text{ g/cm}^3 $ es mucho menor que la del oro puro ($ 19.3 \text{ g/cm}^3 $), la corona no es de oro puro (el joyero intentó estafar al rey).

## 📚 Recursos Específicos
- **Cursos:** "Physics 101" (cualquier curso que cubra estática de fluidos).
- **Artículos/Textos:** Capítulos de Estática de Fluidos en Fox & McDonald o Frank M. White.
- **Simulaciones:** "Under Pressure" y "Buoyancy" (PhET Interactive Simulations).
