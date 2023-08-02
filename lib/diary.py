class Diary:

    def __init__(self):
        self.my_diary = []

    def add(self, entry):
        self.my_diary.append(entry)

    def all(self):
        if self.my_diary == []:
            raise Exception("No entries added yet")
        else:
            return self.my_diary

    def count_words(self):
        word_counts = sum([entry.count_words() for entry in self.my_diary])
        return word_counts

    def reading_time(self, wpm):
        if self.my_diary == []:
            raise Exception("No entries added yet")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self.my_diary == []:
            raise Exception("No entries added yet")
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0

        for entry in self.my_diary:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable