import basilica
import os 
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

conn = basilica.Connection(BASILICA_API_KEY)
print(type(conn))

embedding = conn.embed_sentence('hey this is a cool tweet', model='twitter')
print(embedding) 

tweets = ("Hello World", "artificial intelligence", "another tweet here #cool") 
embeddings = conn.embed_sentences(tweets, model="twitter")
for embed in embeddings: 
    print("----")
    print(len(embed))