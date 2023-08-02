from lib.diary_entries import DiaryEntries

"""
Given a title with contents
We see title reflected in the title property
"""
def test_diary_entries_title():
    diary_entries = DiaryEntries("Title", "Content of diary")
    assert diary_entries.title == "Title"

"""
Given a title with contents
We see title reflected in the contents property
"""
def test_diary_entries_contents():
    diary_entries = DiaryEntries("Title", "Content of diary")
    assert diary_entries.contents == "Content of diary"
