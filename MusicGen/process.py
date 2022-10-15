f = open("test.txt")
lines = f.read()
lines = "\n" + lines
a = lines.split("</tr>")
dic = {}
for i in range(len(a)):
    a[i] = a[i].replace("<tr>\n", "")[5:]
    b = a[i].split("</td>\n<td>")
    try:
        if "/" in b[3]:
            c = b[3].split("/")
            dic[c[0]] = int(b[0])
            dic[c[1]] = int(b[0])
        else:
            dic[b[3]] = int(b[0])
    except:
        pass
print(dic)
