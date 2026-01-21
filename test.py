from vector_db import store

res = store.search(
    query_vector=[0.01] * 4096,
    top_k=3
)

print(res)
