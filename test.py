from __init__ import stacky_error

try:
    with open("logs", 'r') as f:
        pass
except Exception as e:
    stacky_error(e)
