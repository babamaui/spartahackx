python -m venv .venv
./.venv/bin/python -m pip install -r backend/requirements.txt

cd frontend

npm install

cd ..

port=8080
host=localhost
./.venv/bin/python -m flask --app backend/app:app run --port "$port" --host "$host" --reload
