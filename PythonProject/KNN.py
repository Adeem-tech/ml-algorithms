import math
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def knn(X_train, y_train, X_test, k):

    distances = []

    for i in range(len(X_train)):
        d = euclidean_distance(X_test, X_train[i])
        distances.append([d, y_train[i], X_train[i]])

    for i in range(len(distances)):
        for j in range(i+1, len(distances)):
            if distances[i][0] > distances[j][0]:
                distances[i], distances[j] = distances[j], distances[i]

    k_neighbors = distances[:k]

    votes = {}
    for item in k_neighbors:
        label = item[1]
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    max_votes = 0
    predicted_class = None
    for label in votes:
        if votes[label] > max_votes:
            max_votes = votes[label]
            predicted_class = label

    return predicted_class, k_neighbors


X_train = [
    [8.0, 120],
    [6.1, 170],
    [7.1, 168],
    [8.2, 150]
]

y_train = [
    "Action",
    "Action",
    "Comedy",
    "Comedy"
]



rating = float(input("Enter IMDb rating: "))
duration = float(input("Enter movie duration (in minutes): "))

X_test = [rating, duration]
k = 3


prediction, neighbors = knn(X_train, y_train, X_test, k)

print("\nK Nearest Neighbors (distance, genre):")
for n in neighbors:
    print(n[0], n[1])

print("\nPredicted movie genre:", prediction)


action_x = []
action_y = []
comedy_x = []
comedy_y = []

for i in range(len(X_train)):
    if y_train[i] == "Action":
        action_x.append(X_train[i][0])
        action_y.append(X_train[i][1])
    else:
        comedy_x.append(X_train[i][0])
        comedy_y.append(X_train[i][1])

plt.scatter(action_x, action_y)
plt.scatter(comedy_x, comedy_y)

plt.scatter(X_test[0], X_test[1])

for n in neighbors:
    point = n[2]
    plt.plot([X_test[0], point[0]], [X_test[1], point[1]])

plt.xlabel("IMDb Rating")
plt.ylabel("Movie Duration (minutes)")
plt.title("KNN Movie Genre Classification")
plt.show()

