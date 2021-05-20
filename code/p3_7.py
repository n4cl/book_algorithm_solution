# AtCoder Beginner Contest 045 の C で AC 確認済み

def main():
    s = input()
    l = len(s)
    ans = 0

    for bit in range(2**(l - 1)):
        tmp = s[0]
        for i in range(l - 1):
            if bit & (1 << i):
                ans += int(tmp)
                tmp = s[i + 1]
            else:
                tmp += s[i + 1]
        ans += int(tmp)
    print(ans)


main()
