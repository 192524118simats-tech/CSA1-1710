from sklearn.tree import DecisionTreeClassifier

X = [
    [18, 20000],
    [20, 25000],
    [25, 30000],
    [30, 40000],
    [35, 50000],
    [40, 60000]
]

y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

age = int(input("Enter age: "))
income = int(input("Enter income: "))

prediction = model.predict([[age, income]])

if prediction[0] == 1:
    print("Prediction: Yes")
else:
    print("Prediction: No")