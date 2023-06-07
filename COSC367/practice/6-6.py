from csp import *

relations = [
    Relation(
        header=['a', 'b'],
        tuples={(1, -1),
                (1, 1),
                (0, 0)}
    ),

    Relation(
        header=['c', 'd'],
        tuples={(1, -1),
                (1, 0),
                (0, -1)}
    ),

    Relation(
        header=['a', 'b', 'c'],
        tuples={(1, 1, -1),
                (-1, -1, -1)}
    )
]

relations_after_elimination = [
    Relation(
        header=['b', 'c'],
        tuples={(1, -1)}
    ),
    
    Relation(
        header=['c', 'd'],
        tuples={(1, -1),
                (1, 0),
                (0, -1)}
    )
]