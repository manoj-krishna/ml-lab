import csv
import random
import math


def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def split_dataset(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    copy = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy.pop(index))
    return train_set, copy


def separate_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def mean(numbers):
    return sum(numbers)/float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries


def calculate_probability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent


def calculate_class_probabilities(summaries, input_vector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = input_vector[i]
            probabilities[classValue] *= calculate_probability(x, mean, stdev)
    return probabilities


def predict(summaries, input_vector):
    probabilities = calculate_class_probabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for classValue, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = classValue
    return best_label


def get_predictions(summaries, test_set):
    predictions = []
    for i in range(len(test_set)):
        result = predict(summaries, test_set[i])
        predictions.append(result)
    return predictions


def get_accuracy(test_set, predictions):
    correct = 0
    for i in range(len(test_set)):   # print(testSet[i][-1],"",predictions[i]) I
        if test_set[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(test_set))) * 100.0


def main():
    filename = 'lab5.csv'
    split_ratio = 0.67
    dataset = load_csv(filename)
    training_set, test_set = split_dataset(dataset, split_ratio)  # dividing into training and test data
    # trainingSet = dataset #passing entire dataset as training data
    # testSet=[[8.0,183.0,64.0,0.0,0.0,23.3,0.672,32.0]]
    print('Split {0} rows into train={1} and test={2} rows'.format(len(dataset), len(training_set), len(test_set)))
    # prepare model
    summaries = summarize_by_class(training_set)  # test model
    predictions = get_predictions(summaries, test_set)
    accuracy = get_accuracy(test_set, predictions)
    print('Accuracy: {0}%'.format(accuracy))


main()