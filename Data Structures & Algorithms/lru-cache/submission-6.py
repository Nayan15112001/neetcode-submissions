class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.val  = val
            self.key = key
            self.prev = None
            self.next = None


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.left = self.Node(0,0)
        self.right = self.Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.hmap = {}
    
    def remove(self,node):
        prev_n = node.prev
        next_n = node.next
        prev_n.next = next_n
        next_n.prev= prev_n
        
    def add(self,node):
        prev_n = self.right.prev
        prev_n.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev_n

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        new_node = self.Node(key,value)
        if key in self.hmap:
            old_node = self.hmap[key]
            self.remove(old_node)
            del(self.hmap[key])
            self.add(new_node)
            self.hmap[key] = new_node
        else:
            if self.size == self.capacity:
                old_node = self.left.next
                old_node_key = old_node.key
                self.remove(old_node)
                del(self.hmap[old_node_key])
                self.add(new_node)
                self.hmap[key] = new_node
            else:
                self.add(new_node)
                self.hmap[key] = new_node
                self.size+=1




