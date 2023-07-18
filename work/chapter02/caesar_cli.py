import sys
import caesar

# コマンドライン引数の数を確認
if len(sys.argv) < 3:
    print('[使い方] caesar_cli.py "文章" (key_no)')
    quit()
# コマンドライン引数を取得
src = sys.argv[1]
key_no = int(sys.argv[2])

# 暗号化
print(caesar.encrypt(src, key_no))
