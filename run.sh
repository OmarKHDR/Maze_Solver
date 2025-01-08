pip install -q -r requirements.txt
python3 ./app/solutionGen.py "$1"
python3 ./app/flaskapp.py "$2"