

def dist(a,b):
    res= abs(a[0]-b[0]) + abs(a[1]-b[1])
    return res

def all_visited(visited):
    res= True
    for v in visited:
        res= res and v
    return res

def get_dist(cur_xy, shops, dest, visited, total_d):
    if all_visited(visited):
        return total_d+dist(cur_xy, dest)

    min_t_d= float("inf")
    for v_idx in range(len(visited)):
        if visited[v_idx] == False:
            visited[v_idx]= True
            new_d= total_d+dist(cur_xy, shops[v_idx])
            t_d= get_dist(shops[v_idx], shops, dest, visited, new_d)
            min_t_d= min(min_t_d, t_d)
            visited[v_idx]= False
    return min_t_d




def solve(arr):
    src= arr[0]
    dest= arr[-1]
    shops= arr[1:-1]
    visited= [False for _ in shops]

    d= get_dist(src, shops, dest, visited, 0)
    return d



# def main():
#     N= int(input())
#     arr= [[0,0] for _ in range(N+2)]
#     arr[-1][0], arr[-1][1]= int(input()), int(input())
#     arr[0][0], arr[0][1]= int(input()), int(input())
#     for i in range(1, N+1):
#         arr[i][0], arr[i][1]= int(input()), int(input())
#     res= solve(arr)
#     print(res)


def main():
    ip=""
    while(len(ip)==0):
        ip= input()
    N= int(ip)
    ip=""
    while(len(ip)==0):
        ip= input()
    d= [int(x) for x in ip.split(" ")]
    cur=0
    arr= [[0,0] for _ in range(N+2)]
    for x in range(N+2):
        arr[x][0]= d[cur]
        arr[x][1]= d[cur+1]
        cur+=2
    arr[1],arr[-1]= arr[-1],arr[1]
    res= solve(arr)
    print(res)


def main_test():
    T= 1
    for _ in range(T):
        main()

if __name__=="__main__":
    main_test()

# office= [[39,9]]
# home= [[97, 61]]
# shops= [
#     [35,93],
#     [62,64],
#     [96,39],
#     [36,36],
#     [9,59],
#     [59,96],
#     [61,7],
#     [64,43],
#     [43,58],
#     [1, 36]
# ]

# f= office+shops+home

# print(solve(f))
