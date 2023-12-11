from flask import Flask, render_template, request, jsonify
import openai
import langchain, pinecone, os, glob, json, re
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from utils.implementation import que_ans

app = Flask(__name__)

# Flask route to render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Flask route to handle the query from the front end
@app.route('/que_ans', methods=['POST'])
def process_query_route():
    data = request.json
    query = data.get('question')
    language = data.get('language', 'english')
    length_of_answer = data.get('length_of_answer')
    response, source_pdf = que_ans(query, language)
    pdf_name = ', '.join(map(str, source_pdf))
    return jsonify({'response': response, 'pdf_name': pdf_name})

port_number = 5000
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=port_number )