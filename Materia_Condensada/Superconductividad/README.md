# Superconductividad

La superconductividad es un estado cuántico macroscópico de la materia que ocurre en ciertos materiales a muy bajas temperaturas. Se caracteriza por dos fenómenos fundamentales: una resistencia eléctrica exactamente igual a cero y la expulsión del campo magnético de su interior (Efecto Meissner).

## 📜 Contexto Histórico

La superconductividad fue descubierta en 1911 por Heike Kamerlingh Onnes en Leiden al observar que la resistencia del mercurio sólido caía abruptamente a cero al enfriarse a 4.2 K mediante helio líquido. En 1933, Walther Meissner y Robert Ochsenfeld descubrieron el diamagnetismo perfecto en los superconductores. El gran avance teórico se dio en 1957 con la teoría BCS (Bardeen, Cooper y Schrieffer), la cual demostró que los electrones interactuando a través de la red (fonones) pueden formar "pares de Cooper" y condensarse en un estado base colectivo. En 1986, Bednorz y Müller descubrieron los superconductores de alta temperatura (cupratos), un enigma teórico que aún no tiene una explicación completa.

## 🧮 Desarrollo Teórico Profundo

La superconductividad marca un quiebre paradigmático respecto a la conducción de Drude-Sommerfeld. Dejar que la resistividad tienda puramente a cero es un enfoque clásico incompleto: un conductor perfecto "congela" su flujo magnético interior. Un superconductor genuino, sin embargo, posee diamagnetismo perfecto y expulsa activamente el campo estático mediante el **Efecto Meissner-Ochsenfeld**.

### 1. Ecuaciones de London (1935)

Para capturar la fenomenología macroscópica uniendo el flujo sin disipación con el efecto Meissner, los hermanos Heinz y Fritz London postularon dos ecuaciones gobernando a los "electrones superfluidos" de densidad $n_s$.

En ausencia de dispersión, la segunda ley de Newton rige la velocidad $\mathbf{v}$ de los superfluidos en un campo eléctrico $\mathbf{E}$:
$$ m_e \frac{\partial \mathbf{v}}{\partial t} = -e \mathbf{E} $$
Multiplicando por $(-n_s e)$ definimos la densidad de corriente $\mathbf{J}_s = -n_s e \mathbf{v}$, derivando la **Primera Ecuación de London**:
$$ \frac{\partial \mathbf{J}_s}{\partial t} = \frac{n_s e^2}{m_e} \mathbf{E} $$
Esta describe un conductor donde la corriente acelera continuamente mientras haya un $\mathbf{E}$ (resistividad nula).

El paso audaz fue aplicar el rotacional a la ley de Faraday y acoplar el momento canónico $\mathbf{p} = m_e\mathbf{v} - e\mathbf{A}$, exigiendo que el rotacional del momento cinético sea nulo para el estado base coherente macroscópico. Esto arroja la **Segunda Ecuación de London**:
$$ \nabla \times \mathbf{J}_s = -\frac{n_s e^2}{m_e} \mathbf{B} $$

Insertando esta ecuación en el rotacional de la ley estática de Ampère ($\nabla \times \mathbf{B} = \mu_0 \mathbf{J}_s$), y usando la identidad vectorial del rotacional:
$$ \nabla \times (\nabla \times \mathbf{B}) = \mu_0 (\nabla \times \mathbf{J}_s) \implies -\nabla^2 \mathbf{B} = -\frac{\mu_0 n_s e^2}{m_e} \mathbf{B} $$
Reescribimos esto como una ecuación diferencial de Helmholtz atenuada:
$$ \nabla^2 \mathbf{B} = \frac{1}{\lambda_L^2} \mathbf{B} \quad \text{donde} \quad \lambda_L = \sqrt{\frac{m_e}{\mu_0 n_s e^2}} $$
La solución física $\mathbf{B}(x) = \mathbf{B}(0) e^{-x/\lambda_L}$ demuestra que un campo aplicado desde la superficie decae exponencialmente al adentrarse en el volumen. La corriente de apantallamiento en la superficie neutraliza rigurosamente el flujo, forzando un $B_{int}=0$.

### 2. Teoría Microscópica BCS (1957)

La fenomenología de London, siendo macroscópica, no explicaba el origen de $n_s$. La teoría BCS (Bardeen, Cooper, Schrieffer) expuso que el mar de Fermi puro es inestable frente a interacciones atractivas minúsculas. 

