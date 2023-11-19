import pandas as pd
from sentence_transformers import SentenceTransformer, util
# Read the CSV file into a DataFrame
df = pd.read_csv('./../datasets/output_stockerbot.csv')
model = SentenceTransformer('all-MiniLM-L6-v2')
#new file
# Encode the text column using the model
embeddings = model.encode(df['text'],batch_size=64, show_progress_bar=True,convert_to_tensor=True)

# Create a new DataFrame with the embeddings as the data
embeddings_df = pd.DataFrame(embeddings, columns=[f'embedding_{i+1}' for i in range(embeddings.shape[1])])

# Write the updated DataFrame to a CSV file
df2=pd.DataFrame(columns=df.columns)
clusters = util.community_detection(embeddings, min_community_size=600, threshold=0.6)
df2['tweet_count'] = 0 
for i, cluster in enumerate(clusters):
    df2.loc[i] = df.iloc[cluster[0]]
    df2['tweet_count'][i] = len(cluster)

df2.to_csv('./../datasets/output_stockerbot_embed_cleaned.csv', index=False)
