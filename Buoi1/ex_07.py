print("print to text'Done' for end): ")
lines = []
while True:
    line = input()
    if line.lower()== 'Done':
       break
    lines.append(line)
print("\n Row update to Upper: ")
for line in lines:
    print(line.upper())    