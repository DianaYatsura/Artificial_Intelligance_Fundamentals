import numpy as np

class Perceptron:
    def __init__(self, input_size, hidden_size=2):
        """
        Initializes a simple perceptron model.

        Args:
            input_size (int): Number of input features.
        """
        self.input_size = input_size
        self.hidden_size = hidden_size

        self.weight1 = np.random.randn(input_size, hidden_size)
        self.bias1 = np.zeros(hidden_size)

        self.weight2 = np.random.randn(hidden_size)
        self.bias2 = 0.0

    def activation(self, x):
        """
        Activation function (Step function).

        Args:
            x (float): Input value.

        Returns:
            int: 1 if x >= 0, else 0.
        """
        return 1 if x >= 0 else 0

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        self.z1 = np.dot(x, self.weight1) + self.bias1
        self.a1 = self.sigmoid(self.z1)

        self.z2 = np.dot(self.a1, self.weight2) + self.bias2
        self.a2 = self.activation(self.z2)
        return self.a2

    def predict(self, x):
        """
        Predicts the output label using the perceptron model.

        Args:
            x (ndarray): Input features.

        Returns:
            int: Predicted label (1 or 0).
        """
        return self.forward(x)

    def train(self, X, y, num_epochs, learning_rate):
        """
        Trains the perceptron model on the given dataset using the perceptron learning rule.

        Args:
            X (ndarray): Input features of the dataset.
            y (ndarray): Ground truth labels of the dataset.
            num_epochs (int): Number of training epochs.
            learning_rate (float): Learning rate for weight update.
        """
        for _ in range(num_epochs):
            for xi, target in zip(X, y):
                z1 = np.dot(xi, self.weight1) + self.bias1
                a1 = self.sigmoid(z1)
                z2 = np.dot(a1, self.weight2) + self.bias2
                a2 = self.activation(z2)

                errors = target - a2

                delta_hidden = errors * self.weight2 * a1 * (1 - a1)

                self.weight2 += learning_rate * errors * a1
                self.bias2 += learning_rate * errors

                self.weight1 += learning_rate * np.outer(xi, delta_hidden)
                self.bias1 += learning_rate * delta_hidden


# XOR dataset: Input features and corresponding labels
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Create and train the perceptron model
perceptron = Perceptron(input_size=2)
perceptron.train(X, y, num_epochs=1000, learning_rate=0.1)

print("Weight1 (input → hidden):")
print(perceptron.weight1)
print("Bias1:")
print(perceptron.bias1)

print("\nWeight2 (hidden → output):")
print(perceptron.weight2)
print("Bias2:")
print(perceptron.bias2)

# Test the trained model
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for data in test_data:
    prediction = perceptron.predict(data)
    print(f"Input: {data}, Prediction: {prediction}")


