import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam
import matplotlib.pyplot as plt

def create_neural_network(input_dim, hidden_units,learning_rate):
    """
    Create a neural network model with a specified number of hidden units.

    Args:
        input_dim (int): Number of input features.
        hidden_units (int): Number of units in the hidden layer.

    Returns:
        model (Sequential): Compiled neural network model.
    """
    model = Sequential(
        [
            Input(shape=(input_dim,)),
            Dense(units=hidden_units, activation='relu'),
            Dense(1, activation='sigmoid')
        ]
    )

    model.compile(optimizer=Adam(learning_rate=learning_rate),
                  loss='binary_crossentropy', metrics=['accuracy'])

    return model

def train_neural_network(model, X_train, y_train, num_epochs, batch_size):
    """
    Train the neural network model on the training data.

    Args:
        model (Sequential): Compiled neural network model.
        X_train (ndarray): Training input features.
        y_train (ndarray): Training labels.
        num_epochs (int): Number of training epochs.
        batch_size (int): Batch size for training.
    """

    training_history = model.fit(X_train, y_train,
                                 epochs=num_epochs,
                                 batch_size=batch_size,
                                 verbose=1)
    return training_history

# Example data and labels
X_train = np.linspace(-10, 10, 2000)
y_train = (X_train >= 0).astype(int)

X_train = X_train.reshape(-1, 1)

num_epochs = 20
batch_size = 32

# Hyperparameters to experiment with

learning_rates = [0.001, 0.01, 0.1]
hidden_units_list = [4, 8, 16]

# Perform hyperparameter tuning
print("\nStarting hyperparameter tuning (binary classification).\n")
for lr in learning_rates:
    for hidden_units in hidden_units_list:

        print(f"\n=== Experiment: learning_rate={lr}, hidden_units={hidden_units} ===")

        # Create model
        model = create_neural_network(input_dim=1,
                                      hidden_units=hidden_units,
                                      learning_rate=lr)

        # Train model
        training_history = train_neural_network(model, X_train, y_train, num_epochs, batch_size)

        final_loss = training_history.history['loss'][-1]
        final_acc  = training_history.history['accuracy'][-1]

        print(f"Final Loss: {final_loss:.6f}")
        print(f"Final Accuracy: {final_acc:.6f}\n")

        plt.plot(training_history.history['loss'])
        plt.title(f'Loss for lr={lr}, hidden={hidden_units}')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.show()