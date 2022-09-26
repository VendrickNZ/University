from csp import *
import itertools
def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        contraint_list = []
        #print(values, "\n", names, "\n",domains,"\n",csp.var_domains, "\n", csp.constraints, "\n FINISH")
        assignment = {x:v for x, v in zip(names, values)}
        for constraint in csp.constraints:
            contraint_list.append(satisfies(assignment, constraint))
        if all(contraint_list):
            yield assignment


def main():

    crossword_puzzle = CSP(
        var_domains={
            # read across:
            'a1': set("ant,big,bus,car".split(',')),
            'a3': set("book,buys,hold,lane,year".split(',')),
            'a4': set("ant,big,bus,car,has".split(',')),
            # read down:
            'd1': set("book,buys,hold,lane,year".split(',')),
            'd2': set("ginger,search,symbol,syntax".split(',')),
            },
        constraints={
            lambda a1, d1: a1[0] == d1[0],
            lambda d1, a3: d1[2] == a3[0],
            lambda a1, d2: a1[2] == d2[0],
            lambda d2, a3: d2[2] == a3[2],
            lambda d2, a4: d2[4] == a4[0],
            })

    solution = next(iter(generate_and_test(crossword_puzzle)))

    # printing the puzzle similar to the way it actually  looks 
    pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
        solution['d1'], "", solution['d2'], fillvalue=" ")]
    pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
    print("\n".join(pretty_puzzle))

if __name__ == "__main__":
    main()