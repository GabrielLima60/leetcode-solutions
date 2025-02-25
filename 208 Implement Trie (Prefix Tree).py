'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

class Trie:

    def __init__(self):
        self.final = False
        self.branches = {}

    def insert(self, word: str) -> None:
        if word[0] not in self.branches:
            self.branches[word[0]] = Trie()

        if len(word) > 1:
            self.branches[word[0]].insert(word[1:])
        else:
            self.branches[word[0]].final = True

    def search(self, word: str) -> bool:
        if not word:
            if self.final:
                return True
            return False

        elif word[0] in self.branches:
            return self.branches[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
            
        elif prefix[0] in self.branches:
            return self.branches[prefix[0]].startsWith(prefix[1:])
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
