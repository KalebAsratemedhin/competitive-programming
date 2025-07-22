# Last updated: 7/22/2025, 3:23:19 PM
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        colored_balls = {}
        unique_colors = []

        for ball, color in queries:


            if ball in colored_balls:
                prev_color = colored_balls[ball]
                colors[prev_color].remove(ball)
                if not colors[prev_color]:
                    del colors[prev_color]
            
            if color not in colors:
                colors[color] = set()
                
            colors[color].add(ball)
            colored_balls[ball] = color
            unique_colors.append(len(colors))
        
        return unique_colors

