

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
    return val

def rabin_karp(arr, pattern):
    p = 100000000000007
    x = 3
    P = len(pattern)
    P_hash = polyhash(pattern, p, x)
    result = []
    for text in arr:
        string = list(str(text))
        T = len(string)
        if(string == pattern):
            result.append(text)
        if(P >= T):
            continue
        prefix = text[0:P]
        H  = polyhash(prefix, p, x)
        if(P_hash != H):
            continue
        result.append(text)
    return result


strings = list(map(str, input().split()))
prefix = list(str(input()))
result = rabin_karp(strings, prefix)
print(*result)