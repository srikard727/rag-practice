import string
from collections import Counter


documents = [
    "RAG means retrieval augmented generation...",
    "Embeddings turn text into numbers...",
    "A vector database stores embeddings..."
]


def clean_text(text):
    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return text


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


def retrieve_chunks(query, chunks, top_k=2):
    query_words = Counter(clean_text(query).split())

    scored_chunks = []

    for chunk in chunks:
        chunk_words = Counter(clean_text(chunk).split())

        score = 0

        for word in query_words:
            score += min(query_words[word], chunk_words[word])

        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True)

    top_chunks = scored_chunks[:top_k]

    return top_chunks


def main():
    all_chunks = build_chunks(documents, 5)

    query = "What are embeddings?"

    results = retrieve_chunks(query, all_chunks)

    print(results)


if __name__ == "__main__":
    main()