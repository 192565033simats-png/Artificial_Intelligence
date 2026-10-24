# Decision Tree Classification

from sklearn.tree import DecisionTreeClassifier

# Dataset: [Study Hours, Attendance]
X = [
    [1, 50],
    [2, 60],
    [3, 70],
    [4, 80],
    [5, 90],
    [6, 95]
]

# 0 = Fail, 1 = Pass
Y = [0, 0, 0, 1, 1, 1]

# Create and train the Decision Tree
model = DecisionTreeClassifier(random_state=0)
model.fit(X, Y)

# Predict for a new student
study_hours = 4
attendance = 85

prediction = model.predict([[study_hours, attendance]])

if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")
