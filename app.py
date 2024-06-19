class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return ("Task ID: {}, Title: {}, Description: {}, Priority: {}, Status: {}"
                .format(self.id,self.title, self.description,self.priority,self.status))

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.valid_priorities = {'High', 'Medium', 'Low'}
        self.valid_statuses = {'Pending', 'In Progress', 'Completed'}

    def add_task(self, title, description, priority, status):
        if priority not in self.valid_priorities:
            print("Invalid priority. Valid options are: High, Medium, Low.")
            return
        if status not in self.valid_statuses:
            print("Invalid status. Valid options are: Pending, In Progress, Completed.")
            return

        task = Task(self.next_id, title, description, priority, status)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{title}' added successfully with ID {task.id}.")

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        task = self.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        if priority and priority not in self.valid_priorities:
            print("Invalid priority. Valid options are: High, Medium, Low.")
            return
        if status and status not in self.valid_statuses:
            print("Invalid status. Valid options are: Pending, In Progress, Completed.")
            return

        if title:
            task.title = title
        if description:
            task.description = description
        if priority:
            task.priority = priority
        if status:
            task.status = status
        print(f"Task with ID {task_id} updated successfully.")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        if priority not in self.valid_priorities:
            print("Invalid priority. Valid options are: High, Medium, Low.")
            return

        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks found with priority '{priority}'.")
        for task in filtered_tasks:
            print(task)

if __name__ == "__main__":
    while True:
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")

        choice = input("Enter your choice (1-6)")