# The contents of this file seem to have no bearing bug reproduction
# - I001 seems to always be checked for this file, as specified in pyproject.toml
#
# You can illustrate this by re-ordering these imports
import os
import sys

# The following code only exists to use the imports and avoid F401 (imported but unused)
print(os)
print(sys)
