# [QFT-14] Cromodinámica Cuántica en el Retículo (Lattice QCD)

## 1. El Problema del Confinamiento de Color
La Cromodinámica Cuántica (QCD) describe cómo la fuerza fuerte une a los quarks mediante gluones. A altas energías (libertad asintótica), la perturbación matemática funciona. A bajas energías (masa del protón), la fuerza estalla y la teoría de perturbaciones falla. Nadie ha visto jamás un quark aislado (Confinamiento de Color).

## 2. La Formulación de Wilson (Retículo)
Para resolver ecuaciones no perturbativas, Kenneth Wilson propuso discretizar el espacio-tiempo euclidiano en una cuadrícula (Lattice) de espaciado $a$. 
- Los Quarks (Fermiones) habitan en los **sitios** del retículo.
- Los Gluones (Campos de Gauge) habitan en los **enlaces** (*links*) conectando los sitios, representados por matrices del grupo SU(3).

La integral de trayectoria cuántica infinita se convierte en una gigantesca integral múltiple evaluable numéricamente:
$$
Z = \int [dU] [d\psi] [d\bar{\psi}] \, e^{-S_{Lattice}}
$$

## 3. Algoritmos de Monte Carlo
Como una cuadrícula de $32^4$ sitios tiene millones de variables, la integral se evalúa estadísticamente. Usando Algoritmos de Monte Carlo basados en Cadenas de Markov (como Metropolis-Hastings o Hybrid Monte Carlo), los supercomputadores pueden calcular la masa del protón desde puros principios cuánticos con <1% de error.
