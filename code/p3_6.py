# AtCoder Beginner Contest 051 の B で AC 確認済み

def main():
    k, s = map(int, input().split())
    ans = 0
    # x + y - s = z
    for i in range(k + 1):
        for j in range(k + 1):
            z = s - i - j
            if z >= 0 and z <= k:
                ans += 1
    print(ans)

main()
