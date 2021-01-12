import random
import csv

attributes = [
    ['Sunny', 'Rainy'],
    ['Warm', 'Cold'],
    ['Normal', 'High'],
    ['Strong', 'Weak'],
    ['Warm', 'Cool'],
    ['Same', 'Change']
]
print(attributes)
num_attributes = len(attributes)
print("\n The most general hypothesis: [?, ?, ?, ?, ?, ?]", end="\n")
print("\n The most specific hypothesis: [0, 0, 0, 0, 0, 0]", end="\n")
print("\n The Given Training Data Set", end="\n")
a = []
with open('pg1.csv') as file:
    render = csv.reader(file)
    for row in render:
        a.append(row)
        print(row)
print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)
for i in range(0, num_attributes):
    hypothesis[i] = a[0][i]
print("\n Find S: Finding a Maximally Specific Hypothesis", end="\n")
for i in range(0, len(a)):
    if a[i][num_attributes] == ' Yes':
        for j in range(0, num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]

    print('For Training Example No: ' + str(i) + ' the hypothesis is ' + str(hypothesis))

print("\n The Maximally Specific Hypothesis for a given Training Example: ", end="\n")
print(hypothesis)
