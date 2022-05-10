import sys

k = int(input())
print(''.join(sys.stdin.readline().strip()[::k]))