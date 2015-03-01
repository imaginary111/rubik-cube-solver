import rubik
from collections import deque
import time













def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """


    if start==end:
        return []
   
    moves = {}
    moves['F'] = rubik.F
    moves['Fi'] = rubik.Fi
    moves['L'] = rubik.L
    moves['Li'] = rubik.Li
    moves['U'] = rubik.U
    moves['Ui'] = rubik.Ui



    move=moves.values()

    startq=deque([start,None])
    startd={}
    startm={}
    startp={}
    startm[start]=(None)
    startp[start]=(None)
    startd[start]=(start)
    endq=deque([end,None])
    endd={}
    endm={}
    endp={}
    endm[end]=(None)
    endp[end]=(None)
    endd[end]=(end)
    #move=moves.values()
    for i in range(0,7):
        while  True:
            a=startq.popleft()
            if a==None:
                startq.append(None)
                break


            for h in move:
                b=rubik.perm_apply(h,a)
                if b not in startd:
                    startd[b]=(b)
                    startm[b]=(h)
                    startp[b]=(a)
                    startq.append(b)
                if b in endd:
                    forward_path=path(b,startd,startm,startp)
                    backward_path=path(b,endd,endm,endp)
                    forward_path.reverse()


                    return forward_path + backward_path



        while True:
            a=endq.popleft()
            if a==None:
                endq.append(None)
                break


            for h in move:
                b=rubik.perm_apply(rubik.perm_inverse(h),a)
                if b not in endd:
                    endd[b]=(b)
                    endm[b]=(h)
                    endp[b]=(a)
                    endq.append(b)
                if b in startd:
                    forward_path=path(b,startd,startm,startp)
                    backward_path=path(b,endd,endm,endp)
                    forward_path.reverse()

                    return forward_path + backward_path




        #print i
    return None



def path(start,dicti,b,c):
    path=[]
    while b[start] is not None:
        path.append(b[start])
        if c[start] is not None:
            start=c[start]
            
    return path




    
