from time import time

# fib関数の実行結果を覚えておくための辞書型変数
fib_memo = {}
# 再帰的にフィボナッチ数を計算する関数
def fib(n):
    if n <= 1:
        return 1
    # 既に計算済みか確認
    if n in fib_memo:
        return fib_memo[n]
    # 再帰的に関数fibを呼び出して、変数に保存
    fib_memo[n] = fib(n - 2) + fib(n - 1)
    return fib_memo[n]


# n個のフィボナッチ数列を求める関数
def fib_list(n):
    return [fib(n) for n in range(0, n)]


if __name__ == "__main__":
    start = time()
    print(fib_list(38))
    end = time()
    print(f"time: {(end-start)}秒")
