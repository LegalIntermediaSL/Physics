# 🔬 Laboratorio de Simulaciones Jupyter

Este directorio contiene **720 Cuadernos Jupyter (`.ipynb`)** interactivos, clasificados por dificultad y área de la física, que abarcan desde cinemática básica hasta simulaciones de supercomputación y física de frontera.

Cada cuaderno ha sido programado con `numpy`, `scipy` y `matplotlib` para asegurar la máxima eficiencia y visualización.

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

## 📁 Estructura del Directorio

- **13 Áreas Temáticas (Carpetas base)**: Contienen 70 simulaciones iniciales sobre principios fundamentales de la física.
- **`Investigacion_Avanzada/`**: 39 proyectos que exploran fronteras numéricas, topología, relatividad y termodinámica moderna.
- **`Laboratorio_Especializado/`**: 91 algoritmos que detallan problemas específicos y profundos (Teoría BCS, Computación Cuántica, Geodésicas).
- **`Proyectos_de_Supercomputacion/`**: 100 colosales proyectos de física computacional de alto rendimiento (HPC), modelando turbulencia 3D, agujeros negros relativistas y QCD en el retículo.
- **`Compendio_Subtematico/`**: 420 simulaciones masivas (escala industrial) que cubren exhaustivamente cada uno de los 72 subtemas específicos del repositorio.
