# Import key libraries, function and classes
import numpy as np
import pandas as pd

# Note
## (1) - Fiscal years ending December 31
## (2) - ($ in thousands)

# Initialise the free cash flow dataframe
df_free_cash_flow = pd.DataFrame(columns=['2017','2018','2019','2020','2021'],
                                 index=['Tax rate', 'EBIT', '(-) Taxes', '(-) Capital expenditures', '(+) Depreciation', 'Free Cash Flow',
                                        '(+) Investment', 'Free Cash Flow pro forma for investment'])
# Fill the DataFrame with zero
df_free_cash_flow.fillna(0.0, inplace=True)

# Set the tax rate across all years to 35%
df_free_cash_flow.loc['Tax rate',:] = 0.35

# Set the EBIT based on financial analysis of the company
df_free_cash_flow.loc['EBIT',:]= [-500,-1000,1000,2500,4000]

# Calculate tax
df_free_cash_flow.loc['(-) Taxes',:] = df_free_cash_flow.loc['Tax rate',:]*df_free_cash_flow.loc['EBIT',:]

# If take is less than 0 set it to zero as you dont pay tax when EBIT is negative
df_free_cash_flow.loc['(-) Taxes',:] = [x if x >= 0 else 0.0 for x in df_free_cash_flow.loc['(-) Taxes',:].tolist()]

# Set the Capital expenditures
df_free_cash_flow.loc['(-) Capital expenditures',:] = [-500, -2000, -1500, -500, -500]

# Set the Depreciation
df_free_cash_flow.loc['(+) Depreciation',:] = [0, 500, 750, 750, 500]

# Calculate free cash flow
df_free_cash_flow.loc['Free Cash Flow',:] = df_free_cash_flow.loc['EBIT',:] + df_free_cash_flow.loc['(-) Taxes',:] + df_free_cash_flow.loc['(-) Capital expenditures',:] + df_free_cash_flow.loc['(+) Depreciation',:]

print(df_free_cash_flow)
