def bucketsort(arr):
    bucket = []

    for n in range(len(arr)):
        bucket.append([])

    for i in arr:
        index_b = int(i)
        bucket[index_b].append(i)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

    return arr
