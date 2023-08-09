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

## Future objectives
- Deploy to Heroku
- Find out how to handle openai secret key in deployment
- Find out if pdf file can be access in the deployed version
- Connect backend application to rkguo.xyz with proper UI