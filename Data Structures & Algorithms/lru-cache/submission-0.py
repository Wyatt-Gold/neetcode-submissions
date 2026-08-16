class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = None, None

    def get(self, key: int) -> int:
        curr_node = self.cache.get(key)

        if not curr_node:
            return -1

        # Already most recently used
        if curr_node == self.head:
            return curr_node.val

        # Remove curr_node from its current position
        if curr_node == self.tail:
            self.tail = curr_node.prev
            self.tail.next = None
        else:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev

        # Move curr_node to the head
        curr_node.prev = None
        curr_node.next = self.head
        self.head.prev = curr_node
        self.head = curr_node

        return curr_node.val


    def put(self, key: int, value: int) -> None:
        curr_node = self.cache.get(key)

        # Key already exists
        if curr_node:
            curr_node.val = value
            self.get(key)  # Move to most recently used
            return

        # Create new node
        curr_node = Node(key, value)

        if self.head is None:
            self.head = self.tail = curr_node
        else:
            curr_node.next = self.head
            self.head.prev = curr_node
            self.head = curr_node

        self.cache[key] = curr_node
        self.capacity -= 1

        # Remove least recently used
        if self.capacity == -1:
            old_tail = self.tail

            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = old_tail.prev
                self.tail.next = None

            del self.cache[old_tail.key]
            self.capacity = 0