#coding=utf-8

def lst2unicode(lst):
    st=u''
    if isinstance(lst,list):
        st+='('
        for l in lst:
            st+="u'%s'"%l
            st+=','
        st+=')'
    return st

una=u'unicode汉字'

lst=[]

lst.append(una)
lst=lst2unicode(lst)

print (lst)
for i in lst:
    print(i)

bstr=str(una)

print bstr


tb_yhq_murl='aaa&bbb'
tb_yhq_murl=tb_yhq_murl.replace('&','&amp;')
print tb_yhq_murl