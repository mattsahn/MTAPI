# 
# start virtual environment
source .venv/bin/activate

# export env variable
export MTA_SETTINGS=settings.cfg

# run the server
python app.py 

# test a command with curl
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/routes

# deploy to Lambda
zappa update
