# [QFT-07] El Teorema de Goldstone y los Bosones Sin Masa

## 1. Rotura Espontánea de Simetría (SSB)
En la Teoría Cuántica de Campos, decimos que una simetría se "rompe espontáneamente" cuando el Lagrangiano ($\mathcal{L}$) de un sistema obedece cierta simetría continua, pero el estado de mínima energía (el vacío topológico $|0\rangle$) **no la obedece**.

Matemáticamente, si existe un campo escalar complejo $\phi$ con un potencial en forma de "sombrero mexicano" $V(\phi) = \lambda(|\phi|^2 - v^2)^2$, el vacío no se encuentra en $\phi=0$ (donde la simetría es perfecta pero inestable), sino en el valle circular degenerado donde $|\phi| = v$.

## 2. El Enunciado del Teorema de Goldstone
El físico Jeffrey Goldstone demostró un corolario ineludible en 1961:
> **"Por cada generador de una simetría global continua y exacta que se rompa espontáneamente, debe emerger en el espectro de la teoría una partícula escalar (bosón) estrictamente sin masa."**

A estas excitaciones sin masa se les conoce como **Bosones de Nambu-Goldstone**.

## 3. Física de las Excitaciones
Para visualizarlo en el potencial del sombrero mexicano:
- **Excitaciones Radiales:** Requieren energía (subir las paredes del sombrero). Corresponden a partículas con masa (como el Bosón de Higgs).
- **Excitaciones Angulares:** Moverse a lo largo del valle circular degenerado **no requiere energía** porque el potencial es plano ($V=$ constante). Estas oscilaciones sin coste de energía representan partículas con masa de reposo cero: los bosones de Goldstone.

## 4. Ejemplos en la Naturaleza
- **Física de Partículas:** En la Cromodinámica Cuántica (QCD), la ruptura espontánea de la simetría quiral genera los **Piones** ($\pi^0, \pi^\pm$). Debido a que la simetría quiral es solo una simetría aproximada (los quarks tienen un poco de masa), los piones no son perfectamente no-masivos (son *pseudo*-bosones de Goldstone).
- **Materia Condensada:** En un imán ferromagnético, los espines se alinean en una dirección, rompiendo la simetría rotacional $SO(3)$. Las excitaciones de esta simetría rota son los **Magnones** (ondas de espín sin masa).
- **Fonones:** Las ondas de sonido en un cristal son bosones de Goldstone resultantes de la ruptura de la simetría de traslación espacial continua.

## 5. El Mecanismo de Higgs: La Excepción a la Regla
El Teorema de Goldstone solo aplica estrictamente para simetrías **globales**. Cuando la simetría que se rompe es una simetría **local (Gauge)**, ocurre magia cuántica: el bosón de gauge asociado (que originalmente no tiene masa, como un fotón) "se come" al bosón de Goldstone sin masa. 

Al devorarlo, el bosón de gauge adquiere un grado de libertad longitudinal extra, lo que le permite **adquirir masa** (convirtiéndose en bosones $W^\pm$ y $Z^0$). El bosón de Goldstone desaparece del espectro físico. Esto es el Mecanismo de Brout-Englert-Higgs.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Cambridge DAMTP: Quantum Field Theory](http://www.damtp.cam.ac.uk/user/tong/qft.html) - David Tong. (Las notas de clase en vídeo más famosas de la década).
  - [Harvard: Quantum Field Theory I](https://scholar.harvard.edu/schwartz) - Matthew Schwartz.
- **Libros de Texto Canónicos:**
  - *An Introduction to Quantum Field Theory* - Michael E. Peskin & Daniel V. Schroeder. (El estándar de oro para cálculos con diagramas de Feynman).
  - *Quantum Field Theory in a Nutshell* - A. Zee. (Enfoque conceptual y fascinante).
  - *Quantum Field Theory and the Standard Model* - Matthew D. Schwartz.
