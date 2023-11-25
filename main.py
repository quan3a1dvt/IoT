from fastapi import FastAPI
import pickle
model = pickle.load(open('finalized_model.sav', 'rb'))

app = FastAPI() # gọi constructor và gán vào biến app

@app.get("/") 
def predict(tempmax: float, tempmin: float, temp: float, humidity: float):
    return {'result': model.predict([[tempmax, tempmin, temp, humidity]])[0]}
