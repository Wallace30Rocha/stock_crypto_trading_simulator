import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates

# Config page to be centered
st.set_page_config(initial_sidebar_state = 'collapsed', layout = 'wide')

# Variables to be st.writeed in funcion
intro = "This simulation is intended to provide an additional perspective on how stocks and cryptos could be bought and sold based on the Moon Phases, Zodiac Signs and the combination of both.  \nAs old JP used to say: 'Millinaires don't use astrology, billinaires do'. (JP Morgan)  \nThe idea that the financial markets could be influenced by the moon, constallations or even by solar and lunar eclipses has brought me to analyze if this is true or false.  \nOn my previous project I analyzed how the SP500 (1928 - 2023) behaved during each moon phase, zodiac, the combination of both as well as during lunar and solar eclipses.  \nWhat I found is that there are some interesting connections.\nTo have a better undertanding, please navigate through the dashboard bellow."

dashboard = "<div class='tableauPlaceholder' id='viz1684442956241' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;st&#47;stock_astrology_project_presentation_formating&#47;DashIntro&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='stock_astrology_project_presentation_formating&#47;DashIntro' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;st&#47;stock_astrology_project_presentation_formating&#47;DashIntro&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684442956241');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='2327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"

dinamic = "  \nHere we will base the trading of stocks or cryptos on the Moon Phases, Zodiac Signs and the combination of both.\nYou will be able to choose how many years you want to simulate the trading. Each asset has a different time frame. For example, Apple stocks started being traded in late 1980 and Bitcoin in 2010.\nYour choice of years must reflect the asset's availabity which we will provide.\n"

investments_available = "  \nStocks:  \nApple = AAPL  \nMicrosoft = MSTF  \nAmazon = AMZN  \nNvidia: NVDA  \nGoogle = GOOGL  \nBerkshire Hathway = BRK-B  \nMeta = META  \nExxon = XOM  \nTesla = TSLA  \nJP Morgan Chase = JPM  \nCryptocurrancies:  \nBitcoin = BTC  \nEthereum = ETH  \nRipple XRP = XRP  \nLitecoin = LTC"

assets = "  \nThose assets have had a great performance over the years.  \nThe goal here is to buy low and sell high!\nWe will buy on the lowest average moon, zodiac and the combination of both.\nWe will sell on the highest average moon, zodiac and the combination of both.  \nThe idea is to provide an extra strategy to trade. Something that could be conseidered by the investor when making a decision."

tickers = ['AAPL', 'MSTF', 'AMZN', 'NVDA', 'GOOGL', 'BRK-B', 'META', 'XOM', 'TSLA', 'JPM', 'BTC', 'ETH', 'XRP', 'LTC']

#----------------------------------------------------------------------------------------------------------------   
    
def project():
    user_input_data = user_input()
    final_investment_moon = moons(user_input_data)
    final_investment_zodiac = zodiac(user_input_data)
    final_investment_combo = combo(user_input_data)
    buy_hold(user_input_data, final_investment_moon, final_investment_zodiac, final_investment_combo)    
    
#----------------------------------------------------------------------------------------------------------------

def user_input():
    
    image_header = Image.open('header.png')
    st.image(image_header)
    #st.header("Moon Phase & Zodiac Sign Trading Simulator")
    st.subheader(intro)
    st.write('DISCLAIMER: This is not financial advise. I am not a certified financial advisor. This is for research and curiosity purposes only.')
    st.components.v1.html(dashboard, width = 1000, height = 800)    
    st.write(dinamic)
    st.write(investments_available)
    st.write(assets)

