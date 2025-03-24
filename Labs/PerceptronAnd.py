import numpy as np


# Define activation function (unit step)
def unit_step(v):
    return 1 if v >= 0 else 0


# Perceptron training function
def train_perceptron(inputs, targets, weights, bias, learning_rate, epochs=2):
    print("\nStarting Training...")
    print(f"Initial Weights: {weights}, Bias: {bias}\n")

    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}:\n" + "-" * 30)

        for i, x in enumerate(inputs):
            target = targets[i]

            # Compute net input
            net_input = np.dot(weights, x) + bias
            predicted = unit_step(net_input)

            # Compute error
            error = target - predicted

            # Print calculations
            print(f"Input: {x}, Target: {target}")
            print(f"Net Input: {net_input:.2f}, Predicted: {predicted}, Error: {error}")

            # Update weights & bias if error ≠ 0
            if error != 0:
                weights += learning_rate * error * x
                bias += learning_rate * error
                print(f"🔄 Updated Weights: {weights}, Updated Bias: {bias}")

            print()  # Blank line for readability

    return weights, bias


# AND Logic Dataset
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Inputs
targets = np.array([0, 0, 0, 1])  # AND outputs

# Initialize weights and bias
initial_weights = np.array([0.2, 0.5])  # Start with given weights
initial_bias = -0.1
learning_rate = 0.25  # Set learning rate

# Train perceptron
final_weights, final_bias = train_perceptron(
    inputs, targets, initial_weights, initial_bias, learning_rate
)

# Testing trained perceptron
print("\nFinal Weights:", final_weights, "Final Bias:", final_bias)
print("\nTesting Perceptron after Training:")
for x in inputs:
    result = unit_step(np.dot(final_weights, x) + final_bias)
    print(f"AND({x[0]}, {x[1]}) = {result}")
