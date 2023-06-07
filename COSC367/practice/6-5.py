from csp import *

relations = [
    Relation(header=['a', 'b', 'c'],
            tuples={(2, 0, 0),
                    (1, 0, 0),
                    (2, 1, 0),
                    (2, 0, 1)}
        
    ),

    Relation(header=['c', 'd'],
            tuples={(2, 0),
                    (2, 1),
                    (1, 0)})
    
    ### COMPLETE ###
]

csp = CSP(
    var_domains = {var:{0,1,2} for var in 'abcd'},
    constraints = {
        lambda a, b, c: a > b + c,
        lambda c, d: c > d
        }
)


print(len(relations))
print(all(type(r) is Relation for r in relations))
print(sorted(sorted(relations)[0].tuples))