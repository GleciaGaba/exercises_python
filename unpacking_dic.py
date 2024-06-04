#unpacking keys
d = {1: "un", 2: "two", 3:"three"}
a, b, c = d.values()
print(a)
print(b)
print(c)
#unpacking values
a, b, c= {1: "un", 2: "two", 3:"three"}
print(a)
print(b)
print(c)

#unpacking keys and values inside a dic
d = {1: "un", 2: "two", 3:"three"}

(a_key, a_value), (b_key, b_value), (c_key, c_value) = d.items()

print(f"{a_key}={a_value}")
print(f"{b_key}={b_value}")
print(f"{c_key}={c_value}")