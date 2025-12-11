import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from keras.models import load_model

def train_sentiment_analysis_model(texts, labels, max_words, embedding_dim, num_epochs, batch_size):
    """
    Train a neural network model for sentiment analysis using word embeddings.

    Args:
        texts (list): List of text reviews.
        labels (list): List of corresponding sentiment labels (0 or 1).
        max_words (int): Maximum number of words to tokenize.
        embedding_dim (int): Dimension of word embeddings.
        num_epochs (int): Number of training epochs.
        batch_size (int): Batch size for training.
    """
    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(texts)

    sequences = tokenizer.texts_to_sequences(texts)

    max_len = 200
    padded_sequences = pad_sequences(sequences, maxlen=max_len)

    model = Sequential([
        Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=max_len),
        Flatten(),
        Dense(32, activation="relu"),
        Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer="adam",
                  loss="binary_crossentropy",
                  metrics=["accuracy"])

    model.fit(padded_sequences, np.array(labels),
              epochs=num_epochs,
              batch_size=batch_size,
              verbose=1)

    return model, tokenizer, max_len

# Example data: text reviews and sentiment labels
texts = ["Superbly adapted to the screen and extremely faithful to Mary Webb's period novel, this film is a true masterpiece.",
        "A friend of mine showed me this film yesterday, and I was really amazed that someone could make a movie this terrible!",
        "How bad can you make a film.",
        "I saw this movie on PBS the first time. Then I bought the video and watched it countless times.",
        "Don't see this movie! It's... repulsive!"
]
labels = [1, 0, 0, 1, 0]

# Hyperparameters
max_words = 5000
embedding_dim = 32
num_epochs = 5
batch_size = 2

# Train the sentiment analysis model
model, tokenizer, max_len = train_sentiment_analysis_model(
    texts, labels,
    max_words,
    embedding_dim,
    num_epochs,
    batch_size
)

# Load the trained model
model.save("sentiment_model.keras")
print("Model is saved!")

# Load your model file
model = load_model("sentiment_model.keras")
print("Model is loaded!")

# Example new text reviews
new_texts = [
            "On rare occasions a film comes along that has the power to expand the mind, warm the heart and touch the very soul.",
            "This movie can best be described as a very long episode of a very bad sitcom.",
            "I gave this movie 2 instead of 1 just just because I am a polite person.",
            "My ten-year old liked it. For me it was hard to get through it.",
            "This film is brilliant it has cute little dolphins in it and its a great storyline."
]

# Tokenize and pad the new text reviews
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_padded = pad_sequences(new_sequences, maxlen=max_len)

# Use the trained model to predict sentiments
predictions = model.predict(new_padded)

# Convert the predictions to binary labels (0 or 1)
binary_preds = (predictions > 0.5).astype(int)

# Print the predicted sentiments for new text reviews
print("\nPredicted sentiments:")
for text, pred in zip(new_texts, binary_preds):
    print(f"'{text}' → {'Positive' if pred == 1 else 'Negative'}")