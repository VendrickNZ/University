from csp import *

relations = [
      
      ### COMPLETE ###
      Relation(
        header=['a', 'b'],
        tuples={(0, 0),
                (1, -1),
                (1, 1)}
      ),

      Relation(
        header=['c', 'd'],
        tuples={(1, 0),
               (1, -1),
               (0, -1)}
      ),

      Relation(
        header=['a', 'b', 'c'],
        tuples={(1, 1, -1),
                (-1, -1, -1)}
      )
      
] 

relations_after_elimination = [
    
    ### COMPLETE ###
    
    ] 

def main():
    csp = CSP(
    var_domains = {var:{-1,0,1} for var in 'abcd'},
    constraints = {
        lambda a, b: a == abs(b),
        lambda c, d: c > d,
        lambda a, b, c: a * b > c + 1
        }
    )


    print(len(relations))
    print(all(type(r) is Relation for r in relations))

if __name__ == "__main__":
    main()