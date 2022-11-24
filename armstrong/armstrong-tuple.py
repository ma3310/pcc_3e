from inspect import currentframe, getframeinfo
file = currentframe()

bicycles = ['trek', 'Canondale', 'redline', 'specialized']
# Initiate tuple
# tuple = immutable list
immutable_bicycles = ()

# 检查 tuple 是否为空
if not immutable_bicycles:
    print(f'[Line {file.f_lineno}] immutable_bicycles is empty.')

for bicycle in immutable_bicycles:
    print(f'[Line {file.f_lineno}] no contents')

# Initiate 1-element tuple,trailing comma is necessary.
immutable_bicycles = ('trek',)

print(immutable_bicycles.__class__)




