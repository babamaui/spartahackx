python -m venv .venv
Start-Process -FilePath '.\.venv\Scripts\python' -ArgumentList '-m pip install -r backend/requirements.txt' -NoNewWindow -Wait

Set-Location .\frontend
npm install
npm start