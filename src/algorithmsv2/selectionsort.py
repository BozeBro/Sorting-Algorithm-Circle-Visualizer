def selection_sort(array):
    for i in range(len(array)):
        smallest = array[i]
        ind = i
        for j in range(i+1, len(array)):
            if (val := array[j]) < smallest:
                smallest = val
                ind = j
            yield i, i
        array[i], array[ind] = array[ind], array[i]
        yield i, ind

def test_selection_sort(array):
    for i in range(len(array)):
        smallest = array[i]
        ind = i
        for j in range(i+1, len(array)):
            if (val := array[j]) < smallest:
                smallest = val
                ind = j
        array[i], array[ind] = array[ind], array[i]
    return array
