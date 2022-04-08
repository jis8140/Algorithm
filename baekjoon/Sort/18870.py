import sys

# input
sys.stdin.readline()
X_list = list(map(int, sys.stdin.readline().split()))

#sort
X_dict = {ele: idx for idx, ele in enumerate(sorted(set(X_list)))}

#output
print(' '.join(map(str, [X_dict[ele] for ele in X_list])))