Si un electrón deforma localmente la red iónica elástica a su paso, otro electrón que siga su estela "siente" esa acumulación de carga positiva retardada, experimentando una atracción mediada por vibraciones cristalinas (**fonones**). Esta interacción electrón-fonón-electrón supera la repulsión coulómbica repulsiva, emparejando fermiones opuestos en estado de espín singlete ($S=0, L=0$), formando **Pares de Cooper**: $(\mathbf{k}\uparrow, -\mathbf{k}\downarrow)$.

Al aparearse, estos pares adquieren estadística bosónica (aproximadamente) y se condensan en un único estado fundamental coherente macroscópico, descripto por la función de onda de BCS:
$$ |\Psi_{BCS}\rangle = \prod_{\mathbf{k}} \left( u_\mathbf{k} + v_\mathbf{k} c^\dagger_{\mathbf{k}\uparrow} c^\dagger_{-\mathbf{k}\downarrow} \right) |0\rangle $$
donde $|v_\mathbf{k}|^2$ es la probabilidad de que el par $\mathbf{k}$ esté ocupado, y $|u_\mathbf{k}|^2 + |v_\mathbf{k}|^2 = 1$.

Este condensado altamente entrelazado crea un hiato energético o **Gap ($\Delta$)** en el espectro de excitaciones de cuasipartículas de Bogoliubov $E_\mathbf{k} = \sqrt{\epsilon_\mathbf{k}^2 + \Delta^2}$. A diferencia de los aislantes o semiconductores, el gap no ocurre en coordenadas espaciales, sino que el espectro energético entero se abre centrípetamente sobre la superficie de Fermi térmica, imposibilitando la dispersión por impurezas que exijan transferencias de energía menores a $2\Delta$ (romper el par).

A $T=0\,K$, la magnitud del gap predicha por BCS relaciona elegantemente el parámetro microscópico del fonón (la frecuencia de Debye $\omega_D$) con la Temperatura Crítica macroscópica observable $T_c$:
$$ 2\Delta(0) \approx 3.52 k_B T_c $$

### Diagrama: Efecto Meissner vs Conductor Perfecto

```mermaid
graph LR
    subgraph Metal Normal (T > Tc)
    A(Líneas de Campo Magnético) -. Atraviesan Volumen .-> B(B != 0)
    end
    
    subgraph Conductor Perfecto Teórico
    C(Líneas B congeladas in situ) -. La resistencia baja a cero .-> D(B = constante interior)
    end
    
    subgraph Superconductor Real (T < Tc)
    E(Líneas B) -. Expulsión Activa<br>Meissner-Ochsenfeld .-> F[Diamagnetismo Perfecto<br>B = 0 en el Bulk]
    F -. Fluyen Corrientes de Superficie .-> G(Atenuación Exponencial &lambda;_L)
    end
    
    style A fill:#457b9d,stroke:#fff,color:#fff
    style C fill:#d62828,stroke:#fff,color:#fff
    style E fill:#023047,stroke:#fff,color:#fff
    style F fill:#219ebc,stroke:#fff,color:#000
```

## 🛠 Ejemplo Práctico

**Problema:** Un anillo toroidal superconductor es enfriado debajo de su $T_c$ en presencia de un campo magnético coaxial y luego el campo externo se apaga (enfriamiento de campo, o *field-cooling*). 
Debido a la topología multiconexa (un agujero en el centro), el Efecto Meissner expulsa el campo del "bulk" del anillo pero atrapa un flujo magnético en el espacio vacío del hueco. 
Usando el concepto del momento canónico macroscópico de los pares de Cooper y la condición de frontera cuántica de Bloch, deduzca y demuestre matemáticamente que **el flujo magnético $\Phi_B$ atrapado en el agujero está estrictamente cuantizado** en múltiplos del "Cuanto de Flujo" ($\Phi_0 = h/2e$).

**Solución paso a paso:**

1. **Estado Macroscópico Coherente:**
   En un superconductor, todos los pares de Cooper forman un único condensado coherente descrito por una función de onda macroscópica $\Psi = |\Psi_0| e^{i\theta(\mathbf{r})}$, donde $\theta(\mathbf{r})$ es la fase compleja global y $|\Psi_0|^2 \approx n_s/2$ (la densidad de pares, de masa $2m_e$ y carga $q^* = -2e$).

