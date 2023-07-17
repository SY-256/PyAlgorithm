# 変数の初期化
AMOUNT = 278  # 目標金額
num_pattern = 0  # 組み合わせ調査用
min_coin = 9999  # 最小コイン枚数
min_comb = [0, 0, 0]  # 最小コインの枚数の組み合わせ
max_coin = 0  # 最大コイン枚数
max_comb = [0, 0, 0]  # 最大コインの枚数の組み合わせ

# 総当たり
for c1 in range(0, 18 + 1):
    for c5 in range(0, 20 + 1):
        for c10 in range(0, 30 + 1):
            total = (c10 * 10) + (c5 * 5) + c1
            if AMOUNT != total:
                continue
            num_pattern += 1
            # コインの枚数
            num_coin = c10 + c5 + c1
            # 一番少ない硬貨か調べる
            if min_coin > num_coin:
                min_coin = num_coin
                min_comb = [c10, c5, c1]
            # 一番多い硬貨か調べる
            if max_coin < num_coin:
                max_coin = num_coin
                max_comb = [c10, c5, c1]

print(f"組み合わせ数={num_pattern}")
c10, c5, c1 = min_comb
print(f"最小枚数の組み合わせ=10円*{c10} + 5円*{c5} + 1円*{c1}")
c10, c5, c1 = max_comb
print(f"最大枚数の組み合わせ=10円*{c10} + 5円*{c5} + 1円*{c1}")
