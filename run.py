import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", debug=True, reload=True, workers=4)