from fastapi import FastAPI

app = FastAPI()


@app.get('/get-started')
def getStarted():
    return {'Response': 'Hello guys and welcome...'}