def solution(pos):
    col = ["a", "b", "c", "d", "e", "f", "g", "h"]
    x = col.index(pos[0])
    y = int(pos[1]) - 1
    
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    count = 0
    for step in steps:
        nextX = x + step[0]
        nextY = y + step[1]

        if nextX >= 0 and nextX <= 7 and nextY >= 0 and nextY <= 7:
            count += 1
    return count

print(solution(pos="c2"))