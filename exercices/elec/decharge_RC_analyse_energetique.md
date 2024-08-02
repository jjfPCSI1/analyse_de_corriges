# Analyse énergétique d'un circuit RC série avec un condensateur déjà chargé

![](images/decharge_RC_analyse_energetique.webp)

## Énoncé

Considérez un circuit en série composé d'un condensateur de capacité $$C$$ initialement chargé à une tension $$V_0$$ et d'une résistance $$R$$. À l'instant $$t = 0$$, on ferme l'interrupteur du circuit pour permettre au condensateur de se décharger à travers la résistance. 

1. Établissez l'équation différentielle qui régit la tension aux bornes du condensateur en fonction du temps.
2. Calculez l'énergie initialement stockée dans le condensateur.
3. Déterminez l'énergie dissipée par la résistance au cours du temps.
4. Montrez que la somme de l'énergie dissipée par la résistance et de l'énergie restante dans le condensateur est constante au cours du temps.

## Corrigé

1. **Équation différentielle de la tension aux bornes du condensateur** :

   La loi des mailles pour le circuit RC série donne :
   $$
   V(t) = V_R(t) + V_C(t)
   $$

   Où :
   - $$ V_C(t) $$ est la tension aux bornes du condensateur.
   - $$ V_R(t) = i(t)R $$ est la tension aux bornes de la résistance.

   Le courant $$ i(t) $$ est lié à la charge $$ q(t) $$ du condensateur par :
   $$
   i(t) = -\frac{dq}{dt}
   $$

   De plus, $$ q(t) = C V_C(t) $$, donc :
   $$
   i(t) = -C \frac{dV_C}{dt}
   $$

   En substituant $$ i(t) $$ dans l'équation de la maille, on obtient :
   $$
   V_C(t) = -RC \frac{dV_C}{dt} + V_C(t)
   $$

   Simplifions :
   $$
   RC \frac{dV_C}{dt} + V_C(t) = 0
   $$

   Cette équation différentielle a pour solution :
   $$
   V_C(t) = V_0 e^{-\frac{t}{RC}}
   $$

   où $$ V_0 $$ est la tension initiale à $$ t = 0 $$.

2. **Énergie initialement stockée dans le condensateur** :

   L'énergie initiale $$ E_0 $$ stockée dans le condensateur est donnée par :
   $$
   E_0 = \frac{1}{2} C V_0^2
   $$

