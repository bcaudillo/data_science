import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


claims_df = pd.read_csv('claims.csv')
cust_df = pd.read_csv('cust_demographics.csv')
claims_df.head()

cust_df.info()
print("There are " + str(cust_df.duplicated().sum()) + " duplicates in the customer demographic DataFrame.")
print("There are " + str(claims_df.duplicated().sum()) + " duplicates in the claims DataFrame.")

claims_df = claims_df.drop_duplicates()
cust_df = cust_df.drop_duplicates()

print("There are now " + str(cust_df.duplicated().sum()) + " duplicates in the customer demographic DataFrame.")
print("There are now " + str(claims_df.duplicated().sum()) + " duplicates in the claims DataFrame.")
combined_df = pd.merge(claims_df, cust_df, left_on = 'customer_id', right_on = 'CUST_ID', how = 'inner')
combined_df.head(2)
# dropping redundant key:
combined_df = combined_df.drop(columns = ['CUST_ID'])
combined_df.info()
combined_df['claim_amount'].head()

combined_df['claim_amount'] = combined_df['claim_amount'].str.replace('$', '').astype('float')
combined_df['claim_amount'].head(4)
combined_df = combined_df.dropna(subset=['claim_amount'])
combined_df.info()

# check category value counts
print(combined_df['fraudulent'].value_counts())

# create boolean and convert to binary integer encoding
combined_df['fraudulent'] = (combined_df['fraudulent'] == 'Yes').astype('int')

cause_dependence = combined_df.groupby('incident_cause')[['claim_amount', 'fraudulent']].mean(numeric_only=True)
cause_dependence


# A bar chart will work here
clm_amount = cause_dependence['claim_amount'].sort_values(ascending=False)
fig, ax = plt.subplots()
ax.barh(y = clm_amount.index, width=clm_amount.values)
plt.show()

plt.hist(combined_df['claim_amount'], bins = 30)
plt.show()


combined_df["claim_size"] = (combined_df['claim_amount'] >= 10000).map({True: "large", False: "small"})
combined_df["claim_size"].head()

sorted_rates = combined_df.groupby('State')['fraudulent'].mean(numeric_only=True).sort_values(ascending=False)
state_names = sorted_rates[0:15].index #  states with top 10 fraud rates
print(sorted_rates[0:15])
state_names

widestateclaims = combined_df.pivot_table(index = 'State', columns = 'claim_size', values='fraudulent')
widestateclaims.loc[state_names]

# one solution
groupedstateclaims_mean = combined_df.groupby(['State','claim_size'])["fraudulent"].mean().rename('fraud_rate')
groupedstateclaims_count = combined_df.groupby(['State','claim_size'])["fraudulent"].count().rename('count')

groupedstateclaims = pd.concat([groupedstateclaims_mean, groupedstateclaims_count], axis = 1)
groupedstateclaims.head()

# unstacking

claims_fraud_state = groupedstateclaims.loc[state_names,'fraud_rate'].unstack()
claims_fraud_state.head


#making  the plot

fig, ax = plt.subplots()
ax.bar(x = claims_fraud_state.index, height = claims_fraud_state['large'], color ='b', alpha = 0.4, label = 'large_claim')
ax.bar(x = claims_fraud_state.index, height = claims_fraud_state['small'], color ='orange', alpha = 0.4, label = 'small_claim')
ax.legend()
claims_fraud_state

widestateclaims = combined_df.pivot_table(index = 'State', columns = 'claim_size', values='fraudulent').loc[state_names]
widestateclaims

melted_claims = pd.melt(widestateclaims, value_vars=['small', 'large'], value_name='fraud_rate', ignore_index=False)
melted_claims.head()