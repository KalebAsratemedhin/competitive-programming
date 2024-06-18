# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead_people = set()
        self.children = defaultdict(list)
        self.king_name = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead_people.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def preOrderTraversal(person):
            if person not in self.dead_people:
                order.append(person)
            for child in self.children[person]:
                preOrderTraversal(child)
            
        preOrderTraversal(self.king_name)
        return order

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()