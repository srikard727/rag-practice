documents = [
    "RAG means retrieval augmented generation...",
    "Embeddings turn text into numbers...",
    "A vector database stores embeddings..."
]


def chunk_text(text, chunk_size):
    words = text.split()
    print(words)


def main():
    sample_text = documents[0]

    chunks = chunk_text(sample_text, 5)

    print(chunks)


if __name__ == "__main__":
    main()