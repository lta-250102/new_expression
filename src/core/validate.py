from core.entities import WordDto

def validate_word_dto(word_dto: WordDto):
    if not word_dto.english:
        raise ValueError("English is required")
    if not word_dto.vietnamese:
        raise ValueError("Vietnamese is required")
    if not word_dto.pronunciation:
        raise ValueError("Pronunciation is required")
    if not word_dto.meaning:
        raise ValueError("Meaning is required")