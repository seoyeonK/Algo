park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

#[2,1]

# park = ["SOO","OXX","OOO"]
# routes = ["E 2","S 2","W 1"]	

#[0,1]

# park = ["OSO","OOO","OXO","OOO"]
# routes = ["E 2","S 3","W 1"]

#[0,0]

def solution(park, routes):
    answer = []
    H = len(park)
    W = len(park[0])
    cur_x = 0
    cur_y = 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                cur_y = i
                cur_x = j

    def dir_(_y, _x, route):
        d_, len_ = route.split(" ")
        len_ = int(len_)
        temp_y = _y
        temp_x = _x
        
        if d_ == "E":
            for i in range(len_):
                if _x+1 != W and park[_y][_x+1] != "X":
                    _x +=1
                else:
                    _x = temp_x
                    break

        elif d_ == "W":
            for i in range(len_):
                if _x-1 >= 0 and park[_y][_x-1] != "X":
                    _x -=1
                else:
                    _x = temp_x
                    break
                    
                 
        elif d_ == "S":
            for i in range(len_):
                if _y+1 != H and park[_y+1][_x] != "X":
                    _y +=1
                else:
                    _y = temp_y
                    break                    
                 
        elif d_ == "N":
            for i in range(len_):
                if _y-1 >= 0 and park[_y-1][_x] != "X":
                    _y -=1
                else:
                    _y = temp_y
                    break 
        return(_y, _x)
                    
                    

    for route in routes:
        cur_y, cur_x = dir_(cur_y, cur_x, route)   
        
    answer = [cur_y, cur_x]
    return answer


print(solution(park, routes))



#다른사람 풀이
def solution1(park, routes):
    w, h = len(park), len(park[0])
    for i,v in enumerate(park):
        if 'S' in v:
            y,x=i,v.find("S")

    navi = {'E':[1, 0], 'W': [-1, 0], 'S': [0, 1], 'N': [0, -1]}
    for go in routes:
        op, l = go.split(' ')
        l=int(l)
        dir_x, dir_y = navi[op]
        block=False
        if not ((x+dir_x * l) in range(0, h) and (y + dir_y*l) in range(0, w)):
            continue
        for l2 in range(1, l + 1):
            if park[y+dir_y * l2][x+dir_x * l2] == 'X':
                block=True
        if not block:
            x += dir_x * l
            y += dir_y * l

    return [y,x]