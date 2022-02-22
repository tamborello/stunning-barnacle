# Compute Doc2Vec Model Accuracy
# Use multiprocessing for when datasets get bigger than a few thousand

import gensim, multiprocessing, os, pickle, time
from utils.pickle_it import pickle_it
from pathlib import Path

Path = Path('Data/')

# Open your Doc2Vec model
with open(os.path.join(dataPath, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)
# Open your corpus
with open(os.path.join(dataPath, 'corpus.pkl'), 'rb') as f:
    corpus = pickle.load(f)

# Diagnostic
print(type(model), type(corpus), len(corpus))

# For each processed, tagged document (by index), infer its vector, return its most similar document: is it the same document?
def firstSim (index):
    global corpus, model
    return model.docvecs.most_similar([model.infer_vector(corpus[index].words)], topn=1)[0][0] == corpus[index].tags[0]

# Given the indices of the documents, map them to the processing pool
def findFirstSims (indices):
    with multiprocessing.Pool() as pool:
        # return [pool.map(firstSim, indices)]
        return pool.map(firstSim, indices)

if __name__ == "__main__":
    # Get the document indices
    indices = range(len(corpus))
    # Get the start time
    t0 = time.time()
    # print(firstSim(0))
    # Compute, for each processed, tagged document, compute which document is most similar to it
    firstSims = findFirstSims(indices)
    # Stop timing
    elapsedTime = time.time() - t0
    # Save the data
    pickle_it(firstSims, 'firstSims.pkl')
    # Accuracy is proportion of sims that are the documents themselves
    acc = round(sum(firstSims)/len(corpus), 3)
    # print(f"Elapsed time {elapsedTime} for {len(corpus)} items.")
    print(f"Model: {model}, N Items: {len(corpus)}, Accuracy: {acc}, Computation Time: {elapsedTime} s")
