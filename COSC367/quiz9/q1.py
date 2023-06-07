network = {
    
}




if __name__ == "__main__":
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