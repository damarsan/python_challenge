#!/usr/bin/python
from string import maketrans
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet2 = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

repls = dict(zip(alphabet,alphabet2))

message = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
	  bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
      sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


print ''.join(repls.get(x, x) for x in message)


a1 =  str(alphabet).strip('[]')
a2 =  str(alphabet2).strip('[]')

trantab = maketrans(a1, a2)
url="map"

print url.translate(trantab)