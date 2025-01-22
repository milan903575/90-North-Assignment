# 90\_North\_Assignment

## Description

This repository contains a real-time chat application built with Django, a responsive webpage, and AWS Lambda functions for specific use cases.

### Features

1. **Chat Application (Django)**:
   - User authentication with signup and login.
   - Real-time chat functionality using WebSockets.
   - Persistent message storage in the database.
2. **Responsive Webpage**:
   - A static HTML file (`responsive_page.html`) with a fixed navbar, collapsible menu, and adaptive layout.
3. **AWS Lambda Functions**:
   - `add_two_numbers.py`: Adds two numbers and returns the result.
   - `upload_to_s3.py`: Uploads a file to an AWS S3 bucket.

---

## Folder Structure

```
90_North_Assignment/
├── responsive_page.html         # Responsive webpage
├── ChatApp/                     # Django chat application
│   ├── manage.py
│   ├── ChatApp/                 # Django project folder
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── ...
│   ├── chat/                    # Chat app folder
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── templates/
│   │   │   ├── signup.html
│   │   │   └── chat.html
│   │   └── ...
│   ├── staticfiles/             # Collected static files
│   ├── requirements.txt         # Python dependencies
│   └── ...
├── AWS/                         # AWS Lambda functions
│   ├── add_two_numbers.py
│   ├── upload_to_s3.py
└── README.md
```

---

## How to Run the Project

### 1. Running the Django Chat Application

#### Prerequisites

- Python 3.x installed.
- Virtual environment setup (optional but recommended).

#### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/milan903575/90-North-Assignment.git
   cd 90-North-Assignment
   cd ChatApp

   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   # For Linux/Mac source venv/bin/activate 
   venv\Scripts\activate   # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open `http://127.0.0.1:8000/signup/` in your web browser to create an account.

#### Notes

- The WebSocket functionality for real-time chat requires `Redis`. Ensure Redis is running locally or configured properly for production environments.

---

### 2. Running the Responsive Webpage

#### Steps

1. Navigate to the folder containing `responsive_page.html`.
2. Open the file in any web browser (e.g., Chrome, Firefox, Edge):
   - Double-click on the file.
   - Or, right-click and select "Open with..." followed by your preferred browser.

---

### 3. Running AWS Lambda Functions

#### Prerequisites

- AWS CLI installed and configured with appropriate permissions.
- An AWS account with access to Lambda and S3.

#### Deploying `add_two_numbers.py`

1. **Navigate to the AWS Lambda Console**.
2. Create a new Lambda function.
3. Copy the content of `add_two_numbers.py` into the function code editor.
4. Deploy the function.
5. **Test the function**:
   - Use the following JSON payload:
     ```json
     {
         "num1": 5,
         "num2": 4
     }
     ```
   - The response should return:
     ```json
     {
         "result": 9
     }
     ```

#### Deploying `upload_to_s3.py`

1. **Navigate to the AWS Lambda Console**.
2. Create a new Lambda function.
3. Copy the content of `upload_to_s3.py` into the function code editor.
4. Set up an S3 bucket to store files.
5. Deploy the function.
6. **Test the function**:
   - Use the following JSON payload:
     ```json
     {
       "file_name": "example.pdf",
       "file_content": "JVBERi0xLjQKJ... (Base64 encoded content of a PDF)"
     }
     ```
   - Verify that the file is uploaded to the specified S3 bucket.

---

## Hosted Application

Due to limited resources, the application could not be fully deployed. However, the project is fully functional locally and prepared for hosting on PythonAnywhere.

### Hosted Link (For PythonAnywhere)

- [milan903575.pythonanywhere.com](https://milan903575.pythonanywhere.com)

---

## Output:

### Chat App

#### Signup:
![signup](https://github.com/user-attachments/assets/5a4c9e03-380c-4e95-ad8b-22d193a04b7b)


#### Login:
![login](https://github.com/user-attachments/assets/5b176147-4178-40ba-8190-af4ffb67989d)


#### Chat:
![Chat](https://github.com/user-attachments/assets/2753e915-4854-4682-8e0f-705091ffe30e)


### Responsive Web Page

#### Responsive Page:
![responsive](https://github.com/user-attachments/assets/a0af0a9d-bcd4-4369-9dda-a54d12657ca1)


### AWS

#### Add Two Numbers:
![Capture](https://github.com/user-attachments/assets/2d304208-8176-4746-aa1a-248618b69f24)


#### Upload PDF to S3 bucket:
![file_upload](https://github.com/user-attachments/assets/b4f388c1-1c63-44d5-ba52-80b4a1c44d68)


