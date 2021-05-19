# AtCoder Beginner Contest 081 の B で AC 確認済み

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    while True:
        if a[i] % 2 != 0:
            break
        a[i] //= 2
        i += 1

        if i == n-1:
            i = 0
            ans += 1

    print(ans)

main()
