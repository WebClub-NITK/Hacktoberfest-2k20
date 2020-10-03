def polyhash(string, p, x):
    val = ord(string[0])
    y = 1
    for i in range(1, len(string)):
        y = x*y
        if(y>p):
            y = y%p
        val += y*ord(string[i])
    if(val >= p):
        val = val % p
    return val, y


def pre_compute_hashes(arr, P, T, p, x):
    H = [None] * (T-P+1)
    S = arr[T-P:T]
    H[T - P] ,y = polyhash(S, p, x)
    y = y*x
    if(y >= p):
        y = y % p
    for i in range(T-P-1, -1, -1):
        H[i] = (x*H[i+1]) + ord(arr[i]) - (y*ord(arr[i+P]))
        if(H[i] >= p or H[i] < 0):
            H[i] = H[i] % p
    return H

def rabin_karp(arr, pattern):
    p = 100000000000007
    x = 3
    P = len(pattern)
    P_hash, y = polyhash(pattern, p, x)
    result = []
    for text in arr:
        string = list(str(text))
        T = len(string)
        if(string == pattern):
            result.append(text)
            
        if(P >= T):
            continue
        H = pre_compute_hashes(string, P, T, p, x)
        for i in range(T-P+1):
            if(P_hash != H[i]):
                continue
            #if(arr[i:i+P] == pattern):
            result.append(text)
    return result


strings = list(map(str, input().split()))
prefix = list(str(input()))
result = rabin_karp(strings, prefix)
print(*result)