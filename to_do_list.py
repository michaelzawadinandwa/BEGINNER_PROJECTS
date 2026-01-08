class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found")

    def update(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
        else:
            print("Task not found")
