average_case = [-9999999999, 9, 1, 2, 8, 3, 4, 7, 5, 6]
best_case = [-9999999999, 9, 1, 8, 2, 7, 3, 6, 4, 5]
worst_case = [-9999999999, 1, 9, 2, 8, 3, 7, 4, 6, 5]
arr = best_case 

i = 2
k = 0
steps = 0
moves = 0
comparisons = 0
while i < len(arr):
    print "Step #{}:\nArray: {}\nMoves: {}\nComparisons: {}\nArray Size: {}\n{}\n".format(steps, arr, moves, comparisons, len(arr) - 1, "#" * 20)
    sent = k - 2*k/3
    j = i - 1
    t = arr[i] ; moves += 1
    
    comparisons += 1
    while arr[sent] < t < arr[j]:
        arr[j+1] = arr[j] ; moves += 1
        j = j - 1
        comparisons += 1
        steps += 1
    
    arr[j+1] = t ; moves += 1
    i = i + 1
    k = k + 1
    steps = steps + 1    
print "Step #{}:\nArray: {}\nMoves: {}\nComparisons: {}\nArray Size: {}\n{}\n".format(steps, arr, moves, comparisons,len(arr) - 1, "#" * 20)
