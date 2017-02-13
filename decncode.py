#coding=utf-8
#编码转换实例

hz_unicode=u'汉字'
print hz_unicode


hz_utf8='汉字'
print hz_utf8

s=str(hz_utf8)
print s

#去掉前缀u
hz_no_u=hz_unicode.encode('raw_unicode_escape')
hz_n_utf8=hz_no_u.encode('utf8')
print hz_no_u,hz_n_utf8

#unicode转 utf-8
hz_z_utf8=hz_unicode.encode('utf8')
print hz_z_utf8

#unicode转str,会出现错误UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
hz_str=str(hz_unicode)
print hz_str

