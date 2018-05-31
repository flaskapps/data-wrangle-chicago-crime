# Data-wrangling component


Write out `scripts/bootstrap.py` and `scripts/wrangle.py` to 
fetch and filter the data at:

https://data.cityofchicago.org/Public-Safety/Crimes-One-year-prior-to-present/x2n5-8w5q/data

There should be a `stash` directory that holds the raw file. 

And a `static/data` directory that holds the wrangled/cleaned/filtered data file.


### Snippet code for paths

```py
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
```
