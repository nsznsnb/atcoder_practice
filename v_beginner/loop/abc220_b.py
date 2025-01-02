def convert_basek_to_base10(s: str, k: int):
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


K = int(input())
A, B = input().split()

print(convert_basek_to_base10(A, K) * convert_basek_to_base10(B, K))

