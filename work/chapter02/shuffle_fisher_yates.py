import random

# シャッフルを行う関数
def shuffle(arr):
    n = len(arr)  # リストのサイズ
    # n - 1から1まで繰り返す
    for i in reversed(range(1, n)):
        k = random.randint(0, i)  # ランダムな要素を選択
        # 入れ替える
        arr[i], arr[k] = arr[k], arr[i]


if __name__ == "__main__":
    # shuffle関数
    arr = [1, 2, 3, 4, 5, 6, 7]
    for i in range(5):
        shuffle(arr)
        print(arr)
