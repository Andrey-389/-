first = input('1 число- ')
second = input('2 число- ')
third = input('3 число- ')
if first == second and first == third and second == third:
        print(3)
elif first == second or first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)