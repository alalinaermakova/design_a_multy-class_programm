1. Describe the Problem
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
                                ┌────────────────────────────┐
                                │ Diary                      │
                                │                            │
                                │ - contents                 │
                                │ - add(contents)            │
                                │ - read_diary_entries()     │
                                └─────────────┬──────────────┘
                               /              │                \
                              /         owns a list of          \
                             /                ▼                  \ 
 ┌─────────────────────────┐     ┌─────────────────────────┐       ┌─────────────────────────┐
 │ Todos                   │     │ DiaryEntries            │       │ Contacts                │
 │                         │     │                         │       │                         │
 │  - title                │     │ - title                 │       │  - title                │
 │  - initialise(title)    │     │ - contents              │       │  - phone number         │
 │  - complete()           │     │                         │       │  - format()             │
 │                         │     │                         │       │                         │
 └─────────────────────────┘     └─────────────────────────┘       └─────────────────────────┘

    class Diary:

        def __init__(self):
            pass

        def add(self, entry):
            # Parameters:
            #   entry: an instance of DiaryEntry
            # Returns:
            #   Nothing
            # Side-effects:
            #   Adds the entry to the entries list
            pass

        def all():
            # Parameters:
            #   none
            # Returns:
            #   a list of all entries
            pass

        def count_words(self):
            # Returns:
            #   An integer representing the number of words in all diary entries
            # HINT:
            #   This method should make use of the `count_words` method on DiaryEntry.
            pass

        def reading_time(self, wpm):
            # Parameters:
            #   wpm: an integer representing the number of words the user can read
            #        per minute
            # Returns:
            #   An integer representing an estimate of the reading time in minutes
            #   if the user were to read all entries in the diary.
            pass

        def find_best_entry_for_reading_time(self, wpm, minutes):
            # Parameters:
            #   wpm:     an integer representing the number of words the user can
            #            read per minute
            #   minutes: an integer representing the number of minutes the user has
            #            to read
            # Returns:
            #   An instance of DiaryEntry representing the entry that is closest to,
            #   but not over, the length that the user could read in the minutes
            #   they have available given their reading speed.
            pass


    class DiaryEntries:

        # Public Properties:
        #   title: a string
        #   contents: a string

        def __init__(self, title, contents): # title, contents are strings
            # Side-effects:
            #   Sets the title and contents properties
            pass

    class Todo:
        # Public Properties:
        #   task: a string representing the task to be done
        #   complete: a boolean representing whether the task is complete

        def __init__(self, task):
            # Parameters:
            #   task: a string representing the task to be done
            # Side-effects:
            #   Sets the task property
            #   Sets the complete property to False
            pass

        def mark_complete(self):
            # Returns:
            #   Nothing
            # Side-effects:
            #   Sets the complete property to True
            pass

    class Contacts:
        # Public Properties:
        #   phone number: a string representing the phone number
        #   name: a string representing the name
        pass

        def __init__(self, name, tel):
            # Parameters:
            #   name: a string representing the name
            #   tel: a string representing the phone number
            # Side-effects:
            #   Sets the name and phone property
            pass
        
        def format():
            # Returns:
            #   formatted string as "Name's tel: 88890000000"
            pass

3. Examples as Integration Tests

DiaryEntries

"""
Given a title with contents as a string
We see title and contents reflected in the title property
"""

diary_entries = DiaryEntries("Title", "Content of diary")
diary_entries.title ==> "Title"
diary_entries.contents ==> "Content of diary"

Todo

"""
Given one task as a string
We see title reflected in task property
"""

todo = Todo("Do tests")
todo.task ==> "Do tests"

"""
Given one task as a string
We see status reflected in completed property
"""


todo = Todo("Do tests")
todo.completed ==> False

Contacts

"""
Given a name and phone number as a string
We see name and phone num reflected in name and tel property
"""

contact = Contacts("Alina", "0777777777")
assert contact.name ==> "Alina"

"""
Given a name and phone number as a string
We see phone num reflected in name and tel property
"""

contact = Contacts("Alina", "0777777777")
assert contact.tel ==> "0777777777"

Diary

"""
Initially, has an empty list of entries
"""

diary = Diary()
diary.all() == []

"""
Given I add two diary entries
I see them back in the list
"""

diary = Diary()
entry_1 = DiaryEntry("My title 1", "My contents 1")
entry_2 = DiaryEntry("My title 2", "My contents 2")
diary.add(entry_1)
diary.add(entry_2)
assert diary.all() == [entry_1, entry_2]

"""
Given I add one diary entry and one todo task
I see them back in the list
"""

diary = Diary()
entry_1 = DiaryEntries("My title 1", "My contents 1")
todo_1 = Todo("Do tests")
diary.add(entry_1)
diary.add(todo_1)
diary.all() ==> [entry_1, todo_1]

"""
Given I add one diary entry, one todo task, one contact
I see them back in the list
"""

diary = Diary()
entry_1 = DiaryEntries("My title 1", "My contents 1")
todo_1 = Todo("Do tests")
contact_1 = Contacts("Alina", "07777777777")
diary.add(entry_1)
diary.add(todo_1)
diary.add(contact_1)
diary.all() ==> [entry_1, todo_1, contact_1]