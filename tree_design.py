from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def action(self):
        pass

class DecisionNode(Node):
    def __init__(self, leftNode, rightNode):
        self.leftNode = leftNode
        self.rightNode = rightNode

    def action(self, value):
        print("Decide para qual node passar e passa.")
        if value%2 == 1:
            return self.leftNode.action(value)
        else:
            return self.rightNode.action(value)

class LeafNode(Node):
    def __init__(self):
        self.valueList = []
    
    def action(self, value):
        print("Adiciona o valor a sua lista.")
        self.valueList.append(value)
    
    def printValues(self):
        print(f"Valores no nó: {self.valueList}")
        