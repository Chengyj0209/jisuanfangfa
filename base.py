import base64
f=open('1.png','rb')
lsf=base64.b64encode(f.read())
f.close()
with open('ans.txt','w') as fileans:
	fileans.write(str(lsf))
