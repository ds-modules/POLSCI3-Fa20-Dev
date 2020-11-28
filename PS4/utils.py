########PROBLEM 3###########
import pandas as pd
from datascience import Table

def insert_outlier(num_outliers):
    df = reset_data()
    sample_indices = df.sample(n=num_outliers).index
    for i in sample_indices:
        if df.at[i, 'cook_rating'] > 3:
            df.at[i, 'cook_rating'] = np.random.choice(4)
        else:
            df.at[i, 'cook_rating'] = np.random.choice([4, 5, 6])
    r = np.corrcoef(df['dem'], df['cook_rating'])[0][1]
    print('Correlation between percentage of democratic votes and the cook rating is: ' + str(r))
    df.scatter('cook_rating', 'dem');
    
def reset_data():
    data = pd.read_csv('data/house_elections_encoded.csv').drop(columns=['Unnamed: 0'], axis=1)
    return data