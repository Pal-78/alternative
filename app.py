#!/usr/bin/env python
# coding: utf-8

# In[19]:



from flask import Flask, request, jsonify
import pickle


# In[20]:


app = Flask(__name__)




# load model
model = pickle.load(open('model1.pickle','rb'))


# In[23]:


# In[24]:


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Tweet Sentiment Analyzer</h1><p>POST Jason data on /api</p>"




# In[26]:


# curl -X POST -H"Content-Type:application/json" -d@tweet.json http://url/api
#@app.route('/api', methods=['POST','GET'])
@app.route('/api', methods=['POST'])
def process_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
    else:
        return 'Content-Type not supported!'
    results = {}
    for keys in json_data:
        score = model.predict([json_data[keys]])
        score = score[0]
        label = 'POSITIVE'
        if score < 0.5:
            label = 'NEGATIVE'
        results[keys] = label



    return jsonify(results)


# In[27]:

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
