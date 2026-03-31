import chromadb

# create client
client = chromadb.Client()

# create/get collection
collection = client.get_or_create_collection(name="research_papers")