from fastapi import FastAPI
import pickle
from contextlib import asynccontextmanager
from pydantic import BaseModel
from mangum import Mangum


# Input Data Validation using Pydantic
class ModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def predict_iris_type(features):
    # Load the saved SVM model
    model_filename = "./artifacts/model.pkl"
    with open(model_filename, "rb") as model_file:
        svm_model = pickle.load(model_file)

    # Convert the features dictionary to a list of values in the same order as the original features
    feature_values = [
        features["sepal_length"],
        features["sepal_width"],
        features["petal_length"],
        features["petal_width"],
    ]

    # Make predictions on the new data
    prediction = svm_model.predict([feature_values])[0]

    # Convert numeric label to iris type
    iris_types = ["setosa", "versicolor", "virginica"]
    predicted_iris = iris_types[prediction]

    return {"prediction": predicted_iris}


# Life Span Management
ml_models = {}


@asynccontextmanager
async def ml_lifespan_manager(app: FastAPI):
    ml_models["iris_predictor"] = predict_iris_type
    yield
    ml_models.clear()


# Create an instance of FastAPI
app = FastAPI(lifespan=ml_lifespan_manager, debug=True)

# Mangum wrapper for AWS deployment
handler = Mangum(app)


# Root endpoint
@app.get("/")
def index():
    return {"message": "Welcome to the Iris API"}


# Health check endpoint
@app.get("/health")
def check_health():
    return {"status": "ok"}


# Preditcion endpoint
@app.post("/predict")
async def predict(model_input: ModelInput):
    data = model_input.model_dump()
    return ml_models["iris_predictor"](data)


# FOR TESTING IN LOCAL

# import uvicorn
# # Run the FastAPI application
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080)
