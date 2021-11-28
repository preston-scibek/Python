
def quicksort():
    class QSScope: 
        exchanges = 0
        comparisons = 0
    
    def _quicksort(arr, start, end):
#        QSScope.comparisons += 1
        if start < end:
            pivot = partition(arr, start, end)
            _quicksort(arr, start, pivot - 1)
            _quicksort(arr, pivot + 1, end)

    def partition(arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            QSScope.comparisons += 1
            if arr[j] <= pivot:
                i = i + 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                QSScope.exchanges += 1
        temp = arr[i + 1]
        arr[i + 1] = arr[end]
        arr[end] = temp
        QSScope.exchanges += 1
        print "After a parition executed with pivot {} this is the result.\nArray:{}\nComparisons {}, Exchanges {}".format(pivot, arr, QSScope.comparisons, QSScope.exchanges)
        return i + 1

    an_array = [30,80,20,70,60,40,90,10,50]
    _quicksort(an_array, 0, 8)
    print QSScope.comparisons
    print QSScope.exchanges    
    print an_array
    

def insertthirdsort():
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

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print sys.argv[1]
        globals()[sys.argv[1]]() 
