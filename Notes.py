from abc import ABC,abstractmethod
from datetime import datetime


class Field(ABC):
     @abstractmethod
     def __str__(self):
          pass

class Note_id(Field): 
    def __init__(self, note_id) -> None:
        self._id = None
        self.set_id = note_id
     
    @property
    def get_id(self): 
        return self._id
     
    @get_id.setter
    def set_id(self,value): 
        if type(value) is int:
            self._id = value
        else:
            print('Incrorrect ID')               

    def __str__(self):
        return f'{self.get_id}'
     

class Title(Field): 
    def __init__(self, title):
        self._title = None
        self.set_title = title
        
    @property
    def get_title(self):
        return self._title
    
    @get_title.setter
    def set_title(self, new_title: str):
        if new_title == None: 
            raise ValueError('Title None is wrong!') 
        if len(new_title) < 3 or len(new_title) > 10: 
            raise ValueError('Title between 3 and 10 characters long is expected!')
        else:
            self._title = new_title   
             
    def __str__(self):
        return f'{self.get_title}'



class Note(Field):
    def __init__(self, note):
        self._note = None
        self.set_note = note
        
    @property 
    def get_note(self): 
        return self._note
    
    @get_note.setter
    def set_note(self,note): 
        if note == None: 
            raise ValueError('Note None is wrong!')     
        elif len(note) < 3: 
            raise ValueError('Note of 3 or more characters is expected')
        else:
            self._note = note
            
    def __str__(self):
        return f'{self.get_note}'
    
class Tag(Field): 
    def __init__(self, tag):
        self._tag = None
        self.set_tag = tag
        
    @property 
    def get_tag(self): 
        return self._tag
    
    @get_tag.setter 
    def set_tag(self, tag: str):
        tag = tag.split()
        if len(tag) == 0 or len(tag) > 1:
            raise ValueError(f'Tag is wrong, must be word from 3 to 10 characters')
        elif len(tag[0]) < 3 or len(tag[0]) > 10: 
            raise ValueError(f'Tag {tag[0]} has {len(tag[0])} Tag between 3 and 10 characters long is expected!')
        else:
            self._tag = tag[0] 
            
    def __str__(self):
        return f'{self.get_tag}'

class AdditionDate(Field): 
    def __init__(self, date):
        self._date = None
        if date != None:
            self._date = date
        
    @property
    def get_date(self): 
        return str(self._date)
    
    @get_date.setter 
    def set_date(self,date):
        self._date = date
    
    def __str__(self):
        return f'{str(self.get_date)}'


class NotesRecord:    
    def __init__(self, id, title = None, note = None, tag = None):
        self.note_id = Note_id(id)
        self.title = Title(title)
        self.note = Note(note)
        self.tag = []
        if tag != None:
            self.tag.append(Tag(tag))
        self.addition_date = AdditionDate(datetime.now().date())

    def __str__(self):
        return f'ID: {str(self.note_id)}\nTitle: {self.title}\nNote: {self.note}\nTags: {" ".join([str(item) for item in self.tag])} \nDate addition: {str(self.addition_date)} '    

