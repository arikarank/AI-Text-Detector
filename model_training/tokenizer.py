import pandas as pd
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

# Load the dataset
file_path = "D:/AI-Text-Detector/ai1.csv"
df = pd.read_csv(file_path)

# Drop missing values
df.dropna(subset=["text"], inplace=True)

# Extract text data
texts = df["text"].astype(str).tolist()

# Create and fit the tokenizer
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)

# Save the tokenizer
with open("tokenizer.pkl", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Tokenizer saved successfully.")