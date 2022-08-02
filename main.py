from optionprice import Option
# example 1 
print ("hello world")


# TODO (get TDA API to get option)A
def get_option():
  pass

# mystery method.
def evaluate_option_1():
  # for example TQQQ has a price of 33.36, and this trades the 79.25% historical volatility
  # of 14%, and at a strike of of 14.00. R = risk free rate
  option_foo = Option(False, "call", s0=33.36, k=14.00, sigma=0.7925, r=.0267, t=5)
  print(option_foo)
  print(option_foo.getPrice())
  print(option_foo.getPrice(method="MC", iteration=200000))

print(evaluate_option_1())