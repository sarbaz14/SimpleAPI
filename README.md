# FastAPI Web Service

## Introduction
This project is a FastAPI web service designed to calculate factorials of numbers and provide information about client IP address and server time.

## Installation and Setup
1. **Clone the Repository:**
   Clone or download this repository to your local machine.
```
git clone https://github.com/sarbaz14/SimpleAPI.git
```

2. **Install Dependencies:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - Open a terminal or command prompt.
   - Navigate to the directory where the code is located.
```
cd SimpleAPI
```
   
   - Run the following command to install pip
```
sudo apt install python3-pip
```

   - Run the following command to install the required dependencies:
```
python3 -m venv venv
source ~/venv/bin/activate
pip install fastapi uvicorn
```

## Running the Web Service
1. **Start the Server:**
   - After installing the dependencies, stay in the same directory in your terminal or command prompt.
   - Run the following command to start the server:
```
uvicorn main:app --reload
```
   - `app:app` specifies the module and the instance of FastAPI.
   - `--reload` enables auto-reloading so that any changes you make in the code are automatically picked up.

2. **Accessing the Endpoints:**
   - Once the server starts successfully, you can access the endpoints using a web browser, curl, or any HTTP client.
   - Example Endpoints:
     - Factorial Calculation: Open your web browser and navigate to `http://localhost:8000/factorial/5`. Or open terminal and run following command:
```
curl http://localhost:8000/factorial/5
```
   - Client IP and Time: Open your web browser and navigate to `http://localhost:8000/whoami`. Or open terminal and run following command:
```
curl http://localhost:8000/whoami
```

   - You should receive JSON responses with the calculated factorial or client IP and time information.
