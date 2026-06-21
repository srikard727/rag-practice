# 1. Fake documents
documents = [
    "RAG means retrieval augmented generation...",
    "Embeddings turn text into numbers...",
    "A vector database stores embeddings..."
]


# 2. Functions
def chunk_text(text, chunk_size):
    words = text.split()
    print(words)

# 3. Test one function
sample_text = documents[0]

chunks = chunk_text(sample_text, 5)

print(chunks)