# Standard import libraries
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

import base64
import ssl

# load learner for fast.ai
from fastai.vision import *
defaults.device = torch.device('cpu')
learn_bear = load_learner('bears') # !! YOUR FOLDER OF THE MODEL!!

from io import BytesIO

import uvicorn
app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*']) # !! USE ONLY WHEN JSON SERVER IS DIFFERENT THAN HTTP SERVER !! #

# encode image send as base64 string.
def getI420FromBase64(codec):
    # get codec from http
    # codec = codec.encode()
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    return image_data


# predict image and get result 
# img - is a byte array return from getI420FromBase64
# learner is loaded learner
def predict_image_from_bytes(img, learner):
    img = open_image(img)
    pred,_,losses  = learner.predict(img)
    data = sorted(
            zip(learner.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True
        )
    
    # return response as a JSON string
    return JSONResponse({
        "predicted": str(pred),
        "prob": data[0][1],
        "learn": data
    })



# To check if server working
@app.route("/ping", methods=["get"])
async def ping(request):
    return JSONResponse({
        "isWorking": "Yes"
    })

# route to recognize bears from images, by link http://IP:8000/bears
@app.route("/bears", methods=["POST"])
async def bears(request):
    data = await request.form()
    data = data["file"]
    #print(data[:100])
    img = getI420FromBase64(data)
    return predict_image_from_bytes(img, learn_bear)

import twitter
api = twitter.Api(consumer_key='kNACZgzMIq4ANk9K724SKoYcz',
                       consumer_secret='maiUgLBEaqI6s0f4TfetdYtpxgWXtZKkmw2wjK9r7LgdKXQL5D',
                       access_token_key='903561959718649856-FQteoJdVxWeLGxGIXKakBLzjtIxpomK',
                       access_token_secret='ItapEaujj46mNpCVRs9wkbZQuDnqEegU7Fk8VGiVF1mLc')
learn_tweets = load_learner('twitter'); # !! YOUR FOLDER OF THE MODEL!!

def predict(text):
     return str(learn_tweets.predict(text)[0])


@app.route("/twitter", methods=["POST"])
async def get_tweets(request):
	data = await request.form()
	search = data["search"]
	text = api.GetSearch(search,count=30,lang='en')
	textDict = [t.AsDict() for t in text]
	json = [[predict(t['text']), t['text'], t['user']['screen_name']] for t in textDict]
	return JSONResponse({'list': json})

@app.route("/movies_cold", methods=["POST"])
async def movies_cold(request):
	return JSONResponse(
        {'list': [
            {
                'id': 1,
                'title': 'Titanic',
                'year': 1997,
                'description': 'Some description',
                'prob': 0.9,
                'img': 'https://images-na.ssl-images-amazon.com/images/I/51gEpO63aRL.jpg'
            },
             {
                'id': 2,
                'title': 'Alien',
                'year': 1997,
                'description': 'Some description',
                'prob': 0.9,
                'img': 'https://images-na.ssl-images-amazon.com/images/I/31dKO0hfksL.jpg'
            },
             {
                'id': 3,
                'title': 'Incepcja',
                'year': 1997,
                'description': 'Some description',
                'prob': 0.9,
                'img': 'https://ssl-gfx.filmweb.pl/po/08/91/500891/7354571.3.jpg'
            },
        ]}
    )

#learn_skin = load_learner('skin') # !! YOUR FOLDER OF THE MODEL!!
# def acc_camvid(input, target):
#     target = target.squeeze(1)
#     mask = target != void_code
#     return (input.argmax(dim=1)[mask]==target[mask]).float().mean()

# learn_cam = load_learner('camvid')
# @app.route("/skin", methods=["POST"])
# async def skin(request):
#     data = await request.form()
#     data = data["file"]
#     img = getI420FromBase64(data)
#     return predict_image_from_bytes(img, learn_skin)
# @app.route("/camvid", methods=["POST"])
# async def camvid(request):
#     data = await request.form()
#     data = data["file"]
#     img = getI420FromBase64(data)
#     img = open_image(img)
#     im_out,_,_  = learn_cam.predict(img)
    
#     a = image2np(im_out.data)
#     unique, counts = np.unique(a, return_counts=True)

#     data = sorted(
#            zip(learn_cam.data.classes, map(float, counts)),
#            key=lambda p: p[1],
#            reverse=True
#        )

#     import io
#     f = io.BytesIO(b'')
#     plt.imsave(f,a, format='png')
#     encoded = base64.b64encode(f.getvalue()).decode("ascii")
#     return JSONResponse({
#         "file": encoded,
#         "data": data
#     })


# main function, run server as uvicorn
if __name__ == '__main__':
    uvicorn.run(app, 
            host='0.0.0.0', 
            ssl_version=ssl.PROTOCOL_SSLv23,
            ssl_keyfile="./key.key",        # Note that the generated certificates
            ssl_certfile="./cert.crt",      # are used here
            port=8000)
