## Chatbot with API for Ruikang Guo
Context: 02.08.2023 Ruikang Guo resume
#### Dependencies
```
pip install fastapi uvicorn[standard] llama_index openai
```
#### Running the app
```
python -m uvicorn Main:app --reload
```
#### Endpoints
**/**

returns hello mundo

**/api/v1/{your question here}**

returns a response

## CORS config

CORS is a security feature implemented by web browsers to prevent web pages from making requests to a different domain than the one that served the web page. This security measure is in place to protect users from potential security vulnerabilities.

If we don’t do any configuration, the application cannot return anything to the frontend due to CORS error.

```python
# Add these lines
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = ["https://rkguo.xyz"]  # Replace with your allowed origin(s)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # Optional
    allow_methods=["*"],  # Optional, You can adjust the HTTP methods as needed
    allow_headers=["*"],  # Optional, You can adjust the allowed headers as needed
)
```

## Deployment Process

Deployed to Heroku

1. Create requirements.txt
    
    ```bash
    pip freeze > requirements.txt
    ```
    
2. Create a “Procfile”
    
    ```
    web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
    ```
    
3. Create a gitignore
    
    ```
    **/__pycache__/
    .env
    dep
    lambda_artifact.zip
    *.pyc
    *.pyo
    venv/
    ```
    
4. Install Heroku CLI
    
    [The Heroku CLI | Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli)
    
5. Heroku CLI Login
    
    ```bash
    heroku login
    ```
    
6. Create a new Heroku App
    
    Skip this step if you already created an app using the heroku web GUI
    
    ```bash
    heroku create your-app-name
    ```
    
7. Add Heroku remote
    
    ```bash
    git remote add heroku https://git.heroku.com/your-app-name.git
    ```
    
8. Push to heroku
    
    ```bash
    git push heroku your-main-or-master-branch-name
    ```
    
9. Deal with .env files
    
    **Using Heroku Dashboard**:
    
    You can set, modify, or view environment variables from the Heroku dashboard:
    
    - Navigate to **[Heroku Dashboard](https://dashboard.heroku.com/)**
    - Select your application.
    - Go to the "Settings" tab.
    - Find the "Config Vars" section and use the "Reveal Config Vars" button.
    - Here you can add key-value pairs equivalent to what you have in your **`.env`** file.