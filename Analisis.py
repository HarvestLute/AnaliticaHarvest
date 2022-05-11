# %%
import pandas as pd
# %%
df = pd.read_csv("insurance.csv")
df['age'].quantile(0.25)

# %%
df[['age']].quantile([0.25,0.50,0.75])
# %%
IQR = 51-27
Left=27 - 1.5*IQR
Right=51+1.5*IQR
(Left, Right)

# %%
