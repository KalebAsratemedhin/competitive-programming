# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import deque

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        successors = {chr(ord('a') + i): [] for i in range(K)}
        predecessors = {chr(ord('a') + i): 0 for i in range(K)}
        
        for i in range(N - 1):
            curr = alien_dict[i]
            nxt = alien_dict[i + 1]
            j = 0
            
            while j < min(len(curr), len(nxt)) and curr[j] == nxt[j]:
                j += 1
            
            if j < min(len(curr), len(nxt)):
                successors[curr[j]].append(nxt[j])   
                predecessors[nxt[j]] += 1
                
        queue = deque()
        ans = []
        
        for key, value in predecessors.items():
            if value == 0:
                queue.append(key)
                

        while queue:
            node = queue.popleft()
            ans.append(node)
            
            for successor in successors[node]:
                predecessors[successor] -= 1
                if predecessors[successor] == 0:
                    queue.append(successor)

        return "".join(ans)
                
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends