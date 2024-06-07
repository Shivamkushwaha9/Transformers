import pandas as pd

# Read the CSV file
data = pd.read_csv("./Data/Hindi_English_Truncated_Corpus.csv")

# Create a new dictionary column with the desired format
data['translation'] = data.apply(lambda row: {"en": row['english_sentence'], "hi": row['hindi_sentence']}, axis=1)

# Reset the index and set it as the first column
data = data.reset_index().rename(columns={'index': 'id'})

# Select the desired columns
result = data[['id', 'translation']]

print(result)