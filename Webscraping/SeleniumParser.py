input_file = open('plan_numbers_raw.txt', 'r')
raw_text = input_file.readlines()
input_file.close()

plan_numbers = ''.join([c for line in raw_text for c in line if c.isdigit() or c == '#']).split('#')

output = open('plan_numbers.txt', 'w')
[output.write(p + '\n') for p in plan_numbers[1:]]
output.close()