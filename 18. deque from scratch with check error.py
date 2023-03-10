import re
class Deque:
    def __init__(self):
        self.elements = []
        self.commands = []

    def push_front(self, data):
        self.elements.insert(0,data)
        self.commands.append('ok')
    def push_back(self,data):
        self.elements.append(data)
        self.commands.append('ok')
    def pop_front(self):
        if len(self.elements)!=0:
            a = self.elements.pop(0)
            self.commands.append(a)
        else:
            
            self.commands.append('error')
    def pop_back(self):
        if len(self.elements)!=0:
            a = self.elements.pop()
            self.commands.append(a)
        else:
            
            self.commands.append('error')
        
    def front(self):
        if len(self.elements)!=0:
            a = self.elements[0]
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
st = Deque()
a=True
while a:
    a = input()
    if a.startswith('push_back'):
        num = re.findall(r'-?\d+',a)[0]
        st.push_back(num)
    if a.startswith('push_front'):
        num = re.findall(r'-?\d+',a)[0]
        st.push_front(num)
    if a=='pop_front':
        st.pop_front()
    if a=='pop_back':
        st.pop_back()
    if a=='front':
        st.front()
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
