import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

hours = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance: "))

x1 = hours / 6
x2 = attendance / 100

hidden = sigmoid(2 * x1 + 2 * x2 - 2)
output = sigmoid(3 * hidden - 1.5)

print("Output:", round(output, 2))

if output >= 0.5:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")