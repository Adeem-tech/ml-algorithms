from collections import defaultdict

X = [
    ["Sunny", "Hot", "High", "Weak"],
    ["Sunny", "Hot", "High", "Strong"],
    ["Overcast", "Hot", "High", "Weak"],
    ["Rain", "Mild", "High", "Weak"],
    ["Rain", "Cool", "Normal", "Weak"],
    ["Rain", "Cool", "Normal", "Strong"],
    ["Overcast", "Cool", "Normal", "Strong"],
    ["Sunny", "Mild", "High", "Weak"],
    ["Sunny", "Cool", "Normal", "Weak"],
    ["Rain", "Mild", "Normal", "Weak"],
    ["Sunny", "Mild", "Normal", "Strong"],
    ["Overcast", "Mild", "High", "Strong"],
    ["Overcast", "Hot", "Normal", "Weak"],
    ["Rain", "Mild", "High", "Strong"]
]


y = [
    "No", "No", "Yes", "Yes", "Yes", "No", "Yes",
    "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"
]

class_count = defaultdict(int)
for label in y:
    class_count[label] += 1

total = len(y)

priors = {c: class_count[c] / total for c in class_count}


feature_count = defaultdict(int)

for row, label in zip(X, y):
    for i, value in enumerate(row):
        feature_count[(i, value, label)] += 1


def predict(sample):
    posteriors = {}

    for c in priors:
        prob = priors[c]

        for i, value in enumerate(sample):
            count = feature_count[(i, value, c)]
            prob *= count / class_count[c]

        posteriors[c] = prob

    return max(posteriors, key=posteriors.get), posteriors


test = ["Sunny", "Cool", "High", "Strong"]

result, probs = predict(test)

print("Posterior probabilities:", probs)
print("Final Prediction:", result)
