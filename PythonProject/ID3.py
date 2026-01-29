import math
from collections import Counter

data = [
 ["Sunny","Hot","High","Weak","No"],
 ["Sunny","Hot","High","Strong","No"],
 ["Cloudy","Hot","High","Weak","Yes"],
 ["Rain","Mild","High","Weak","Yes"],
 ["Rain","Cool","Normal","Weak","Yes"],
 ["Rain","Cool","Normal","Strong","No"],
 ["Cloudy","Cool","Normal","Strong","Yes"],
 ["Sunny","Mild","High","Weak","No"],
 ["Sunny","Cool","Normal","Weak","Yes"],
 ["Rain","Mild","Normal","Weak","Yes"],
 ["Sunny","Mild","Normal","Strong","Yes"],
 ["Cloudy","Mild","High","Strong","Yes"],
 ["Cloudy","Hot","Normal","Weak","Yes"],
 ["Rain","Mild","High","Strong","No"]
]

features = ["Weather","Temperature","Humidity","Wind"]

def entropy(data):
    labels = [row[-1] for row in data]
    counts = Counter(labels)

    ent = 0
    for c in counts.values():
        p = c / len(labels)
        ent -= p * math.log2(p)

    return ent

def info_gain(data, feature_index):
    total_entropy = entropy(data)

    values = set(row[feature_index] for row in data)

    weighted_entropy = 0
    for v in values:
        subset = [row for row in data if row[feature_index] == v]
        weighted_entropy += (len(subset)/len(data)) * entropy(subset)

    return total_entropy - weighted_entropy

def best_feature(data):
    gains = []

    for i in range(len(data[0]) - 1):
        gains.append(info_gain(data, i))

    return gains.index(max(gains))


def id3(data, features):
    labels = [row[-1] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if len(features) == 0:
        return Counter(labels).most_common(1)[0][0]

    best = best_feature(data)
    tree = {features[best]: {}}

    values = set(row[best] for row in data)

    for v in values:
        sub_data = [row[:best] + row[best+1:] for row in data if row[best] == v]
        sub_features = features[:best] + features[best+1:]

        tree[features[best]][v] = id3(sub_data, sub_features)

    return tree

tree = id3(data, features)
print(tree)
