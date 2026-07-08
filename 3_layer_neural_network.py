import numpy as np

# ----------------------------
# Activation Functions
# ----------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# ----------------------------
# Dataset (XOR)
# ----------------------------
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# ----------------------------
# Network Architecture
# Input = 2
# Hidden1 = 4
# Hidden2 = 4
# Output = 1
# ----------------------------

np.random.seed(42)

W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))

W2 = np.random.randn(4, 4)
b2 = np.zeros((1, 4))

W3 = np.random.randn(4, 1)
b3 = np.zeros((1, 1))

learning_rate = 0.1
epochs = 10000

# ----------------------------
# Training
# ----------------------------
for epoch in range(epochs):

    # ---------- Forward Propagation ----------

    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    z3 = np.dot(a2, W3) + b3
    output = sigmoid(z3)

    # ---------- Loss ----------
    loss = np.mean((y - output) ** 2)

    # ---------- Backpropagation ----------

    error_output = y - output
    d_output = error_output * sigmoid_derivative(output)

    error_hidden2 = np.dot(d_output, W3.T)
    d_hidden2 = error_hidden2 * sigmoid_derivative(a2)

    error_hidden1 = np.dot(d_hidden2, W2.T)
    d_hidden1 = error_hidden1 * sigmoid_derivative(a1)

    # ---------- Update Weights ----------

    W3 += learning_rate * np.dot(a2.T, d_output)
    b3 += learning_rate * np.sum(d_output, axis=0, keepdims=True)

    W2 += learning_rate * np.dot(a1.T, d_hidden2)
    b2 += learning_rate * np.sum(d_hidden2, axis=0, keepdims=True)

    W1 += learning_rate * np.dot(X.T, d_hidden1)
    b1 += learning_rate * np.sum(d_hidden1, axis=0, keepdims=True)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss = {loss:.6f}")

# ----------------------------
# Predictions
# ----------------------------
print("\nPredictions:")

z1 = np.dot(X, W1) + b1
a1 = sigmoid(z1)

z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)

z3 = np.dot(a2, W3) + b3
predictions = sigmoid(z3)

print(predictions.round(3))