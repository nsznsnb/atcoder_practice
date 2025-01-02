def conv_base_to_10(s: str, k: int):
    """
        K進数を10進数に変換
        args
            s: k進数の値
            k: 何進数か(2<=k<=10)
    """
    result = 0
    for ch in s:
        result *= k
        result += ord(ch) - ord('0')
    return result

def conv_base10_to_K(s: str, k: int):
    """
        10進数をK進数に変換
        args
            s: 19進数の値
            k: 何進数か(2<=k<=10)
    """
    num = int(s)
    result = ""
    while num > 0:
        result = str(num % k) + result
        num //= k
    if result == "":
        result = "0"
    return result

def conv_base8_to_9(s: str):
    """
        8進数を9進数に変換
        args
            s: 8進数の値
    """
    v_base_10 = conv_base_to_10(s, 8)
    return conv_base10_to_K(v_base_10, 9)


N, K = input().split()
K = int(K)

ans = N
for i in range(K):
    ans = conv_base8_to_9(ans)
    s = ""
    for ch in ans:
        if ch == "8":
            s += "5"
        else:
            s += ch
    ans = s

print(ans)