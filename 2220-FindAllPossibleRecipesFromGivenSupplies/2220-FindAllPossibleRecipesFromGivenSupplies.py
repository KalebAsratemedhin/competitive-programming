# Last updated: 7/22/2025, 3:26:54 PM
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        made_with = defaultdict(list)
        requirements = defaultdict(set)
        indegree = {}

        for idx, recipe in enumerate(recipes):
            requirements[recipe] = set(ingredients[idx])
            for ingredient in ingredients[idx]:
                made_with[ingredient].append(recipe)
                indegree[recipe] = indegree.get(recipe, 0) + 1
                indegree[ingredient] = indegree.get(ingredient, 0)

        queue = deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for recipe in made_with[node]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)

        store = set(supplies)
        ans = []


        for node in order:
            can_be_made = True
            if not requirements[node] and node not in store:
                continue
            for requirement in requirements[node]:
                if requirement not in store:
                    can_be_made = False
            if can_be_made:
                store.add(node)
            if can_be_made and requirements[node]:
                ans.append(node)

        return ans


                  