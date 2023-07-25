def power(n, m):
    if m == 0:
        return 1
    if m < 0:
        return 1 / (n * power(n, abs(m) - 1))
    return n * power(n, m - 1)


def test_power():
    assert power(2, 2) == pow(2, 2)
    assert power(2, -2) == pow(2, -2)
    assert power(2, 3) == pow(2, 3)
    assert power(2, -3) == pow(2, -3)


if __name__ == "__main__":
    print(power(2, 0))
