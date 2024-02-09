from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def add_new_panel():
    return {"message": "Hello"}
