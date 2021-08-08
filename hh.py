table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr={}
for i in range(58):
	tr[table[i]]=i
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608

def bta(x):
	r=0
	for i in range(6):
		r+=tr[x[s[i]]]*58**i
	return (r-add)^xor

def atb(x):
	x=(x^xor)+add
	r=list('BV1  4 1 7  ')
	for i in range(6):
		r[s[i]]=table[x//58**i%58]
	return ''.join(r)
##-------------------------------------------
import easygui as g
import sys
while 1:
        choce = g.buttonbox(msg='仅供参考^_^\n\n请选择转换类型：', title='视频编号转换器', choices=('av转bv', 'bv转av','退出'))
##-------------------------------------------av -> bv
        if choce == 'av转bv':
                avh = g.enterbox(msg='输入av号（不带av）：', title='av转bv', default='', strip=True)
                if avh == None  :
                        None
                else :
                        avh = int(avh)
                        if avh < 0 :
                                g.msgbox('av号不为负数！','警告')
                        else :
                                bvh = atb(avh)
                                g.msgbox(bvh,'转换结果')
##---------------------------------------------bv -> av
        elif choce == 'bv转av' :
                bvh = g.enterbox(msg='输入bv号（带BV）：', title='bv转av', default='', strip=True)
                if bvh == None :
                        None
                else :
                        avh = bta(str(bvh))
                        g.msgbox(avh,'转换结果')
        else :
                sys.exit(0) 
