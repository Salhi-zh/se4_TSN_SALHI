Exercise 2.4:


Nous attendons que la condition dans la boucle while soit vérifiée indéfiniment, et A est doublé à chaque itération, tandis qu'au cours de l'exécution, nous rencontrons un comportement non trivial :

Le comportement observé dans le code résulte du format IEEE-754 en double précision, qui utilise une mantisse de 52 bits stockés et un exposant de 11 bits. La clé pour comprendre le seuil à $2^{53}$ réside dans le $\textbf{bit de tête implicite}$ de la mantisse, qui fournit une précision effective de 53 bits. La valeur d'un nombre normalisé est donnée par :
$$
(-1)^{\text{signe}} \times (1.\text{mantisse})_2 \times 2^{\text{exposant} - 1023}
\]
$$
L'écart entre les nombres représentables consécutifs, appelé ULP (Unit in the Last Place), est de $2^{k-52}$ pour les nombres dans l'intervalle $[2^k, 2^{k+1})$.

Pour $A = 2^{52}$ ($k=52$), l'ULP est $2^0 = 1$. Ainsi, $A + 1 = 2^{52} + 1$ est exactement représentable, et l'opération $(A + 1.0) - A$ donne $1.0$.

Cependant, pour $A = 2^{53}$ ($k=53$), l'ULP devient $2^{53-52} = 2^1 = 2$. Le nombre représentable suivant après $2^{53}$ est $2^{53} + 2$. La valeur $2^{53} + 1$ se situe exactement à mi-chemin entre ces deux et, selon la règle d'arrondi au pair, est arrondie à $2^{53}$. Par conséquent, $A + 1.0$ s'évalue à $A$, et $(A + 1.0) - A$ devient $0$, ce qui brise la condition de boucle.

Ceci démontre comment la précision limitée de l'arithmétique flottante rend les opérations inexactes au-delà de $2^{53}$, limitant fondamentalement la précision numérique dans les calculs à grande échelle.

