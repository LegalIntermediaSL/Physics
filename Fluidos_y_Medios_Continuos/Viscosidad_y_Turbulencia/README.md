# Viscosidad y Turbulencia
Los fluidos reales poseen fricción interna, conocida como viscosidad. Dependiendo de la velocidad y geometría, el flujo puede ser ordenado (laminar) o caótico y mezclado (turbulento). El estudio de la turbulencia es uno de los mayores problemas abiertos de la física clásica.

## 📜 Contexto Histórico
Isaac Newton fue el primero en modelar la viscosidad en 1687. En el siglo XIX, Claude-Louis Navier y George Gabriel Stokes derivaron las ecuaciones fundamentales de flujo viscoso. En 1883, Osborne Reynolds demostró experimentalmente la transición entre flujo laminar y turbulento, definiendo el Número de Reynolds.

## 🧮 Desarrollo Teórico Profundo
**Ley de Viscosidad de Newton:**
El esfuerzo cortante $ \tau $ es proporcional al gradiente de velocidad:
$ \tau = \mu \frac{\partial u}{\partial y} $
donde $ \mu $ es la viscosidad dinámica.

**Número de Reynolds ($ Re $):**
Un número adimensional que predice el régimen de flujo:
$ Re = \frac{\rho v D}{\mu} = \frac{v D}{\nu} $
donde $ D $ es una longitud característica (como el diámetro de un tubo) y $ \nu = \mu/\rho $ es la viscosidad cinemática.
- $ Re < 2100 $: Flujo Laminar
- $ 2100 < Re < 4000 $: Transición
- $ Re > 4000 $: Flujo Turbulento

**Ecuaciones de Navier-Stokes:**
La forma vectorial para fluido incompresible es:
$ \rho \left( \frac{\partial \mathbf{v}}{\partial t} + \mathbf{v} \cdot \nabla \mathbf{v} \right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f} $

**Ley de Poiseuille:**
Para flujo laminar a través de un tubo cilíndrico de radio $ R $ y longitud $ L $, el caudal volumétrico es:
$ Q = \frac{\pi R^4 \Delta P}{8 \mu L} $

## 🛠 Ejemplo Práctico
**Problema:** Sangre a $ 37^\circ \text{C} $ ($ \rho = 1060 \text{ kg/m}^3 $, $ \mu = 4 \times 10^{-3} \text{ Pa}\cdot\text{s} $) fluye a través de una arteria de $ 4 \text{ mm} $ de diámetro a una velocidad promedio de $ 0.3 \text{ m/s} $. Determina si el flujo es laminar o turbulento y calcula la caída de presión en una longitud de $ 10 \text{ cm} $.

**Solución paso a paso:**
1. Calculamos el Número de Reynolds ($ D = 0.004 \text{ m}, v = 0.3 \text{ m/s} $):
   $ Re = \frac{\rho v D}{\mu} = \frac{1060 \times 0.3 \times 0.004}{4 \times 10^{-3}} = \frac{1.272}{0.004} = 318 $
   Como $ Re = 318 < 2100 $, el flujo es fuertemente **laminar**.
2. Al ser laminar, podemos aplicar la Ley de Poiseuille. Relacionamos $ Q $ con $ v $:
   $ Q = v A = v (\pi r^2) $
3. Sustituyendo $ Q $ en la ecuación de Poiseuille ($ r = 0.002 \text{ m} $):
   $ v \pi r^2 = \frac{\pi r^4 \Delta P}{8 \mu L} \implies \Delta P = \frac{8 \mu L v}{r^2} $
4. Calculamos $ \Delta P $ ($ L = 0.1 \text{ m} $):
   $ \Delta P = \frac{8 (4 \times 10^{-3}) (0.1) (0.3)}{(0.002)^2} = \frac{9.6 \times 10^{-4}}{4 \times 10^{-6}} = 240 \text{ Pa} $.

## 📚 Recursos Específicos
- **Cursos:** "Fluid Mechanics" (Módulos de fricción y tuberías - Coursera), "Advanced Fluid Mechanics" (MIT OCW).
- **Artículos/Textos:** *Transport Phenomena* (Bird, Stewart, Lightfoot), Notas sobre Navier-Stokes.
- **Simulaciones:** Túneles de viento virtuales, software CFD (Computational Fluid Dynamics) introductorio (OpenFOAM).
