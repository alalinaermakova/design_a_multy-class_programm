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