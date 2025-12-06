from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def action(self, value):
        pass

class DecisionNode(Node):
    def __init__(self, threshold, leftNode=None, rightNode=None):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.threshold = threshold

    def action(self, value):
        print("Decide para qual node passar e passa.")
        if value > self.threshold:
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
        
def State(ABC):
    @abstractmethod
    def process(self, builder):
        pass

class SplittingState(State):
    def processs(self, builder):
        if builder.root == None:
            print("Cria nó raiz caso não tenha.")
            builder.root = DecisionNode(10)
            builder.currentNode = builder.root
        else:
            print("Divide o nó atual em dois.")
            builder.currentNode.leftNode = LeafNode()
            builder.currentNode.rightNode = LeafNode()

            print("Checa se deve parar voltando pro stopping state:")
            builder.state = StoppingState()

class PruningState(State):
    def process(self, builder):
        print("Faz poda.")
        #No caso como é mock não faz
        builder.state = None
    
class StoppingState(State):
    def process(self, builder):
        print("Verifica se para.")
        criterioParadaAtingido = False

        if criterioParadaAtingido:
            print("Procede pra pruning.")
            builder.state = PruningState()
        else:
            print("Volta a dividir.")
            builder.state = SplittingState()

class TreeBuilder():
    def __init__(self):
        self.currentNode = None
        self.state = None
        self.root = None
    
    def runState(self):
        if self.state:
            self.state.process(self)

class PreOrderIterator():
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration

        currentNode = self.stach.pop()

        if isinstance(currentNode, DecisionNode):
            if currentNode.leftNode:
                self.stack.append(currentNode.rightNode)
            if currentNode.rightNode:
                self.stack.append(currentNode.rightNode)
            
        return currentNode

class Visitor(ABC):
    @abstractmethod
    def visit(self):
        pass

class DepthVisitor(Visitor):
    def __init__(self, depth):
        self.currentDepth = 0
        self.depth = depth

    def visit(self, node, currentDepth):
        if self.depth == currentDepth:
            return node, currentDepth
        
        if isinstance(node, DecisionNode):
            if node.leftNode:
                return self.visit(node.leftNode, currentDepth + 1)
            if node.rightNode:
                return self.visit(node.RightNode, currentDepth + 1)

        return None, 0

class CountLeavesVisitor(Visitor):
    def __init__(self):
        self.leafCount = 0

    def visit(self, node):
        self.leafCount += 1

        if isinstance(node, DecisionNode):
            if node.leftNode:
                self.visit(node.leftNode)
            if node.rightNode:
                self.visit(node.RightNode)
    

                