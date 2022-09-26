from itertools import product
def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will eventually hold the value we are interested in
    for var in network:
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 
        
        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
        parents = []
        for parent in network[var]['Parents']:
            parents.append(assignment[parent])
        parents = tuple(parents)
        if assignment[var]:
            p *= network[var]['CPT'][parents]
        else:
            p *= 1 - network[var]['CPT'][parents]
    return p

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Find the hidden variables
    # Initialise a raw distribution to [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        for values in product((True, False), repeat=len(hidden_vars)):
                hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
                hidden_assignments
            # Update the assignment (we now have a complete assignment)
            # Update the raw distribution by the probability of the assignment.
    # Normalise the raw distribution and return it
        return hidden_assignments


if __name__ == "__main__":
    
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