from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for name_t in self.tasks:
            if task_name == name_t.name:
                name_t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for pos, tasks in enumerate(self.tasks):
            if tasks.completed:
                count += 1
                del self.tasks[pos]

        return f"Cleared {count} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for task in self.tasks:
            result += f"\n{task.details()}"
        return result