3. **Énergie dissipée par la résistance au cours du temps** :

   L'énergie dissipée par la résistance, $$ E_R(t) $$, au cours du temps est obtenue en intégrant la puissance dissipée $$ P_R(t) = i^2(t)R $$ :

   La puissance dissipée par la résistance est :
   $$
   P_R(t) = i^2(t) R = \left(-C \frac{dV_C}{dt}\right)^2 R
   $$

   En remplaçant $$ V_C(t) $$ par son expression :
   $$
   P_R(t) = \left(C \frac{d}{dt}\left(V_0 e^{-\frac{t}{RC}}\right)\right)^2 R
   $$
   $$
   P_R(t) = \left(C \cdot -\frac{V_0}{RC} e^{-\frac{t}{RC}}\right)^2 R
   $$
   $$
   P_R(t) = \left(\frac{CV_0}{RC} e^{-\frac{t}{RC}}\right)^2 R
   $$
   $$
   P_R(t) = \frac{C^2 V_0^2}{R^2C^2} e^{-\frac{2t}{RC}} R
   $$
   $$
   P_R(t) = \frac{V_0^2}{R} e^{-\frac{2t}{RC}}
   $$

   L'énergie dissipée par la résistance est donc l'intégrale de cette puissance par rapport au temps, de 0 à $$ t $$ :

   $$
   E_R(t) = \int_0^t P_R(t') \, dt' = \int_0^t \frac{V_0^2}{R} e^{-\frac{2t'}{RC}} \, dt'
   $$

   Cette intégrale est résolue par :
   $$
   E_R(t) = \frac{V_0^2}{R} \int_0^t e^{-\frac{2t'}{RC}} \, dt'
   $$
   $$
   E_R(t) = \frac{V_0^2}{R} \left[-\frac{RC}{2} e^{-\frac{2t'}{RC}}\right]_0^t
   $$
   $$
   E_R(t) = \frac{V_0^2 RC}{2R} \left(1 - e^{-\frac{2t}{RC}}\right)
   $$
   $$
   E_R(t) = \frac{1}{2} C V_0^2 \left(1 - e^{-\frac{2t}{RC}}\right)
   $$

4. **Vérification de la conservation de l'énergie totale** :

   L'énergie restante dans le condensateur au temps $$ t $$, $$ E_C(t) $$, est donnée par :
   $$
   E_C(t) = \frac{1}{2} C V_C(t)^2 = \frac{1}{2} C \left(V_0 e^{-\frac{t}{RC}}\right)^2
   $$
   $$
   E_C(t) = \frac{1}{2} C V_0^2 e^{-\frac{2t}{RC}}
   $$

   La somme de l'énergie dissipée et de l'énergie restante dans le condensateur doit être égale à l'énergie initiale $$ E_0 $$ :
   $$
   E_R(t) + E_C(t) = \frac{1}{2} C V_0^2 \left(1 - e^{-\frac{2t}{RC}}\right) + \frac{1}{2} C V_0^2 e^{-\frac{2t}{RC}}
   $$
   $$
   E_R(t) + E_C(t) = \frac{1}{2} C V_0^2 \left(1 - e^{-\frac{2t}{RC}} + e^{-\frac{2t}{RC}}\right)
   $$
   $$
   E_R(t) + E_C(t) = \frac{1}{2} C V_0^2
   $$

   Ainsi, l'énergie totale est constante et égale à l'énergie initiale $$ E_0 $$, ce qui montre que l'énergie est conservée dans le système.

## Questions d'analyse

1. Pourquoi l'énergie mécanique totale du circuit est-elle conservée, même si une partie de l'énergie est dissipée sous forme de chaleur ?
2. Quel rôle joue la constante de temps $$ \tau = RC $$ dans l'évolution temporelle de l'énergie dans le circuit ?
3. Si la capacité du condensateur était doublée, comment cela affecterait-il la dissipation d'énergie par la résistance et l'énergie restante dans le condensateur ?
4. Comment la résistance $$ R $$ influence-t-elle la vitesse de décharge du condensateur ?
5. Que se passe-t-il pour l'énergie dissipée par la résistance si la résistance tend vers zéro ?

## Corrigé des questions d'analyse

1. L'énergie mécanique totale du circuit est conservée car toute l'énergie initialement stockée dans le condensateur est soit dissipée par la résistance sous forme de chaleur, soit reste stockée dans le condensateur. La dissipation ne crée pas de perte d'énergie du point de vue du système complet, seulement une conversion en une autre forme.
2. La constante de temps $$ \tau = RC $$ détermine le taux de décharge du condensateur et de dissipation de l'énergie dans la résistance. Plus la constante de temps est grande, plus la décharge est lente.
3. Si la capacité du condensateur est doublée, l'énergie initiale $$ E_0 $$ est également doublée. L'énergie dissipée par la résistance au cours du temps sera donc plus importante, tout comme l'énergie restante dans le condensateur.
4. La résistance $$ R $$ détermine la vitesse de décharge du condensateur. Une plus grande résistance ralentit la décharge, augmentant ainsi la constante de temps et ralentissant la dissipation de l'énergie.
5. Si la résistance tend vers zéro, la dissipation d'énergie par la résistance se fait extrêmement rapidement, et toute l'énergie est instantanément convertie en chaleur. Cela conduit à une décharge instantanée du condensateur.

