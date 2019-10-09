import pandas as pd
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
plt.style.use('seaborn-paper')

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


def boxplots(npt, pt, wst, wsw):
    wperc_boxplot_data = [non_playoff_teams['W%'],
                          playoff_teams['W%'], WS_teams['W%'], WS_winners['W%']]
    pitchWAR_boxplot_data = [non_playoff_teams['Pitching_fWAR'],
                             playoff_teams['Pitching_fWAR'], WS_teams['Pitching_fWAR'], WS_winners['Pitching_fWAR']]
    batWAR_boxplot_data = [non_playoff_teams['Batting_fWAR'],
                           playoff_teams['Batting_fWAR'], WS_teams['Batting_fWAR'], WS_winners['Batting_fWAR']]
    pitchWPA_boxplot_data = [non_playoff_teams['Pitching_WPA'],
                             playoff_teams['Pitching_WPA'], WS_teams['Pitching_WPA'], WS_winners['Pitching_WPA']]
    batWPA_boxplot_data = [non_playoff_teams['Batting_WPA'],
                           playoff_teams['Batting_WPA'], WS_teams['Batting_WPA'], WS_winners['Batting_WPA']]
    pitchWPALI_boxplot_data = [non_playoff_teams['Pitching_WPA/LI'],
                               playoff_teams['Pitching_WPA/LI'], WS_teams['Pitching_WPA/LI'], WS_winners['Pitching_WPA/LI']]
    batWPALI_boxplot_data = [non_playoff_teams['Batting_WPA/LI'],
                             playoff_teams['Batting_WPA/LI'], WS_teams['Batting_WPA/LI'], WS_winners['Batting_WPA/LI']]
    gs = gridspec.GridSpec(2, 4)
    fig = plt.figure(figsize=(16, 4.5))
    ax0 = plt.subplot(gs[:, :2])  # W%
    ax1 = plt.subplot(gs[0, 2])  # p fWAR
    ax2 = plt.subplot(gs[1, 2])  # b fWAR
    ax3 = plt.subplot(gs[0, 3])  # p WPA
    ax4 = plt.subplot(gs[1, 3])  # p WPA

    ax0.boxplot(wperc_boxplot_data)
    ax0.set_xticklabels(['Non-Playoff', 'Playoff', 'WS', 'WS Winner'])
    ax0.set_ylabel('Winning %')
    ax1.boxplot(pitchWAR_boxplot_data)
    ax1.set_xticklabels(['Non-Playoff', 'Playoff', 'WS', 'WS Winner'])
    ax1.set_ylabel('Pitching fWAR')
    ax2.boxplot(batWAR_boxplot_data)
    ax2.set_xticklabels(['Non-Playoff', 'Playoff', 'WS', 'WS Winner'])
    ax2.set_ylabel('Batting fWAR')
    ax3.boxplot(pitchWPA_boxplot_data)
    ax3.set_xticklabels(['Non-Playoff', 'Playoff', 'WS', 'WS Winner'])
    ax3.set_ylabel('Pitching WPA')
    ax4.boxplot(batWPA_boxplot_data)
    ax4.set_xticklabels(['Non-Playoff', 'Playoff', 'WS', 'WS Winner'])
    ax4.set_ylabel('Batting WPA')
    fig.suptitle(
        'Characteristics of Non-Playoff Teams, Playoff Teams, World Series Teams and World Series Winning Teams (2009-2018)')
    fig.subplots_adjust(left=.05, right=.96, wspace=0.33, top=.9)


def correlations(npt, pt, wst, wsw):
    gs = gridspec.GridSpec(1, 2)
    fig = plt.figure(figsize=(16, 4.5))
    ax1 = plt.subplot(gs[0, 0])  # p fWAR
    ax2 = plt.subplot(gs[0, 1])  # b fWAR

    ax1.scatter(non_playoff_teams['Pitching_fWAR'],
                non_playoff_teams['Batting_fWAR'], c='#00A3E0', s=25, label='Non Playoff Teams')
    ax1.scatter(playoff_teams['Pitching_fWAR'], playoff_teams['Batting_fWAR'],
                c='#F4911E', s=25, label='Playoff Teams')
    ax1.scatter(non_playoff_teams['Pitching_fWAR'].mean(),
                non_playoff_teams['Batting_fWAR'].mean(), c='black', s=200, label='Non Playoff Teams Centroid', marker='*')
    ax1.scatter(playoff_teams['Pitching_fWAR'].mean(), playoff_teams['Batting_fWAR'].mean(),
                c='#002D62', s=200, label='Playoff Teams Centroid', marker='*')
    ax2.scatter(non_playoff_teams['Pitching_WPA'],
                non_playoff_teams['Batting_WPA'], c='#00A3E0', s=25, label='Non Playoff Teams')
    ax2.scatter(playoff_teams['Pitching_WPA'], playoff_teams['Batting_WPA'],
                c='#F4911E', s=25, label='Playoff Teams')
    ax2.scatter(non_playoff_teams['Pitching_WPA'].mean(),
                non_playoff_teams['Batting_WPA'].mean(), c='black', s=200, label='Non Playoff Teams Centroid', marker='*')
    ax2.scatter(playoff_teams['Pitching_WPA'].mean(), playoff_teams['Batting_WPA'].mean(),
                c='#002D62', s=200, label='Playoff Teams Centroid', marker='*')
    ax1.set_xlabel('Pitching fWAR')
    ax1.set_ylabel('Batting fWAR')
    ax1.legend(prop={'size': 7})
    ax2.set_xlabel('Pitching WPA')
    ax2.set_ylabel('Batting WPA')
    ax2.legend(prop={'size': 7})
    fig.suptitle('Relationships Between Team Pitching/Batting fWAR and WPA (2009-2018)')
    fig.tight_layout()
    fig.subplots_adjust(left=.05, right=.96, wspace=0.33, top=0.9, bottom=0.14)


data = pd.read_csv('ChampTeams.csv')
print(data.head())

non_playoff_teams = data.loc[data['Playoffs_Team'].isin([0])]
playoff_teams = data.loc[data['Playoffs_Team'].isin([1])]
WS_teams = data.loc[data['WS_Team'].isin([1])]
WS_winners = data.loc[data['WS_Winner'].isin([1])]

boxplots(non_playoff_teams, playoff_teams, WS_teams, WS_winners)
correlations(non_playoff_teams, playoff_teams, WS_teams, WS_winners)


plt.show()
