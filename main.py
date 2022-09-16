# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

l = [0,1,2,3,4,5,6,7,8]
print(mean_var_std.calculate(l))

# Run unit tests automatically
main(module='test_module', exit=False)