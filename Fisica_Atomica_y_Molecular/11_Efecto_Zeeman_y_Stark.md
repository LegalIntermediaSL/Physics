# Efecto Zeeman y Stark en Átomos

## 1. El Átomo Sometido a Campos Externos
Los niveles de energía atómica, previstos por Bohr y formalizados en la Ecuación de Dirac, son degenerados. Varios orbitales de electrones con diferente espín magnético o forma 3D (diferente número cuántico $m_l$) tienen exactamente la misma energía. Sin embargo, al encender un campo magnético o eléctrico de fondo, la simetría rotacional esférica se "rompe".
Los orbitales degenerados reaccionan diferente, y las líneas espectrales atómicas solitarias se agrietan y multiplican visualmente (Multipletes). 

## 2. Efecto Zeeman Normal (Campo Magnético)
Descubierto por Pieter Zeeman, ocurre por la interacción entre el Momento Bipolar Magnético orbital del electrón ($\vec{\mu} = -\frac{e}{2m}\vec{L}$) y un campo externo $\vec{B}$.
El Hamiltoniano adquiere un término extra perturbativo $H_Z = -\vec{\mu} \cdot \vec{B}$.
La energía espectral de un estado con un momento angular de proyección orbital magnética $m_l$ (ej, los tres estados $p$: -1, 0, 1) se bifurca linealmente:

$$
\Delta E = \mu_B B m_l
$$

Donde $\mu_B$ es el Magnetón de Bohr. Un láser de una sola frecuencia emitido por este átomo se divide puramente en tres láseres adyacentes distintos (Triplete de Lorentz clásico). 

## 3. Efecto Zeeman Anómalo y Espín Relativista
Sin embargo, para campos débiles y átomos complejos con números atómicos impar, las líneas no se rompían en tres, sino en esquemas enrevesados inexplicables (Efecto Anómalo). ¡Esta anomalía fue la primera prueba palpable en la historia del Espín del electrón! 
Debemos acoplar el número cuántico de espín intrínseco ($S$) relativista. La ruptura de niveles depende del Momento Angular Total $\vec{J} = \vec{L} + \vec{S}$ e incorpora el exótico **Factor g de Landé**:

$$
\Delta E = g_J \mu_B B m_j
$$

Para campos inmensos, este delicado acoplamiento interno "Espín-Órbita" (la interacción magnética entre el espín del electrón y el núcleo orbitando) se sobrepasa y destruye, restaurando la división clásica sencilla (el **Efecto Paschen-Back**).

## 4. Efecto Stark (Campo Eléctrico)
Similarmente, Johannes Stark descubrió la división espectral bajo campos Eléctricos intensos $\vec{E}$. Las órbitas de los electrones se distorsionan y se "estiran" asimétricamente polarizándose $\Delta E = - \vec{p}_{e} \cdot \vec{E}$. Afecta drásticamente las transiciones del Hidrógeno y es utilizado hoy para enfriamiento atómico cuántico.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.421: Atomic and Optical Physics I](https://ocw.mit.edu/courses/8-421-atomic-and-optical-physics-i-spring-2014/) - Prof. Wolfgang Ketterle (Premio Nobel por el condensado de Bose-Einstein).
  - [Oxford University: Atomic and Laser Physics](https://podcasts.ox.ac.uk/series/atomic-and-laser-physics).
- **Libros de Texto Canónicos:**
  - *Atomic Physics* - Christopher J. Foot.
  - *Physics of Atoms and Molecules* - B.H. Bransden & C.J. Joachain.
- **Lecturas Fundamentales:**
  - Artículos originales de Ketterle y Cornell sobre el enfriamiento láser y el BEC.
