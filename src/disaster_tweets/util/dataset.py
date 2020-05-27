import pandas as pd
import disaster_tweets

def dataset_to_df():
    tweet= pd.read_csv(disaster_tweets.data_dir / 'raw/train.csv')
    test=pd.read_csv(disaster_tweets.data_dir / 'raw/test.csv')
    return [tweet,test]
