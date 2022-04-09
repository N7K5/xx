

def do_move(pos, str, times):
    print(str, times)
    x,y,z= pos[0],pos[1],pos[2]
    U,D,E,W,N,S=0,0,0,0,0,0
    for c in str:
        if c=="U": U+=1
        if c=="D": D+=1
        if c=="E": E+=1
        if c=="W": W+=1
        if c=="N": N+=1
        if c=="S": S+=1
    E= (E-W)*times
    S= (S-N)*times
    D= (D-U)*times
    x= (x+E)%(1e8+1)
    y= (y+S)%(1e8+1)
    z= (z+D)%(1e8+1)
    return[x,y,z]




def solve(str):
    move= [0,0,0]
    st= list()
    for c in str:
        if c==']':
            cur= ""
            while len(st)>0  and st[-1]!="[":
                cur= st.pop(-1)+cur
            if len(st)>0: st.pop(-1)
            times= ""
            while len(st)>0 and st[-1].isdigit():
                times+=st.pop(-1)
            if times=="": times=1
            else:
                t_rev= times[::-1]
                times=0
                for t in t_rev:
                    times= times*10+int(t)
            move= do_move(move, cur, times)
        else:
            st.append(c)
    cur= "".join(st)
    move= do_move(move, cur, 1)
    return [int(move[0]), int(move[1]), int(move[2])]




def secretAgent(n, arr):
    res= solve(arr)
    return str(res[0])+" "+str(res[1])+" "+str(res[2])
