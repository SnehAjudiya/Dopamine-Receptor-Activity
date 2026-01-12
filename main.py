from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Literal
import pandas as pd
import joblib

model = joblib.load("model.pkl")

app = FastAPI(
    title="Dopamine Receptor pEC50 Predictor",
    version="1.0",
    description="Predicts pEC50 values for dopamine receptor ligands"
)

class PredictionInput(BaseModel):
    LogP: float = Field(..., description="Octanol-water partition coefficient")
    MW: float = Field(..., gt=0, description="Molecular weight")
    TPSA: float = Field(..., gt=0, description="Topological polar surface area")

    Ring_Count: int = Field(..., ge=0, description="Number of rings")
    Rotatable_Bonds: int = Field(..., ge=0, description="Rotatable bonds count")
    H_Donors: int = Field(..., ge=0, description="Hydrogen bond donors")
    H_Acceptors: int = Field(..., ge=0, description="Hydrogen bond acceptors")

    Target_Name: Literal["D1", "D2", "D3", "D4", "D5"] = Field(..., description="Target group")
    Assay_Type: Literal["A", "B", "F"] = Field(..., description="Dopamine receptor subtype")

class PredictionOutput(BaseModel):
    pEC50: float

@app.get("/")
def health():
    return {"status": "API running"}

@app.post("/predict", response_model=PredictionOutput)
def predict_pEC50(data: PredictionInput):
    try:
        input_df = pd.DataFrame([{
            "LogP": data.LogP,
            "MW": data.MW,
            "TPSA": data.TPSA,
            "Ring_Count": data.Ring_Count,
            "Rotatable_Bonds": data.Rotatable_Bonds,
            "H_Donors": data.H_Donors,
            "H_Acceptors": data.H_Acceptors,
            "Assay Type": data.Assay_Type,
            "Target Name": data.Target_Name
        }])

        prediction = model.predict(input_df)[0]
        return PredictionOutput(pEC50=float(prediction))


    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))