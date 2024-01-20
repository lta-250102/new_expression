from datetime import datetime
from pydantic import BaseModel
from core.types import WordType
import uuid


class BaseEntity:
    id: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = None

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        self.updated_at = kwargs.get('updated_at', None)

    def dict(self):
        return self.__dict__

class Word(BaseEntity):
    english: str
    type: WordType
    vietnamese: str
    pronunciation: str
    meaning: str = None
    examples: list[str] = []
    tags: list[str] = []
    synonyms: list[str] = []
    antonyms: list[str] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.english = kwargs.get('english')
        try:
            self.type = WordType[kwargs.get('type').upper()]
        except:
            self.type = WordType.UNKNOWN
        self.vietnamese = kwargs.get('vietnamese')
        self.pronunciation = kwargs.get('pronunciation')
        self.meaning = kwargs.get('meaning', None)
        self.examples = kwargs.get('examples', [])
        self.tags = kwargs.get('tags', [])
        self.synonyms = kwargs.get('synonyms', [])
        self.antonyms = kwargs.get('antonyms', [])

    def dict(self):
        dict = self.__dict__
        dict['type'] = self.type.name.lower()
        return dict
    
class WordDto(BaseModel):
    english: str
    type: str
    vietnamese: str
    pronunciation: str
    meaning: str
    examples: list[str] = []
    tags: list[str] = []
    synonyms: list[str] = []
    antonyms: list[str] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.english = kwargs.get('english')
        self.type = kwargs.get('type')
        self.vietnamese = kwargs.get('vietnamese')
        self.pronunciation = kwargs.get('pronunciation')
        self.meaning = kwargs.get('meaning', None)
        self.examples = kwargs.get('examples', [])
        self.tags = kwargs.get('tags', [])
        self.synonyms = kwargs.get('synonyms', [])
        self.antonyms = kwargs.get('antonyms', [])
