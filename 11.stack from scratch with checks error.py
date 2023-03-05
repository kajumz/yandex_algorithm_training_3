import re
class Stack:
    def __init__(self):
        self.elements = []
        self.commands = []

    def push(self, data):
        self.elements.append(data)
        self.commands.append('ok')
        

    def pop(self):
        if len(self.elements)!=0:
            a = self.elements.pop()
            self.commands.append(a)
        else:
            
            self.commands.append('error')
        
    def back(self):
        if len(self.elements)!=0:
            a = self.elements[-1]
            self.commands.append(a)
        else:
            
            self.commands.append('error')
            
    def size(self):
        a=len(self.elements)
        self.commands.append(a)
    def clear(self):
        self.elements.clear()
        self.commands.append('ok')
    def exit(self):
        self.commands.append('bye')
    def show(self):
        for i in self.commands:
            print(i)
st = Stack()
a=True
while a:
    a = input()
    if a.startswith('push'):
        num = re.findall(r'-?\d+',a)[0]
        st.push(num)
    if a=='back':
        st.back()
    if a=='size':
        st.size()
    if a=='clear':
        st.clear()
    if a=='pop':
        st.pop()
    if a=='exit':
        st.exit()
        a=False
st.show()
