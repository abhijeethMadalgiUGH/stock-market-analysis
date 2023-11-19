from sentence_transformers import SentenceTransformer, util

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('./../datasets/output_stockerbot_embed.csv')

# Select only the columns that begin with 'embedding'
embedding_columns = [col for col in df.columns if col.startswith('embedding')]

# Create a new DataFrame with the selected columns
corpus_embeddings = df[embedding_columns]

clusters = util.community_detection(corpus_embeddings, min_community_size=25, threshold=0.75)

df['cluster'] = clusters


df.to_csv('./../datasets/output_stockerbot_cluster.csv', index=False)