#-------------
    
    #USER
    # Input the stock 
    user_stock = st.selectbox('What stock or crypto would you like to simulate the trades with? Please type the ticker: ', tickers)
    
    if user_stock == 'AAPL':
        user_stock = 'apple_all_columns.csv'
        st.write('\nApple was a great choice!')
    elif user_stock == 'MSTF':
        user_stock = 'microsoft_all_columns.csv'
        st.write('\nMicrosoft was a great choice!')
    elif user_stock == 'AMZN':
        user_stock = 'amazon_all_columns.csv'
        st.write('\nAmazon was a great choice!')
    elif user_stock == 'NVDA':
        user_stock = 'nvidia_all_columns.csv'
        st.write('\nNvidia was a great choice!')
    elif user_stock == 'GOOGL':
        user_stock = 'google_all_columns.csv'
        st.write('\nGoogle was a great choice!')
    elif user_stock == 'BRK-B':
        user_stock = 'berkshire_all_columns.csv'
        st.write('\nBerkshire Hathway was a great choice!')
    elif user_stock == 'META':
        user_stock = 'meta_all_columns.csv'
        st.write('\nMeta was a great choice!')
    elif user_stock == 'XOM':
        user_stock = 'exxon_all_columns.csv'
        st.write('\nExxon Mobile was a great choice!')
    elif user_stock == 'TSLA':
        user_stock = 'tesla_all_columns.csv'
        st.write('\nTesla was a great choice!')
    elif user_stock == 'JPM':
        user_stock = 'jpm_all_columns.csv'
        st.write('\nJP Morgan Chase was a great choice!')
    elif user_stock == 'BTC':
        user_stock = 'btc_all_columns.csv'
        st.write('\nBitcoin was a great choice!')
    elif user_stock == 'ETH':
        user_stock = 'eth_all_columns.csv'
        st.write('\nEthereum was a great choice!')
    elif user_stock == 'XRP':
        user_stock = 'xrp_all_columns.csv'
        st.write('\nRipple XRP was a great choice!')
    elif user_stock == 'LTC':
        user_stock = 'ltc_all_columns.csv'
        st.write('\nLitecoin was a great choice!')

#-------------

    # Read the moon phase and zodiac CSV file into a DataFrame
    m_z = pd.read_csv(r'moon_zodiac_csv\moon_phases_zodiac_tomerge.csv')
    # Read the stock data CSV file into a DataFrame
    stock_data = pd.read_csv(fr'stocks_all_columns_csv\{user_stock}')
    # Merge the two DataFrames on the 'date' column
    merge_mz = pd.merge(stock_data, m_z, on='date')        

#-------------

    # Display asset lenght
    # Calculate the number of years between the dates
    date_min = datetime.strptime(merge_mz['date'].iloc[0], "%Y-%m-%d")
    date_max = datetime.strptime(merge_mz['date'].iloc[-1], "%Y-%m-%d")
    years_diff = date_max.year - date_min.year
    st.write(f'The asset you chose started being traded on {date_min.date()} and for this simulation the maximum date to trade is {date_max.date()}.  \nYou can choose up to {years_diff} years to simulate the trades.')
       
    # In the dropdown section set a limit number based on the max_input
    #Input how many years of trades. It cannot be older than date_min
    user_years = st.number_input('How many years would you like to simulate the investment trades? ', min_value = 0, max_value = years_diff, step = 1)

    # Specify the lines in the dataframe from years chosen by user
    mask_years = merge_mz['date'].str[: 4].astype(int) >= (merge_mz['date'].str[: 4].astype(int).max() - user_years)
    # Apply Mask
    years_df = merge_mz.loc[mask_years]
       
    return years_df

#----------------------------------------------------------------------------------------------------------------

def moons(years_df):
    
    #MOON
    # Calculate the mean percent change for each moon phase
    mean_m = years_df.groupby('moon_phase')['percent_change'].mean()
    # Sort the mean percent change values in ascending order
    mean_sorted = mean_m.sort_values(ascending=False)
    # Create a DataFrame with the sorted mean percent change values
    mean_df_m = pd.DataFrame(mean_sorted)
    # Transform the index 'moon_phase' in a column
    mean_df_m = mean_df_m.reset_index()
    st.subheader("MOON PHASES")
    st.write('\nThese are the average daily performance of your stock during each of those moon phases:\n\n')
    st.dataframe(data=mean_df_m, use_container_width=False)
    # Create a barplot of mean percent change vs. moon_phase 
    fig_moon, ax = plt.subplots(figsize = (3, 2))
    custom_palette = ["black" if val > 0 else "grey" for val in mean_df_m['percent_change']]
    moon_chart = sns.barplot(data=mean_df_m, x='percent_change', y='moon_phase', ax = ax, palette = custom_palette)
    ax.tick_params(axis='y', labelsize=4)
    ax.tick_params(axis='x', labelsize=4)
    plt.xlabel('Percent Change', fontsize = 4)
    plt.ylabel('Moon Phase', fontsize = 4)
    st.pyplot(fig_moon, use_container_width = False)
       
