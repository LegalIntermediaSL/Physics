# Relaciones de Dispersión (Kramers-Kronig)

En la física de medios materiales (óptica, dieléctricos, acústica) y en la dispersión de partículas subatómicas, la respuesta de un sistema a un estímulo externo (como un campo eléctrico $E(\omega)$) viene dada por una función de respuesta compleja $\chi(\omega) = \chi'(\omega) + i\chi''(\omega)$.

*   La parte real $\chi'$ describe la **dispersión** (ej. el índice de refracción, que retarda la onda).
*   La parte imaginaria $\chi''$ describe la **absorción** o **disipación** (ej. la pérdida de energía de la onda).

## 1. El Principio de Causalidad
Las relaciones de Kramers-Kronig (KK) son un milagro del análisis complejo. Dictaminan que las partes real e imaginaria de cualquier función de respuesta física ¡no son independientes! Están atadas matemáticamente de por vida si, y solo si, el sistema respeta la **Causalidad** (el efecto no puede preceder a la causa; el sistema no puede responder antes de ser estimulado).

## 2. Las Ecuaciones de Kramers-Kronig
Utilizando el Teorema de Cauchy en el semiplano superior de la frecuencia compleja, se derivan las siguientes transformadas de Hilbert:

$$
\chi'(\omega) = \frac{1}{\pi} \mathcal{P} \int_{-\infty}^{\infty} \frac{\chi''(\omega')}{\omega' - \omega} d\omega'
$$

$$
\chi''(\omega) = -\frac{1}{\pi} \mathcal{P} \int_{-\infty}^{\infty} \frac{\chi'(\omega')}{\omega' - \omega} d\omega'
$$

*(Donde $\mathcal{P}$ denota el Valor Principal de Cauchy).*

## 3. Implicaciones Físicas
Si mides el espectro de *absorción* ($\chi''$) de un material a todas las frecuencias en el laboratorio (cuánta luz bloquea), puedes usar Kramers-Kronig en un ordenador para calcular matemáticamente cuál debe ser exactamente su *índice de refracción* ($\chi'$) a cualquier frecuencia, sin necesidad de medirlo. Causalidad + Variable Compleja imponen una rigidez total sobre las propiedades de la materia.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Carl Bender: Mathematical Physics (Washington University)](https://www.youtube.com/playlist?list=PL1B1123DDB9DD4668) - Brillantes clases de perturbaciones, asintóticos y WKB impartidas por un genio del análisis.
- [ICTP: Mathematics for Physicists](https://www.youtube.com/user/ictp) - Herramientas analíticas puras desde Trieste.
