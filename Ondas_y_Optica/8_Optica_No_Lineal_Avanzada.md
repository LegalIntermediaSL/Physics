# Óptica No Lineal y Medios Anisótropos

## 1. Polarización de la Materia
En la óptica clásica lineal enseñada en la universidad, la relación óptica entre el campo eléctrico de un haz de luz incidente $\vec{E}$ y la polarización generada en los átomos del material dieléctrico (vidrio, cristal) $\vec{P}$ es puramente proporcional y lineal:

$$
\vec{P} = \varepsilon_0 \chi^{(1)} \vec{E}
$$

Donde $\chi^{(1)}$ es la susceptibilidad eléctrica. El material actúa armónicamente: la luz que entra a una frecuencia "roja", altera y rebota a la misma frecuencia "roja".

## 2. Régimen Láser No Lineal
En 1960 se inventó el Láser de Rubí emitiendo intensidades eléctricas estelares ($> 10^8$ V/m). A estas intensidades astronómicas colosales, la luz arranca y sacude fuertemente los electrones más allá de su pozo de potencial armónico Hookeano. La polarización real en el átomo debe modelarse expandiéndose en una Serie de Taylor tensorial profunda:

$$
\vec{P} = \varepsilon_0 \left( \chi^{(1)} \vec{E} + \chi^{(2)} \vec{E}\vec{E} + \chi^{(3)} \vec{E}\vec{E}\vec{E} + \dots \right)
$$

Los términos cuadráticos ($\chi^{(2)}$) y cúbicos ($\chi^{(3)}$) gobiernan la **Óptica No Lineal**.

## 3. Generación de Segundos Armónicos (SHG)
Si inyectamos un puntero láser monocolor $E(t) = E_0 \cos(\omega t)$ extremadamente potente en un cristal asimétrico (ej. Niobato de Litio), el término óptico de segundo orden $\chi^{(2)}$ elevará la onda armónica al cuadrado $(\cos(\omega t))^2$.

Por la trigonometría básica de ángulo doble ($\cos^2 x = \frac{1 + \cos(2x)}{2}$), el cristal no lineal literalmente creará fotones oscilando a **frecuencia doble (2$\omega$)**. 
Físicamente, dos fotones rojos infrarrojos chocarán cuánticamente dentro del enrejado de cristal fusionándose en **un solo fotón verde** hiper-energético (Generación de Segundos Armónicos). Así es como funcionan los potentes y comerciales "punteros láser verdes".

## 4. Mezcla de Cuatro Ondas y Conjugación de Fase ($\chi^{(3)}$)
A nivel cúbico $\chi^{(3)}$, todos los materiales isotrópicos (incluso gases o fibra de vidrio) revelan el Efecto Kerr Óptico: el Índice de Refracción del vidrio ($n$) se vuelve dependiente de la intensidad de la luz que lo cruza ($n = n_0 + n_2 I$). 
Un láser hiperintenso se curvará a sí mismo enfocándose y colapsando catastróficamente (Autoenfoque). También permite cruzar láseres generando espejos mágicos temporales ("Espejo Conjugado en Fase") donde la luz reflejada retrocede exactamente y revierte cualquier distorsión por aberraciones.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.03: Physics III: Vibrations and Waves](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/) - Walter Lewin.
  - [Stanford: Lasers and Optics](https://online.stanford.edu/courses) - Recursos del departamento de Óptica de Stanford.
- **Libros de Texto Canónicos:**
  - *Optics* - Eugene Hecht. (El texto clásico de pregrado).
  - *Principles of Optics* - Max Born & Emil Wolf. (El texto más profundo, clásico absoluto).
  - *Quantum Optics* - Marlan O. Scully & M. Suhail Zubairy. (Para la frontera cuántica).
