# serverless-lambda-docker-deployment
Outlines a streamlined method for deploying containerized applications on AWS Lambda, facilitating serverless computing within Dockerized environments.


## Folder structure
```
└── 📁serverless-lambda-docker-deployment
    └── .gitignore
    └── 📁artifacts
        └── model.pkl
    └── Dockerfile
    └── LICENSE
    └── main.py
    └── README.md
    └── requirements.txt
    └── train.py
```

Deploying an ML model using FastAPI, Docker, and AWS Lambda with API Gateway involves several steps. Below is a comprehensive guide to help you through this process.


<center><img src="https://postimg.cc/144vrBZc"/></center>

## Step 1: Train Your Model

Utilizing the Iris classification dataset, a Support Vector Machine (SVM) classifier was trained for model development. The resultant model was saved as a pickle file within the designated "artifacts" directory. The training script can be found in `train.py`.

## Step 2: Create the FastAPI Application

I have developed a FastAPI application for prediction in `main.py`.

#### Salient Features:

- **FastAPI Integration**: Utilizes FastAPI, a modern, fast (high-performance) web framework for building APIs with Python. FastAPI's asynchronous capabilities coupled with Mangum's compatibility with AWS Lambda enable high scalability and performance for handling concurrent requests efficiently.
- **Input Data Validation**: Implements Pydantic for input data validation, ensuring robustness and reliability of incoming requests.
- **Machine Learning Model Prediction**: Loads a pre-trained Support Vector Machine (SVM) model for predicting Iris types based on provided features.
- **Asynchronous Context Manager**: Implements an asynchronous context manager (`ml_lifespan_manager`) for managing the lifecycle of machine learning models within the FastAPI application. Before the application starts taking requests, we prepare by storing the prediction model function in the dictionary with machine learning models, simulating the expensive startup operation of loading the model.
- **AWS Deployment Compatibility**: Utilizes Mangum, a library for deploying ASGI applications (such as FastAPI) in AWS Lambda with API Gateway integration, enabling seamless integration with AWS infrastructure for scalable and cost-effective deployment.

## Step 3: Create a Dockerfile

This Dockerfile configuration utilizes the AWS Lambda Python runtime image from the public Elastic Container Registry (ECR). It copies the `requirements.txt` and `main.py` files to the Lambda task root directory, along with any artifacts located in the `artifacts/` directory. Subsequently, it installs the Python dependencies specified in `requirements.txt` using pip. Finally, the command `CMD ["main.handler"]` is set to execute the `handler` function within the `main.py` file upon Lambda function invocation.

## Step 4: Set Up AWS Lambda with Docker

1. **Create an AWS ECR Repository**: Establish an Amazon Elastic Container Registry (ECR) repository to store your Docker image, providing a centralized location for managing and deploying container images securely.
   
2. **Tag and Push Docker Image to ECR**: After creating the repository, tag your Docker image appropriately and push it to the ECR repository, involving authentication with your AWS credentials and pushing the image to the designated ECR repository.
   
3. **Create a Lambda Function Using Docker Image**: With the Docker image successfully stored in the ECR repository, proceed to create a Lambda function utilizing this image, configuring Lambda to pull the Docker image from ECR and execute it as a serverless function, enabling seamless integration with AWS Lambda's serverless environment.

### Step 5: Setting Up API Gateway

1. **Create a New API**:
   - Navigate to the API Gateway console and create a new HTTP API, defining a route (e.g., `/predict`).
   
2. **Integrate the Lambda Function**:
   - Within the `/predict` route, set up an integration with the previously created Lambda function.
   
3. **Deploy the API**:
   - After configuration and testing, deploy the API, noting the endpoint URL for accessing your API.



