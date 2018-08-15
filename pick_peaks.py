"""
regex that has at least:
-6 char
-one lower case character
-one upper case character
-one digit

"""

import re
the_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{6,}$"

