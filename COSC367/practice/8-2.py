from itertools import product

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    # Initialise a raw distribution to [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        for values in product((True, False), repeat=len(hidden_vars)):
            # Update the assignment (we now have a complete assignment)
            # Update the raw distribution by the probability of the assignment.
    # Normalise the raw distribution and return it


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))