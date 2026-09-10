from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to NIIT Ltd"}

# Route to display info for hello world
@app.get("/hello/")
def helloworld():
    return {"message": "Welcome to HelloWorld"}