2. **Momento y Velocidad Superfluida:**
   El operador de momento de un paquete bosónico en campo magnético es $\mathbf{p} = \hbar \nabla \theta$. Físicamente, el momento canónico es $\mathbf{p} = M\mathbf{v}_s + q^*\mathbf{A}$. 
   Igualando y operando sobre los pares de masa $2m_e$ y carga $-2e$:
   $$ \hbar \nabla \theta = (2m_e)\mathbf{v}_s - 2e\mathbf{A} $$

3. **Curva de Integración Topológica:**
   Seleccionemos una curva cerrada $C$ arbitraria alrededor del agujero interior del toroide, localizada **profundamente dentro del espesor (bulk)** del superconductor.
   Debido al efecto Meissner exponencial, la corriente de apantallamiento sólo fluye en una cáscara delgada superficial. Profundo en el bulk, **la velocidad del superfluido desaparece** ($\mathbf{v}_s \approx 0$).
   Por ende, a lo largo de $C$:
   $$ \hbar \nabla \theta \approx -2e \mathbf{A} $$

4. **Integración de Línea y Teorema de Stokes:**
   Integramos ambos lados del gradiente de la fase a lo largo de la trayectoria cerrada $C$:
   $$ \oint_C \hbar \nabla \theta \cdot d\mathbf{l} = -2e \oint_C \mathbf{A} \cdot d\mathbf{l} $$
   Por el Teorema de Stokes aplicado al potencial vectorial electrodinámico, la integral de contorno de $\mathbf{A}$ equivale al flujo magnético netamente abrazado por $C$:
   $$ \oint_C \mathbf{A} \cdot d\mathbf{l} = \iint_S (\nabla \times \mathbf{A}) \cdot d\mathbf{S} = \iint_S \mathbf{B} \cdot d\mathbf{S} = \Phi_B $$
   
5. **Condición de Periodicidad Cuántica:**
   La función de onda macroscópica $\Psi$ debe ser estrictamente monoevaluada al rotar $360^\circ$ alrededor del toroide ($\mathbf{r} \to \mathbf{r}$). Esto demanda rigurosamente que la fase $\theta(\mathbf{r})$ cambie exactamente en un múltiplo entero de $2\pi$:
   $$ \Delta\theta = \oint_C \nabla \theta \cdot d\mathbf{l} = 2\pi n \quad \text{donde } n \in \mathbb{Z} $$

6. **Relación de Cuantización de Flujo:**
   Insertando $\Delta\theta = 2\pi n$ y la definición de Stokes $\Phi_B$ en nuestro paso de integración previo:
   $$ \hbar (2\pi n) = -2e \Phi_B $$
   Tomando el valor absoluto para la magnitud física del flujo atrapado:
   $$ \Phi_B = n \left( \frac{h}{2e} \right) = n \Phi_0 $$

**Conclusión Física:** El flujo magnético incrustado topológicamente dentro del anillo no es continuo, sino que viene en bultos atómicos macroscópicos irreducibles llamados "Fluxones" ($\Phi_0 = h/2e \approx 2.067 \times 10^{-15} \, \text{Wb}$). La presencia del divisor fundamental $2e$ (carga dual) es la prueba experimental más contundente e indiscutible de que la superconductividad está orquestada por el apareamiento de electrones, siendo el pilar verificatorio final del modelo BCS.

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Longitud de Penetración de London $\lambda_L$
A partir de la ecuación de London $\nabla \times \mathbf{J}_s = -\frac{n_s e^2}{m} \mathbf{B}$, deduzca que el campo magnético decae exponencialmente dentro de un superconductor (efecto Meissner) y encuentre la expresión de la longitud de penetración $\lambda_L$.

**Solución paso a paso:**
Partimos de la ley de Ampère en magnetostática (despreciando la corriente de desplazamiento):
$$ \nabla \times \mathbf{B} = \mu_0 \mathbf{J}_s $$
Tomamos el rotacional en ambos lados de esta ecuación:
$$ \nabla \times (\nabla \times \mathbf{B}) = \mu_0 (\nabla \times \mathbf{J}_s) $$
Usando la identidad vectorial $\nabla \times (\nabla \times \mathbf{B}) = \nabla(\nabla \cdot \mathbf{B}) - \nabla^2 \mathbf{B}$.
Como por la ley de Gauss magnética $\nabla \cdot \mathbf{B} = 0$, obtenemos:
$$ -\nabla^2 \mathbf{B} = \mu_0 (\nabla \times \mathbf{J}_s) $$
Ahora sustituimos la ecuación de London:
$$ -\nabla^2 \mathbf{B} = \mu_0 \left( -\frac{n_s e^2}{m} \mathbf{B} \right) $$
Reordenando:
$$ \nabla^2 \mathbf{B} = \frac{\mu_0 n_s e^2}{m} \mathbf{B} $$
Definimos la constante $\lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}$, con lo que la ecuación diferencial queda:
$$ \nabla^2 \mathbf{B} = \frac{1}{\lambda_L^2} \mathbf{B} $$
Para una interfaz plana superconductora en $x=0$ ocupando el semiespacio $x>0$, con un campo paralelo a la superficie $B(0) = B_0$, la solución unidimensional es:
$$ B(x) = B_0 e^{-x / \lambda_L} $$
Esto demuestra matemáticamente el efecto Meissner: el campo decae en una distancia característica $\lambda_L$, la longitud de penetración de London.

