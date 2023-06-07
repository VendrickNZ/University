import math
def euclidean_distance(v1, v2):
    sum = 0
    for i in range (len(v1)):
        sum += (v1[i] - v2[i]) ** 2
    return math.sqrt(sum)

def majority_element(labels):
    counts={label: 0 for label in labels}
    for label in labels:
        counts[label] += 1
    
    return max(counts, key=lambda label: counts[label])

def knn_predict(input, examples, distance, combine, k):
    if not k <= len(examples):
        k = len(examples)
    neighbours = sorted(examples, key=lambda example: distance(input, example[0]))
    print('neighbours=', neighbours)
    selected = neighbours[:k]
    i = k
    while i < len(examples) and distance(input, neighbours[i - 1][0]) == distance(input, neighbours[i][0]):
        selected.append(neighbours[i])
        i += 1
    return combine([neighbour[1] for neighbour in selected])


examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()