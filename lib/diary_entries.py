class DiaryEntries:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        
    def count_words(self):
        word = self.contents.split()
        return len(word)