### Problema 2: Cuantización del Flujo Magnético
Demuestre que el flujo magnético atrapado en un anillo superconductor está cuantizado en unidades de $\Phi_0 = h/2e$.

**Solución paso a paso:**
Consideremos la función de onda macroscópica de los pares de Cooper que forman el condensado superconductor:
$$ \Psi(\mathbf{r}) = \sqrt{n_s} e^{i\theta(\mathbf{r})} $$
El operador momento mecánico de un par de Cooper en un campo electromagnético (vector potencial $\mathbf{A}$) es $m\mathbf{v} = \mathbf{p} - q\mathbf{A} = \hbar \nabla \theta - q\mathbf{A}$.
La densidad de corriente superfluda es:
$$ \mathbf{J}_s = n_s q \mathbf{v} = \frac{n_s q}{m} (\hbar \nabla \theta - q\mathbf{A}) $$
Si trazamos una curva cerrada $C$ en el interior grueso del anillo, a una distancia de la superficie mayor que la longitud de penetración $\lambda_L$, la corriente $\mathbf{J}_s$ allí es cero.
$$ 0 = \hbar \nabla \theta - q\mathbf{A} \implies \nabla \theta = \frac{q}{\hbar} \mathbf{A} $$
Integramos a lo largo del contorno cerrado $C$:
$$ \oint_C \nabla \theta \cdot d\mathbf{l} = \frac{q}{\hbar} \oint_C \mathbf{A} \cdot d\mathbf{l} $$
Por el teorema de Stokes, la integral de $\mathbf{A}$ alrededor de $C$ es el flujo magnético total $\Phi$ que atraviesa el área encerrada.
$$ \Delta \theta = \frac{q}{\hbar} \Phi $$
Para que la función de onda $\Psi$ sea monoevaluada al dar una vuelta completa, el cambio de fase $\Delta \theta$ debe ser un múltiplo entero de $2\pi$:
$$ \Delta \theta = 2\pi n $$
Por lo tanto:
$$ 2\pi n = \frac{q}{\hbar} \Phi \implies \Phi = n \frac{h}{q} $$
Como los portadores en el estado superconductor son pares de Cooper, tienen carga $q = 2e$.
$$ \Phi = n \frac{h}{2e} \equiv n \Phi_0 $$
Donde $\Phi_0 \approx 2.067 \times 10^{-15}$ Wb es el cuanto de flujo magnético.

### Problema 3: Termodinámica del Campo Crítico
Para un superconductor de tipo I, utilice los argumentos termodinámicos macroscópicos para calcular la diferencia de densidad de energía libre (estado normal vs estado superconductor) en función del campo crítico termodinámico $H_c(T)$.

**Solución paso a paso:**
Cuando se aplica un campo magnético $H < H_c$ a un superconductor, este lo expulsa perfectamente (Meissner), actuando como un diamagneto perfecto con magnetización $M = -H$.
El trabajo magnético diferencial realizado sobre la unidad de volumen de material es $dG = -\mu_0 M \cdot dH = \mu_0 H dH$.
Integramos este trabajo desde campo nulo hasta el campo aplicado $H_a$:
$$ G_s(T, H_a) - G_s(T, 0) = \int_0^{H_a} \mu_0 H dH = \frac{1}{2} \mu_0 H_a^2 $$
La energía libre del estado superconductor aumenta cuadráticamente con el campo debido a las corrientes superficiales generadas para expulsarlo.
Para un metal normal, la magnetización es despreciable $M \approx 0$, por lo que la energía libre no cambia significativamente con el campo externo: $G_n(T, H_a) \approx G_n(T, 0)$.
La transición del estado superconductor al estado normal ocurre precisamente al campo crítico $H_c(T)$, donde las energías libres de ambas fases se igualan:
$$ G_s(T, H_c) = G_n(T, H_c) $$
Sustituyendo la expresión para el estado superconductor en $H_c$:
$$ G_s(T, 0) + \frac{1}{2} \mu_0 H_c(T)^2 = G_n(T, 0) $$
Reordenando:
$$ \Delta G(T) = G_n(T, 0) - G_s(T, 0) = \frac{1}{2} \mu_0 H_c(T)^2 $$
Esta ecuación nos da la diferencia de energía de estabilización (o energía de condensación) del estado superconductor frente al estado normal a campo magnético nulo. Se observa que el campo crítico representa una medida directa de la fuerza de la condensación superconductora.

