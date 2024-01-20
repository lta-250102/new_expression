from fastapi import FastAPI, HTTPException
from core.entities import Word, WordDto
from core.validate import validate_word_dto
from core.config import storage_config
from core.cambridge_dict import search_word
import pyarrow as pa
from core.converter import *
import pyarrow.parquet as pq
import eng_to_ipa as p 
import pandas as pd
import json
import csv

app = FastAPI()


@app.post("/add/manual", status_code=200)
def add_word(request: WordDto):
    try:
        validate_word_dto(request)
        # word = Word(**request.model_dump())
        word = dto_to_word(request)
        df = pd.read_csv(storage_config['dic_path'])
        if request.english in df['english'].values:
            return {"message": "Word already exists"}
        l = word_to_list(word)
        with open(storage_config['dic_path'], 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(l)
        # new_df = pd.DataFrame([word.dict()])
        # full_df = pd.concat([df, new_df], ignore_index=True)
        # full_df.to_csv(storage_config['dic_path'], index=False)
        return {"message": "Add word successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/add/cambridge/{word}", status_code=200)
def add_word(word: str):
    try:
        word = search_word(word)
        df = pd.read_csv(storage_config['dic_path'])
        if word.english in df['english'].values:
            return {"message": "Word already exists"}
        l = word_to_list(word)
        with open(storage_config['dic_path'], 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(l)
        # new_df = pd.DataFrame([word.dict()])
        # full_df = pd.concat([df, new_df], ignore_index=True)
        # full_df.to_csv(storage_config['dic_path'], index=False)
        return {"message": "Add word successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/search/{word}", status_code=200)
def search(word: str):
    try:
        word_existed = False
        with open(storage_config['dic_path'], 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == word:
                    word_existed = True
                    break
        if not word_existed:
            return {"message": "Word not found"}
        word = list_to_word(row)
        dto = word_to_dto(word)
        return dto.__dict__
        # for k, v in word_dict.items():
        #     if k in ['examples', 'tags', 'synonyms', 'antonyms']:
        #         word_dict[k] = json.loads(v.replace("'", '"'))
        # word_dto = WordDto(**word_dict)
        # return word_dto.__dict__
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))