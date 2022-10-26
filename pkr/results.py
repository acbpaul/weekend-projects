# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:59:18 2022

@author: adr_p
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

############################# Random #####################################

df = pd.read_csv('random-results.csv')

# random = df[(df.playerType0 == 'random')&(df.playerType1=='random')]

df.strategyP1 = pd.to_numeric(df.strategyP1)
df.actionP1 = pd.to_numeric(df.actionP1)

# r0 = random[(random.strategyP0 == random.strategyP1)]

# import ast

# r0.log = r0.log.apply(lambda x: ast.literal_eval(x))

# sns
# r0.resultP0.apply(lambda x: pd.Series(x)).boxplot(figsize=(10,10),rot=45)


# depict visualization
# fig, ax = plt.subplots()
# sns.stripplot(data=random, x="strategyP0", y="resultP0",  hue="strategyP1",ax=ax)
# ax.set_ylim(0, 1)
# plt.show()

df = df.rename({'strategyP0':'Aleatoriedade P2',
                        'strategyP1':'Aleatoriedade P1',
                        'resultP1':'Vitórias P1'}, axis =1)

# depict visualization
fig, ax = plt.subplots()
sns.stripplot(data=df, x="Aleatoriedade P1", y="Vitórias P1",  hue="Aleatoriedade P2",ax=ax,s=8)
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax.set_ylim(-0.01, 1.1)
plt.legend(loc='upper right', title='Aleatoriedade P2', fontsize = 14)
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
fig.set_size_inches(8.5, 5.5)
# fig.savefig('random.png', dpi=100)
plt.show()

####################################################################

######################## Iterações pré-pós-flop ########################

df = pd.read_csv('results0.csv')
df = df[df.playerType1 == 'trained']

df = df[(df.strategyP1 == 'strategy1280000-2') | (df.strategyP1 == 'strategy160000-2') 
        | (df.strategyP1 == 'strategy320000-2') | (df.strategyP1 == 'strategy640000-2')]

# random = df[(df.playerType0 == 'random')&(df.playerType1=='random')]

df['regret-pre-P1'] = df.strategyP1.apply(lambda x: x[x.find('-')+1:])
df['regret-pos-P1'] = df.actionP1.apply(lambda x: x[x.find('-')+1:])

df = df.rename({'strategyP0':'Aleatoriedade P2',
                        'strategyP1':'Treinamento pré-flop',
                        'resultP1':'Vitórias'}, axis =1)
df = df[df['regret-pos-P1'] == '2']

df1 = df[df['Aleatoriedade P2'] == 0]
df2 = df[df['Aleatoriedade P2'] == 0.25]
df3 = df[df['Aleatoriedade P2'] == 0.5]
df4 = df[df['Aleatoriedade P2'] == 0.75]

# depict visualization
fig, ax = plt.subplots(2,2)