#-------------
    
    # Get the lowest moon phase value from 'merge_mz'
    low_moon = mean_df_m['moon_phase'].iloc[7]
    # Get the highest moon phase value from 'merge_mz'
    high_moon = mean_df_m['moon_phase'].iloc[0]
    # Mask to stop in the last possible sell
    last_high_index_moon = years_df[(years_df['moon_phase'] == high_moon)].index[-1]
    
            
    # User input how much money to simulate   
    user_money_moon = st.number_input('How much money would you like to simulate the investment trades based on the moon phases? $', min_value = 0, step = 1)
    st.write('\nRemember: We will buy during days where the moon has the lowest average percent change and sell in the highest!')
    st.write(f'\nEverytime that the moon is {low_moon} you will buy ${user_money_moon} worth of this stock and sell when the moon is {high_moon}.')
    st.write(f'\nNote that this is a coumpound strategy which means that every time that you sell you will use the amount from the last sale plus the ${user_money_moon} that you previously commited to invest to perform the next buying operation.\n')

#--------------

    # Define variables to track the total investment amount, total profit, and the number of shares bought
    total_investment_moon = 0.0
    total_profit_moon = 0.0
    shares_to_sell_moon = 0.0
    buy_operations_moon = 0.0
    compound_investment_moon = user_money_moon
    
    log_moon = []
    # Iterate through the DataFrame rows
    for index, row in years_df.iterrows():
        current_moon_phase = row['moon_phase']
        
        # Buy stock if the current moon phase matches the low_moon mask
        if current_moon_phase == low_moon:
            buy_price_moon = row['open']
            shares_to_buy_moon = compound_investment_moon / buy_price_moon
            total_investment_moon += user_money_moon
            shares_to_sell_moon += shares_to_buy_moon
            compound_investment_moon = user_money_moon
            buy_operations_moon += 1
            log_moon.append(f"Buy {shares_to_buy_moon:.2f} shares at {buy_price_moon:.2f} on moon phase {current_moon_phase}")
        
        # Sell all previously bought shares if the current moon phase matches the high_moon mask and shares are currently held
        elif current_moon_phase == high_moon and shares_to_sell_moon > 0:
            sell_price_moon = row['close']
            profit_moon = (sell_price_moon - buy_price_moon) * shares_to_sell_moon
            total_investment_moon -= user_money_moon
            total_profit_moon += profit_moon
            log_moon.append(f"Sell {shares_to_sell_moon:.2f} shares at {sell_price_moon:.2f} on moon phase {current_moon_phase}. Profit: {profit_moon:.2f}")
            shares_to_sell_moon = 0.0
            compound_investment_moon = total_investment_moon + total_profit_moon + user_money_moon + user_money_moon
    
        #Break the loop when the last occurrence of high_combo is reached
        if index == last_high_index_moon:
            break
            
    if st.checkbox('Check trading logs here (moon phases).'):
        st.write(log_moon)
            
    # Calculate the final amount of mo_moonney the user has
    final_investment_moon = user_money_moon * buy_operations_moon
    final_amount_moon = final_investment_moon + total_profit_moon
    
    # Box with results
    box_style = """
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: black;
    color: white
    """
    # Create the box with text inside
    st.markdown(
    f'<div style="{box_style}">'
    '<h3 style="color: white;">Moon Phases Trading Outcome</h3>'
    f'<p style="margin-bottom: 5px;">Total Investment on the market based on moon phases: ${final_investment_moon}.</p>'
    f'<p style="margin-bottom: 5px;">Total Profit: ${total_profit_moon:.2f}.</p>'
    f'<p>Total Amount that you now have after trading on the moon phases: ${final_amount_moon:.2f}.</p>'
    '</div>',
    unsafe_allow_html=True
    )
        
    return final_investment_moon

#----------------------------------------------------------------------------------------------------------------

def zodiac(years_df):
    
    #ZODIAC
    # Calculate the mean percent change for each zodiac
    mean_z = years_df.groupby('zodiac')['percent_change'].mean()
    # Sort the mean percent change values in ascending order
    mean_sorted_z = mean_z.sort_values(ascending=False)
    # Create a DataFrame with the sorted mean percent change values
    mean_df_z = pd.DataFrame(mean_sorted_z)
    # Transform the index 'zodiac' in a column
    mean_df_z = mean_df_z.reset_index()
    st.subheader("  \nZODIAC SIGNS")
    st.write('\nThese are the average daily performance of your stock during each of those zodiacs:\n\n')
    st.dataframe(data=mean_df_z, use_container_width=False)
    # Create a barplot of mean percent change vs. zodiac
    fig_zodiac, ax_z = plt.subplots(figsize = (3, 2))
    custom_palette = ["black" if val > 0 else "grey" for val in mean_df_z['percent_change']]
    zodiac_chart = sns.barplot(data=mean_df_z, x='percent_change', y='zodiac', ax = ax_z, palette = custom_palette)
    ax_z.tick_params(axis='y', labelsize=4)
    ax_z.tick_params(axis='x', labelsize=4)
    plt.xlabel('Percent Change', fontsize = 4)
    plt.ylabel('Zodiac', fontsize = 4)
    st.pyplot(fig_zodiac, use_container_width = False)
    
