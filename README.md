# Stacky

This is a simple package which when used as demonstrated below, will automatically open a web browser and query Stack Overflow for the Exception received.


```python
from stacky import stacky_error

try:
    # do something here
except Exception as e:
    stacky_error(e))

```

Stacky uses the **webbrowser** library to open your default webbrowser and automatically query StackOverflow for your exception.
 