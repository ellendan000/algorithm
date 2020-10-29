import algorithm.sort as s 

givenArray = [9, 1, 6, 2, 4, 8, 3, 5, 7]
expectArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_selection_sort():
    assert expectArray == s.selection_sort(givenArray)

def test_quick_sort():
    assert expectArray == s.quick_sort(givenArray)

def test_merge_sort():
    assert expectArray == s.merge_sort(givenArray)