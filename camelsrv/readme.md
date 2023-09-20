## 获取用户数据接口

#### 接口URL
> https://<域名>/user/query/<用户id>

#### 请求方式
> GET

#### 请求url参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
query | id\|gacha_token\|orders.{id\|complement.*}" | String | 否 | 指定要获取的成员树, 在下文会解释, 无此参数则等价于query=\*

#### 成功响应示例
```javascript
{"code": 1, 
"msg": "ok", 
"dat": {"id": "1145141919810", "gacha_token": 3, "orders": [{"id": 1, "complement": null}, {"id": 2, "complement": {"id": 3, "owner": {}, "items": {"0": 1, "1": 102}, "extra": {"favorite": "仙人掌"}, "complement": {}, "status": 2}}]}
}
```
#### 失败响应示例
```javascript
{
    "code": -1,
    "msg": "Some random err msg.",
    "dat": {}
}
```
#### 响应状态
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
code | 1 or -1 | Integer | 状态码（成功or失败）
msg | ok/<错误信息> | String | 获取成功/失败 

#### User(用户)数据成员
成员名 | 示例值 | 成员类型 | 参数描述
--- | --- | --- | ---
id | 114514 | String | 校园卡号
gacha_token | 3 | Integer | 抽卡剩余次数
order_token | 2 | Integer | 可发起订单剩余次数
possessions | [1, 114, 514] | Integer Array | 拥有的装备列表
orders | [\<order>, \<order>] | Order ref Array | 发起的订单列表

## 获取订单数据接口

#### 接口URL
> https://<域名>/order/query/<订单id>

#### 请求方式、请求URL参数、成功响应示例、失败响应示例、响应状态
同上

#### Order(订单)数据成员

成员名 | 示例值 | 成员类型 | 参数描述
--- | --- | --- | ---
id | 333 | Integer | 订单id
owner | 114514 | String | 发起人用户id
items | {"0":1, "1": 100, "2":203} | Integer Dictionary | 各槽位选择的装备
extra | {"favorite_food":"仙人掌"} | String Dictionary | 额外信息
complement | \<order> | Order ref \| null | 情侣订单?
status | 0 | 0 : 未提交 \| 1 : 等待配对 \| 2 : 已提交 | 订单状态

## 成员树语法

#### 示例1:
> a.{b|c}

意为获取查询到数据的a成员, 并获取a成员的b成员和c成员

#### 示例2: 
> {a|b.child1|c.{child2|child3}}

意为获取查询到数据的a, b和c成员, 并获取b的child1成员和c的child1及child2成员

#### 示例3: 
> \*.\*

意为获取查询到数据的全部成员, 并且对于全部成员需要再递归一次获取全部成员

注: 试图查询不存在的成员或查询非Model数据的成员不会使请求失败, 服务器会忽略对不存在的成员的查询

## 发起订单

#### 接口URL
> https://<域名>/order/create/

#### 请求方式
> POST

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
user_id | 1145141919810 | String | 是 | 用户id
cp_inv_code | 364364 | int | 否 | 情侣邀请码, 若填入则会将该订单与邀请码对应的订单配对

#### 成功响应示例
```javascript
{"code":1, "msg":"ok", "dat": 333}
```
注: dat的值为创建的订单id

#### 失败响应示例
```javascript
{
    "code": -1,
    "msg": "Some random err msg.",
    "dat": {}
}
```

#### 响应状态
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
code | 1 or -1 | Integer | 状态码（成功or失败）
msg | ok/<错误信息> | String | 获取成功/失败

## 为订单创建邀请码

#### 接口URL
> https://<域名>/order/start_cp/

#### 请求方式
> POST

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
user_id | 1145141919810 | String | 是 | 用户id
order_id | 364364 | int | 是 | 需要创建邀请码的订单id

#### 成功响应示例
```javascript
{"code":1, "msg":"ok", "dat": "52YJSP"}
```
注: dat的值为邀请码

#### 失败响应示例
```javascript
{
    "code": -1,
    "msg": "Some random err msg.",
    "dat": {}
}
```

## 提交订单

#### 接口URL
> https://<域名>/order/submit/

#### 请求方式
> POST

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
user_id | 1145141919810 | String | 是 | 用户id
order_id | 364364 | int | 是 | 订单id
items | {"0":1, "1":103, "2":200} | Integer Dictionary | 是 | 选择的装备
extra | {"favorite":"无花果"} | String Dictionary | 是 |额外信息

#### 成功响应示例
```javascript
{"code":1, "msg":"ok", "dat": {}}
```

#### 失败响应示例
```javascript
{
    "code": -1,
    "msg": "Some random err msg.",
    "dat": {}
}
```
## 五连抽

#### 接口URL
> https://<域名>/user/gacha5/

#### 请求方式
> POST

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
user_id | 1145141919810 | String | 是 | 用户id

#### 成功响应示例
```javascript
{"code":1, "msg":"ok", "dat": [1, 2, 3, 4, 5]}
```
注: dat的值为此次抽卡获取的装备列表
#### 失败响应示例
```javascript
{
    "code": -1,
    "msg": "Some random err msg.",
    "dat": {}
}
```