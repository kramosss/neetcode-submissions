class PrefixTree:

    def __init__(self):
        self._data = []
        

    def insert(self, word: str) -> None:
        self._data.append(word)


    def search(self, word: str) -> bool:
        if word in self._data:
            return True 
        else:
            return False 
        

    def startsWith(self, prefix: str) -> bool:
        for i in range(len(self._data)):
            if self._data[i][:len(prefix)] == prefix:
                return True 
        return False 
        
        