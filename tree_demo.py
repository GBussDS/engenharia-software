from tree_design import *

print("Criação da árvore:")
builder = TreeBuilder()

step = 0
maxStep = 4
while builder.state is not None and step < maxStep:
    builder.runState()
    step+=1

print('#'*100)



