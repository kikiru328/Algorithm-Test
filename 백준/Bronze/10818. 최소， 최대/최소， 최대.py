def solution():
    N = int(input())
    Ns = list(map(int, input().split()))
    print(f"{min(Ns)} {max(Ns)}")
solution()