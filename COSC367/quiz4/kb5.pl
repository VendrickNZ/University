directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

contains(X, Y) :- directlyIn(Y, X); directlyIn(Z, X), contains(Z, Y).