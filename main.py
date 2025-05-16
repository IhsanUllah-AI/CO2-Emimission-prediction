from fastapi import FastAPI
import joblib
#load model
model=joblib.load("CO2_Emmission")
def Co2_Emission(engine_size,Cylinders,FC_city,FC_hwy,FC_comb):
       inp=[[engine_size,Cylinders,FC_city,FC_hwy,FC_comb]]
       prediction=model.predict(inp)
       return prediction
    
#create fastapi instance 
app=FastAPI()

@app.get("/emmission/{engine_size}/{Cylinders}/{FC_city}/{FC_hwy}/{FC_comb}")
async def emmison(engine_size:float,Cylinders:float,FC_city:float,FC_hwy:float,FC_comb:float):
       prediction=Co2_Emission(engine_size,Cylinders,FC_city,FC_hwy,FC_comb)
       return f"CO2 Emissions(g/km):{prediction}"