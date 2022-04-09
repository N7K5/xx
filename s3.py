

def solve_c_clockwise(arr, s_x, s_y):
    n, m= len(arr), len(arr[0])
    x,y= s_x, s_y
    if s_x==0 and s_y==0:
        current_move= "r"
    elif s_x==0 and s_y!=0:
        current_move= "u"
    elif s_x!=0 and s_y==0:
        current_move= "d"
    else:
        current_move= "l"
    

    res=0
    res_max= 0
    total_rem= m*n
    while total_rem>0:
        total_rem-=1

        if arr[x][y]==1:
            res+=1
            res_max= max(res_max, res)
            # print("---")
            # print(x,y)
        else:
            res=0
            # print("")

        arr[x][y]=2
        
        if current_move=="r":
            x+=1
            if x>=n or arr[x][y]==2:
                current_move="d"
                x-=1
                y+=1
        elif current_move=="u":
            y-=1
            if y<0 or arr[x][y]==2:
                current_move= "r"
                x+=1
                y+=1
        elif current_move=="d":
            y+=1
            if y>=m or arr[x][y]==2:
                current_move= "l"
                y-=1
                x-=1
        elif current_move=="l":
            x-=1
            if x<0 or arr[x][y]==2:
                current_move= "u"
                x+=1
                y-=1
    return res_max








def solve_clockwise(arr, s_x, s_y):
    n, m= len(arr), len(arr[0])
    x,y= s_x, s_y
    if s_x==0 and s_y==0:
        current_move= "l"
    elif s_x==0 and s_y!=0:
        current_move= "d"
    elif s_x!=0 and s_y==0:
        current_move= "u"
    else:
        current_move= "r"
    
    print(current_move)

    res=0
    res_max= 0
    total_rem= m*n
    while total_rem>0:
        total_rem-=1

        if arr[x][y]==1:
            res+=1
            res_max= max(res_max, res)
            # print("---")
            # print(x,y)
        else:
            res=0
            # print("")

        arr[x][y]=2
        
        if current_move=="r":
            x+=1
            if x>=n or arr[x][y]==2:
                current_move="u"
                x-=1
                y-=1
        elif current_move=="u":
            y-=1
            if y<0 or arr[x][y]==2:
                current_move= "l"
                x-=1
                y+=1
        elif current_move=="d":
            y+=1
            if y>=m or arr[x][y]==2:
                current_move= "r"
                y-=1
                x+=1
        elif current_move=="l":
            x-=1
            if x<0 or arr[x][y]==2:
                current_move= "d"
                x+=1
                y+=1
    return res_max





def redRope(n,m,sp,ca,a):

    n, m= len(arr), len(arr[0])

    if sp==0:
        s_x, s_y= 0,0
    elif sp==1:
        s_x, s_y= 0,1
    elif sp==2:
        s_x, s_y= 1,1
    else:
        s_x, s_y= 1,0

    if ca==0:
        f= solve_clockwise
    else:
        f= solve_c_clockwise

    res= f(a, s_x, s_y)
    return res




