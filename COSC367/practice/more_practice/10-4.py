def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        sum = 0
        for i in range(len(input)):
            sum += (weights[i] * input[i])
        decision_boundary = bias + sum
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        return int(decision_boundary >= 0)
    
    return perceptron # this line is fine

def accuracy(classifier, inputs, expected_outputs):
    total_right = 0
    n = len(inputs)
    for i in range(n):
        if classifier(inputs[i]) == expected_outputs[i]:
            total_right += 1
    return total_right / n

perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))