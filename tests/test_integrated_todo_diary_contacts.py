from lib.diary import Diary
from lib.diary_entries import DiaryEntries
from lib.todo import Todo
from lib.contacts import Contacts
import pytest

"""
Given I add two diary entries
I see them back in the list
"""

def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "My contents 1")
    entry_2 = DiaryEntries("My title 2", "My contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given I add one diary entry and one todo task
I see them back in the list
"""

def test_adds_and_lists_diary_entry_and_todo_task():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "My contents 1")
    todo_1 = Todo("Do tests")
    diary.add(entry_1)
    diary.add(todo_1)
    assert diary.all() == [entry_1, todo_1]

"""
Given I add one diary entry, one todo task, one contact
I see them back in the list
"""

def test_adds_and_lists_diary_entry_todo_and_contacts():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "My contents 1")
    todo_1 = Todo("Do tests")
    contact_1 = Contacts("Alina", "88890000000")
    diary.add(entry_1)
    diary.add(todo_1)
    diary.add(contact_1)
    assert diary.all() == [entry_1, todo_1, contact_1]

"""
Given I add two diary entries
And I call #count words
I get the sum of all words of the contents in the diary entries
""" 

def test_counts_of_all_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "One two")
    entry_2 = DiaryEntries("My title 2", "Three four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

"""
Given I add two diary entries, one long one short
And I call #find_best_entry_for_reading_time
With wpm and minutes that means I can only read the short one
Then #find_best_entry_for_reading_time returns the shortest one
"""

def test_find_best_entry_for_reading_time_returns_entry_that_fits_time():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "One two three")
    entry_2 = DiaryEntries("My title 2", "One two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can read that enrty
Then #find_best_entry_for_reading_time returns that entry
"""

def test_find_best_entry_for_reading_time_returns_singlr_entry_that_fits_time():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "One two three")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I cannot read that enrty
Then #find_best_entry_for_reading_time returns None
"""

def test_find_best_entry_for_reading_time_returns_none_if_single_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "One two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None


"""
Given I add two diary entries
And I call #find_best_entry_for_reading_time
With a wpm amd minutes that means I could read both
Then #find_best_entry_for_reading_time return the longer one
"""

def test_find_best_entry_for_reading_time_return_the_longest():
    diary = Diary()
    entry_1 = DiaryEntries("My title 1", "One two three")
    entry_2 = DiaryEntries("My title 2", "One two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2