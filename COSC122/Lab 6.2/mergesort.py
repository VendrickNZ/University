result = []
i=0
j=0
count = 0
while i < len(left) and j < len(right):
    count += 1
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
# add any left-overs
while i < len(left):
    result.append(left[i])
    i += 1

while j < len(right):
    result.append(right[j])
    j += 1