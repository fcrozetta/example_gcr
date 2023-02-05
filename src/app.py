import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Sample Container API")


@app.get("/variable")
def get_sample_variable():
    variable = os.getenv("EXAMPLE_VARIABLE", "NOT FOUND")
    return JSONResponse({"EXAMPLE_VARIABLE": variable})
