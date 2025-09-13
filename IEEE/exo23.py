

"""On sait que les fonctions sont equivalents , donc on prend, la recurrence suivante à resoudre : 
          X[n+1] = f(X[n])
          X[n+1] = (R+1)*X[n] - R*X[n]²"""
X = 0.5
R = 3.0

for _ in range(10000000):


    X = (R+1)*X - R*X*X

print(f"The last iteration X = {X}")
# Chaos ,unstable function
