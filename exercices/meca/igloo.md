# Calcul de l'angle de décollage d'un Inuit sur un igloo hémisphérique

![](images/igloo.webp)

## Énoncé

Un Inuit est assis au sommet de son igloo, supposé être une demi-sphère de rayon $$ R $$. À un certain angle $$ \theta $$ par rapport à la verticale, il commence à glisser sans frottements le long de la surface de l'igloo. Déterminez l'angle $$ \theta_d $$ (par rapport à la verticale) auquel il décolle de la surface de l'igloo.

1. Établissez les équations du mouvement de l'Inuit dans un repère polaire en considérant les projections des forces.
2. Exprimez la force normale $$ N $$ agissant sur l'Inuit en fonction de l'angle $$ \theta $$.
3. Déterminez l'angle $$ \theta_d $$ auquel la force normale devient nulle.

## Corrigé

1. **Équations du mouvement dans un repère polaire** :

   Dans un repère polaire, nous définissons la position de l'Inuit par son rayon $$ r(t) $$ et son angle $$ \theta(t) $$. Ici, $$ r(t) = R $$ est constant, car l'Inuit reste à la surface de l'igloo.

   Les accélérations radiale et orthoradiale sont données par :
   
   - Accélération radiale (projetée le long du rayon) :
     $$
     a_r = \ddot{r} - r\dot{\theta}^2
     $$

   - Accélération orthoradiale (projetée perpendiculairement au rayon) :
     $$
     a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}
     $$

   Puisque $$ r(t) = R $$ est constant, alors $$ \dot{r} = \ddot{r} = 0 $$, ce qui simplifie les équations :
   
   - Accélération radiale :
     $$
     a_r = -R\dot{\theta}^2
     $$

   - Accélération orthoradiale :
     $$
     a_\theta = R\ddot{\theta}
     $$

   Les forces agissant sur l'Inuit sont son poids $$ \vec{P} = mg\vec{e}_r $$ (dirigé vers le bas) et la force normale $$ \vec{N} $$ (perpendiculaire à la surface de l'igloo).

   - La composante radiale de la force est :
     $$
     F_r = N - mg \cos(\theta)
     $$
     En utilisant la deuxième loi de Newton dans la direction radiale, nous avons :
     $$
     N - mg \cos(\theta) = m(-R\dot{\theta}^2)
     $$

   - La composante orthoradiale de la force est :
     $$
     F_\theta = mg \sin(\theta)
     $$
     En utilisant la deuxième loi de Newton dans la direction orthoradiale, nous avons :
     $$
     mg \sin(\theta) = mR\ddot{\theta}
     $$

2. **Expression de la force normale $$ N $$** :

   À partir de l'équation radiale, on isole $$ N $$ :
   $$
   N = mg \cos(\theta) - mR\dot{\theta}^2
   $$

   Pour déterminer l'expression de $$ \dot{\theta} $$, utilisons l'équation orthoradiale :
   $$
   \ddot{\theta} = \frac{g}{R} \sin(\theta)
   $$

   Multiplions chaque côté par $$ \dot{\theta} $$ pour faciliter l'intégration :
   $$
   \dot{\theta} \ddot{\theta} = \frac{g}{R} \sin(\theta) \dot{\theta}
   $$

   Cela devient :
   $$
   \frac{1}{2} \frac{d}{dt}(\dot{\theta}^2) = \frac{g}{R} \sin(\theta) \dot{\theta}
   $$

   En intégrant par rapport au temps $$ t $$ et en supposant que $$ \dot{\theta} = 0 $$ à $$ \theta = 0 $$, nous obtenons :
   $$
   \frac{1}{2} \dot{\theta}^2 = -\frac{g}{R} \cos(\theta) + C
   $$

   Avec la condition initiale $$ \theta = 0 $$ et $$ \dot{\theta} = 0 $$, nous avons $$ C = \frac{g}{R} $$.

   Ainsi, l'équation devient :
   $$
   \frac{1}{2} \dot{\theta}^2 = \frac{g}{R} (1 - \cos(\theta))
   $$

   En isolant $$ \dot{\theta} $$, nous obtenons :
   $$
   \dot{\theta} = \sqrt{\frac{2g}{R} (1 - \cos(\theta))}
   $$

3. **Angle de décollage $$ \theta_d $$** :

   L'Inuit décolle lorsque la force normale $$ N $$ devient nulle :
   $$
   mg \cos(\theta_d) - mR\dot{\theta}^2 = 0
   $$

   En substituant l'expression de $$ \dot{\theta} $$ dans l'équation pour $$ N $$ :
   $$
   mg \cos(\theta_d) = mR\left(\frac{2g}{R}(1 - \cos(\theta_d))\right)
   $$

   Simplifions :
   $$
   g \cos(\theta_d) = 2g(1 - \cos(\theta_d))
   $$
   $$
   \cos(\theta_d) = 2 - 2\cos(\theta_d)
   $$
   $$
   3\cos(\theta_d) = 2
   $$
   $$
   \cos(\theta_d) = \frac{2}{3}
   $$

   En calculant l'angle :
   $$
   \theta_d = \cos^{-1}\left(\frac{2}{3}\right) \approx 48.19^\circ
   $$

   Ainsi, l'Inuit décolle de l'igloo à un angle d'environ $$ 48.19^\circ $$ par rapport à la verticale.

## Questions d'analyse

1. Pourquoi le rayon $$ r $$ est-il constant dans cet exercice ?
2. Expliquez pourquoi l'Inuit décolle lorsque la force normale devient nulle.
3. Comment la composante orthoradiale de l'accélération dépend-elle de l'angle $$ \theta $$ ?
4. Si le rayon de l'igloo augmentait, cela changerait-il l'angle de décollage ?
5. Si la gravité $$ g $$ augmentait, comment cela affecterait-il l'angle de décollage ?

## Corrigé des questions d'analyse

1. Le rayon $$ r $$ est constant parce que l'Inuit reste à la surface de l'igloo qui est une demi-sphère de rayon fixe $$ R $$. Il ne se rapproche ni ne s'éloigne du centre de l'igloo.
2. L'Inuit décolle lorsque la force normale devient nulle car cela indique qu'il n'y a plus de contact entre lui et la surface de l'igloo, et la seule force agissant est son poids.
3. La composante orthoradiale de l'accélération dépend de l'angle $$ \theta $$ par la relation $$ \ddot{\theta} = \frac{g}{R} \sin(\theta) $$, montrant que l'accélération augmente avec l'augmentation de l'angle.
4. Si le rayon de l'igloo augmentait, cela n'affecterait pas l'angle de décollage puisque l'angle dépend uniquement du rapport des forces gravitationnelles et géométriques, pas de la taille absolue de l'igloo.
5. Si la gravité $$ g $$ augmentait, cela n'affecterait pas l'angle de décollage car l'équation pour $$ \theta_d $$ est indépendante de $$ g $$, bien que la vitesse de décollage serait plus élevée avec une gravité plus forte.

