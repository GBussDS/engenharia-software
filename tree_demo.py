from tree_design import *

print("Demonstração TreeBuilder e State:\n")

builder = TreeBuilder()

step = 0
maxStep = 4
while builder.state is not None and step < maxStep:
    builder.runState()
    step+=1

print('#'*100)

print("Demonstração Node:\n")
root = builder.root

print("Valor entrando maior que o threshold fixo de 10:\n")
root.action(15)

print("\nValor entrando menor que o threshold fixo de 10:\n")
root.action(5)


print('#'*100)

print("Demonstração Iterador:\n")
iterator = PreOrderIterator(root)

for node in iterator:
    print(node.__class__.__name__)
    if isinstance(node, LeafNode):
        node.printValues()
    
print('#'*100)

print("Demonstração CountLeavesVisitor:\n")

countVisitor = CountLeavesVisitor()

root.accept(countVisitor)

print(f"Nós encontrados: {countVisitor.leafCount}")
