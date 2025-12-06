from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def action(self, value: int):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass

class DecisionNode(Node):
    def __init__(self, threshold, leftNode:Node = None, rightNode:Node = None):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.threshold = threshold

    def action(self, value: int):
        if value > self.threshold:
            print("DecisionNode: maior que threshold, passou para a esquerda.")
            return self.leftNode.action(value)
        else:
            print("DecisionNode: menor que threshold, passou para a direita.")
            return self.rightNode.action(value)
    
    def accept(self, visitor):
        visitor.visitDecision(self)

class LeafNode(Node):
    def __init__(self):
        self.valueList = []
    
    def action(self, value: int):
        print("LeafNode: Adiciona o valor a sua lista.")
        self.valueList.append(value)
    
    def accept(self, visitor):
        visitor.visitLeaf(self)

    def printValues(self):
        print(f"Valores no nó: {self.valueList}")
        
class State(ABC):
    @abstractmethod
    def process(self, builder):
        pass

class SplittingState(State):
    def process(self, builder):
        if builder.root == None:
            print("SplittingState: criando nó raiz.")
            builder.root = DecisionNode(10)
            builder.currentNode = builder.root

            #Checa se deve parar voltando pro stopping state
            builder.state = StoppingState()
        else:
            print("SplittingState: dividindo o nó atual em dois.")
            builder.currentNode.leftNode = LeafNode()
            builder.currentNode.rightNode = LeafNode()

            #Checa se deve parar voltando pro stopping state
            builder.state = StoppingState()

class PruningState(State):
    def process(self, builder):
        print("Prunning State: poda.")
        #No caso como é mock não faz
        builder.state = None
    
class StoppingState(State):
    def process(self, builder):
        print("Stopping State: verifica se para.")
        criterioParadaAtingido = False

        if criterioParadaAtingido:
            print("Stopping State: procede pra pruning.")
            builder.state = PruningState()
        else:
            print("Stopping State: volta pro SplittingState.")
            builder.state = SplittingState()

class TreeBuilder():
    def __init__(self):
        self.currentNode = None
        self.state = SplittingState()
        self.root = None
    
    def runState(self):
        if self.state:
            self.state.process(self)

class PreOrderIterator():
    def __init__(self, root: Node):
        self.stack = []
        if root:
            self.stack.append(root)

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration

        currentNode = self.stack.pop()

        if isinstance(currentNode, DecisionNode):
            if currentNode.leftNode:
                self.stack.append(currentNode.leftNode)
            if currentNode.rightNode:
                self.stack.append(currentNode.rightNode)
            
        return currentNode

class Visitor(ABC):
    @abstractmethod
    def visitDecision(self, node: Node):
        pass

    def visitLeaf(self, node: Node):
        pass

class DepthVisitor(Visitor):
    def __init__(self, depth: int):
        self.currentDepth = 0
        self.depth = depth
        self.matchingNodes = []

    def visitDecision(self, node: DecisionNode):
        if self.depth == self.currentDepth:
            print("DepthVisitor: nó encontrado na profundidade.")
            self.matchingNodes.append(node)
            return
        
        self.currentDepth += 1

        if node.leftNode:
            node.leftNode.accept(self)
        if node.rightNode:
            node.rightNode.accept(self)

        self.currentDepth -= 1

    def visitLeaf(self, node: LeafNode):
        if self.currentDepth == self.depth:
            print("DepthVisitor: folha encontrada na profundidade.")
            self.matchingNodes.append(node)


class CountLeavesVisitor(Visitor):
    def __init__(self):
        self.leafCount = 0

    def visitDecision(self, node):
        if node.leftNode:
            node.leftNode.accept(self)
        if node.rightNode:
            node.rightNode.accept(self)

    def visitLeaf(self, node):
        print("CountLeavesVisitor: contando folha.")
        self.leafCount += 1

        