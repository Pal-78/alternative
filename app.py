#!/usr/bin/env python
# coding: utf-8

# In[19]:



import flask
from flask import Flask, request, jsonify



# In[20]:


app = Flask(__name__)


# In[21]:



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Tweet Sentiment Analyzer</h1><p>POST Jason data on /api</p>"




# In[26]:


# curl -X POST -H"Content-Type:application/json" -d@tweet.json http://url/api
@app.route('/api', methods=['POST','GET'])
def process_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.json
    else:
        return 'Content-Type not supported!'
    results = {}
    for keys in json_data:
        score = int(json_data[keys])
        label = 'POSITIVE'
        if score < 0.5:
            label = 'NEGATIVE'
        results[keys] = [label]
    return jsonify(results)


# In[27]:

#if __name__ == '__main__':
#    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
