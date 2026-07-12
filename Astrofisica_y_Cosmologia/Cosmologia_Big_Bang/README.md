# Cosmología del Big Bang

La Cosmología del Big Bang es el modelo estándar sobre el origen y evolución del universo, que postula que este comenzó en un estado extremadamente caliente y denso hace unos 13.800 millones de años, y ha estado expandiéndose y enfriándose desde entonces.

## 📜 Contexto Histórico

En la década de 1920, las soluciones a las ecuaciones de la Relatividad General de Einstein por parte de Alexander Friedmann (1922) y Georges Lemaître (1927) sugerían que el universo no era estático, sino dinámico (pudiendo expandirse o contraerse). Einstein, prefiriendo un universo estático, introdujo la Constante Cosmológica para forzar esta quietud.

Sin embargo, en 1929, Edwin Hubble descubrió la **Ley de Hubble-Lemaître**: las galaxias se alejan de nosotros con una velocidad proporcional a su distancia, la primera prueba empírica de la expansión del universo. Lemaître propuso la teoría del "Átomo Primigenio", sugiriendo que si hoy el universo se expande, en el pasado debió estar concentrado en un punto.

El modelo rival de Estado Estacionario (Fred Hoyle, 1948) perdió apoyo definitivamente cuando en 1964 Arno Penzias y Robert Wilson descubrieron accidentalmente el **Fondo Cósmico de Microondas (CMB)**, el remanente térmico previsto por la teoría del Big Bang. En los 90s, el estudio de supernovas tipo Ia reveló que esta expansión está acelerada debido a la llamada **Energía Oscura**.

---

## 🧮 Desarrollo Teórico Profundo

El universo a gran escala se asume homogéneo e isótropo (Principio Cosmológico). La geometría del espacio-tiempo está descrita por la **Métrica de Friedmann-Lemaître-Robertson-Walker (FLRW)**:

$$ds^2 = c^2 dt^2 - a(t)^2 \left[ \frac{dr^2}{1 - kr^2} + r^2(d\theta^2 + \sin^2\theta d\phi^2) \right]$$

Donde:
- $a(t)$ es el **factor de escala cosmológico** (describe cómo crece el espacio).
- $k$ es el parámetro de curvatura espacial ($k=0$ plano, $k=1$ cerrado, $k=-1$ abierto).

Sustituyendo esta métrica en las Ecuaciones de Einstein, se obtienen las **Ecuaciones de Friedmann**:

1. **Primera Ecuación de Friedmann (Evolución de la expansión):**
   $$H^2 = \left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}$$
   Donde $H(t) \equiv \dot{a}/a$ es el **Parámetro de Hubble**.

2. **Segunda Ecuación de Friedmann (Ecuación de Aceleración):**
   $$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3} \left( \rho + \frac{3P}{c^2} \right) + \frac{\Lambda c^2}{3}$$
   Donde $\rho$ es la densidad de energía y $P$ la presión.

**Densidad Crítica:**
Si tomamos $k=0$ y $\Lambda=0$, el universo es plano. La densidad requerida para esto es la densidad crítica:
$$\rho_c = \frac{3H^2}{8\pi G}$$

**Desplazamiento al Rojo (Redshift):**
La expansión estira la longitud de onda de la luz:
$$1 + z = \frac{\lambda_{\text{observada}}}{\lambda_{\text{emitida}}} = \frac{a(t_0)}{a(t_e)}$$
Donde $t_0$ es el tiempo actual y $t_e$ el tiempo de emisión.

---

## 🛠 Ejemplo Práctico

**Problema:** Suponiendo que el universo actual está dominado por materia no relativista, ¿cómo escala el factor de escala $a(t)$ con el tiempo?

**Solución paso a paso:**
1. Para la materia (polvo), la ecuación de continuidad hidrodinámica cósmica dice que la densidad disminuye con el volumen: 
   $$\rho_m \propto a^{-3} \implies \rho_m = \frac{\rho_0}{a^3}$$
   (Asumiendo $a(t_0) = 1$).
2. Partimos de la primera Ecuación de Friedmann para un universo plano ($k=0$) sin constante cosmológica ($\Lambda=0$):
   $$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3} \rho_m$$
3. Sustituyendo $\rho_m$:
   $$\frac{\dot{a}^2}{a^2} = \frac{8\pi G \rho_0}{3 a^3} \implies \dot{a}^2 = \frac{8\pi G \rho_0}{3 a}$$
4. Por lo tanto, $\dot{a} \propto a^{-1/2}$. Tomemos una constante de proporcionalidad $C$:
   $$\frac{da}{dt} = C a^{-1/2}$$
5. Integramos por separación de variables:
   $$\int a^{1/2} da = \int C dt$$
   $$\frac{2}{3} a^{3/2} = C t \implies a^{3/2} \propto t$$
6. Despejando $a(t)$:
   $$a(t) \propto t^{2/3}$$
**Conclusión:** En un universo plano y dominado por materia (como fue gran parte de la historia del universo antes de la dominación de la energía oscura), el factor de escala crece como $t^{2/3}$.

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
- **Stanford University: Cosmology (Leonard Susskind)** - Parte del Theoretical Minimum.
- **MIT 8.286 The Early Universe** - Clases por Alan Guth (creador de la teoría inflacionaria).
- **Perimeter Institute Seminars** - Para debates contemporáneos en cosmología.

### 📝 Artículos e Interactivos Interesantes
- [Planck Legacy Archive (ESA)](http://pla.esac.esa.int/) - Acceso a los mapas e imágenes reales del fondo cósmico de microondas.
- [Ned Wright's Cosmology Calculator](http://www.astro.ucla.edu/~wright/CosmoCalc.html) - Herramienta interactiva para calcular tiempos y distancias según corrimiento al rojo y parámetros cósmicos.
- [Wikipedia: Timeline of the early universe](https://en.wikipedia.org/wiki/Timeline_of_the_early_universe) - Un repaso cronológico profundo de las primeras fracciones de segundo.
