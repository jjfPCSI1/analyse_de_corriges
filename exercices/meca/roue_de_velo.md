# Mouvement d'un point emporté par une roue de vélo

![](images/roue_de_velo.webp)

## Énoncé

Considérez un point $$ P $$ situé sur le bord d'une roue de vélo de rayon $$ R $$ roulant sans glisser sur le sol. La roue tourne avec une vitesse angulaire constante $$ \omega $$. On choisit l'origine du repère au centre de la roue, avec l'axe $$ x $$ horizontal et l'axe $$ y $$ vertical.

1. Écrivez les coordonnées $$ x(t) $$ et $$ y(t) $$ du point $$ P $$ en fonction du temps.
2. Calculez les composantes de la vitesse du point $$ P $$ en fonction du temps.
3. Déterminez les composantes de l'accélération du point $$ P $$ en fonction du temps.
4. Trouvez les coordonnées du point $$ P $$ et sa vitesse au temps $$ t = 1 \, \text{s} $$, en utilisant les valeurs $$ R = 0.5 \, \text{m} $$ et $$ \omega = 2 \, \text{rad/s} $$.

## Corrigé

1. **Coordonnées $$ x(t) $$ et $$ y(t) $$ du point $$ P $$ en fonction du temps** :

   Le mouvement du point $$ P $$ est une combinaison du mouvement de rotation autour du centre de la roue et du mouvement de translation de la roue le long de l'axe $$ x $$.

   La position du centre de la roue à l'instant $$ t $$ est :
   $$
   x_c(t) = R \omega t
   $$

   La position du point $$ P $$ par rapport au centre de la roue est donnée par :
   $$
   x_r(t) = R \cos(\omega t)
   $$
   $$
   y_r(t) = R \sin(\omega t)
   $$

   Donc, les coordonnées du point $$ P $$ en fonction du temps sont :
   $$
   x(t) = x_c(t) + x_r(t) = R \omega t + R \cos(\omega t)
   $$
   $$
   y(t) = y_r(t) = R \sin(\omega t)
   $$

2. **Composantes de la vitesse du point $$ P $$ en fonction du temps** :

   La vitesse est la dérivée des coordonnées par rapport au temps :
   $$
   v_x(t) = \frac{dx(t)}{dt} = R \omega - R \omega \sin(\omega t)
   $$
   $$
   v_y(t) = \frac{dy(t)}{dt} = R \omega \cos(\omega t)
   $$

   Donc, les composantes de la vitesse sont :
   $$
   v_x(t) = R \omega (1 - \sin(\omega t))
   $$
   $$
   v_y(t) = R \omega \cos(\omega t)
   $$

3. **Composantes de l'accélération du point $$ P $$ en fonction du temps** :

   L'accélération est la dérivée des composantes de la vitesse par rapport au temps :
   $$
   a_x(t) = \frac{dv_x(t)}{dt} = -R \omega^2 \cos(\omega t)
   $$
   $$
   a_y(t) = \frac{dv_y(t)}{dt} = -R \omega^2 \sin(\omega t)
   $$

   Donc, les composantes de l'accélération sont :
   $$
   a_x(t) = -R \omega^2 \cos(\omega t)
   $$
   $$
   a_y(t) = -R \omega^2 \sin(\omega t)
   $$

4. **Coordonnées du point $$ P $$ et sa vitesse au temps $$ t = 1 \, \text{s} $$** :

   Utilisons les valeurs $$ R = 0.5 \, \text{m} $$ et $$ \omega = 2 \, \text{rad/s} $$.

   - Coordonnées :
     $$
     x(1) = R \omega \cdot 1 + R \cos(\omega \cdot 1) = 0.5 \times 2 \times 1 + 0.5 \cos(2) \approx 1 + 0.5 \times (-0.4161) \approx 1 - 0.2081 = 0.7919 \, \text{m}
     $$
     $$
     y(1) = R \sin(\omega \cdot 1) = 0.5 \sin(2) \approx 0.5 \times 0.9093 = 0.45465 \, \text{m}
     $$

   - Composantes de la vitesse :
     $$
     v_x(1) = R \omega (1 - \sin(\omega \cdot 1)) = 0.5 \times 2 \times (1 - \sin(2)) \approx 1 \times (1 - 0.9093) \approx 1 \times 0.0907 = 0.0907 \, \text{m/s}
     $$
     $$
     v_y(1) = R \omega \cos(\omega \cdot 1) = 0.5 \times 2 \times \cos(2) \approx 1 \times (-0.4161) = -0.4161 \, \text{m/s}
     $$

     La vitesse totale est :
     $$
     v(1) = \sqrt{v_x(1)^2 + v_y(1)^2} = \sqrt{(0.0907)^2 + (-0.4161)^2} = \sqrt{0.0082 + 0.1732} = \sqrt{0.1814} \approx 0.4257 \, \text{m/s}
     $$

## Questions d'analyse

1. Pourquoi la position du point $$ P $$ est-elle une combinaison du mouvement de rotation et du mouvement de translation ?
2. Expliquez pourquoi la composante horizontale de la vitesse dépend du sinus de l'angle de rotation.
3. Pourquoi l'accélération totale du point $$ P $$ est-elle constante ?
4. Comment la vitesse angulaire constante $$ \omega $$ influence-t-elle le mouvement du point $$ P $$ ?
5. Si la roue avait un rayon différent, comment cela affecterait-il les équations du mouvement ?

## Corrigé des questions d'analyse

1. La position du point $$ P $$ est une combinaison du mouvement de rotation et du mouvement de translation parce que le point $$ P $$ se déplace non seulement autour du centre de la roue, mais aussi avec la roue qui avance le long de l'axe $$ x $$.
2. La composante horizontale de la vitesse dépend du sinus de l'angle de rotation parce que le mouvement circulaire du point $$ P $$ autour du centre de la roue produit des variations périodiques dans les composantes horizontales et verticales de la vitesse.
3. L'accélération totale du point $$ P $$ est constante car elle est la somme vectorielle des accélérations centripète et tangentielle, qui sont déterminées par la vitesse angulaire constante $$ \omega $$.
4. La vitesse angulaire constante $$ \omega $$ influence le mouvement du point $$ P $$ en produisant une accélération centripète constante et en déterminant la fréquence des oscillations dans les composantes de la position et de la vitesse.
5. Si la roue avait un rayon différent, les amplitudes des oscillations dans les équations du mouvement changeraient proportionnellement au nouveau rayon, modifiant les valeurs des coordonnées, de la vitesse et de l'accélération.