## 💻 Simulaciones Computacionales

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_meissner_effect():
    x = np.linspace(0, 5, 200)
    lambda_L = 1.0 # London penetration depth
    
    B_x = np.exp(-x / lambda_L)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, B_x, label='$B(x) = B_0 e^{-x/\lambda_L}$', lw=2, color='blue')
    plt.fill_between(x, B_x, alpha=0.2, color='blue')
    plt.axvline(0, color='k', lw=2, label='Superficie del Superconductor')
    
    plt.xlabel('Profundidad x (en unidades de $\lambda_L$)')
    plt.ylabel('Campo Magnético B(x)')
    plt.title('Simulación: Efecto Meissner y Atenuación de London')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    plot_meissner_effect()
```

## 📚 Recursos Específicos

### Cursos
1. **[Introducción a la Superconductividad (Coursera / NPTEL)](https://www.coursera.org):** Excelente cubrimiento de fenomenología y London.
2. **[Solid State Physics 2 (MIT OCW)](https://ocw.mit.edu):** Dedica una parte muy sustancial a la teoría de Ginzburg-Landau y BCS.
3. **[Superconductivity and Superfluidity (Cambridge lectures)](https://www.cam.ac.uk):** Fenómenos cuánticos macroscópicos relacionados.
4. **[Quantum Matter (edX)](https://www.edx.org):** Analiza pares de Cooper y estados topológicos superconductores.
5. **[Applied Superconductivity (Stanford)](https://online.stanford.edu):** Enfocado en aplicaciones de ingeniería (SQUIDs, imanes MRI).

### Artículos y Simulaciones
1. **["Theory of Superconductivity" (Bardeen, Cooper, Schrieffer, 1957)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.108.1175):** El artículo original de Physical Review, fundamental en la física del siglo XX.
2. **[PhET - Superconductivity (legacy)](https://phet.colorado.edu):** Simulación visual del efecto Meissner y diamagnetismo perfecto.
3. **["High-Temperature Superconductivity" (Bednorz & Müller, Nobel lecture)](https://www.nobelprize.org):** Historia de los cupratos.
4. **[Vórtices de Abrikosov (Simulaciones GL)](https://github.com):** Scripts en Python/MATLAB para visualizar la red de vórtices en superconductores Tipo II.
5. **["Quantum Computing with Superconducting Qubits" (Review en Nature)](https://www.nature.com):** Superconductividad aplicada a la tecnología de frontera actual.
6. **[Documentales sobre levitación magnética y Maglev](https://www.youtube.com):** Para ver el efecto macroscópico del pinning de flujo.
7. **[QuTiP (Quantum Toolbox in Python)](https://qutip.org/):** Útil para simular circuitos superconductores (SQUIDs y transmones).
8. **["Room-temperature superconductivity" (Debates recientes en Nature)](https://www.nature.com):** Literatura contemporánea sobre los polémicos avances recientes (hidruros bajo presión).

### 📖 Referencias Útiles y Bibliografía
1. [Tinkham, M. *Introduction to Superconductivity*](https://store.doverpublications.com). McGraw-Hill. (El libro definitivo sobre el tema).
2. [Schrieffer, J. R. *Theory of Superconductivity*](https://archive.org). CRC Press.
3. [De Gennes, P. G. *Superconductivity of Metals and Alloys*](https://archive.org). Westview Press.
4. [Ashcroft, N. W., & Mermin, N. D. *Solid State Physics*](https://archive.org) (Capítulo 34).
5. [Kittel, C. *Introduction to Solid State Physics*](https://archive.org) (Capítulo sobre superconductividad).
