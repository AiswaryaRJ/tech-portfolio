import pandas as pd
import numpy as np
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'], name='Product Reviews')
pd.Series([1, 2, 3, 4, 5], index=['A','B','C','D','E'], name='Numbers')
