"""
Minimalistic Python test file. See python.ipynb for more robust tests.

Tested with dev 2018 and dev2021. Some differences in code syntax, make sure to
select variable conda_env_ver appropriately depending on which environment is
used.

If rpy2 calls fail, try setting R_HOME path explicitly below.
"""
conda_env_ver = "dev2018" # either dev2018 pr dev2021

# Set R_HOME path explicitly, change path string to your location
#import os
#os.environ['R_HOME'] = '/Users/<your user>/anaconda3/envs/<env name>/lib/R'

# Imports
import sys
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

print("Python exe path is:")
print(sys.executable)
print("\n")

print("sys.path contains:")
print(sys.path)
print("\n")

df = pd.DataFrame([1,2,4])
print("Pandas data frame:")
print(df)

# Pandas df to R df, transform with tidyverse, convert back to pandas. See
# https://rpy2.github.io/doc/latest/html/pandas.html
# https://rpy2.github.io/doc/latest/html/introduction.html
print("Pandas df to R df, transform with tidyverse, convert back to pandas:")
r_tidyverse = importr('tidyverse')
ro.r('''
    transform_df <- function(df) {
        df = df %>% 
          group_by(str_values) %>% 
          summarise(int_values = sum(int_values))
        return(as.data.frame(df))
    }
    '''
)
transform_df = ro.globalenv['transform_df']

pd_df = pd.DataFrame({
    'int_values': [1,2,3],
    'str_values': ['abc', 'def', 'abc']
})

if conda_env_ver == "dev2021":

  with localconverter(ro.default_converter + pandas2ri.converter):
    r_df = ro.conversion.py2rpy(pd_df)

  r_df = transform_df(r_df)

  with localconverter(ro.default_converter + pandas2ri.converter):
    pd_df_again = ro.conversion.rpy2py(r_df)

elif conda_env_ver == "dev2018":

  pandas2ri.activate()
  r_df = pandas2ri.py2ri(pd_df)
  r_df = transform_df(r_df)
  pd_df_again = pandas2ri.ri2py_dataframe(r_df)


print(pd_df_again)
