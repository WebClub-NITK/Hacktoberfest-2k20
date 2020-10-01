
"""
Push O(1) :Push Element To Top
Pop O(1) : POP Element From Top
get_max O(1) : Returns max Element from the stack
Peek O(1): Returns Top Element
Size O(1) : Returns Size of the stack
"""
class Stack:
    def __init__(self):
        self.items = []
        self.itemmax=[]
        self.top=0

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if self.items[self.top-1] < item or self.top==0:
            self.itemmax.append(item)
        else:
            self.itemmax.append(self.items[self.top-1])
        self.top=self.top+1
    def pop(self):
        self.top=self.top-1
        self.itemmax.pop()
        return self.items.pop()

    def peek(self):
        return self.items[self.top-1]

    def size(self):
        return len(self.items)
    def get_max(self):
        return self.itemmax[self.size()-1]

if __name__ == "__main__":
    stack=Stack()
    stack.push(10)
    print("Pushed Element :",stack.peek())
    print("Max Element :", stack.get_max())
    
    stack.push(2)
    print("Pushed Element :",stack.peek())
    print("Max Element :", stack.get_max())
    
    stack.push(50)
    print("Pushed Element :",stack.peek())
    print("Max Element :", stack.get_max())
    stack.push(45)
    print("Pushed Element :",stack.peek())
    print("Max Element :", stack.get_max())
    stack.push(30)
    print("Pushed Element :",stack.peek())
    print("Max Element :", stack.get_max())
    print("==========================")
    while stack.size()!=0:
        print("Max Element :", stack.get_max())
        print("Poped Element :",stack.pop())
       

    
