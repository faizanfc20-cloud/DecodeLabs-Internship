from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# =========================
# STEP 1: Load Dataset
# =========================
iris = load_iris()

X = iris.data
y = iris.target

print("=" * 50)
print("IRIS DATASET INFORMATION")
print("=" * 50)

print("Dataset Shape:", X.shape)
print("Feature Names:", iris.feature_names)
print("Target Classes:", iris.target_names)

# =========================
# STEP 2: Split Dataset
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# =========================
# STEP 3: Create Models
# =========================
models = {
    "Decision Tree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier(),
    "Logistic Regression": LogisticRegression(max_iter=200)
}

scores = {}

print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

# =========================
# STEP 4: Train & Evaluate
# =========================
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    scores[name] = accuracy

    print(f"\n{name}")
    print("Accuracy:", round(accuracy * 100, 2), "%")

# =========================
# STEP 5: Best Model
# =========================
best_model_name = max(scores, key=scores.get)

print("\n" + "=" * 50)
print("BEST MODEL")
print("=" * 50)

print("Best Model:", best_model_name)
print("Best Accuracy:", round(scores[best_model_name] * 100, 2), "%")

best_model = models[best_model_name]

predictions = best_model.predict(X_test)

# =========================
# STEP 6: Classification Report
# =========================
print("\n" + "=" * 50)
print("CLASSIFICATION REPORT")
print("=" * 50)

print(classification_report(y_test, predictions))

# =========================
# STEP 7: Confusion Matrix
# =========================
print("\n" + "=" * 50)
print("CONFUSION MATRIX")
print("=" * 50)

print(confusion_matrix(y_test, predictions))

# =========================
# STEP 8: Accuracy Graph
# =========================
plt.figure(figsize=(8, 5))
plt.bar(scores.keys(), scores.values())

plt.title("Classification Algorithm Comparison")
plt.xlabel("Algorithms")
plt.ylabel("Accuracy")

plt.ylim(0.8, 1.05)

for i, value in enumerate(scores.values()):
    plt.text(i, value + 0.01, f"{value:.2f}", ha='center')

plt.show()