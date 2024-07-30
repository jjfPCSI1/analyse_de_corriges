# Mouvement circulaire uniformément accéléré dans la base polaire

![](images/mouvement_circulaire_uniformement_accelere.webp)

## Énoncé

Considérez une particule de masse $$m$$ se déplaçant sur une trajectoire circulaire de rayon $$R = 2 \, \text{m}$$. La particule commence à partir du repos et subit une accélération angulaire constante $$\alpha = 0.5 \, \text{rad/s}^2$$.

1. Exprimez les coordonnées radiale et angulaire de la position de la particule en fonction du temps dans la base polaire.
2. Déterminez les composantes radiale et angulaire de la vitesse de la particule en fonction du temps.
3. Calculez les composantes radiale et angulaire de l'accélération de la particule.
4. Trouvez la vitesse et l'accélération de la particule à $$t = 4 \, \text{s}$$.

## Corrigé

1. **Coordonnées radiale et angulaire de la position** :

   En base polaire, la position d'une particule se déplaçant sur une trajectoire circulaire est donnée par :
   $$
   \vec{r}(t) = R \vec{e}_r
   $$

   La coordonnée angulaire $$\theta(t)$$ est déterminée par l'accélération angulaire constante $$\alpha$$ :
   $$
   \theta(t) = \frac{1}{2} \alpha t^2
   $$

   En remplaçant les valeurs données :
   $$
   \theta(t) = \frac{1}{2} \times 0.5 \, \text{rad/s}^2 \times t^2 = 0.25 \, \text{rad/s}^2 \times t^2
   $$

   Donc, les coordonnées de la position en base polaire sont :
   $$
   \vec{r}(t) = R \vec{e}_r \quad \text{et} \quad \theta(t) = 0.25 t^2
   $$

2. **Composantes radiale et angulaire de la vitesse** :

   La composante radiale de la vitesse $$v_r(t)$$ est nulle car le rayon est constant :
   $$
   v_r(t) = \frac{dR}{dt} = 0
   $$

   La composante angulaire de la vitesse $$v_\theta(t)$$ est donnée par :
   $$
   v_\theta(t) = R \frac{d\theta(t)}{dt} = R \alpha t
   $$

   En remplaçant les valeurs données :
   $$
   v_\theta(t) = 2 \, \text{m} \times 0.5 \, \text{rad/s}^2 \times t = t \, \text{m/s}
   $$

   Donc, les composantes de la vitesse sont :
   $$
   v_r(t) = 0 \quad \text{et} \quad v_\theta(t) = t \, \text{m/s}
   $$

3. **Composantes radiale et angulaire de l'accélération** :

   La composante radiale de l'accélération $$a_r(t)$$ est donnée par l'accélération centripète :
   $$
   a_r(t) = -R \left(\frac{d\theta(t)}{dt}\right)^2 = -R (\alpha t)^2
   $$

   En remplaçant les valeurs données :
   $$
   a_r(t) = -2 \, \text{m} \times (0.5 \, \text{rad/s}^2 \times t)^2 = -0.5 t^2 \, \text{m/s}^2
   $$

   La composante angulaire de l'accélération $$a_\theta(t)$$ est donnée par :
   $$
   a_\theta(t) = R \frac{d^2\theta(t)}{dt^2} = R \alpha
   $$

   En remplaçant les valeurs données :
   $$
   a_\theta(t) = 2 \, \text{m} \times 0.5 \, \text{rad/s}^2 = 1 \, \text{m/s}^2
   $$

   Donc, les composantes de l'accélération sont :
   $$
   a_r(t) = -0.5 t^2 \, \text{m/s}^2 \quad \text{et} \quad a_\theta(t) = 1 \, \text{m/s}^2
   $$

4. **Vitesse et accélération à $$t = 4 \, \text{s}$$** :

   - Vitesse :
     $$
     v_r(4) = 0 \quad \text{et} \quad v_\theta(4) = 4 \, \text{m/s}
     $$

     La vitesse totale est :
     $$
     v = \sqrt{v_r^2 + v_\theta^2} = \sqrt{0 + 4^2} = 4 \, \text{m/s}
     $$

   - Accélération :
     $$
     a_r(4) = -0.5 \times 4^2 = -0.5 \times 16 = -8 \, \text{m/s}^2
     $$

     $$
     a_\theta(4) = 1 \, \text{m/s}^2
     $$

     L'accélération totale est :
     $$
     a = \sqrt{a_r^2 + a_\theta^2} = \sqrt{(-8)^2 + 1^2} = \sqrt{64 + 1} = \sqrt{65} \approx 8.06 \, \text{m/s}^2
     $$

## Questions d'analyse

1. Pourquoi la composante radiale de la vitesse est-elle nulle dans ce cas ?
2. Expliquez le rôle de l'accélération angulaire constante dans le mouvement circulaire uniformément accéléré.
3. Comment la composante radiale de l'accélération dépend-elle du temps ? Pourquoi ?
4. Comparez la direction des composantes radiale et angulaire de l'accélération.
5. Si la particule commençait avec une vitesse angulaire initiale non nulle, comment cela affecterait-il les équations de mouvement ?

## Corrigé des questions d'analyse

1. La composante radiale de la vitesse est nulle car le rayon de la trajectoire circulaire est constant. La particule ne s'éloigne ni ne se rapproche du centre du cercle.
2. L'accélération angulaire constante produit une variation linéaire de la vitesse angulaire avec le temps, ce qui entraîne une augmentation uniforme de la vitesse tangente le long de la trajectoire circulaire.
3. La composante radiale de l'accélération dépend du temps de manière quadratique car elle est proportionnelle au carré de la vitesse angulaire, qui augmente linéairement avec le temps.
4. La composante radiale de l'accélération est dirigée vers le centre du cercle (centripète), tandis que la composante angulaire de l'accélération est tangente à la trajectoire, perpendiculaire à la composante radiale.
5. Si la particule commençait avec une vitesse angulaire initiale non nulle, les équations de mouvement devraient inclure cette vitesse initiale. La position angulaire serait donnée par $$ \theta(t) = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2 $$, où $$ \omega_0 $$ est la vitesse angulaire initiale.