sns.stripplot(data=df1, x="Treinamento pré-flop", y="Vitórias",  hue="actionP1",ax=ax[0,0],s=7).set(title='Arrependimento P1 = 2 | Aleatoriedade P2 = 0' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[0,0].set_ylim(0, 1.1)
plt.sca(ax[0, 0])
plt.xticks([0,1,2,3], ['160k','320k','640k','1.28M'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[0,0].get_legend_handles_labels()
plt.legend(loc='lower right', title='Treinamento pós-flop', labels=['100k', '500k', '2M'], handles=hands)

sns.stripplot(data=df2, x="Treinamento pré-flop", y="Vitórias",  hue="actionP1",ax=ax[0,1],s=7).set(title='Arrependimento P1 = 2 | Aleatoriedade P2 = 0.25' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[0,1].set_ylim(0, 1.1)
plt.sca(ax[0, 1])
plt.xticks([0,1,2,3], ['160k','320k','640k','1.28M'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[0,1].get_legend_handles_labels()
plt.legend(loc='lower right', title='Treinamento pós-flop', labels=['100k', '500k', '2M'], handles=hands)

sns.stripplot(data=df3, x="Treinamento pré-flop", y="Vitórias",  hue="actionP1",ax=ax[1,0],s=7).set(title='Arrependimento P1 = 2 | Aleatoriedade P2 = 0.5' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[1,0].set_ylim(0, 1.1)
plt.sca(ax[1, 0])
plt.xticks([0,1,2,3], ['160k','320k','640k','1.28M'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[1,0].get_legend_handles_labels()
plt.legend(loc='lower right', title='Treinamento pós-flop', labels=['100k', '500k', '2M'], handles=hands)

sns.stripplot(data=df4, x="Treinamento pré-flop", y="Vitórias",  hue="actionP1",ax=ax[1,1],s=7).set(title='Arrependimento P1 = 2 | Aleatoriedade P2 = 0.75' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[1,1].set_ylim(0, 1.1)
plt.sca(ax[1, 1])
plt.xticks([0,1,2,3], ['160k','320k','640k','1.28M'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[1,1].get_legend_handles_labels()
plt.legend(loc='lower right', title='Treinamento pós-flop', labels=['100k', '500k', '2M'], handles=hands)

fig.set_size_inches(12.5, 8.5)
fig.tight_layout(pad=1.0)
# fig.savefig('pre-pos.png', dpi=100)
plt.show()




##########################################################################

######################## Iterações arrependimento ########################


df = pd.read_csv('results0.csv')
df = df[df.playerType1 == 'trained']

df = df[(df.strategyP1 == 'strategy640000-2') | (df.strategyP1 == 'strategy640000-4') 
        | (df.strategyP1 == 'strategy640000-6') | (df.strategyP1 == 'strategy640000-8')]

# random = df[(df.playerType0 == 'random')&(df.playerType1=='random')]

df['regret-pre-P1'] = df.strategyP1.apply(lambda x: x[x.find('-')+1:])
df['regret-pos-P1'] = df.actionP1.apply(lambda x: x[x.find('-')+1:])

df['train-pre-P1'] = df.strategyP1.apply(lambda x: x[x.find('s')+1:x.find('-')])
df['train-pos-P1'] = df.actionP1.apply(lambda x: x[x.find('s')+1:x.find('-')])

df = df.rename({'strategyP0':'Aleatoriedade P2',
                        'strategyP1':'Treinamento pré-flop',
                        'resultP1':'Vitórias', 
                        'regret-pre-P1':'Arrependimento Pré-flop'},axis =1)
df = df[df['train-pos-P1'] == '500000']

df1 = df[df['Aleatoriedade P2'] == 0]
df2 = df[df['Aleatoriedade P2'] == 0.25]
df3 = df[df['Aleatoriedade P2'] == 0.5]
df4 = df[df['Aleatoriedade P2'] == 0.75]

# depict visualization
fig, ax = plt.subplots(2,2)

sns.stripplot(data=df1, x="Arrependimento Pré-flop", y="Vitórias",  hue="regret-pos-P1",ax=ax[0,0],s=7).set(title='Treinamento = 640k e 500k | Aleatoriedade P2 = 0' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[0,0].set_ylim(0, 1.1)
plt.sca(ax[0, 0])
plt.xticks([0,1,2,3], ['2','4','6','8'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[0,0].get_legend_handles_labels()
plt.legend(loc='lower right', title='Arrependimento pós-flop', labels=['2','4','7','10'], handles=hands)

sns.stripplot(data=df2,  x="Arrependimento Pré-flop", y="Vitórias",  hue="regret-pos-P1",ax=ax[0,1],s=7).set(title='Treinamento = 640k e 500k | Aleatoriedade P2 = 0.25' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[0,1].set_ylim(0, 1.1)
plt.sca(ax[0, 1])
plt.xticks([0,1,2,3],['2','4','6','8'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[0,1].get_legend_handles_labels()
plt.legend(loc='lower right', title='Arrependimento pós-flop', labels=['2','4','7','10'], handles=hands)

sns.stripplot(data=df3,  x="Arrependimento Pré-flop", y="Vitórias",  hue="regret-pos-P1",ax=ax[1,0],s=7).set(title='Treinamento = 640k e 500k | Aleatoriedade P2 = 0.5' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[1,0].set_ylim(0, 1.1)
plt.sca(ax[1, 0])
plt.xticks([0,1,2,3],['2','4','6','8'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[1,0].get_legend_handles_labels()
plt.legend(loc='lower right', title='Arrependimento pós-flop', labels=['2','4','7','10'], handles=hands)

sns.stripplot(data=df4,  x="Arrependimento Pré-flop", y="Vitórias",  hue="regret-pos-P1",ax=ax[1,1],s=7).set(title='Treinamento = 640k e 500k | Aleatoriedade P2 = 0.75' )
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[1,1].set_ylim(0, 1.1)
plt.sca(ax[1, 1])
plt.xticks([0,1,2,3],['2','4','6','8'])
plt.yticks([0, 0.25, 0.50, 0.75, 1.0])
hands, labs = ax[1,1].get_legend_handles_labels()
plt.legend(loc='lower right', title='Arrependimento pós-flop', labels=['2','4','7','10'], handles=hands)

fig.set_size_inches(12.5, 8.5)
fig.tight_layout(pad=1.0)
# fig.savefig('regret.png', dpi=100)
plt.show()


##########################################################################

######################## Top Ten  ########################################



df = pd.read_csv('results0.csv')
df = df[df.strategyP0 == 0]
df = df[df.playerType1 == 'trained']

df.sort_values(by='resultP1',ascending=False,inplace=True)

df = df.head(10)

df['train-pre-P1'] = df.strategyP1.apply(lambda x: int(x[x.find('y')+1:x.find('-')]))
df['train-pos-P1'] = df.actionP1.apply(lambda x: int(x[x.find('s')+1:x.find('-')]))

df['regret-pre-P1'] = df.strategyP1.apply(lambda x: int(x[x.find('-')+1:]))
df['regret-pos-P1'] = df.actionP1.apply(lambda x: int(x[x.find('-')+1:]))

df.sort_values(by=['train-pre-P1'],ascending=False,inplace=True)

# depict visualization
fig, ax = plt.subplots(1,2)

fig.suptitle('Aleatoriedade = 0')

sns.stripplot(data=df, x="train-pre-P1", y="resultP1",  hue="regret-pre-P1",ax=ax[0],s=8)
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[0].set_ylim(0.5, 0.6)
ax[0].set(xlabel='Treinamento pré-flop', ylabel='Vitórias')
plt.sca(ax[0])
plt.xticks([0,1,2,3,4],['80k','160k','320k','640k','1.28M'])
hands, labs = ax[0].get_legend_handles_labels()
plt.legend(loc='lower right', title='Arrependimento pré-flop', labels=['2','4','7','10'], handles=hands)

sns.stripplot(data=df, x="train-pos-P1", y="resultP1",  hue="regret-pos-P1",ax=ax[1],s=8)
# g.set_axis_labels("Estratégia Jogador 1", "Vitórias Jogador 1", labelpad=10)
ax[1].set_ylim(0.5, 0.6)
ax[1].set(xlabel='Treinamento pós-flop',ylabel=None)
plt.sca(ax[1])
plt.yticks([])
plt.xticks([0,1],['100k','500k'])
hands, labs = ax[1].get_legend_handles_labels()
plt.legend(loc='lower right', title='Arrependimento pós-flop', labels=['2','4','7','10'], handles=hands)

fig.set_size_inches(8.5, 4.5)
fig.tight_layout(pad=1.0)
# fig.savefig('best.png', dpi=100)
plt.show()



# a = pd.read_csv('actions/actions500000-4.csv')
# a.rename(columns={'Unnamed: 0':'Hand'},inplace=True)