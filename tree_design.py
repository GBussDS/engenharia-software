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

class TreeBuilder():
    def __init__(self):
        self.currentNode = None
        self.state = None
        self.root = None
        
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