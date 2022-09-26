likes(bob, chocolate).
hungry(alice).

eats(person, thing) :- likes(person, thing).
eats(person, thing) :- hungry(person), edible(thing).