from tree_design import *

print("Criação da árvore:")
builder = TreeBuilder()

step = 0
maxStep = 4
while builder.state is not None and step < maxStep:
    builder.runState()
    step+=1

print('#'*100)

root = builder.root

print("\nValor entrando maior que o threshold fixo de 10:\n")
root.action(15)

print("\nValor entrando menor que o threshold fixo de 10:\n")
root.action(5)

print('#'*100)



