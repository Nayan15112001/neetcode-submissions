class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def remove(self,lru):
            prev_node = lru.prev
            next_node = lru.next

            prev_node.next = next_node
            next_node.prev = prev_node

    def add(self,key,value):
        new_node = self.Node(key,value)
        prev_node = self.right.prev
        prev_node.next = new_node
        self.right.prev = prev_node.next
        new_node.prev = prev_node
        new_node.next = self.right
        self.hmap[key] = new_node


    def __init__(self, capacity: int):
        self.hmap = {}
        self.size = 0
        self.node = self.Node(0,0)
        self.left = self.Node(0,0)
        self.right = self.Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
  
    def get(self, key: int) -> int:
        if key in self.hmap:
            # remove from least used position  
            new_node = self.hmap[key]
            prev_node = new_node.prev
            next_node = new_node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            # add to the most used position
            self.add(key,new_node.val)

            return self.hmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            old_node = self.hmap[key]
            old_node_prev = old_node.prev
            old_node_next = old_node.next
            old_node_prev.next = old_node_next
            old_node_next.prev = old_node_prev
            self.add(key,value)

 
        else:
            if self.size == self.capacity:
                lru = self.left.next
                del(self.hmap[lru.key])
                self.remove(lru)
                self.add(key,value)

            else:
                self.add(key,value)
                self.size+=1


        print(self.hmap)