#--------------

    # Get the lowest moon phase value from 'merge_mz'
    low_zodiac = mean_df_z['zodiac'].iloc[11]
    # Get the highest zodiac phase value from 'merge_mz'
    high_zodiac = mean_df_z['zodiac'].iloc[0]
    # Mask to stop in the last possible sell
    last_high_index_zodiac = years_df[(years_df['zodiac'] == high_zodiac)].index[-1]
            
    # User input how much money to simulate   
    user_money_zodiac = st.number_input('How much money would you like to simulate the investment trades based on the zodiac signs? $', min_value = 0, step = 1)
    st.write(f'\nEverytime that the zodiac is {low_zodiac} you will buy ${user_money_zodiac} worth of this stock and sell when the zodiac is {high_zodiac}.')
    st.write(f'\nNote that this is a coumpound strategy which means that every time that you sell you will use the amount from the last sale plus the ${user_money_zodiac} that you previously commited to invest to perform the next buying operation.\n')
        
#--------------

    # Define variables to track the total investment amount, total profit, and the number of shares bought
    total_investment_zodiac = 0.0
    total_profit_zodiac = 0.0
    shares_to_sell_zodiac = 0.0
    buy_operations_zodiac = 0.0
    compound_investment_zodiac = user_money_zodiac
    
    log_zodiac = []
    # Iterate through the DataFrame rows
    for index, row in years_df.iterrows():
        current_zodiac = row['zodiac']
        
        # Buy stock if the current moon phase matches the low_moon mask
        if current_zodiac == low_zodiac:
            buy_price_zodiac = row['open']
            shares_to_buy_zodiac = compound_investment_zodiac / buy_price_zodiac
            total_investment_zodiac += user_money_zodiac
            shares_to_sell_zodiac += shares_to_buy_zodiac
            compound_investment_zodiac = user_money_zodiac
            buy_operations_zodiac += 1
            log_zodiac.append(f"Buy {shares_to_buy_zodiac:.2f} shares at {buy_price_zodiac:.2f} on zodiac {current_zodiac}")
        
        # Sell all previously bought shares if the current moon phase matches the high_moon mask and shares are currently held
        elif current_zodiac == high_zodiac and shares_to_sell_zodiac > 0:
            sell_price_zodiac = row['close']
            profit_zodiac = (sell_price_zodiac - buy_price_zodiac) * shares_to_sell_zodiac
            total_investment_zodiac -= user_money_zodiac
            total_profit_zodiac += profit_zodiac
            log_zodiac.append(f"Sell {shares_to_sell_zodiac:.2f} shares at {sell_price_zodiac:.2f} on zodiac {current_zodiac}. Profit: {profit_zodiac:.2f}")
            shares_to_sell_zodiac = 0.0
            compound_investment_zodiac = total_investment_zodiac + total_profit_zodiac + user_money_zodiac + user_money_zodiac
    
        #Break the loop when the last occurrence of high_combo is reached
        if index == last_high_index_zodiac:
            break
            
    if st.checkbox('Check trading logs here (zodiac signs).'):
        st.write(log_zodiac)
            
    # Calculate the final amount of money the user has
    final_investment_zodiac = user_money_zodiac * buy_operations_zodiac
    final_amount_zodiac = final_investment_zodiac + total_profit_zodiac
    
    # Box to display results
    box_style = """
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: black;
    color: white
    """
    # Create the box with text inside
    st.markdown(
    f'<div style="{box_style}">'
    '<h3 style="color: white;">Zodiac Trading Outcome</h3>'
    f'<p style="margin-bottom: 5px;">Total Investment on the market based on zodiac: ${final_investment_zodiac}.</p>'
    f'<p style="margin-bottom: 5px;">Total Profit: ${total_profit_zodiac:.2f}.</p>'
    f'<p>Total Amount that you now have after trading on the zodiac signs: ${final_amount_zodiac:.2f}.</p>'
    '</div>',
    unsafe_allow_html=True
    )
    
    return final_investment_zodiac
    
#----------------------------------------------------------------------------------------------------------------

