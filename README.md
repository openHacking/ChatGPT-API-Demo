# ChatGPT API Demo

## Installation

1. Install dependencies
```shell
pip install -r requirements.txt
```

2. Create a new `.env` file
write API key
```shell
OPENAI_API_KEY = '[YOUR_API_KEY]'
```

## Usage

### Use ChatGPT with Flask
Start app
```shell
python -m flask --app app.py run
```

then test

```shell
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"message":"Hello"}' \
  http://127.0.0.1:5000/chat
```

More detail: [Develop an Intelligent Chat Program Using Python and ChatGPT API](https://lwebapp.com/en/post/python-chatgpt-api)

### Use ChatGPT API

```shell
py api.py
```

More detail: [Python + ChatGPT API Development | Based on gpt-3.5-turbo model](https://lwebapp.com/en/post/chatgpt-api)