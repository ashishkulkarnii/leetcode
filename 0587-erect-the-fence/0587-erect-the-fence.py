class Solution(object):
    def outerTrees(self, trees):
        trees.sort()
        
        def orientation(tree1, tree2, tree3):
            return (tree3[1] - tree1[1]) * (tree2[0] - tree1[0]) - (tree3[0] - tree1[0]) * (tree2[1] - tree1[1])
        
        stack_h = []
        stack_l = []
        
        for tree in trees:
            while len(stack_h) >= 2 and orientation(stack_h[-2], stack_h[-1], tree) > 0:
                stack_h.pop()
            while len(stack_l) >= 2 and orientation(stack_l[-2], stack_l[-1], tree) < 0:
                stack_l.pop()

            stack_h.append(tuple(tree))
            stack_l.append(tuple(tree))

        
        return set(stack_h + stack_l)
