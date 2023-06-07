network = {
    'X1' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (1+1)/(3+4),
            (False,): (2+1)/(4+4)
        }
    },

    'X2' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (1+1)/(3+4),
            (False,): (2+1)/(4+4)
        }
    },

    'X3' : {
        'Parents' : ['Y'],
        'CPT' : {
            (True,): (0+1)/(3+4),
            (False,): (0+1)/(4+4)
        }
    },

    'Y' : {
        'Parents' : [],
        'CPT' : {
            (): (3+1)/(7+2)
        }
    }
}

# network = {
#     'X1' : {
#         'Parents' : ['Y'],
#         'CPT' : {
#             (True,): (0+2)/(4+3),
#             (False,): (1+2)/(3+3)
#         }
#     },

#     'X2' : {
#         'Parents' : ['Y'],
#         'CPT' : {
#             (True,): (1+2)/(4+3),
#             (False,): (1+2)/(3+3)
#         }
#     },

#     'Y' : {
#         'Parents' : [],
#         'CPT' : {
#             (): (4+2)/(7+4)
#         }
#     }
# }
print("{:0.2f}".format(network['Y']['CPT'][()]))