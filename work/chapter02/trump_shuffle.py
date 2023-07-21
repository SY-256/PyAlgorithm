import random

MARKS = ["♥", "♦", "♠", "♣"]
NUMS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def get_label(no):
    mark = no // 13
    num = no % 13
    return MARKS[mark] + NUMS[num]


def get_shuffle(arr):
    n = len(arr)
    for i in reversed(range(0, n)):
        k = random.randint(0, i)
        arr[i], arr[k] = arr[k], arr[i]
    return arr


if __name__ == "__main__":
    # カードの生成
    cards = list(range(0, 52))
    # シャッフル
    cards = get_shuffle(cards)
    # 先頭7枚表示
    print(list(map(get_label, cards[:7])))
