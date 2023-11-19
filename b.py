def solve(n):
    ans = 0;
    i = n
    while(i > 0):
        for j in range(0,i):
           ans+=1
        i = i// 2
    print(ans)

solve(5)