# Charge d'un condensateur dans un circuit RC

## Énoncé

1. On considère un circuit composé d'un générateur idéal de force électromotrice $$E$$, d'une résistance interne $$r$$, et d'un ensemble parallèle comprenant une résistance $$R$$ et un condensateur de capacité $$C$$. Le condensateur est initialement déchargé. Établir l'équation différentielle régissant la charge $$q(t)$$ du condensateur.
2. Résoudre cette équation différentielle pour obtenir l'expression de $$q(t)$$.
3. Déterminer la constante de temps $$\tau$$ du circuit.
4. Calculer la charge maximale $$q_{\text{max}}$$ que peut atteindre le condensateur.
5. Déterminer l'expression de la tension aux bornes du condensateur en fonction du temps $$V_C(t)$$.

## Corrigé

1. **Établissement de l'équation différentielle** :

    - La tension aux bornes du condensateur et de la résistance en parallèle est la même : $$ V_C(t) = V_R(t) $$.
    - La loi des mailles donne : $$ E - i_r r - V_C = 0 $$, où $$ i_r $$ est le courant à travers la résistance interne $$ r $$.
    - Le courant $$ i $$ fourni par le générateur se divise en deux courants : $$ i = i_R + i_C $$.
    - Utilisant la loi d'Ohm pour la résistance $$ R $$ : $$ V_R = i_R R $$.
    - Pour le condensateur, $$ i_C = \frac{dq}{dt} $$ et $$ V_C = \frac{q}{C} $$.
    - La loi des mailles devient : $$ E - r(i_R + \frac{dq}{dt}) - V_C = 0 $$.
    - Remplaçons $$ i_R $$ par $$ \frac{V_C}{R} $$ et $$ V_C $$ par $$ \frac{q}{C} $$ : $$ E - r(\frac{q}{RC} + \frac{dq}{dt}) - \frac{q}{C} = 0 $$.
    - Réarrangeons pour obtenir l'équation différentielle : $$ \frac{dq}{dt} + \left(\frac{1}{R} + \frac{1}{r}\right)\frac{q}{C} = \frac{E}{r} $$.

2. **Résolution de l'équation différentielle** :

    - L'équation différentielle est de la forme $$ \frac{dq}{dt} + \frac{1}{\tau} q = \frac{E}{r} $$, où $$ \tau = \frac{C r R}{r + R} $$.
    - La solution générale de cette équation est : $$ q(t) = q_{\text{max}} (1 - e^{-\frac{t}{\tau}}) $$.
    - La charge maximale $$ q_{\text{max}} = \frac{ECr}{r + R} $$.

3. **Constante de temps $$\tau$$** :

    - La constante de temps du circuit est $$ \tau = \frac{C r R}{r + R} $$.

4. **Charge maximale $$ q_{\text{max}} $$** :

    - La charge maximale que peut atteindre le condensateur est $$ q_{\text{max}} = \frac{ECr}{r + R} $$.

5. **Tension aux bornes du condensateur $$ V_C(t) $$** :

    - La tension aux bornes du condensateur est $$ V_C(t) = \frac{q(t)}{C} $$.
    - En utilisant l'expression de $$ q(t) $$ : $$ V_C(t) = \frac{E r}{r + R} (1 - e^{-\frac{t}{\tau}}) $$.

## Questions d'analyse

1. Pourquoi est-il nécessaire d'utiliser la loi des mailles pour établir l'équation différentielle ?
2. Quelles sont les implications physiques de la constante de temps $$\tau$$ dans le circuit RC en parallèle ?
3. Pourquoi la charge maximale $$ q_{\text{max}} $$ du condensateur est-elle égale à $$ \frac{ECr}{r + R} $$ ?
4. Comment se comportent la charge $$ q(t) $$ et la tension $$ V_C(t) $$ aux bornes du condensateur pour $$ t \rightarrow \infty $$ ?
5. En quoi l'équation $$ \frac{dq}{dt} + \left(\frac{1}{R} + \frac{1}{r}\right)\frac{q}{C} = \frac{E}{r} $$ reflète-t-elle la nature transitoire de la charge d'un condensateur ?

## Corrigé des questions d'analyse

1. **Utilisation de la loi des mailles** :
    - La loi des mailles permet de relier les tensions dans le circuit en appliquant le principe de conservation de l'énergie. Elle est essentielle pour établir une relation entre les différentes composantes du circuit (résistances, condensateur, générateur).

2. **Implications physiques de $$\tau$$** :
    - La constante de temps $$\tau = \frac{C r R}{r + R}$$ représente le temps caractéristique du circuit pour atteindre environ 63% de la charge maximale. Elle décrit la vitesse à laquelle le condensateur se charge ou se décharge dans un circuit RC en parallèle.

3. **Charge maximale $$ q_{\text{max}} $$** :
    - $$ q_{\text{max}} = \frac{ECr}{r + R} $$ découle de la relation $$ q = CV $$ lorsque la tension aux bornes du condensateur atteint la tension de la source ajustée par les résistances du circuit. Cela se produit quand le condensateur est complètement chargé.

4. **Comportement pour $$ t \rightarrow \infty $$** :
    - Pour $$ t \rightarrow \infty $$, $$ q(t) \rightarrow q_{\text{max}} = \frac{ECr}{r + R} $$ et $$ V_C(t) \rightarrow \frac{E r}{r + R} $$. Le condensateur atteint sa charge maximale et la tension à ses bornes devient constante.

5. **Nature transitoire de l'équation** :
    - L'équation $$ \frac{dq}{dt} + \left(\frac{1}{R} + \frac{1}{r}\right)\frac{q}{C} = \frac{E}{r} $$ montre que la charge du condensateur varie dans le temps jusqu'à ce qu'elle atteigne un état stable. Les termes en $$ \frac{dq}{dt} $$ et $$ \frac{q}{C} $$ représentent respectivement les contributions transitoires et permanentes de la charge.
