def all_variants(text):
    n = len(text)
    for lenght in range(1, n+1):
        for start in range ( n - lenght +1):
            yield text[start:start+lenght]


a = all_variants("abc")
for i in a:
    print(i)