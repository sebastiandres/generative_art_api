run:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000
install:
	pip install -r requirements.txt 