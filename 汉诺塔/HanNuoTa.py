
def hanoi(n, a, buffer, c):
    if(n == 1):
        print(a,"--->",c)
        return hanoi(n-1, a, c, buffer)
        hanoi(1, a, buffer, c)
        hanoi(n-1, buffer, a, c)
def main():
    n = int(input("请输入汉诺塔铜盘的个数:"))
    hanoi(n, "a", "b", "c")
if __name__ == "__main__":
    main()

