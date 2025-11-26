print("1. Determine whether the student passes (1) or fails (0) based on:")
print(" a. Hours studied")
print(" b. Hours of sleep")
print("Given weights w1 = 0.6, w2 = 0.4, bias = -3")
print("Step function with a threshold of 1\n")

inputs_list = [(8, 7), (3, 4)]
weights = [0.6, 0.4]
bias = -3
threshold = 1

for idx, inputs in enumerate(inputs_list, start=1):
    output = 0
    for i in range(len(inputs)):
        output += inputs[i] * weights[i]
    output += bias

    activate = output >= threshold
    prediction = 1 if activate else 0
    
    print(f"Input {idx}: {inputs}")
    print(f"Weighted sum (with bias): {output: .2f}")
    print(f"Activation (output >= {threshold}): {activate}")
    print(f"Prediction (Pass=1, Fail=0): {prediction}\n")

print("2. Perceptron as AND gate:")
print("Weights: w1 = 1, w2 = 1, Bias = -1.5")
print("Step function threshold: 0\n")

weights = [1, 1]
bias = -1.5
threshold = 0

inputs_list = [(0, 0), (0, 1)]

for idx, inputs in enumerate(inputs_list, start=1):
    output = 0
    for i in range(len(inputs)):
        output += inputs[i] * weights[i]
    output += bias
    
    activate = output >= threshold
    prediction = 1 if activate else 0
    
    print(f"Input {idx}: {inputs}")
    print(f"Weighted sum (with bias): {output}")
    print(f"Activation (output >= {threshold}): {activate}")
    print(f"Prediction (AND output): {prediction}\n")
