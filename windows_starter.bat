CD %CD%\backendflask

set FLASK_APP=main
set FLASK_DEBUG=1

call .\venv\Scripts\activate

pip3 install -r ./requirements.txt

pytest .\testing

start cmd /k "CD ..\frontend-react\stataflow-flix && npm start"

flask run