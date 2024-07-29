# Fibre optique à saut d'indice

## Énoncé

1. Une fibre optique à saut d'indice est constituée d'un cœur de matériau transparent de rayon $$a$$ et d'indice de réfraction $$n_1$$, entouré d'une gaine d'indice de réfraction $$n_2$$ ($$n_2 < n_1$$). La lumière est guidée dans le cœur de la fibre grâce à la réflexion totale interne.
2. Rappelez le principe de fonctionnement d'une fibre optique à saut d'indice.
3. Déterminez l'angle critique $$\theta_c$$ pour lequel la réflexion totale interne se produit à l'interface cœur-gaine.
4. Calculez l'angle d'acceptance maximal $$\theta_{\text{max}}$$ pour lequel la lumière entrant dans la fibre sera guidée par réflexion totale interne.
5. Si $$n_1 = 1.5$$ et $$n_2 = 1.4$$, calculez les valeurs de $$\theta_c$$ et $$\theta_{\text{max}}$$.

## Corrigé

1. **Principe de fonctionnement d'une fibre optique à saut d'indice** :
   Une fibre optique à saut d'indice utilise la différence d'indice de réfraction entre le cœur ($$n_1$$) et la gaine ($$n_2$$) pour confiner la lumière dans le cœur. Lorsque la lumière atteint l'interface cœur-gaine avec un angle d'incidence supérieur à l'angle critique $$\theta_c$$, elle subit une réflexion totale interne et reste confinée dans le cœur de la fibre, permettant ainsi le transport de la lumière sur de longues distances avec peu de perte.

2. **Détermination de l'angle critique $$\theta_c$$** :
   L'angle critique $$\theta_c$$ est donné par la loi de Snell à l'interface cœur-gaine :
   $$
   \sin(\theta_c) = \frac{n_2}{n_1}
   $$

3. **Calcul de l'angle d'acceptance maximal $$\theta_{\text{max}}$$** :
   L'angle d'acceptance maximal $$\theta_{\text{max}}$$ est l'angle d'incidence maximal à l'entrée de la fibre pour lequel la lumière sera guidée par réflexion totale interne. En utilisant le principe de réflexion totale interne et la géométrie du trajet de la lumière dans la fibre, on trouve :
   $$
   \sin(\theta_{\text{max}}) = \sqrt{n_1^2 - n_2^2}
   $$

4. **Calcul des valeurs pour $$n_1 = 1.5$$ et $$n_2 = 1.4$$** :
   - Pour $$\theta_c$$ :
     $$
     \sin(\theta_c) = \frac{1.4}{1.5} \approx 0.933
     $$
     Donc,
     $$
     \theta_c = \arcsin(0.933) \approx 68.91^\circ
     $$

   - Pour $$\theta_{\text{max}}$$ :
     $$
     \sin(\theta_{\text{max}}) = \sqrt{1.5^2 - 1.4^2} = \sqrt{2.25 - 1.96} = \sqrt{0.29} \approx 0.539
     $$
     Donc,
     $$
     \theta_{\text{max}} = \arcsin(0.539) \approx 32.48^\circ
     $$

## Questions d'analyse

1. Pourquoi la réflexion totale interne est-elle essentielle pour le fonctionnement des fibres optiques ?
2. Si l'indice de réfraction du cœur $$n_1$$ est légèrement supérieur à celui de la gaine $$n_2$$, comment cela affecte-t-il l'angle critique et l'angle d'acceptance ?
3. Pourquoi utilise-t-on des matériaux avec une différence d'indice de réfraction bien définie pour les cœurs et les gaines des fibres optiques ?
4. Comment serait modifié l'angle d'acceptance si l'indice de réfraction de la gaine $$n_2$$ augmentait ?
5. Quel serait l'effet d'une impureté à l'interface cœur-gaine sur la performance de la fibre optique ?

## Corrigé des questions d'analyse

1. La réflexion totale interne est essentielle pour le fonctionnement des fibres optiques car elle permet de confiner la lumière dans le cœur de la fibre. Cela minimise les pertes de signal et permet le transport efficace de la lumière sur de longues distances.
2. Si l'indice de réfraction du cœur $$n_1$$ est légèrement supérieur à celui de la gaine $$n_2$$, l'angle critique $$\theta_c$$ augmente, ce qui signifie que la lumière peut entrer dans la fibre avec un angle plus large tout en restant confinée par réflexion totale interne. L'angle d'acceptance $$\theta_{\text{max}}$$ devient également plus grand.
3. On utilise des matériaux avec une différence d'indice de réfraction bien définie pour assurer une réflexion totale interne efficace et stable. Une différence trop faible pourrait ne pas confiner efficacement la lumière, tandis qu'une différence trop grande pourrait causer des pertes dues à des effets dispersifs ou à la fabrication plus complexe de la fibre.
4. Si l'indice de réfraction de la gaine $$n_2$$ augmentait, l'angle critique $$\theta_c$$ diminuerait, ce qui rendrait plus difficile la condition de réflexion totale interne. Par conséquent, l'angle d'acceptance $$\theta_{\text{max}}$$ diminuerait également, réduisant la plage d'angles pour lesquels la lumière peut entrer et être guidée dans la fibre.
5. Une impureté à l'interface cœur-gaine pourrait perturber la réflexion totale interne, causant des pertes de signal, une dispersion accrue et une diminution de la performance globale de la fibre optique. Cela pourrait aussi introduire des modes de propagation indésirables, affectant la qualité du signal transmis.
