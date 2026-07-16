# Autómatas Celulares y Sistemas Complejos Discretos

## 1. Paradigma de la Complejidad Discreta
Propuestos por von Neumann y Ulam, los Autómatas Celulares (CA) modelan el caos espacial discreto. El espacio, el tiempo y los estados son variables cuantizadas. Un tablero multidimensional donde el estado de una célula obedece una regla algorítmica local con base en su vecindario.

## 2. El Juego de la Vida (John Conway)
El autómata bidimensional universalmente famoso. Las reglas para una cuadrícula con vecindario de Moore (8 vecinos adyacentes) son:
1. Una célula muerta con exactamente 3 vecinas vivas "nace".
2. Una célula viva con 2 o 3 vecinas sobrevive.
3. En cualquier otro caso, la célula muere por subpoblación o superpoblación.

A pesar de su trivialidad, genera estructuras complejas autopropulsadas (Gliders), puertas lógicas e impredecibilidad equivalente a la completitud de Turing (Halting Problem incomputable).

## 3. Autómatas Unidimensionales de Wolfram
Stephen Wolfram analizó los 256 posibles autómatas elementales unidimensionales (2 estados, rango 1 vecindario).
Las reglas se definen mapeando los $2^3 = 8$ posibles patrones binarios. 

Clasificación cualitativa de Dinámica (Regla 30 y 110):
- **Clase 1:** Convergencia a un estado homogéneo.
- **Clase 2:** Convergencia a un límite periódico o estructuras localizadas.
- **Clase 3 (Caos):** Comportamiento seudoaleatorio (Regla 30). Su atractor es estocástico.
- **Clase 4 (Complejidad):** Transición del borde del caos. Generación de estructuras de vida prolongada análogas al Juego de la Vida (Regla 110, probada universal para computación algorítmica).

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Santa Fe Institute (Complexity Explorer)](https://www.complexityexplorer.org/) - Cursos en Dinámica No Lineal, Caos y Sistemas Complejos.
  - [MIT 2.050J: Nonlinear Dynamics and Chaos](https://ocw.mit.edu/courses/18-062j-mathematics-of-machine-learning-fall-2015/) - Prof. Steven Strogatz (Cornell Lectures, muy populares en YouTube).
- **Libros de Texto Canónicos:**
  - *Nonlinear Dynamics and Chaos* - Steven H. Strogatz. (La "Biblia" introductoria).
  - *Classical Mechanics* (Sección de Caos) - John R. Taylor.
  - *Fractal Geometry of Nature* - Benoit Mandelbrot.
