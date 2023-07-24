# 1からnまでの合計を求める関数
def rec_sum(n):
    # 1以下なら1を返す
    if n <= 1:
        return 1
    # 1からn-1までの合計を再帰的に求めnを足す
    return n + rec_sum(n - 1)


# 1～10までの合計を表示
print(rec_sum(10))
