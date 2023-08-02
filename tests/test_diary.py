from lib.diary import *
import pytest

"""
Initially, has an empty list of entries
Should rise an error if list is empty
"""

def test_raise_an_error_if_list_is_empty():
    diary = Diary()
    with pytest.raises(Exception) as error:
        diary.all()
    assert str(error.value) == "No entries added yet"

"""
Initially, word count is zero
"""

def test_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0

def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as error:
        diary.reading_time(2)
    assert str(error.value) == "No entries added yet"

"""
Initially, #find_best_entry_for_reading_time should rise an error
"""

def test_initially_find_best_entry_for_reading_time_raises_an_error():
    diary = Diary()
    with pytest.raises(Exception) as error:
        diary.find_best_entry_for_reading_time(2, 2)
    assert str(error.value) == "No entries added yet"