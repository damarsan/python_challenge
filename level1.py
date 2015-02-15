#!/usr/bin/python
import string
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet2 = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

repls = dict(zip(alphabet,alphabet2))

message = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
	  bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
      sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

#res = reduce(lambda a, kv: a.replace(*kv), repls.iteritems(), str)

print ''.join(repls.get(x, x) for x in message)

url="http://www.pythonchallenge.com/pc/def/map.html"

a1 =  str(alphabet).strip('[]')
a2 =  str(alphabet2).strip('[]')


trans = string.maketrans(a1,a2)
print (url.translate(trans))
