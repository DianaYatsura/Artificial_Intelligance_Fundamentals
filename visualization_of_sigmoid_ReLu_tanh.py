import numpy as np
import matplotlib.pyplot as plt


class ActivationVisualizer:
    def sigmoid(self, x):
        """
        Sigmoid activation function.

        Args:
            x (float): Input value.

        Returns:
            float: Output of the sigmoid function.
        """
        return 1 / (1 + np.exp(-x))


    def relu(self, x):
        """
        Rectified Linear Unit (ReLU) activation function.

        Args:
            x (float): Input value.

        Returns:
            float: Output of the ReLU function.
        """
        return np.maximum(0,x)

    def tanh(self, x):
        """
        Hyperbolic tangent (tanh) activation function.

        Args:
            x (float): Input value.

        Returns:
            float: Output of the tanh function.
        """
        return np.tanh(x)
    def calculate_values(self, x_range=(-10,10), num_points=400):
        x = np.linspace(x_range[0], x_range[1], num_points)
        y_sigmoid = self.sigmoid(x)
        y_relu = self.relu(x)
        y_tanh = self.tanh(x)
        return x, y_sigmoid, y_relu, y_tanh

    def plot_functions(self, x_range=(-10,10), num_points=400):
        x, y_sigmoid, y_relu, y_tanh = self.calculate_values(x_range, num_points)

        plt.subplot(3, 1, 1)
        plt.plot(x, y_sigmoid, color="blue")
        plt.title('Sigmoid')
        plt.xlabel("Input")
        plt.ylabel("Output")

        plt.subplot(3, 1, 2)
        plt.plot(x, y_relu,  color="yellow")
        plt.title('ReLu')
        plt.xlabel("Input")
        plt.ylabel("Output")

        plt.subplot(3, 1, 3)
        plt.plot(x, y_tanh, color="red")
        plt.title('Tanh')
        plt.xlabel("Input")
        plt.ylabel("Output")

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    visualizer = ActivationVisualizer()
    visualizer.plot_functions()