def combo(years_df):
    
    #COMBO
    # Calculate the mean percent change for each zodiac
    mean_combo = years_df.groupby(['moon_phase','zodiac'])['percent_change'].mean()
    # Sort the mean percent change values in ascending order
    mean_sorted_combo = mean_combo.sort_values(ascending=False)
    # Create a DataFrame with the sorted mean percent change values
    mean_df_combo = pd.DataFrame(mean_sorted_combo)
    # Transform the index 'moon_phase' in a column
    mean_df_combo = mean_df_combo.reset_index()
    # Select the desired rows from mean_df_combo
    head_rows = mean_df_combo.head(3)
    tail_rows = mean_df_combo.tail(3)
    # Concatenate the selected rows into filtered_mean_df_combo
    filtered_mean_df_combo = pd.concat([head_rows, tail_rows])
    st.subheader("  \nCOMBINATION MOON PHASES & ZODIAC SIGNS")
    st.write('\nThese are the average daily performance of your stock during the combos of moon & zodiac (only displaying on the table the top three and worse three performers):')
    st.dataframe(data=filtered_mean_df_combo, use_container_width=False)
    # Create chart to display combo 
    #mean_df_combo['mask_combo'] = mean_df_combo['percent_change'] > 0
    #custom_palette = {True: 'black', False: 'grey'}
    #combo_chart = sns.catplot(data=mean_df_combo, x="percent_change", y="zodiac", row="moon_phase", kind="bar", aspect = 2, height=2, palette = custom_palette, hue = 'mask_combo')
    #st.pyplot(combo_chart)
      
    # Create chart to display combo 
    mean_df_combo['mask_combo'] = mean_df_combo['percent_change'] > 0
    custom_palette = {True: 'black', False: 'grey'}
    sns.set(font_scale = 0.5)
    fig_combo, ax_c = plt.subplots(figsize = (3, 2))
    combo_chart = sns.catplot(data=mean_df_combo, x = "percent_change", y = "zodiac", row = "moon_phase", kind = "bar", aspect = 2, height = 2, palette = custom_palette, hue = 'mask_combo', ax = ax_c)
    ax_c.tick_params(axis = 'both', labelsize = 4)
    ax_c.set_xlabel('Percent Change', fontsize = 4)
    ax_c.set_ylabel('Zodiac', fontsize = 4)
    for ax_row in combo_chart.axes:
        for ax_col in ax_row:
            ax_col.title.set_fontsize(4)
    combo_chart.fig.subplots_adjust(hspace = 0.5)
    st.pyplot(combo_chart)    
    
#--------------

    # Get the lowest moon phase value from 'mean_df_combo'
    low_combo = mean_df_combo.loc[mean_df_combo.index[95], ['moon_phase', 'zodiac']]
    # Get the highest moon phase value from 'mean_df_combo'
    high_combo = mean_df_combo.loc[mean_df_combo.index[0], ['moon_phase', 'zodiac']]
    # Find the index of the last occurrence of high_combo
    last_high_index_combo = years_df[(years_df['moon_phase'] == high_combo['moon_phase']) & (years_df['zodiac'] == high_combo['zodiac'])].index[-1]
    
    # Count how many buying and selling operations will be based on the time chosen by the user
            
    # User input how much money to simulate    
    user_money_combo = st.number_input('How much money would you like to simulate the investment trades based on the combo? For this category try a higher ammount. $', min_value = 0, step = 1)
    st.write(f'\nEvery time that the combo is {low_combo["moon_phase"]} {low_combo["zodiac"]} you will buy ${user_money_combo} worth of this stock and sell when the combo is {high_combo["moon_phase"]} {high_combo["zodiac"]}.')
    st.write(f'\nNote that this is a coumpound strategy which means that every time that you sell you will use the amount from the last sale plus the ${user_money_combo} that you previously commited to invest to perform the next buying operation.\n')

