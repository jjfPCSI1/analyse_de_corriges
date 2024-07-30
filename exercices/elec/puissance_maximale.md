# Calcul de la puissance reçue par une résistance dans un circuit en série

![](elec/images/puissance_maximale.webp)

## Énoncé

Considérez un circuit électrique composé d'un générateur de tension $$E$$, et de deux résistances $$r$$ et $$R$$ en série. Le but est de calculer la puissance reçue par $$R$$ et de montrer qu'elle est maximale lorsque $$r = R$$. Les valeurs des composants sont :
- $$E = 12 \, V$$
- $$r = 5 \, \Omega$$
- $$R = 10 \, \Omega$$

1. Calculez le courant $$I$$ dans le circuit.
2. Déterminez la puissance $$P_R$$ reçue par la résistance $$R$$.
3. Montrez que la puissance reçue par $$R$$ est maximale lorsque $$r = R$$.

## Corrigé

1. **Calcul du courant dans le circuit** :
   La résistance totale du circuit est la somme des résistances en série :
   $$
   R_{\text{total}} = r + R
   $$

   Le courant $$I$$ dans le circuit est donné par la loi d'Ohm :
   $$
   I = \frac{E}{R_{\text{total}}} = \frac{E}{r + R}
   $$

   En remplaçant les valeurs données :
   $$
   I = \frac{12 \, V}{5 \, \Omega + 10 \, \Omega} = \frac{12 \, V}{15 \, \Omega} = 0.8 \, A
   $$

2. **Calcul de la puissance reçue par $$R$$** :
   La puissance reçue par la résistance $$R$$ est donnée par :
   $$
   P_R = I^2 R
   $$

   En remplaçant les valeurs calculées :
   $$
   P_R = (0.8 \, A)^2 \times 10 \, \Omega = 0.64 \, A^2 \times 10 \, \Omega = 6.4 \, W
   $$

3. **Démonstration que la puissance reçue par $$R$$ est maximale lorsque $$r = R$$** :
   La puissance reçue par $$R$$ peut être exprimée en fonction de $$r$$ et $$R$$ :
   $$
   P_R = I^2 R = \left( \frac{E}{r + R} \right)^2 R
   $$

   Pour trouver le maximum de $$P_R$$, nous devons prendre la dérivée de $$P_R$$ par rapport à $$R$$ et l'égaliser à zéro :
   $$
   P_R = \frac{E^2 R}{(r + R)^2}
   $$

   Dérivons $$P_R$$ par rapport à $$R$$ :
   $$
   \frac{\mathrm{d}P_R}{\mathrm{d}R} = \frac{E^2 (r + R)^2 \cdot 1 - E^2 R \cdot 2 (r + R)}{(r + R)^4}
   $$
   $$
   \frac{\mathrm{d}P_R}{\mathrm{d}R} = \frac{E^2 (r + R)^2 - 2E^2 R (r + R)}{(r + R)^3}
   $$
   $$
   \frac{\mathrm{d}P_R}{\mathrm{d}R} = \frac{E^2 (r + R - 2R)}{(r + R)^3}
   $$
   $$
   \frac{\mathrm{d}P_R}{\mathrm{d}R} = \frac{E^2 (r - R)}{(r + R)^3}
   $$

   Pour trouver le maximum, on met la dérivée égale à zéro :
   $$
   \frac{E^2 (r - R)}{(r + R)^3} = 0
   $$

   Cela implique :
   $$
   r - R = 0
   $$
   Donc,
   $$
   r = R
   $$

   Pour vérifier que c'est bien un maximum, nous pouvons vérifier la dérivée seconde :
   $$
   \frac{\mathrm{d}^2P_R}{\mathrm{d}R^2} = \frac{\mathrm{d}}{\mathrm{d}R} \left( \frac{E^2 (r - R)}{(r + R)^3} \right)
   $$
   Sans faire tout le calcul ici, il peut être montré que la dérivée seconde est négative lorsque $$r = R$$, confirmant qu'il s'agit bien d'un maximum.

   Ainsi, la puissance reçue par $$R$$ est maximale lorsque $$r = R$$.

## Questions d'analyse

1. Pourquoi la puissance reçue par $$R$$ dépend-elle de la somme des résistances $$r$$ et $$R$$ ?
2. Comment la loi d'Ohm est-elle utilisée pour déterminer le courant dans le circuit ?
3. Si la résistance $$r$$ était fixée et que $$R$$ pouvait varier, comment pourrait-on trouver expérimentalement la valeur de $$R$$ pour laquelle la puissance est maximale ?
4. Quel est l'impact de la valeur de la tension $$E$$ sur la condition $$r = R$$ pour maximiser la puissance ?
5. Si $$R$$ était beaucoup plus grande que $$r$$, comment cela affecterait-il la puissance reçue par $$R$$ ? Justifiez votre réponse en termes de résistance totale et de courant.

## Corrigé des questions d'analyse

1. La puissance reçue par $$R$$ dépend de la somme des résistances $$r$$ et $$R$$ car elles sont en série, et donc la tension totale est répartie entre les deux résistances selon leurs valeurs respectives. Le courant dans le circuit est déterminé par la résistance totale.
2. La loi d'Ohm est utilisée pour déterminer le courant en divisant la tension totale fournie par le générateur par la résistance totale du circuit. Ce courant est le même à travers toutes les résistances en série.
3. Expérimentalement, on pourrait varier $$R$$ et mesurer la puissance reçue par $$R$$ à chaque valeur. La puissance maximale serait observée lorsque $$r = R$$, conformément à la démonstration théorique.
4. La valeur de la tension $$E$$ n'affecte pas la condition $$r = R$$ pour maximiser la puissance. Cette condition est indépendante de $$E$$ et dépend uniquement des résistances.
5. Si $$R$$ était beaucoup plus grande que $$r$$, la résistance totale serait dominée par $$R$$, et le courant dans le circuit serait très faible. La faible valeur de courant signifierait que la puissance reçue par $$R$$ serait également faible, car $$P_R = I^2 R$$ et $$I$$ serait faible.
