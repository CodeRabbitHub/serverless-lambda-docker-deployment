import os
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def main():
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data  # Features
    y = iris.target  # Target variable

    # Splitting the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Creating the SVM model
    svm_model = SVC(
        kernel="linear"
    )  # You can change the kernel type here (linear, polynomial, radial basis function, etc.)

    # Training the model
    svm_model.fit(x_train, y_train)

    # Making predictions on the test data
    y_pred = svm_model.predict(x_test)

    # Calculating the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Create the directory if it doesn't exist
    os.makedirs("./artifacts/", exist_ok=True)
    # Save all ML components to pickle
    model_filename = "./artifacts/model.pkl"
    with open(model_filename, "wb") as model_file:
        pickle.dump(svm_model, model_file)


if __name__ == "__main__":
    main()
