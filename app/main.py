from fastapi import FastAPI

app = FastAPI()


@app.get('/get-started')
def getStarted():
    return {'Response': 'Hello guys and welcome...'}
    
    
    
@app.get('/items/{item_id}')
def getItem(item_id):
    return {'Response': f'The item you selected costs 20 Euros'}
