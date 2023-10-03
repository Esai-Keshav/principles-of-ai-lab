class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, relation, node):
        self.edges.append((relation, node))

    def __str__(self):
        return self.name


class SemanticNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, name):
        node = Node(name)
        self.nodes.append(node)
        return node

    def __str__(self):
        result = "Semantic Network:\n"
        for node in self.nodes:
            result += f"{node} has relations:\n"
            for relation, related_node in node.edges:
                result += f"  - {relation}: {related_node}\n"
        return result


# Create a semantic network
semantic_net = SemanticNetwork()

while True:
    print("1. Add Node")
    print("2. Add Relationship")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        node_name = input("Enter node name: ")
        semantic_net.add_node(node_name)
        print(f"Node '{node_name}' added.")
    elif choice == "2":
        node_name = input("Enter node name: ")
        relation = input("Enter relation: ")
        related_node_name = input("Enter related node name: ")

        # Find the nodes with the specified names
        node = next((n for n in semantic_net.nodes if n.name == node_name), None)
        related_node = next(
            (n for n in semantic_net.nodes if n.name == related_node_name), None
        )

        if node and related_node:
            node.add_edge(relation, related_node)
            print(
                f"Relationship added: {node_name} -> {relation} -> {related_node_name}"
            )
        else:
            print("One or both nodes not found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

# Display the semantic network
print(semantic_net)
