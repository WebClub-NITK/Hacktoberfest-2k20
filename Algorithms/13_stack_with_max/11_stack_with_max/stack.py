
"""
Push O(1) :Push Element To Top
Pop O(1) : POP Element From Top
get_max O(n) : Returns max Element from the stack
Peek O(n): Returns Top Element
Size O(1) : Returns Size of the stack
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def get_max(self):
        return max(self.items)

if __name__ == "__main__":
    stack=Stack()
    stack.push(5)
    stack.push(10)
    stack.push(50)
    stack.push(59)
    stack.push(30)
    
    print("Max Element :", stack.get_max())

    while stack.size()!=0:
        print(stack.pop())
