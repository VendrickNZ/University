from numbers import Number

network = {
    'X1' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (1+2)/(4+4),
            (False,): (3+2)/(3+4)
        }
    },

    'X2' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (1+2)/(4+4),
            (False,): (2+2)/(3+4)
        }
    },

    'X3' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (0+2)/(4+4),
            (False,): (0+2)/(3+4)
        }
    },

    'Y' : {
        'Parents' : [],
        'CPT' : {
            (): (4+2)/(7+4)
        }
    }
}

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")

for assignment, prob in sorted(network['Y']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))

for assignment, prob in sorted(network['X1']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))

for assignment, prob in sorted(network['X2']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))

