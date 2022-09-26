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

if __name__ == "__main__":
    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}


    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p))

    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p))

    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p)) 

    
    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
    p = joint_prob(network, {'A': False, 'B':False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B':False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B':True})
    print("{:.5f}".format(p)) 

    
    network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

    p = joint_prob(network, {'John': True, 'Mary': True,
                            'Alarm': True, 'Burglary': False,
                            'Earthquake': False})
    print("{:.8f}".format(p))        