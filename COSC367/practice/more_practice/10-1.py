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

print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")