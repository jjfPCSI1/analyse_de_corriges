# Calcul de la tension centrale dans un circuit avec deux résistances et deux générateurs idéaux de tension

![](images/tension_centrale_E1_R1_R2_E2.webp)

## Énoncé

Considérez un circuit électrique composé de deux résistances $$R_1$$ et $$R_2$$ en série, connectées à deux générateurs de tension idéaux $$E_1$$ et $$E_2$$ en série. Le générateur $$E_1$$ est connecté en série avec $$R_1$$, et $$R_2$$ est connecté en série avec $$E_2$$, formant une boucle complète. Les valeurs des composants sont les suivantes :
- $$R_1 = 10 \, \Omega$$
- $$R_2 = 20 \, \Omega$$
- $$E_1 = 12 \, V$$
- $$E_2 = 5 \, V$$

Calculez la tension entre le point de jonction des deux générateurs et le point de jonction des deux résistances.

## Corrigé

1. **Principe du circuit** :
   Dans un circuit en série, le courant est le même à travers tous les composants. La tension totale dans le circuit est la somme des tensions fournies par les générateurs, et la tension aux bornes de chaque résistance est donnée par la loi d'Ohm.

2. **Calcul du courant dans le circuit** :
   La tension totale fournie par les générateurs est :
   $$
   E_{\text{total}} = E_1 + E_2 = 12 \, V + 5 \, V = 17 \, V
   $$

   La résistance totale du circuit est :
   $$
   R_{\text{total}} = R_1 + R_2 = 10 \, \Omega + 20 \, \Omega = 30 \, \Omega
   $$

   Le courant dans le circuit est donc :
   $$
   I = \frac{E_{\text{total}}}{R_{\text{total}}} = \frac{17 \, V}{30 \, \Omega} \approx 0.567 \, A
   $$

3. **Calcul des tensions aux bornes des résistances** :
   La tension aux bornes de $$R_1$$ est :
   $$
   V_{R_1} = I \cdot R_1 = 0.567 \, A \times 10 \, \Omega = 5.67 \, V
   $$

   La tension aux bornes de $$R_2$$ est :
   $$
   V_{R_2} = I \cdot R_2 = 0.567 \, A \times 20 \, \Omega = 11.33 \, V
   $$

4. **Calcul de la tension centrale** :
   La tension centrale $$V_C$$ est la différence de potentiel entre le point de jonction des deux générateurs et le point de jonction des deux résistances. Comme $$V_{R_1}$$ et $$V_{R_2}$$ sont en série avec leurs générateurs respectifs, nous avons :
   $$
   V_C = E_1 - V_{R_1} = 12 \, V - 5.67 \, V = 6.33 \, V
   $$

   ou

   $$
   V_C = V_{R_2} - E_2 = 11.33 \, V - 5 \, V = 6.33 \, V
   $$

   Donc, la tension centrale $$V_C$$ est de 6.33 V.

## Questions d'analyse

1. Pourquoi la somme des tensions fournies par les générateurs est-elle égale à la somme des tensions aux bornes des résistances ?
2. Que se passerait-il si les valeurs de $$R_1$$ et $$R_2$$ étaient inversées ?
3. Comment la tension centrale serait-elle affectée si la valeur de $$E_2$$ était augmentée ?
4. Pourquoi est-il important de considérer que les générateurs et résistances sont en série dans ce type de calcul ?
5. Comment pourrait-on modifier le circuit pour obtenir une tension centrale de 0 V ?

## Corrigé des questions d'analyse

1. La somme des tensions fournies par les générateurs est égale à la somme des tensions aux bornes des résistances en raison de la loi des mailles de Kirchhoff, qui stipule que la somme algébrique des différences de potentiel dans une maille fermée est nulle.
2. Si les valeurs de $$R_1$$ et $$R_2$$ étaient inversées, le courant dans le circuit resterait le même, mais les tensions aux bornes des résistances changeraient, affectant ainsi la tension centrale.
3. Si la valeur de $$E_2$$ était augmentée, la tension totale du circuit augmenterait, ce qui augmenterait le courant et donc la tension aux bornes de chaque résistance. La tension centrale augmenterait également.
4. Il est important de considérer que les générateurs et résistances sont en série car cela garantit que le courant est le même à travers tous les composants, simplifiant ainsi les calculs de tension et de courant.
5. Pour obtenir une tension centrale de 0 V, les valeurs des générateurs et des résistances pourraient être ajustées de manière à ce que les tensions aux bornes des résistances compensent exactement les tensions des générateurs. Par exemple, si $$E_1$$ et $$E_2$$ étaient égaux et $$R_1$$ et $$R_2$$ étaient ajustés en conséquence.
