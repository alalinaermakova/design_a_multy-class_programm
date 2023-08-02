class Todo:
    def __init__(self, task):
        self.task = task
        self.completed = False
        pass

    def mark_complete(self):
        if self.completed == False:
            self.completed = True
        pass