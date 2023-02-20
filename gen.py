print("""<button onclick="show(1)"><h1><py-script>print (liste["1n"])</py-script></h1></button>""")

for i in range (50):
    print("<button onclick=", '"show(',i, ')"', '><h1><py-script>print (liste["', i,'n"])</py-script></h1></button>', sep='')