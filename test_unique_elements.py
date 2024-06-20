def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = {1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10}

    l = list(set(l))


    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
