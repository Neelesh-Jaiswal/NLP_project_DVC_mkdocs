# Featurization Stage

- Explanation for CountVectorizer
```python
from sklearn.feature_extraction.text import CountVectorizer

max_features = 4
ngrams = 2 # tri gram

vectorizer = CountVectorizer(max_features=max_features, ngram_range=(1, ngrams))
X = vectorizer.fit_transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_names_out())
```
- Explanation of np.csr_matrix
```python
import numpy as np
from scipy.sparse import csr_matrix


A = np.array([
    [1,0,0,0,0,1,0],
    [0,1,0,3,0,0,0],
    [0,0,0,0,1,0,2]
])

print(A)


S = csr_matrix(A)
print(S)
print(type(S))

B = S.todense()
print(B)
```

- PRC Explanation

```python
precision, recall, prc_threshold = [0.1, 0.2, 0.4, 0.9, 0.99, 0.22, 0.66], [0.1, 0.2, 0.4, 0.9, 0.99, 0.22, 0.66], [0.1, 0.2, 0.4, 0.9, 0.99, 0.22, 0.66]

n_th = 4

print(list(zip(precision, recall, prc_threshold))[::n_th])
```