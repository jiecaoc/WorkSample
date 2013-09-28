from sets import Set
from StringIO import StringIO
class Example:
    """
    class of Example
    """
    def __init__(self, att_pairs):
        self.keyValue = {}
        self.keys = []
        for (k, v) in att_pairs:
            self.keyValue[k] = v
            self.keys.append(k)

    def getValue(self, k):
        """
        given a key, return value
        """
        return self.keyValue[k]

    def getKeyList(self):
        """
        return the list of keys 
        """
        return self.keys 
        
    def __str__(self):
        return self.keyValue.__str__()
        

class Attribute:
    """
    class of attribute,
    example:
       att = attribute("Name")
       att.addValue("Jiecao Chen")
       att.addValue("XYZ")
       print att.key()
       print att.values()
    """
    def __init__(self, keyString):
        self.valueList = []
        self.keyString = keyString

    def addValue(self, v):
        self.valueList.append(v)

    def key(self):
        return self.keyString

    def values(self):
        """
        return the list of values
        """
        return self.valueList


    


class Tree:
    """
    provide the structure support of a Decision Tree
    """
    def __init__(self, att):
        self.attribute = att
        self.Children = {}

    def addChild(self, v, cd):
        self.Children[v] = cd
    
    def getAttr(self):
        return self.attribute.key()
    
    def getChildrenList(self):
        return self.Children.items()
    def getClassValue(self):
        if self.attribute.key() == 'classification':
            return self.attribute.values()[0]
        else:
            return 'none'
    def getChildren(self):
        return self.Children

    def __str__(self):
        #output = StringIO()
        #output = printTree(self, output)
        #return output.getvalue()
        return self.attribute.key()
    
    def makeDecision(self, eg):
        return decide(self, eg)
        

def decide(tree, eg):
    """
    recursively make decision using the tree
    """
    if tree.getClassValue() != 'none':
        return tree.getClassValue()
    key = tree.getAttr()
    v = eg.getValue(key)
    return decide(tree.getChildren()[v], eg)
