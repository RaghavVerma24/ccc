N = int(input())

memoize = {}


def traverse(w, sofar=0):
    global n_subtrees

    if w in memoize:
        return memoize[w]
    else:
        if w == 1:
            memoize[w] = sofar + 1
            return sofar + 1
        else:
            temp = 0
            for k in range(2, w + 1):
                common_w = int(w / k)
                temp += traverse(common_w)

            memoize[w] = sofar + temp
            return sofar + temp


out = traverse(N)
print(out)
