import pandas as pd

top_countries = ['France', 'United Kingdom', 'Italy']
bottom_countries = ['Malta', 'Ireland', 'Tunisia']
all_countries = top_countries + bottom_countries

# Coffee data from 1991
coffee_top = [5567, 2341, 4256]
coffee_bottom = [12, 112, 90]
coffee_all = coffee_top + coffee_bottom

# Death rates from 1991
death_top = [9.2, 11.3, 9.7]
death_bottom = [7.9, 8.9, 5.3]
death_all = death_top + death_bottom

df_all = pd.DataFrame({
    'Country': all_countries,
    'Coffee': coffee_all,
    'Death': death_all
})

# Get only years 1998-1999
coffee_df = pd.read_csv("coffee-consumption.csv")
coffee_df.rename(columns={coffee_df.columns[0]: "Country"}, inplace=True)
coffee_ts = coffee_df[['Country', '1998', '1999']].copy()


death_df = pd.read_csv("death-rates.csv")
death_df.rename(columns={"Country Name": "Country"}, inplace=True)
death_ts = death_df[['Country', '1998', '1999']].copy()

# Only get the countries we need
coffee_ts = coffee_ts[coffee_ts['Country'].isin(all_countries)]
death_ts = death_ts[death_ts['Country'].isin(all_countries)]

# Time series graph
time_series_data = {}
for country in all_countries:
    coffee_row = coffee_ts[coffee_ts['Country'] == country]
    death_row = death_ts[death_ts['Country'] == country]
    if not coffee_row.empty and not death_row.empty:
        coffee_values = coffee_row[['1998','1999']].iloc[0].tolist()
        death_values = death_row[['1998','1999']].iloc[0].tolist()
        time_series_data[country] = {"Year": [1998, 1999],
                                     "Coffee": coffee_values,
                                     "Death": death_values}
    else:
        time_series_data[country] = {"Year": [1998, 1999],
                                     "Coffee": [None, None],
                                     "Death": [None, None]}

