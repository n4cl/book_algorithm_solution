
def main():
    n = int(input())
    mini, ans = float('inf'), float('inf')
    for i in range(n):
        a = int(input())
        if ans > a:
            if mini > a:
                ans = mini
                mini = a
            else:
                ans = a
    print(ans)

main()
