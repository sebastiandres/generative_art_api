# Generative art API

This is a simple API for generating generative art.

## Installation

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Manual Steps

```shell
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Online

I've used render.com to deploy it to [generative-art-api.onrender.com](https://generative-art-api.onrender.com)

## Swagger UI

As usual, the swagger is on the [/docs endpoint](https://generative-art-api.onrender.com/docs).