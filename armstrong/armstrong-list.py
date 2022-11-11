from inspect import currentframe, getframeinfo
file = currentframe()

bicycles = ['trek', 'Canondale', 'redline', 'specialized']
print("List bicycles:", bicycles)
print(f"First element of bicycles: bicycles[0] = {bicycles[0].title()}.")
print(f"Last element of bicycles: bicycles[-1] = {bicycles[-1].title()}.", '\n')

# Change the 4th element
statement = "bicycles[3] = 'phoenix'"
print('Execute:', statement); exec(statement)
print(f'Current bicycles: {bicycles}\n')

# Insert element as 4th element
statement = "bicycles.insert(3, 'specialized')"
print('Execute:', statement); exec(statement)
print(f'Current bicycles: {bicycles}')

# Delete last element
statement = "del bicycles[-1]"
print('\nExecute:', statement); exec(statement)
print(f'Current bicycles: {bicycles}')

# Add element
statement = "bicycles.append('phoenix')"
print('\nExecute:', statement); exec(statement)
print(f'Current bicycles: {bicycles}')

# Add multiple elements (Add another list)
statement = "bicycles.extend(['forever', 'giant'])"
print(f'\n[Line {file.f_lineno}] Execute:', statement, 'to add another list.'); exec(statement)
print(f'[Line {file.f_lineno}] Current bicycles: {bicycles}')

# Pop last element
last = ''
statement = "last = bicycles.pop()"
print('\nExecute:', statement); exec(statement)
print(f'Popped value: {last}\nCurrent bicycles: {bicycles}')

# remove first occurrence element by value
statement = "bicycles.remove('trek')"
print('\nExecute:', statement); exec(statement)
print(f'Current bicycles: {bicycles}')

# List Sorting for presenting
print(f'\n[Line {file.f_lineno}] Temporarily sorted bicycles:', sorted(bicycles))
print(f'[Line {file.f_lineno}] Original bicycles:', bicycles)


# Pop 3rd element
specified = ''
statement = "specified = bicycles.pop(2)"
print('\nExecute:', statement); exec(statement)
print(f'Popped value: {specified}\nCurrent bicycles: {bicycles}')

# Change the order of List
bicycles.sort()
print(f'\n[Line {file.f_lineno}] Permanently sorted bicycles:', bicycles)
bicycles.sort(reverse=True)
print(f'[Line {file.f_lineno}] Permanently reversely sorted bicycles:', bicycles)
bicycles.reverse()
print(f'[Line {file.f_lineno}] Permanently reverse bicycles:', bicycles)

# Length of list
print(f'\n[Line {file.f_lineno}] !!for loop demonstration, statements in loop must be indented by same spaces!!')
print(f'[Line {file.f_lineno}] {len(bicycles)} bicycles in the list, they are:')
for bicycle in bicycles:
    print(f"\t{bicycle}")
print(f'[Line {file.f_lineno}] {len(bicycles)} bicycles in the list, last 2 (bicycles[-2:]) are:')
for bicycle in bicycles[-2:]:
    print(f"\t{bicycle.title()}")

# Copy list
copied_bicycles = bicycles[:]
print(f'\n[Line {file.f_lineno}] Copy list: copied_bicycles = bicycles[:]')
print(f'[Line {file.f_lineno}] copied_bicycles =', copied_bicycles)


# generate number list by range()
number_list = list(range(2, 27, 3))
print(f'\n[Line {file.f_lineno}] list(range(2, 27, 3)) =', number_list)
print(f'[Line {file.f_lineno}] list(value**4 for value in range(6)) =', list(value**4 for value in range(6)))
print(f'[Line {file.f_lineno}] list(value**5 for value in range(6)) =', list(value**5 for value in range(6)))

print(f'\n[Line {file.f_lineno}] for-loop', range(1, 6))
for value in range(1, 6):
    print('\t', value)
digits = []
print(f'[Line {file.f_lineno}] for-loop range(6) print value ** 2, 3, 5')
for value in range(6):
    digits.append(value)
    digits.extend([value**2, value**3, value**5])
    print('\t', value, value ** 2, value ** 3, value ** 5)

print('\nStatistics of digits:', digits)
print(f'\tmin(digits) =', min(digits))
print(f'\tmax(digits) =', max(digits))
print(f'\tsum(digits) =', sum(digits))




