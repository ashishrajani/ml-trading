import numpy as np


def test_run():
    print(np.array([[2, 3, 4], [2, 3, 4]]))
    print(np.empty(5))
    print(np.empty((5, 4)))
    print(np.empty((5, 4, 3)))
    print(np.ones((5, 4, 3), dtype=np.int_))
    print(np.random.random((5, 4, 3)))
    print(np.random.rand(5, 4, 3))
    print(np.random.normal(50, 10, size=(2, 3)))
    print(np.random.randint(0, 10, size=(2, 3)))
    print(np.random.randint(0, 10, size=(2, 3)).shape)
    print(len(np.random.randint(0, 10, size=(2, 3)).shape))
    print(np.random.randint(0, 10, size=(2, 3)).size)
    print(np.random.randint(0, 10, size=(2, 3)).dtype)

    np.random.seed(123)
    a = np.random.randint(0, 10, size=(5, 4))
    print(a)
    print(a.sum())
    print(a.sum(axis=0))
    print(a.sum(axis=1))
    print(a.min(axis=0))
    print(a.max(axis=1))
    print(a.mean(axis=1))

    print(a[a<2])
    print(2 * a)
    print(a / 2)
    print(a / 2.0)


if __name__ == "__main__":
    test_run()