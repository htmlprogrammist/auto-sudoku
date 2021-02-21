import main

matrix = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split())),
          list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split())),
          list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]

main.main(matrix)  # 1 2 3 4 5 6 7 8 9
"""
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8
"""
