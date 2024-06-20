import random
def test_random_list():
 
    l = [random.randint(1,100) for _ in range(10)]
    l.sort()
    print(l)

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))
