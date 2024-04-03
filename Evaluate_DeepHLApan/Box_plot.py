# -*- coding: utf-8 -*-

# sequence matching
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%

"""
No predictor peptides data 
"""
ep = 'epoch1000'
batch_size = 10000 # 10000 peptides
method = 'WGAN-GP'

data_path = method + '/' + 'VGAN_predicted_result.csv'
generate = pd.read_csv(data_path)
imm = generate['immunogenic score'].values

seq = generate['Peptide'].values
WGANGP_seq= seq

df = pd.DataFrame({'immunogenicity':imm})

"""
With predictor peptides data 
"""
ep = 'epoch1000'
batch_size = 10000 # 10000 peptides
method = 'Goal-directed_WGAN-GP'

data_path = method + '/' + 'GGAN_predicted_result.csv'
generate = pd.read_csv(data_path)
imm = generate['immunogenic score'].values

seq = generate['Peptide'].values
GD_seq = seq

df2 = pd.DataFrame({'immunogenicity':imm})

"""
Combine two dataframe
"""

df_labled = df
df_labled['Method'] = 'WGAN-GP'
df2_labled = df2
df2_labled['Method'] = 'Goal-directed WGAN-GP'
df_concate = pd.concat([df2_labled, df_labled])
df_concate['Immunogenicity score'] = df_concate['immunogenicity']

#%% Box plot
plt.rcParams['figure.figsize']
# [6.4, 4.8]
# print(sns.color_palette().as_hex())
# blue: #1f77b4
# orange: #ff7f0e
fig3, ax3 = plt.subplots(figsize=(6.6, 4.8))
sns.boxplot(data=df_concate, x="Method", y="Immunogenicity score",saturation=0.5,width=0.5,palette=['#ff7f0e', '#1f77b4'], ax=ax3)
sns.stripplot(data=df_concate, x="Method", y="Immunogenicity score",palette=['#ffb482', '#a1c9f4'], size=1, alpha=0.5, ax=ax3)
# iterate through the axes containers
for c in ax3.xaxis.get_major_ticks():
    c.label.set_fontsize(15)
for c in ax3.yaxis.get_major_ticks():
    c.label.set_fontsize(15)
plt.title('DeepHLApan',fontsize=25, weight='bold')
plt.ylabel('Immunogenicity score',fontsize=20, weight='bold')
plt.xlabel('Methods',fontsize=20, weight='bold')
plt.grid()
plt.show()

#%% Count unique sequence
# our generated peptides
g_unq_rows, g_count = np.unique(GD_seq,return_counts=1)
g_num_unq = len(g_count)
print('# of unique peptides from our method: ' + str(g_num_unq))
print('Most frequent sequence: ' + str(g_unq_rows[np.argmax(g_count)] + ', ' + str(np.max(g_count)) + ' occurance'))

# others generated peptides
w_unq_rows, w_count = np.unique(WGANGP_seq,return_counts=1)
w_num_unq = len(w_count)
print('# of unique peptides from other method: ' + str(w_num_unq))
print('Most frequent sequence: ' + str(w_unq_rows[np.argmax(w_count)] + ', ' + str(np.max(w_count)) + ' occurance'))
