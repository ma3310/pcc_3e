from inspect import currentframe, getframeinfo
file = currentframe()

bicycles = ['trek', 'Canondale', 'redline', 'specialized']
# Initiate tuple
immutable_bicycles = ()

# Initiate 1-element tuple,trailing comma is necessary.
immutable_bicycles = ('trek',)

print(immutable_bicycles.__class__)




