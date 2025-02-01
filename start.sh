if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
else
    PYTHON_CMD=python
fi

$PYTHON_CMD -m venv .venv
./.venv/bin/$PYTHON_CMD -m pip install -r backend/requirements.txt

cd frontend

npm install

cd ..

port=8080
host=localhost
./.venv/bin/$PYTHON_CMD -m flask --app backend/app:app run --port "$port" --host "$host" --reload
