import sys
from json import load
from os.path import dirname, abspath, join
import logging
import argparse

import uvicorn


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, help='server address')
    parser.add_argument('--port', type=int, help='server port')
    parser.add_argument('-r', action='store_true', help='make development easier')
    args = parser.parse_args()

    config: dict
    base_dir = dirname(abspath(__file__))
    persist_dir = join(base_dir, "..", "config.json")

    with open(persist_dir, 'r') as f:
        config = load(f)

    if args.port and args.host:
        uvicorn.run(
            "main:app",
            host=args.host,
            port=args.port,
            reload=args.r
        )
    else:
        uvicorn.run(
            "main:app",
            host=config["server_address"],
            port=config["server_port"],
            reload=config["server_reload"]
        )