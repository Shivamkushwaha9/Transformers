import pandas as pd
from datasets import Dataset

#Dataset is taken from KAGGLE
df = pd.read_csv("Data/Hindi_English_Truncated_Corpus.csv",nrows=50000)

df.dropna(inplace=True)

def reconstructed_data(row):
    return {
        
        'id' : str(row['source']),
        
        'translation' : {
            'en': row['english_sentence'], #en for en
            'hi' : row['hindi_sentence'] #hi for hindi 
        }
    }
    
reconstructed_data = df.apply(reconstructed_data, axis=1).to_list()

ds_raw = Dataset.from_list(reconstructed_data)
