
def main():
    n = int(input())
    top, bottom = -1, float('inf')
    for i in range(n):
        a = int(input())

        if top < a:
            top = a
        if bottom > a:
            bottom = a

    print(top - bottom)

main()
