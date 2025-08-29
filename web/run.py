import sys
import logging

import uvicorn


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)