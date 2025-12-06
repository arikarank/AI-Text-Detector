import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Load the dataset
file_path = "D:/AI-Text-Detector/ai1.csv"
df = pd.read_csv(file_path)

# Drop missing values
df.dropna(subset=["text", "label"], inplace=True)

# Extract text and labels
texts = df["text"].astype(str).tolist()
labels = df["label"].astype(int).tolist()

# Tokenize and pad the texts
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)

# Convert texts to sequences
sequences = tokenizer.texts_to_sequences(texts)

# Determine an appropriate max sequence length
maxlen = min(100, max(len(seq) for seq in sequences)) if sequences else 100  # Handle empty sequences
data = pad_sequences(sequences, maxlen=maxlen)

# Stratified Train-Test Split
from sklearn.model_selection import StratifiedShuffleSplit
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in sss.split(data, labels):
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = np.array(labels)[train_index], np.array(labels)[test_index]

# Build LSTM model
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=128, input_length=maxlen),
    LSTM(128, dropout=0.2, recurrent_dropout=0.2),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid for binary classification
])

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Save the model
model.save('ai_detection_lstm_model.h5')

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc}")
