# OpenAI-Compatible Tiny Mock

Implements `POST /v1/chat/completions` with the standard OpenAI response structure.

## Deploy
1. Push these files to a GitHub repository.
2. Render Dashboard → New → Web Service → connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Test `https://YOUR-SERVICE.onrender.com/health`.
6. Submit:
   `{"url":"https://YOUR-SERVICE.onrender.com/v1/chat/completions","model":"tiny-mock"}`

## Run locally
`pip install -r requirements.txt`
`uvicorn main:app --host 0.0.0.0 --port 8000`
