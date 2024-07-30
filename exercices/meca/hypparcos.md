# Étude de l'orbite elliptique du satellite Hipparcos

## Énoncé

Le satellite Hipparcos a été lancé sur une orbite elliptique autour de la Terre avec une altitude minimale (périgée) de 400 km et une altitude maximale (apogée) de 36000 km. La Terre a un rayon de 6371 km et une masse de $$ 5.972 \times 10^{24} \, \text{kg} $$.

1. Déterminez les distances du périgée et de l'apogée par rapport au centre de la Terre.
2. Calculez le demi-grand axe $$ a $$ de l'orbite elliptique.
3. Calculez l'excentricité $$ e $$ de l'orbite.
4. Utilisez la loi des aires de Kepler pour déterminer la vitesse du satellite au périgée et à l'apogée.
5. Calculez la période orbitale du satellite en utilisant la troisième loi de Kepler.

## Corrigé

1. **Distances du périgée et de l'apogée par rapport au centre de la Terre** :

   - Distance au périgée $$ r_p $$ :
     $$
     r_p = R_T + h_p = 6371 \, \text{km} + 400 \, \text{km} = 6771 \, \text{km}
     $$

   - Distance à l'apogée $$ r_a $$ :
     $$
     r_a = R_T + h_a = 6371 \, \text{km} + 36000 \, \text{km} = 42371 \, \text{km}
     $$

2. **Calcul du demi-grand axe $$ a $$ de l'orbite elliptique** :

   Le demi-grand axe $$ a $$ est la moyenne des distances au périgée et à l'apogée :
   $$
   a = \frac{r_p + r_a}{2}
   $$

   En remplaçant les valeurs données :
   $$
   a = \frac{6771 \, \text{km} + 42371 \, \text{km}}{2} = \frac{49142 \, \text{km}}{2} = 24571 \, \text{km}
   $$

3. **Calcul de l'excentricité $$ e $$ de l'orbite** :

   L'excentricité $$ e $$ est donnée par :
   $$
   e = \frac{r_a - r_p}{r_a + r_p}
   $$

   En remplaçant les valeurs données :
   $$
   e = \frac{42371 \, \text{km} - 6771 \, \text{km}}{42371 \, \text{km} + 6771 \, \text{km}} = \frac{35600 \, \text{km}}{49142 \, \text{km}} \approx 0.724
   $$

4. **Vitesse du satellite au périgée et à l'apogée** :

   La vitesse au périgée $$ v_p $$ et à l'apogée $$ v_a $$ peuvent être déterminées en utilisant la loi des aires de Kepler et la conservation de l'énergie mécanique :

   - Vitesse au périgée :
     $$
     v_p = \sqrt{GM \left( \frac{2}{r_p} - \frac{1}{a} \right)}
     $$

   - Vitesse à l'apogée :
     $$
     v_a = \sqrt{GM \left( \frac{2}{r_a} - \frac{1}{a} \right)}
     $$

   Où $$ G = 6.67430 \times 10^{-11} \, \text{m}^3 \, \text{kg}^{-1} \, \text{s}^{-2} $$ est la constante gravitationnelle et $$ M = 5.972 \times 10^{24} \, \text{kg} $$ est la masse de la Terre.

   En remplaçant les valeurs (en utilisant des unités SI) :
   - Pour la vitesse au périgée :
     $$
     v_p = \sqrt{6.67430 \times 10^{-11} \times 5.972 \times 10^{24} \left( \frac{2}{6771 \times 10^3} - \frac{1}{24571 \times 10^3} \right)}
     $$
     $$
     v_p = \sqrt{398600.5 \left( \frac{2}{6771 \times 10^3} - \frac{1}{24571 \times 10^3} \right)}
     $$
     $$
     v_p \approx 10.73 \, \text{km/s}
     $$

   - Pour la vitesse à l'apogée :
     $$
     v_a = \sqrt{6.67430 \times 10^{-11} \times 5.972 \times 10^{24} \left( \frac{2}{42371 \times 10^3} - \frac{1}{24571 \times 10^3} \right)}
     $$
     $$
     v_a = \sqrt{398600.5 \left( \frac{2}{42371 \times 10^3} - \frac{1}{24571 \times 10^3} \right)}
     $$
     $$
     v_a \approx 1.46 \, \text{km/s}
     $$

5. **Période orbitale du satellite en utilisant la troisième loi de Kepler** :

   La troisième loi de Kepler donne la période orbitale $$ T $$ en fonction du demi-grand axe $$ a $$ :
   $$
   T^2 = \frac{4 \pi^2 a^3}{GM}
   $$

   Donc, la période $$ T $$ est :
   $$
   T = 2 \pi \sqrt{\frac{a^3}{GM}}
   $$

   En remplaçant les valeurs données :
   $$
   T = 2 \pi \sqrt{\frac{(24571 \times 10^3)^3}{6.67430 \times 10^{-11} \times 5.972 \times 10^{24}}}
   $$
   $$
   T = 2 \pi \sqrt{\frac{1.481 \times 10^{23}}{3.986 \times 10^{14}}}
   $$
   $$
   T \approx 2 \pi \sqrt{3.715 \times 10^8} \approx 2 \pi \times 19272 \approx 1.21 \times 10^5 \, \text{s}
   $$
   $$
   T \approx 121000 \, \text{s} \approx 33.6 \, \text{heures}
   $$

## Questions d'analyse

1. Pourquoi les distances du périgée et de l'apogée sont-elles mesurées par rapport au centre de la Terre et non à la surface ?
2. Comment l'excentricité de l'orbite affecte-t-elle la forme de l'orbite elliptique ?
3. Pourquoi la vitesse du satellite est-elle maximale au périgée et minimale à l'apogée ?
4. Comment la loi des aires de Kepler explique-t-elle les variations de vitesse du satellite ?
5. Si le demi-grand axe de l'orbite augmentait, comment cela affecterait-il la période orbitale du satellite ?

## Corrigé des questions d'analyse

1. Les distances du périgée et de l'apogée sont mesurées par rapport au centre de la Terre car les lois de Kepler et la gravitation universelle s'appliquent aux centres de masse des corps en interaction gravitationnelle.
2. L'excentricité de l'orbite détermine à quel point l'ellipse est allongée. Une excentricité de 0 correspond à une orbite circulaire, tandis qu'une excentricité proche de 1 correspond à une orbite très allongée.
3. La vitesse du satellite est maximale au périgée car il est le plus proche de la Terre, où l'attraction gravitationnelle est la plus forte. À l'apogée, la distance étant plus grande, l'attraction gravitationnelle est plus faible, et donc la vitesse est minimale.
4. La loi des aires de Kepler stipule que le rayon vecteur d'un satellite balaie des aires égales en des temps égaux. Cela signifie que le satellite se déplace plus rapidement lorsqu'il est plus proche de la Terre (périgée) et plus lentement lorsqu'il est plus éloigné (apogée).
5. Si le demi-grand axe de l'orbite augmentait, la période orbitale du satellite augmenterait également. Selon la troisième loi de Kepler, la période orbitale est proportionnelle à la racine carrée du cube du demi-grand axe.

