st = [9, 4, 1, 7]

st.append(3)
st.pop()

while st:
    i = st.pop()
    if (i < 7): st.append(i+1)
    print(i)

print(st)
print(st is None) # False