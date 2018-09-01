# STX0102
def LRC_calc(data):
	buff=[0]*len(data)
	for i in range(len(data)):
		buff[i]=hex(ord(data[i]))[2:]

	buff.append('02')
	buff2=[0]*len(buff)
	for i in range(len(buff)):
		buff2[i]=int(buff[i],16)

	lrc=hex(sum(buff2))[2:]
	n=len(lrc)
	if n > 2:
		lrc=lrc[n-2:]
	#print(lrc)
	return lrc

#LRC_calc('01421X0016')