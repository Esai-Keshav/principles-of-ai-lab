class TreeNode:
    def __init__(self, score):
        self.score = score
        self.children = []


# Build a tree with scores at each node
root = TreeNode(2)
root.children = [TreeNode(7), TreeNode(5), TreeNode(4)]

root.children[0].children = [TreeNode(3), TreeNode(8), TreeNode(3)]
root.children[1].children = [TreeNode(1), TreeNode(2), TreeNode(6)]
root.children[2].children = [TreeNode(2), TreeNode(4), TreeNode(7)]


# Define the alpha-beta pruning function
def alpha_beta(node, depth, alpha, beta, is_maximizing):
    if depth == 0 or not node.children:
        return node.score

    if is_maximizing:
        max_eval = float("-inf")
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


if __name__ == "__main__":
    result = alpha_beta(root, 3, float("-inf"), float("inf"), True)
    print("Optimal value:", result)
