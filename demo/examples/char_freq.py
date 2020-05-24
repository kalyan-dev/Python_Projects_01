# char frequency


st = "this is awesome. That is also great".upper()

for n in range(65,91):
    ch = chr(n)
    if st.count(ch) == 0:
        continue
    print(f"{ch} - {st.count(ch)}")