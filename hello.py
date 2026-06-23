documents = [
    "RAG means retrieval augmented generation...",
    "Embeddings turn text into numbers...",
    "A vector database stores embeddings..."
]


def chunk_text(text, chunk_size):
    words = text.split()
    chunks = []

    for n in range(0, len(words), chunk_size):
        word_group = words[n:n + chunk_size]
        chunk = " ".join(word_group)
        chunks.append(chunk)

    return chunks


def build_chunks(documents, chunk_size):
    all_chunks = []

    for document in documents:
        chunks = chunk_text(document, chunk_size)
        all_chunks.extend(chunks)

    return all_chunks


def main():
    all_chunks = build_chunks(documents, 5)

    print(all_chunks)


if __name__ == "__main__":
    main()