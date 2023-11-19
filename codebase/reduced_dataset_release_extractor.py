import pandas as pd

df = pd.read_csv('./../datasets/reduced_dataset-release.csv')

df=df.rename(columns={'TWEET':'text', 'DATE':'timestamp',})

df.to_csv('./../datasets/output_stockerbot.csv', mode='a', header=False,index=False)