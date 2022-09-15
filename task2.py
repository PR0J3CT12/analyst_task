import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df1 = pd.read_csv("processed data.csv")
    name = 0
    for area in df1['area'].unique():
        df2 = df1.loc[df1['area'] == area]
        fig, ax = plt.subplots(figsize=(15, 10))
        for cluster in df2['cluster_name'].unique():
            df3 = df2.loc[df1['cluster_name'] == cluster]
            ax.scatter(x=df3['x'], y=df3['y'], color=df3['color'], linewidths=0.25, edgecolors='black')
        for i in range(len(df2)):
            keyword = str(df2.iloc[i]['keyword'])
            if len(keyword) > 15:
                keyword = keyword.replace(' ', '\n', 2)
            x = float(df2.iloc[i]['x'] + 0.1)
            y = float(df2.iloc[i]['y'] + 0.1)
            plt.annotate(keyword, xy=(x, y))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.suptitle(area, y=0.05, fontsize=20)
        plt.legend(df2['cluster_name'].unique(), loc='best', framealpha=0.1)
        name += 1
        plt.savefig(f"plot{name}.png")