# 🔬 Laboratorio de Simulaciones Jupyter

Bienvenido a la joya de la corona del repositorio: La **Boutique de Simulaciones Jupyter**. 

Tras una purga masiva de cuadernos generados algorítmicamente, hemos pivotado hacia un modelo de curaduría de altísima calidad. Actualmente albergamos **187 simulaciones de física de élite**. Cada cuaderno ha sido diseñado a mano para abordar un fenómeno físico avanzado de forma interactiva y visual (con librerías como `numpy`, `scipy` y `matplotlib 3D`).

## Estructura de la Boutique

Todas nuestras simulaciones están organizadas en las mismas 16 áreas teóricas del repositorio principal:

- [x] **Mecánica Clásica**: (Caos determinista, Péndulos dobles acoplados).
- [x] **Relatividad**: (Agujero Negro de Kerr, Lentes gravitacionales, Expansión de Friedmann).
- [x] **Mecánica Cuántica**: (Efecto Aharonov-Bohm, Oscilaciones de Rabi, Barreras de potencial).
- [x] **Astrofísica y Cosmología**: (Espectro del CMB, Inflación Eterna, Juego de la Vida de Conway, Vacíos de Cuerdas).
- [x] **Termodinámica**: (Motores estocásticos, Fluctuaciones de Langevin).
- [x] **Electromagnetismo**: (Guías de onda, Radiación de sincrotrón).
- [x] **Métodos Matemáticos**: (Flujo de Ricci, Polinomios de Legendre, Funciones de Bessel, Armónicos Esféricos).
- [x] **Teoría Cuántica de Campos (NUEVO)**: (Mecanismo de Higgs, Renormalización QED/QCD, Lattice QCD, Propagadores de Feynman, Efecto Casimir).
- [x] **Gravedad Cuántica y Cuerdas (NUEVO)**: (Vibraciones de Supercuerdas, Entropía de Strominger-Vafa, D-Branas, Redes de Espín LQG, Geometría Calabi-Yau).

## 🚀 Cómo Ejecutar los Cuadernos en la Nube (Recomendado)

Para tu comodidad, todos los cuadernos están pre-configurados para ejecutarse de forma interactiva en la nube usando los servidores de Google, sin necesidad de instalar absolutamente nada en tu ordenador.

1. Navega por las subcarpetas de este directorio.
2. Haz clic en el cuaderno `.ipynb` que te interese visualizar.
3. En la parte superior del cuaderno, verás un botón como este: 
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)
4. Haz clic en él y el cuaderno se abrirá en **Google Colab**.
5. Presiona `Shift + Enter` para ejecutar las celdas de código de forma interactiva.

> [!TIP]
> **Truco de Navegación:** Debido a las políticas de seguridad de GitHub, los enlaces siempre se abren en la pestaña actual. Para abrir la simulación en una pestaña nueva sin perder tu lugar en GitHub, **haz clic con la rueda del ratón** sobre la insignia de Colab, o mantén pulsado **Ctrl / Cmd** al hacer clic.

*Nota: Para que el botón funcione, este repositorio debe estar sincronizado ("pusheado") a tu cuenta de GitHub de forma pública o darle permisos a Colab para repositorios privados.*

## 💻 Cómo Ejecutar los Cuadernos Localmente

Si prefieres ejecutar el código en tu propia computadora, sigue estos pasos:

1. Asegúrate de tener Python 3 instalado.
2. Abre una terminal y navega hasta la raíz de este repositorio.
3. Instala las dependencias necesarias:
   ```bash
   pip install jupyterlab numpy scipy matplotlib sympy
   ```
4. Inicia Jupyter Lab:
   ```bash
   jupyter lab
   ```
5. Se abrirá una pestaña en tu navegador web. Desde ahí, navega a la carpeta `Simulaciones_Jupyter/` y abre cualquier cuaderno.

- **13 Áreas Temáticas (Carpetas base)**: Todas las simulaciones del repositorio han sido consolidadas en sus áreas principales. Por ejemplo, `Relatividad/` contiene más de 150 cuadernos, `Mecanica_Clasica/` cientos más, etc. Estas carpetas unifican las simulaciones de la fase base, las de investigación avanzada, laboratorio especializado, proyectos de supercomputación y el compendio galáctico masivo.
