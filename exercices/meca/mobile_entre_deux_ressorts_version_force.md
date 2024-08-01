# Mouvement d'un mobile sous l'action de deux ressorts identiques

## Énoncé

Un mobile autoporteur peut effectuer un mouvement de translation suivant un axe $$Ox$$ horizontal sous l'action de deux ressorts identiques, chacun ayant une constante de raideur $$k$$ et une longueur à vide $$\ell_0$$. Les ressorts sont fixés à des points fixes situés aux positions $$x = -L$$ et $$x = L$$ sur l'axe $$Ox$$. Le mobile est initialement à la position $$x = 0$$, où les ressorts sont à leur longueur à vide.

1. Établissez l'expression de la force exercée par chaque ressort sur le mobile lorsqu'il est à une position $$x$$.
2. Déduisez l'expression de la force résultante agissant sur le mobile.
3. En déduisant l'équation différentielle du mouvement du mobile, montrez que son mouvement est harmonique simple et déterminez la pulsation propre du système.
4. Calculez la période des oscillations.

## Corrigé

1. **Expression de la force exercée par chaque ressort** :

   Lorsque le mobile est à une position $$x$$, les longueurs des ressorts sont respectivement $$\ell_1 = \ell_0 + x + L$$ pour le ressort situé à $$x = -L$$ et $$\ell_2 = \ell_0 - x + L$$ pour le ressort situé à $$x = L$$.

   La force exercée par un ressort est donnée par la loi de Hooke :
   $$
   F = -k (\ell - \ell_0)
   $$

   - Force exercée par le ressort situé à $$x = -L$$ :
     $$
     F_1 = -k (\ell_1 - \ell_0) = -k (\ell_0 + x + L - \ell_0) = -k (x + L)
     $$

   - Force exercée par le ressort situé à $$x = L$$ :
     $$
     F_2 = -k (\ell_2 - \ell_0) = -k (\ell_0 - x + L - \ell_0) = -k (-x + L)
     $$

2. **Expression de la force résultante agissant sur le mobile** :

   La force résultante $$F_{\text{res}}$$ est la somme des forces exercées par les deux ressorts :
   $$
   F_{\text{res}} = F_1 + F_2
   $$

   En remplaçant les expressions de $$F_1$$ et $$F_2$$ :
   $$
   F_{\text{res}} = -k (x + L) + -k (-x + L)
   $$
   $$
   F_{\text{res}} = -k (x + L) - k (-x + L)
   $$
   $$
   F_{\text{res}} = -k x - k L - k (-x) + k L
   $$
   $$
   F_{\text{res}} = -k x + k x
   $$
   $$
   F_{\text{res}} = -2k x
   $$

3. **Équation différentielle du mouvement du mobile et pulsation propre** :

   En appliquant la deuxième loi de Newton, on obtient :
   $$
   m \ddot{x} = F_{\text{res}}
   $$
   $$
   m \ddot{x} = -2k x
   $$

   Ce qui se réécrit sous forme d'équation différentielle :
   $$
   \ddot{x} + \frac{2k}{m} x = 0
   $$

   Cette équation différentielle est celle d'un oscillateur harmonique simple avec une pulsation propre $$\omega_0$$ donnée par :
   $$
   \omega_0 = \sqrt{\frac{2k}{m}}
   $$

4. **Période des oscillations** :

   La période des oscillations $$T$$ est reliée à la pulsation propre $$\omega_0$$ par la relation :
   $$
   T = \frac{2\pi}{\omega_0}
   $$

   En remplaçant l'expression de $$\omega_0$$ :
   $$
   T = \frac{2\pi}{\sqrt{\frac{2k}{m}}}
   $$
   $$
   T = 2\pi \sqrt{\frac{m}{2k}}
   $$

## Questions d'analyse

1. Pourquoi la force résultante exercée sur le mobile est-elle proportionnelle à son déplacement $$x$$ ?
2. Expliquez comment la position initiale du mobile influence le mouvement harmonique simple.
3. Si la constante de raideur des ressorts doublait, comment cela affecterait-il la pulsation propre et la période des oscillations ?
4. Si la masse du mobile était quadruplée, comment cela affecterait-il la pulsation propre et la période des oscillations ?
5. Quel est l'effet des longueurs initiales des ressorts sur la force résultante et le mouvement du mobile ?

## Corrigé des questions d'analyse

1. La force résultante est proportionnelle au déplacement $$x$$ car les deux ressorts exercent des forces proportionnelles à leur allongement ou compression, selon la loi de Hooke, et ces forces sont opposées au déplacement.
2. La position initiale du mobile détermine son énergie potentielle initiale et influence la phase du mouvement harmonique simple, mais la fréquence reste inchangée.
3. Si la constante de raideur des ressorts doublait, la pulsation propre $$\omega_0$$ augmenterait d'un facteur $$\sqrt{2}$$, et la période des oscillations $$T$$ serait divisée par $$\sqrt{2}$$.
4. Si la masse du mobile était quadruplée, la pulsation propre $$\omega_0$$ serait divisée par 2, et la période des oscillations $$T$$ doublerait.
5. Les longueurs initiales des ressorts influencent la force résultante lorsqu'ils ne sont pas à leur longueur à vide, mais dans ce problème, à la position initiale $$x = 0$$, les ressorts sont à leur longueur à vide, donc ils n'exercent aucune force initiale sur le mobile.

