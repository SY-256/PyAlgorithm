# リングバッファを初期化
def ringbuffer_new(size):
    return {"head": 0, "tail": 0, "size": 0, "buffer": [0 for _ in range(size)]}


# リングバッファに値を追加
def ringbuffer_write(rb, v):
    # 書き込み
    rb["buffer"][rb["tail"]] = v
    # 次回書き込み先を後ろに移動
    rb["tail"] = (rb["tail"] + 1) % len(rb["buffer"])
    # バッファがいっぱいになったか
    if rb["size"] >= len(rb["buffer"]):
        rb["head"] = (rb["head"] + 1) % len(rb["buffer"])
    else:
        rb["size"] += 1


# リングバッファから値を取得
def ringbuffer_read(rb):
    if rb["size"] <= 0:
        return None
    v = rb["buffer"][rb["head"]]
    rb["size"] -= 1
    # 読み込み位置を後ろに移動
    rb["head"] = (rb["head"] + 1) % len(rb["buffer"])
    return v


# リングバッファのテスト
def test_ringbuffer1():
    # リングバッファを作成
    rb = ringbuffer_new(3)
    # 値を追加
    ringbuffer_write(rb, 0)
    ringbuffer_write(rb, 1)
    ringbuffer_write(rb, 2)
    assert ringbuffer_read(rb) == 0
    assert ringbuffer_read(rb) == 1
    assert ringbuffer_read(rb) == 2


# リングバッファのテスト（その2）
def test_ringbuffer2():
    rb = ringbuffer_new(3)
    # 1から100まで書き込み
    for i in range(1, 100 + 1):
        ringbuffer_write(rb, i)
    assert ringbuffer_read(rb) == 98
    assert ringbuffer_read(rb) == 99
    assert ringbuffer_read(rb) == 100
    assert ringbuffer_read(rb) is None
