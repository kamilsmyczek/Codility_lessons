import stack  
def solution(H):
    if not H:
        return 1
    cnt = 1    
    lastHeight = H[0]
    wall = Stack()
    wall.push(lastHeight)
    
    for i in H[1:]:
        if i == lastHeight:
            continue
            
        cnt += 1
        
        while wall.size() > 0 and i < wall.peek():
            wall.pop()
            
        if wall.size() > 0 and i == wall.peek():
            cnt -= 1
        else:
            wall.push(i)
            
        lastHeight = i 
 
    return cnt