import sys
s = sys.argv
if len(s) != 3:
    print("Invalid Input")
else:
    s1 = s[1]
    s2 = s[2]
    m = len(s1)
    n = len(s2)
    if m != n:
        print(False)
    else:
        dic = {}
        res = True
        for i in range(n):
            if dic.get(s1[i]) == None:
                dic[s1[i]] = s2[i]
            else:
                if dic[s1[i]] != s2[i]:
                    res = False
        print(res)

