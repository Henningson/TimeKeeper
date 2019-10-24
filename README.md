# TimeKeeper
More functionality will be added as I need it. Feel free to copy and change everything as you need.  
Usage is shown in the code example below:

``` 
from time_keeper import TimeKeeper

# You can use datetime.time objects and ints interchangeably.
# Remember that when you just use ints, only full hours are available right now.

# Will pause the execution inbetween 1pm and 2pm.
tk = TimeKeeper(13, 14)
tk.check_time()


# Will pause the execution from now until 2:32pm.
tk = TimeKeeper(datetime.datetime.now().time(), datetime.time(14, 32))
tk.check_time()
```
