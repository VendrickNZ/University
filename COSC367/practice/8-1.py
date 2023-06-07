def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will eventually hold the value we are interested in
    for var in network:
        parents = []
        for parent in network[var]['Parents']:
            parents.append(assignment[parent])
        parents = tuple(parents)
        if assignment[var]:
            p *= network[var]['CPT'][parents]
        else:
            p *= 1 - network[var]['CPT'][parents]
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 
        
        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
    
    return p


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))