import faiss
import pickle

INDEX_PATH = "vectorstore/faiss.index"
META_PATH = "vectorstore/metadata.pkl"


def save_index(index):
    faiss.write_index(index, INDEX_PATH)


def load_index():
    return faiss.read_index(INDEX_PATH)


def save_metadata(data):
    with open(META_PATH, "wb") as f:
        pickle.dump(data, f)


def load_metadata():
    with open(META_PATH, "rb") as f:
        return pickle.load(f)