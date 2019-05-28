# 141.Dictionary comprehension with if else - Python tutorial 138
# we want this output d = {a: even, a:odd}
even_odd = {i:("even" if i%2==0 else "odd")for i in range(1,11)}
print(even_odd)