#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import numpy as np
import requests
import matplotlib.pyplot as plt


# In[2]:


url='https://api-ml78.herokuapp.com/predict'

pic_list = np.loadtxt("tests/pic_list.csv", dtype=str).tolist()
mask = np.load("tests/Mask.npy")


# In[3]:


app = Flask(__name__, static_url_path='/static')


# In[4]:


@app.route('/')
def index():
    return render_template('index.html', pic_list=pic_list)


# In[5]:


@app.route('/compute', methods=['POST', 'GET'])
def compute():
    if request.method == 'POST':
        pic_name = request.form['choice']
        i = pic_list.index(pic_name)
        pic = plt.imread('tests/'+pic_name)
        pic_mask = mask[i]
        files = {'image': open('tests/'+pic_name,'rb')}
        r = requests.post(url, files=files)
        if r.status_code == 200:
            predicted_mask = r.json()[0]
        else:
            predicted_mask = np.zeros((224,224))
        plt.subplot(1, 3, 1)
        plt.title('picture')
        plt.imshow(pic)
        plt.subplot(1, 3, 2)
        plt.title('mask')
        plt.imshow(pic_mask)
        plt.subplot(1, 3, 3)
        plt.title('predicted mask')
        plt.imshow(predicted_mask)
        fn = 'static/result'+str(i)+'.png'
        plt.savefig(fn)

        return render_template('index.html', pic_list=pic_list, user_image=fn)


# In[6]:


if __name__ == '__main__':
    app.run(port=5001)
    #app.run(debug=True, use_reloader=False)


# In[ ]:





# In[ ]:
