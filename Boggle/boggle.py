class Trie():
    def __init__(self, fileName):
        self.trie = {}
        f = open(fileName,"r");
        lines = f.readlines();
        for i in lines:
            self.addWord(i.rstrip(),self.trie)

    def addWord(self, word, indict):
        word = word.upper()
        if len(word) == 0:
            indict[None] = None
        else:
            topLet = word[0]
            if topLet not in indict:
                indict[topLet] = {}
            self.addWord(word[1:],indict[topLet])

    def isWord(self, inword):
        inword = inword.upper()
        current = self.trie
        for char in inword:
            if char not in current:
                return False
            else:
                current = current[char]
        if None in current:
            return True
        return False

    def inTrie(self, inword):
        inword = inword.upper()
        current = self.trie
        for char in inword:
            if char not in current:
                return False
            else:
                current = current[char]
        return True

class Letter():
    def __init__(self, value):
        self.value = value
        self.neighbors = set()

    def addNeighbor(self, nnode):
        self.neighbors.add(nnode)

class BoggleBoard():
    def __init__(self):
        self.nodelist = {}
        self.numnodes = 0
        self.dictionary = Trie('words_alpha.txt')
    
    def buildBoard(self,inMat):
        for rindex, r in enumerate(inMat):
            for cindex, c in enumerate(r):
                self.addNode((rindex,cindex),c)
        for loc in self.nodelist:
            r, c = loc
            neigh = [(r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)]
            for l in neigh:
                if l[0] >=0 and l[0] < 4 and l[1] >=0 and l[1] < 4:
                    self.addNeighbor(loc,l)


    def addNode(self, loc, value):
        newLet = Letter(value)
        self.numnodes += 1
        self.nodelist[loc] = newLet

    def addNeighbor(self, locA, locB):
        for i in [locA, locB]:
            if i not in self.nodelist:
                return "Error no node"
        self.nodelist[locA].addNeighbor(self.nodelist[locB])
        self.nodelist[locB].addNeighbor(self.nodelist[locA])
    
    def findWords(self, innode):
        self.visited.add(innode)
        self.currentword += innode.value
        if self.dictionary.isWord(self.currentword):
            self.words.append(self.currentword)
        for n in innode.neighbors:
            if n not in self.visited and self.dictionary.inTrie(self.currentword+n.value):
                self.findWords(n)
        self.currentword = self.currentword[:-1]

    def solveBoard(self):
        print("solving board")
        self.words = []
        self.currentword = ""
        self.visited = set()
        for loc in self.nodelist:
            self.visited = set()
            self.currentword = ""
            self.findWords(self.nodelist[loc])
        #self.findWords(self.nodelist[(0,1)])
        #self.currentword = ""
        #self.visited = set()
        #self.findWords(self.nodelist[(0,0)])
        print("words in board: {}".format(self.words))

bb = [['Y','L','T','V'],['O','N','I','E'],['B','A','G','R'],['L','H','M','O']]
newboard = BoggleBoard()
newboard.buildBoard(bb)
newboard.solveBoard()
