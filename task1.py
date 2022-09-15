import pandas as pd

if __name__ == '__main__':
    df1 = pd.read_excel("Тестовое задание.xlsx")
    df1.dropna(inplace=True)
    df1['y'] = pd.to_numeric(df1['y'], errors="coerce")
    df1 = df1[['area', 'cluster', 'cluster_name', 'keyword', 'x', 'y', 'count']]
    df1.loc[df1["cluster"] == 0, 'color'] = 'red'
    df1.loc[df1["cluster"] == 1, 'color'] = 'green'
    df1.loc[df1["cluster"] == 2, 'color'] = 'blue'
    df1.loc[df1["cluster"] == 3, 'color'] = 'yellow'
    df1 = df1.drop_duplicates(subset=['area', 'keyword'])
    df1 = df1.sort_values(by=["area", "cluster", "cluster_name", "count"], ascending=[True, True, True, False])
    df1.to_csv('processed data.csv')
