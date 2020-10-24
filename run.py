import uvicorn

if __name__ == "__main__":
    uvicorn.run("lionheart:app", debug=True, reload=True, workers=3)