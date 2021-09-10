import pandas as pd
import seaborn as sns
import utils
# TODO: All the code to produce your graphs for Stage 1 goes here!

# In the Banknote Authentication Dataset, are the data points linearly separable / almost linearly separable?
# What are we to make of the kind of Machine Learning models that we should use on this dataset?
bank_df = utils.get_banknote_df()

bank_feats = ['Variance', 'Skewness', 'Curtosis', 'Entropy', 'Class']

for i in range(len(bank_feats)):
    for j in range(i + 1, len(bank_feats)):
        ind_var = bank_feats[i]
        dep_var = bank_feats[j]

        sns.scatterplot(data=bank_df, x=ind_var, y=dep_var)

# In the RI Transit Stops Dataset, what does the breakdown of the data look like when looking specifically at 
# the features 'driver_race' and 'search_conducted'? How about 'driver_race' and 'stop_outcome', or 'driver_race' 
# and 'is_arrested'? What can we say about the relationship between our features of interest, if at all?

    # for each seach conduct look at do a pie chart of driver race

# How does the number of traffic stops change through the years in the Transit Stops Dataset?