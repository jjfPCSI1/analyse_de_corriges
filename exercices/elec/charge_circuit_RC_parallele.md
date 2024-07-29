# Charge d'un condensateur dans un circuit RC

## Énoncé

1. On considère un circuit composé d'un générateur idéal de force électromotrice \(E\), d'une résistance interne \(r\), d'une résistance \(R\) en parallèle avec un condensateur de capacité \(C\). Le condensateur est initialement déchargé. Établir l'équation différentielle régissant la charge \(q(t)\) du condensateur.
2. Résoudre cette équation différentielle pour obtenir l'expression de \(q(t)\).
3. Déterminer la constante de temps \(\tau\) du circuit.
4. Calculer la charge maximale \(q_{\text{max}}\) que peut atteindre le condensateur.
5. Déterminer l'expression de la tension aux bornes du condensateur en fonction du temps \(V_C(t)\).

## Corrigé

1. **Établissement de l'équation différentielle** :

    - En appliquant la loi des mailles, nous avons : \( E - i(r+R) - \frac{q}{C} = 0 \), où \( i = \frac{dq}{dt} \).
    - En réarrangeant, nous obtenons : \( E = r \frac{dq}{dt} + R \frac{dq}{dt} + \frac{q}{C} \).
    - Simplifions : \( E = (r + R) \frac{dq}{dt} + \frac{q}{C} \).
    - L'équation différentielle est donc : \( E = (r + R) \frac{dq}{dt} + \frac{q}{C} \).

2. **Résolution de l'équation différentielle** :

    - La solution de cette équation différentielle linéaire du premier ordre est de la forme : \( q(t) = q_{\text{max}} (1 - e^{-\frac{t}{\tau}}) \).
    - Pour déterminer \( q_{\text{max}} \) et \(\tau\), utilisons les conditions initiales et la forme de l'équation :
        - \( q_{\text{max}} = EC \).
        - \( \tau = C (r + R) \).

3. **Constante de temps \(\tau\)** :

    - La constante de temps du circuit est \( \tau = C (r + R) \).

4. **Charge maximale \( q_{\text{max}} \)** :

    - La charge maximale que peut atteindre le condensateur est \( q_{\text{max}} = EC \).

5. **Tension aux bornes du condensateur \( V_C(t) \)** :

    - La tension aux bornes du condensateur est \( V_C(t) = \frac{q(t)}{C} \).
    - En utilisant l'expression de \( q(t) \) : \( V_C(t) = E (1 - e^{-\frac{t}{\tau}}) \).

## Questions d'analyse

1. Pourquoi utilise-t-on la loi des mailles pour établir l'équation différentielle ?
2. Quelles sont les implications physiques de la constante de temps \(\tau\) dans le circuit RC ?
3. Pourquoi la charge maximale \( q_{\text{max}} \) du condensateur est-elle égale à \( EC \) ?
4. Comment se comportent la charge \( q(t) \) et la tension \( V_C(t) \) aux bornes du condensateur pour \( t \rightarrow \infty \) ?
5. En quoi l'équation \( E = (r + R) \frac{dq}{dt} + \frac{q}{C} \) reflète-t-elle la nature transitoire de la charge d'un condensateur ?

## Corrigé des questions d'analyse

1. **Utilisation de la loi des mailles** :
    - La loi des mailles permet de relier les tensions dans le circuit en appliquant le principe de conservation de l'énergie. Elle est essentielle pour établir une relation entre les différentes composantes du circuit (résistances, condensateur, générateur).

2. **Implications physiques de \(\tau\)** :
    - La constante de temps \(\tau = C (r + R)\) représente le temps caractéristique du circuit pour atteindre environ 63% de la charge maximale. Elle décrit la vitesse à laquelle le condensateur se charge ou se décharge.

3. **Charge maximale \( q_{\text{max}} \)** :
    - \( q_{\text{max}} = EC \) découle de la relation \( q = CV \) lorsque la tension aux bornes du condensateur atteint la force électromotrice \(E\). Cela se produit quand le condensateur est complètement chargé.

4. **Comportement pour \( t \rightarrow \infty \)** :
    - Pour \( t \rightarrow \infty \), \( q(t) \rightarrow q_{\text{max}} = EC \) et \( V_C(t) \rightarrow E \). Le condensateur atteint sa charge maximale et la tension à ses bornes devient égale à la force électromotrice du générateur.

5. **Nature transitoire de l'équation** :
    - L'équation \( E = (r + R) \frac{dq}{dt} + \frac{q}{C} \) montre que la charge du condensateur varie dans le temps jusqu'à ce qu'elle atteigne un état stable. Les termes en \( \frac{dq}{dt} \) et \( \frac{q}{C} \) représentent respectivement les contributions transitoires et permanentes de la charge.
