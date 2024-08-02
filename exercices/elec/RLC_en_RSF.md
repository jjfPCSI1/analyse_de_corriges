# Analyse énergétique d'un circuit RLC série

![](images/RLC_en_RSF.webp)

## Énoncé

On considère un circuit électrique série composé d'une résistance $$R$$, d'une inductance $$L$$, et d'une capacité $$C$$. Ce circuit est alimenté par une source de tension sinusoïdale de la forme $$u(t) = U_0 \cos(\omega t)$$.

1. **Équation différentielle** : Établissez l'équation différentielle régissant la tension $$u_C(t)$$ aux bornes du condensateur.
2. **Régime sinusoïdal forcé** : Trouvez l'expression de la tension $$u_C(t)$$ et du courant $$i(t)$$ dans le régime sinusoïdal forcé.
3. **Puissance moyenne** : Calculez la puissance moyenne dissipée par la résistance $$R$$.
4. **Facteur de puissance** : Déterminez le facteur de puissance du circuit en fonction des paramètres $$R$$, $$L$$, $$C$$, et $$\omega$$.
5. **Énergie totale** : Calculez l'énergie totale emmagasinée dans le circuit à un instant donné.

## Corrigé

1. **Équation différentielle :**

   Dans un circuit RLC série, la loi des mailles donne :

   $$ 
   u(t) = u_R(t) + u_L(t) + u_C(t) 
   $$

   où :

   - $$ u_R(t) = R i(t) $$ est la tension aux bornes de la résistance,
   - $$ u_L(t) = L \frac{di(t)}{dt} $$ est la tension aux bornes de l'inductance,
   - $$ u_C(t) = \frac{1}{C} \int i(t) \, dt $$ est la tension aux bornes du condensateur.

   En utilisant la relation entre le courant et la tension du condensateur, on a :

   $$
   i(t) = C \frac{du_C(t)}{dt}
   $$

   En substituant cette relation dans l'équation de la loi des mailles, nous obtenons :

   $$
   U_0 \cos(\omega t) = R C \frac{du_C(t)}{dt} + L C \frac{d^2u_C(t)}{dt^2} + u_C(t)
   $$

   L'équation différentielle s'écrit donc :

   $$
   L C \frac{d^2u_C(t)}{dt^2} + R C \frac{du_C(t)}{dt} + u_C(t) = U_0 \cos(\omega t)
   $$

2. **Régime sinusoïdal forcé :**

   En régime sinusoïdal forcé, on cherche une solution particulière de la forme $$ u_C(t) = V_0 \cos(\omega t + \varphi) $$.

   Le courant est alors :

   $$
   i(t) = C \frac{du_C(t)}{dt} = -\omega C V_0 \sin(\omega t + \varphi)
   $$

   En substituant $$ u_C(t) $$ dans l'équation différentielle, nous obtenons l'amplitude et la phase de la tension :

   $$
   V_0 = \frac{U_0}{\sqrt{\left(1 - L C \omega^2\right)^2 + (R C \omega)^2}}
   $$

   et l'angle de phase :

   $$
   \varphi = \arctan\left(\frac{R C \omega}{1 - L C \omega^2}\right)
   $$

3. **Puissance moyenne :**

   La puissance moyenne dissipée par la résistance $$R$$ est donnée par :

   $$
   P_{\text{moy}} = \frac{1}{T} \int_0^T R i(t)^2 \, dt
   $$

   En utilisant $$ i(t) = I_0 \cos(\omega t + \varphi) $$, où $$ I_0 = \omega C V_0 $$, la puissance moyenne s'exprime :

   $$
   P_{\text{moy}} = \frac{R I_0^2}{2} = \frac{R (\omega C V_0)^2}{2}
   $$

   En remplaçant $$ V_0 $$, on obtient :

   $$
   P_{\text{moy}} = \frac{R \omega^2 C^2 U_0^2}{2\left(\left(1 - L C \omega^2\right)^2 + (R C \omega)^2\right)}
   $$

4. **Facteur de puissance :**

   Le facteur de puissance $$\cos(\varphi)$$ est donné par :

   $$
   \cos(\varphi) = \frac{1}{\sqrt{1 + \left(\frac{R C \omega}{1 - L C \omega^2}\right)^2}}
   $$

5. **Énergie totale :**

   L'énergie totale emmagasinée dans le circuit est la somme des énergies stockées dans le condensateur et l'inductance :

   - Énergie dans le condensateur : $$ E_C = \frac{1}{2} C u_C(t)^2 $$
   - Énergie dans l'inductance : $$ E_L = \frac{1}{2} L i(t)^2 $$

   Ainsi, l'énergie totale est :

   $$
   E_{\text{totale}} = \frac{1}{2} C u_C(t)^2 + \frac{1}{2} L i(t)^2
   $$

## Questions d'analyse

1. **Méthode** : Pourquoi est-il préférable de chercher une solution particulière sous la forme $$u_C(t) = V_0 \cos(\omega t + \varphi)$$ en régime sinusoïdal forcé ?

2. **Bornes d'intégration** : Justifiez le choix des bornes d'intégration pour le calcul de la puissance moyenne.

3. **Unité et cohérence** : Vérifiez la cohérence dimensionnelle de l'expression de $$V_0$$.

4. **Recherche d'erreurs** : Dans l'expression de la puissance moyenne, quelle erreur commune doit-on éviter ?

5. **Analyse physique** : Que représente le facteur de puissance, et pourquoi est-il important pour l'efficacité énergétique du circuit ?

## Corrigé des questions d'analyse

1. **Méthode** : La recherche d'une solution particulière sous la forme $$u_C(t) = V_0 \cos(\omega t + \varphi)$$ est justifiée car le circuit est excité par une source de tension sinusoïdale. En régime forcé, la réponse du circuit suit la forme de l'excitation. Cela simplifie les calculs et permet de déterminer directement l'amplitude et la phase de la tension et du courant en régime permanent.

2. **Bornes d'intégration** : Les bornes d'intégration $$0$$ à $$T$$ sont choisies pour correspondre à une période complète du signal sinusoïdal, où $$T = \frac{2\pi}{\omega}$$. Cela permet de calculer la puissance moyenne sur une période entière, capturant ainsi toutes les variations temporelles du courant.

3. **Unité et cohérence** : L'expression de $$V_0$$ est :

   $$
   V_0 = \frac{U_0}{\sqrt{\left(1 - L C \omega^2\right)^2 + (R C \omega)^2}}
   $$

   La dimension de $$V_0$$ est celle d'une tension, soit $$\text{Volts}$$. L'unité de chaque terme dans le dénominateur est sans dimension (puisque chaque terme est de la forme \((1 - LC\omega^2)\) et \((RC\omega)\), qui sont tous les deux sans dimension), garantissant ainsi que $$V_0$$ a bien l'unité de tension.

4. **Recherche d'erreurs** : Une erreur fréquente dans le calcul de la puissance moyenne est d'oublier de diviser par $$T$$ lors de l'intégration sur une période. Cela peut conduire à une surestimation de la puissance dissipée. Il est essentiel de diviser l'intégrale par $$T$$ pour obtenir la moyenne correcte.

5. **Analyse physique** : Le facteur de puissance $$\cos(\varphi)$$ est une mesure de l'efficacité avec laquelle le circuit utilise la puissance électrique. Il représente le rapport entre la puissance réelle dissipée par le circuit et la puissance apparente fournie par la source. Un facteur de puissance proche de 1 indique que la majorité de la puissance fournie est utilisée pour un travail utile, minimisant les pertes énergétiques.
