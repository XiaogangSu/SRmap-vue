import requests
import json
from shapely.geometry.geo import *


# 20200522
# 增加change_password 接口，允许用户更新密码
# 所有接口response返回json格式结果时增加了code字段，code==0 成功，code==-1 失败，方便前端快速判断服务器响应内容状态

headers={}
headers['Content-Type'] = 'application/json;charset=utf-8'

# host='http://127.0.0.1:5001'
host='http://121.199.14.136:5001'

# 注册用户
ret=requests.get(host+'/auth/register',{'username':'liujishu002','password':'123456'},headers=headers)
print(ret.json())
ret_obj=ret.json()
if ret_obj['code']==0:
       print('注册成功')
elif ret_obj['code']==-1:
       print('注册失败')


#  更新密码

ret=requests.get(host+'/auth/change_password',{'username':'liujishu002','password1':'123456','password2':'111111'},headers=headers)
print(ret.json())
ret_obj=ret.json()
if ret_obj['code']==0:
       print('修改密码成功')
elif ret_obj['code']==-1:
       print('修改密码失败')
########################################################################################################################
# 获取用户令牌token
ret=requests.get(host+'/auth/get_token',{'username':'liujishu002','password':'123456'},headers=headers)
print(ret.json())

ret=requests.get(host+'/auth/get_token',{'username':'liujishu002','password':'111111'},headers=headers)
print(ret.json())

token=ret.json()['token']
# token=''
########################################################################################################################

#添加一张照片或任意文件

headers={}
# headers['Content-Type'] = 'application/json;charset=utf-8'
headers['token']=token#用户令牌
headers['filename']='a.jpg'

ret=requests.post(host+'/dao/upload',files={'file':open('d:/a.jpg','rb')},headers=headers)
print(ret.json())

md5_1=ret.json()['md5']


headers['filename']='b.jpg'

ret=requests.post(host+'/dao/upload',files={'file':open('d:/b.jpg','rb')},headers=headers)
print(ret.json())

md5_2=ret.json()['md5']

########################################################################################################################
#获取照片

headers['token']=token#用户令牌
param={
       'md5':md5_1
        }

ret=requests.get(host+'/dao/download',param, headers=headers)
print(ret.content)
print(len(ret.content))


param={
       'md5':md5_2
        }

ret=requests.get(host+'/dao/download',param, headers=headers)
print(ret.content)
print(len(ret.content))
########################################################################################################################

# 添加一个地理要素


geo=Point(121.319306,31.240986)

# geo=LineString([[121.319306,31.240986],[121.353494,31.242901],[121.423194,31.230346]])

# geo=Polygon([[121.319306,31.240986],[121.353494,31.242901],[121.423194,31.230346],[121.319306,31.240986]])

geojson=mapping(geo)#转geojson

attrs={'k1':'v1','k2':'v2','k3':'v3','md5_list':[md5_1,md5_2]}

headers['token']=token#用户令牌
param={
       'title':'我添加的第一个地理要素',#title用于对地理要素的简要说明，并支持类似like查询
       'layer':'001',#使用layer标签标识要素所属图层
       'gj':geojson,#geojson格式的几何对象
       'attrs':attrs}#自由添加的属性

json_str=json.dumps(param, ensure_ascii=False)#将可能还有汉字的json格式的param转为字符串

data=bytes(json_str,encoding='utf-8')#将字符串转为utf-8格式编码的字节流

# 将字节流，post到add_feature接口
ret=requests.post(host+'/dao/add_feature',data=data, headers=headers)

print(ret.json())


########################################################################################################################
# 基于minx,miny,maxx,maxy地理范围检索用户的地理要素，同时可以添加可选的检索条件，包括，title中的keyword关键字，layer名称，t1和t2时间范围，offset偏移量，limit每页返回最大记录数

headers['token']=token#用户令牌
param={
       'keyword':'第一',#title用于对地理要素的简要说明，并支持类似like查询
       'layer':'001',#使用layer标签标识要素所属图层
       'offset':0,
       'limit':10,
       't1':'20200101010101',
       't2':'20201201010101',
       'minx':121,
       'miny':31,
       'maxx':121.5,
       'maxy':31.5
        }


ret=requests.get(host+'/dao/search_bound',param, headers=headers)
print(ret.text)
print(ret.json())

########################################################################################################################

#增加用户的私有数据信息k,v




headers['token']=token#用户令牌
param={ 'k':'tel',
       'v':'13581534627'}

json_str=json.dumps(param, ensure_ascii=False)#将可能还有汉字的json格式的param转为字符串

data=bytes(json_str,encoding='utf-8')#将字符串转为utf-8格式编码的字节流

# 将字节流，post到add_feature接口
ret=requests.post(host+'/dao/update_user_info',data=data, headers=headers)

print(ret.json())


#增加用户的私有数据信息k,attrs

attrs={'k1':'v1','k2':'v2','k3':'v3','md5_list':[md5_1,md5_2]}

headers['token']=token#用户令牌
param={ 'k':'attrs',
       'v':attrs}

json_str=json.dumps(param, ensure_ascii=False)#将可能还有汉字的json格式的param转为字符串

data=bytes(json_str,encoding='utf-8')#将字符串转为utf-8格式编码的字节流

# 将字节流，post到add_feature接口
ret=requests.post(host+'/dao/update_user_info',data=data, headers=headers)

print(ret.json())

########################################################################################################################
#获取用户私有数据信息
headers['token']=token#用户令牌
param={'k':'tel'}
ret=requests.get(host+'/dao/get_user_info',param, headers=headers)
print(ret.text)
print(ret.json())

headers['token']=token#用户令牌
param={'k':'attrs'}
ret=requests.get(host+'/dao/get_user_info',param, headers=headers)
print(ret.text)
print(ret.json())