st = [9, 4, 8, 7]

st.append(3)
st.append(5)
st.append(1)
print(st)

print(st.pop())
print(st)

while st: print(st.pop())
print(st)
print(st is None) # False