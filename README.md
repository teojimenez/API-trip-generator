# API-trip-generator
Flask App that returns x day trip, given city and days parameters with the openai API

## Instructions

### Create a modified enviroment
```python
python -m venv env
```
### Activate the enviroment
```bash
source env/bin/activate
# Deactivate the enviroment with:
deactivate
```
### Install all libraries
```
pip install -r requirements.txt
```

### Add data into the .env file
```
API_KEY -> openai API key
TOKEN -> token to access the api
PORT=8080
```
### **EXTRA** ~ Deploy on gcloud (when gcloud is configurated)

```bash
gcloud run deploy --source .
```
