class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        guards_set = {(guard[0],guard[1]) for guard in guards}
        walls_set= {(wall[0],wall[1]) for wall in walls}
        on_guard = set()

        for guard in guards:
            for j in [(1,0), (0,1), (-1, 0), (0, -1)]:
                dx = j[0]
                dy = j[1]
                x = guard[0]
                y = guard[1]
                while 0 <= dx + x < m and 0 <= dy + y < n and (x+dx, y+dy) not in walls_set and (x+dx, y+dy) not in guards_set:
                    on_guard.add((x+dx, y+dy))
                    x += dx
                    y += dy

        return m*n - len(guards_set) - len(walls_set) - len(on_guard)
            
