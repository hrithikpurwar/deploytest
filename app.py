from __future__ import absolute_import
from __future__  import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import cv2
import numpy as np
import os
from mamonfight22 import *
from flask import Flask , request , jsonify
from PIL import Image
from io import BytesIO
import time
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'



graph = tf.compat.v1.get_default_graph()
#model22._make_predict_function()

app = Flask("main-fight")

@app.route('/',methods= ['GET','POST'])
def main_fight(accuracyfight=0.91):
    with graph.as_default():
    #with tf.Graph().as_default():

        np.random.seed(1234)
        model22 = mamon_videoFightModel2(tf)

        res_mamon = {}
        # if os.path.exists('./tmp.mp4'):
        #     os.remove('./tmp.mp4')
        #filev = request.files['file']
        # file = open("tmp.mp4", "wb")
        # file.write(filev.read())
        # file.close()
        vid = video_mamonreader(cv2,"https://drive.google.com/file/d/1CWPUtttwSj2jBjKOlJb-vHcHZxf_kJAb/view?usp=sharing")
        datav = np.zeros((1, 30, 160, 160, 3), dtype=np.float)
        datav[0][:][:] = vid
        millis = int(round(time.time() * 1000))


        f , precent = pred_fight(model22,datav,acuracy=0.65)

        res_mamon = {'fight':f , 'precentegeoffight':str(precent)}

        millis2 = int(round(time.time() * 1000))
        res_mamon['processing_time'] =  str(millis2-millis)
        resnd = jsonify(res_mamon)
        resnd.status_code = 200
        print(res_mamon)
        return resnd


app.run(host='0.0.0.0',port=5000)
