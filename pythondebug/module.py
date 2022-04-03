import numpy as np
import pandas as pd

def test_function():
    """Test function for notebook debugging examples."""

    df = pd.DataFrame(
        np.random.rand(3, 3),
        columns=["col1", "col2", "col3"],
        index=[1, 2, 1]
    )
    df = df.groupby(df.index).sum()

    # For IPython/notebook debugging solution
    #from IPython.core.debugger import set_trace
    #set_trace()

    print("Value of col3 at index 2 is {}".format(df.loc[2, "col4"]))

    return df
