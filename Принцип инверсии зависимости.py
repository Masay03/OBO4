# class Book():
#     def read(self):
#         print('Чтение книги')
#
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()

from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print('Чтение книги')

class AudioBook(StorySource):
    def get_story(self):
        print('Чтение аудиокниги')

class StoryReader:
    def __init__(self, story_source: StorySource):
        self.story_source = story_source
    def tell_story(self):
        self.story_source.get_story()

book = Book()
reader = StoryReader(book)

readerBook = StoryReader(Book())

readerAudioBook = StoryReader(AudioBook())

readerBook.tell_story()
readerAudioBook.tell_story()