# 实现前缀树的初始化、插入、搜索
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char=None
        self.leaf=dict()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word: 
            self.leaf['']=None
            return
        elif word[0] not in self.leaf:
            self.leaf[word[0]]=Trie()
        self.leaf[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word: 
            return '' in self.leaf
        elif word[0] in self.leaf:
            return self.leaf[word[0]].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix: return True
        elif prefix[0] in self.leaf:
            return self.leaf[prefix[0]].startsWith(prefix[1:])
        return False
