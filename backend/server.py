import movies_server as ms

# Standard import libraries
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

import base64
import ssl

# load learner for fast.ai
from fastai import *
from fastai.vision import *
defaults.device = torch.device('cpu')

from io import BytesIO
import uvicorn
app = Starlette()
# !! USE ONLY WHEN JSON SERVER IS DIFFERENT THAN HTTP SERVER !! #
app.add_middleware(CORSMiddleware, allow_origins=['*'])

# To check if server working


@app.route("/ping", methods=["get"])
async def ping(request):
    return JSONResponse({
        "isWorking": "Yes"
    })


@app.route("/movies_cold", methods=["POST"])
async def movies_cold(request):
    return PlainTextResponse(
        ms.get_movies_cold().to_json(orient='records'))


@app.route("/movies_get", methods=["POST"])
async def movies_get(request):  # we move selected values
    data = await request.json()
    print(type(data), data)
    return PlainTextResponse(
        ms.get_movies_recommendations(data).to_json(orient='records'))

# main function, run server as uvicorn
if __name__ == '__main__':
    uvicorn.run(app,
                host='0.0.0.0',
                # ssl_version=ssl.PROTOCOL_SSLv23,
                # ssl_keyfile="./key.key",        # Note that the generated certificates
                # ssl_certfile="./cert.crt",      # are used here
                port=8001)