#--------------   
    
    # Define variables to track the total investment amount, total profit, and the number of shares bought
    total_investment_combo = 0.0
    total_profit_combo = 0.0
    shares_to_sell_combo = 0.0
    buy_operations_combo = 0
    compound_investment_combo = user_money_combo
    
    log_combo = []
    # Iterate through the DataFrame rows
    for index, row in years_df.iterrows():
        current_combo = row['moon_phase'] + ' ' + row['zodiac']
        
        # Buy stock if the current moon phase matches the low_moon mask
        if current_combo == low_combo["moon_phase"] + ' ' + low_combo["zodiac"]:
            buy_price_combo = row['open']
            shares_to_buy_combo = compound_investment_combo / buy_price_combo
            total_investment_combo += user_money_combo
            shares_to_sell_combo += shares_to_buy_combo
            compound_investment_combo = user_money_combo
            buy_operations_combo += 1
            log_combo.append(f"Buy {shares_to_buy_combo:.2f} shares at {buy_price_combo:.2f} on combo {current_combo}")
        
        # Sell all previously bought shares if the current moon phase matches the high_moon mask and shares are currently held
        elif current_combo == high_combo["moon_phase"] + ' ' + high_combo["zodiac"] and shares_to_sell_combo > 0:
            sell_price_combo = row['close']
            profit_combo = (sell_price_combo - buy_price_combo) * shares_to_sell_combo
            total_investment_combo -= user_money_combo
            total_profit_combo += profit_combo
            log_combo.append(f"Sell {shares_to_sell_combo:.2f} shares at {sell_price_combo:.2f} on combo {current_combo}. Profit: {profit_combo:.2f}")
            shares_to_sell_combo = 0.0
            compound_investment_combo = total_investment_combo + total_profit_combo + user_money_combo+ user_money_combo
    
        #Break the loop when the last occurrence of high_combo is reached
        if index == last_high_index_combo:
            break
            
    if st.checkbox('Check trading logs here (combination moon & zodiac).'):
        st.write(log_combo)
            
    # Calculate the final amount of money the user has
    final_investment_combo = user_money_combo * buy_operations_combo
    final_amount_combo = final_investment_combo + total_profit_combo 
    
    box_style = """
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: black;
    color: white
    """
    # Create the box with text inside
    st.markdown(
    f'<div style="{box_style}">'
    '<h3 style="color: white;">Combination Moon Phases & Zodiac Signs Trading Outcome</h3>'
    f'<p style="margin-bottom: 5px;">Total Investment on the market based on combo: ${final_investment_combo}.</p>'
    f'<p style="margin-bottom: 5px;">Total Profit: ${total_profit_combo:.2f}.</p>'
    f'<p>Total Amount that you now have after trading on the combo: ${final_amount_combo:.2f}.</p>'
    '</div>',
    unsafe_allow_html=True
    )

    return final_investment_combo   
    
#----------------------------------------------------------------------------------------------------------------

def buy_hold(years_df, final_investment_moon, final_investment_zodiac, final_investment_combo):
    
    buy_hold_moon = final_investment_moon / years_df.iloc[0, 2]
    sell_hold_moon = buy_hold_moon * years_df.iloc[-1, 5]
    
    buy_hold_zodiac = final_investment_zodiac / years_df.iloc[0, 2]
    sell_hold_zodiac = buy_hold_zodiac * years_df.iloc[-1, 5]
    
    buy_hold_combo = final_investment_combo / years_df.iloc[0, 2]
    sell_hold_combo = buy_hold_combo * years_df.iloc[-1, 5]
    
    st.subheader('  \nThe box bellow is a simulation of how much money you have had if you just have invested the entire amount at once in the beginning of the timeframe that you chose and held the assets until selling them on the last day of the timeframe.  \n') 
    
    box_style = """
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: black;
    color: white
    """
    # Create the box with text inside
    st.markdown(
    f'<div style="{box_style}">'
    '<h3 style="color: white;">Buy & Hold Comparison</h3>'
    f'<p style="margin-bottom: 5px;">Istead of trading by Moon Phases - Buying {final_investment_moon} worth of your choice of asset on {years_df.iloc[0, 0]} and selling on {years_df.iloc[-1, 0]} you would now have: ${sell_hold_moon:.2f}.</p>'
    f'<p style="margin-bottom: 5px;">Istead of trading by Zodiac Signs - Buying {final_investment_zodiac} worth of your choice of asset on {years_df.iloc[0, 0]} and selling on {years_df.iloc[-1, 0]} you would now have: ${sell_hold_zodiac:.2f}.</p>'
    f'<p>Istead of trading by Combination Moon & Zodiac - Buying {final_investment_combo} worth of your choice of asset on {years_df.iloc[0, 0]} and selling on {years_df.iloc[-1, 0]} you would now have: ${sell_hold_combo:.2f}.</p>'
    '</div>',
    unsafe_allow_html=True
    )
    
    st.write('  \nThank you for using the simulator. There are definetely more analysis to be made as well as a need to a deeper undertanding in astrology in order to make more solid decisions about this kind of trading strategy.')
    
    
project()