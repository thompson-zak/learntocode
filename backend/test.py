from main import formatCompletions
import json


def testformatCompletions1():
    file = open('./test_resources/sample_completion_1.json')
    completion = json.load(file)
    print("Loaded completion from file 1...")
    completionWithKey = [{
        "key": 1,
        "completion": completion
    }]
    formattedCompletions = formatCompletions(completionWithKey)
    print("----------------------------------")
    return formattedCompletions

def testformatCompletions2():
    file = open('./test_resources/sample_completion_2.json')
    completion = json.load(file)
    print("Loaded completion from file 2...")
    completionWithKey = [{
        "key": 1,
        "completion": completion
    }]
    formattedCompletions = formatCompletions(completionWithKey)
    print("----------------------------------")
    return formattedCompletions


if __name__ == "__main__":
    testformatCompletions1()
    testformatCompletions2()