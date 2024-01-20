from core.entities import Word, WordDto
import json


def word_to_dto(word: Word) -> WordDto:
    try:
        return WordDto(
            english=word.english,
            type=word.type.name.lower(),
            vietnamese=word.vietnamese,
            pronunciation=word.pronunciation,
            meaning=word.meaning,
            examples=word.examples,
            tags=word.tags,
            synonyms=word.synonyms,
            antonyms=word.antonyms)
    except Exception as e:
        raise e

def dto_to_word(dto: WordDto) -> Word:
    try:
        return Word(
            english=dto.english,
            type=dto.type,
            # type=WordType[dto.type.upper()],
            vietnamese=dto.vietnamese,
            pronunciation=dto.pronunciation,
            meaning=dto.meaning,
            examples=dto.examples,
            tags=dto.tags,
            synonyms=dto.synonyms,
            antonyms=dto.antonyms)
    except Exception as e:
        raise e

def word_to_list(word: Word) -> list:
    try:
        return [
            word.id,
            word.english,
            word.type.name.lower(),
            word.vietnamese,
            word.pronunciation.encode('utf-8'),
            word.meaning,
            '\n'.join(word.examples),
            '\n'.join(word.tags),
            '\n'.join(word.synonyms),
            '\n'.join(word.antonyms),
            word.created_at,
            word.updated_at
        ]
    except Exception as e:
        raise e

def list_to_word(lst: list) -> Word:
    try:
        return Word(
            id=lst[0],
            english=lst[1],
            type=lst[2],
            vietnamese=lst[3],
            pronunciation=lst[4].decode('utf-8'),
            meaning=lst[5],
            examples=lst[6].split('\n'),
            tags=lst[7].split('\n'),
            synonyms=lst[8].split('\n'),
            antonyms=lst[9].split('\n'),
            created_at=lst[10],
            updated_at=lst[11]
            )
    except Exception as e:
        raise e
