# ### A library for Common Functions

# Import the basic functions
import pandas as pd
import numpy as np


def import_transactions(path='data/transactions.csv'):
    """
    This function gets all the transactions from the default location, unless otherwise
    specified, and returns a data frame

    :param path: The path to the transactions file that was downloaded from mint
    :returns df: A Pandas data frame obejct for analysis
    """
    
    #df = pd.read_csv(path, parse_dates=[0])
    #df = df.set_index('Date')
    #df['Date'] = df.index
    
    df = pd.read_csv(path)

    return df


def clean_transactions(df):
    """ 
    Take the raw transactions in df formate and clean out the things that 
    we don't want to look at

    :param df: A Pandas data frame created from mint transactions
    :returns df: A Pandas data frame that has been cleaned up
    """
    
    # Clean up the data

    # Replace NaN values in 'Labels' with 'None'
    df = df.fillna('None')

    # Split all labels by spaces, there should be no spaces in your labels for this to work..
    df['Labels'] = df['Labels'].str.split(' ', expand=True)
    df['Labels'] = df['Labels'].str.split(' ')


    # Remove all CC Payments
    dfCreditCard = df[df['Category'] == 'Credit Card Payment']
    df = df[df['Category'] != 'Credit Card Payment']

    # Remove all income
    dfIncome = df[(df['Category'] == 'Paycheck') | (df['Category'] == 'Bonus')]
    df = df[~((df['Category'] == 'Paycheck') | (df['Category'] == 'Bonus'))]
    df = df[df['Category'] != 'Reimbursment']

    # Remove taxes
    dfTaxes = df[(df['Category'] == 'Taxes') | (df['Category'] == 'State Tax')]
    df = df[~((df['Category'] == 'Taxes') | (df['Category'] == 'State Tax'))]

    # Remove Hide From Budgets
    df = df[df['Category'] != 'Hide from Budgets & Trends']

    # Remove all transfers
    df = df[df['Category'] != 'Transfer']

    # Remove all Reimbursments
    df = df[df['Category'] != 'Reimbursments']
    
    # Return the cleaned df
    return df


def build_macro_categories(df):
    """
    Create and add the Macro Categories to the df since Mint doesn't do 
    this for us...

    :param df: A Pandas data frame object
    :returns df: A Pandas data frame object
    """
    
    # Create a MacroCategory
    dictMacroCategory = dict.fromkeys(['Gas & Fuel'], 
                                      'Auto & Transport')
    dictMacroCategory.update(dict.fromkeys(['Comcast Cable', 'iCloud Storage', 'Netflix', 'Spotify'],
                                           'Entertainment'))
    dictMacroCategory.update(dict.fromkeys(['Investing', 'Savings'], 
                                           'Financial'))
    dictMacroCategory.update(dict.fromkeys(['Alcohol & Bars', 'Coffee Shops', 'Groceries', 'Restaurants'],
                                           'Food & Dining'))
    dictMacroCategory.update(dict.fromkeys(['Gym'], 
                                           'Health & Fitness'))
    dictMacroCategory.update(dict.fromkeys(['Mortgage & Rent'], 
                                           'Home'))
    dictMacroCategory.update(dict.fromkeys(['Laundry'], 
                                           'Personal Care'))
    dictMacroCategory.update(dict.fromkeys(['Shopping', 'Books', 'Clothing', 'Electronics & Software',
                                            'Hobbies', 'Home Goods', 'Kitchen Goods', 'Other Shopping',
                                            'Sporting Goods'], 
                                           'Shopping'))
    dictMacroCategory.update(dict.fromkeys(['Other'], 
                                           'Other'))


    # Apply the macro categories to the df
    df['Macro Category'] = df['Category'].map(dictMacroCategory)
    #dictMacroCategory['Alcohol & Bars']
    
    return df

