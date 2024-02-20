# The percentage sign can also be used for formatting strings
# In this case %d stands for a decimal value and .1f stands for a floating point value with 1 decimal point precision
now, tonight = 32, 23.75
print('It is %d C° outside. It is expected to be %.1f C° tonight. ' % (now, tonight))
