from lib.todo import Todo

"""
Given one task as a string
We see title reflected in task property
"""

def test_todo_task_entry():
    todo = Todo("Do tests")
    assert todo.task == "Do tests"

"""
Given one task as a string
We see status reflected in completed property
"""

def test_todo_task_entry():
    todo = Todo("Do tests")
    assert todo.completed == False

"""
Given one task as a string
We call #mark_complete and recieve True
"""

def test_todo_task_entry():
    todo = Todo("Do tests")
    todo.mark_complete()
    assert todo.completed == True