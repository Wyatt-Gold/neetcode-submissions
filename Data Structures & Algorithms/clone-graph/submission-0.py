class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = {node: Node(node.val)}
        queue = collections.deque([node])

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                hashmap[curr_node].neighbors.append(hashmap[neighbor])

        return hashmap[node]