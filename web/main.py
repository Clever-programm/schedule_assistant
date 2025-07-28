from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def status():
    """
    Simple function to get status
    :return: server status
    """

    return {"status": "ok"}