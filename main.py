import json
import demjson

keyword=["name","value"]
result=""
inputstr="""[
{
    "domain": ".aliyun.com",
    "expirationDate": 1612270772,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__yunlog_session__",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1612184372711",
    "id": 1
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1667982699,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1265750652.1604910699",
    "id": 2
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "_hvn_login",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "6",
    "id": 3
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "_samesite_flag_",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "true",
    "id": 4
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "_tb_token_",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "5360ae3fab1e3",
    "id": 5
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "a_d",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": ".aliyun.com",
    "id": 6
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "a_l",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "aliyun",
    "id": 7
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "a_u",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "28454D5540FE3264C7A193029123106035846710E8282081B6D216EBE1BC7BBFF339700ECB94E1934E3DC6599CE9937328DC61AF47D7A6695CCB314328CEE212E9B9F653710BC04B36E28011E87409D8BC603EFD2BDF18F760938C73846B3C7AD7D78A492E5C13E6A520EF44B0907F7FE931DEA17953EAA00DF93F2B2884936194823EEE601E121D201E84EACEC6CC920B2C9148F96A56F69F31FDA8A783A7B383D88E48E0AADD494367BAF4631D9150F24F6D408A3922398664B8A774EE9CB0713F65F1835A256BD5CF6CE019E47522302705500F7FF173D380C228128702FDCC8135D312030B98A0F1104CD898A582A8743940C02BDF11679B96779F65E1027FE1C5142D3601F58610B70A60A7ACB84B59003833B17C5DB3E8D2723C017F94229CB28EFB8FF706F5C1B1A988D0EBC592C0FCADF06FA32FB8355C4A1E2562681856FB3CE75325D9143906D1D017FBF4B22A7065C2749EF33D6916B5C93B41A90745ABE0C3A5A9C44BD343C922E33DEB1AB6268E826AFCC2CDC6A5635487BD8C44A11CC620A88ED9F57EC5F0BC575E097E231A658FEBFD25ED4DA34489F76E10B127E5BF2FE4A630460053F866C35B3B0BB4D4A6965D850664DCCBCFC1BB6CD72EAAFC065D809E5DF76F2C529F1F8EA492C524D5A67FEDA913BF657513AAF28D6776F42FE5876E5DFE2404AE8F8BD22CC264928C35708BC3CF0ED5238E750B4F3D7AAB9B8B9D36A9C1D3FE50B973C9495F6D4DCA63E20F32247AC669B2BE526A75081C04DC6A52A0791842E7E5FE0276C77D854B0FA9998DF6E30872171CC5BF28DC61AF47D7A6695CCB314328CEE2123BF70533C40629C0B2AAB83ED9D0369E403A5A447E7BE90982E6E43E81F27B32A569FB179B957EE01A598B9061B25EBF501A4FC6802D648E0E3E242C75A36FB806B448C5CE88490A94B2231D86784C543DED84CA8073709D30AD7A239B3A1C590799BC19AA09C9D33C601E77A97A668F54D996053CB1E577F3E13F6953B81A30",
    "id": 8
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "a_u_t",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "237A3383A9A5CFAA9E37D4648AC39E57",
    "id": 9
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1613568934,
    "hostOnly": false,
    "httpOnly": false,
    "name": "activeRegionId",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "cn-shanghai",
    "id": 10
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1614784185,
    "hostOnly": false,
    "httpOnly": false,
    "name": "aliyun_choice",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "CN",
    "id": 11
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1614781454.105792,
    "hostOnly": false,
    "httpOnly": false,
    "name": "aliyun_country",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "CN",
    "id": 12
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "aliyun_lang",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "zh",
    "id": 13
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1927549454.105919,
    "hostOnly": false,
    "httpOnly": false,
    "name": "aliyun_site",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "CN",
    "id": 14
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1612699239,
    "hostOnly": false,
    "httpOnly": false,
    "name": "aliyunAliothSource",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "eyJzcG0iOiI1MTc2LjIxMTAzNDA2LkpfNjE3NDA0MzI1MC5kNDY1Iiwic2NtIjoiMjAxNDA3MjIuMzYyMi40LjM0NDkifQ==",
    "id": 15
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1614686832,
    "hostOnly": false,
    "httpOnly": false,
    "name": "aliyunMerakSource",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "WyJzd2FzLjkyNjkyNDUuMjQzMzYzNjI3Lm5vbi4yMDE0MDcyMnxNXzI1NTU5NXxffFZfMS4yNTU1OTUuIiwidm0uMTI0OTA4MjAuMTkwODcxNjEyLm5vbi4yMDE0MDcyMnxNXzM5MjIzOXxffFZfMS4zOTIyMzkuIiwiaGJyX2JhY2t1cHN0b3JhZ2VfYmFnLjkyNTA4NzIuODQ0NzIzNDc4Lm5vbi4yMDE0MDcyMnxNXzI0MzY3OHxffFZfMS4yNDM2NzguIl0=",
    "id": 16
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "aone_user_ticket",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "\"NDIyZTA0OTUtYjY5Ni00NTA4LTllMzUtYTRjMzYxYWViMDg2U3VuIEphbiAzMSAyMToyOToyNCBDU1QgMjAyMQ==\"",
    "id": 17
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "aone_user_uuid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "422e0495-b696-4508-9e35-a4c361aeb086",
    "id": 18
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "CC-XSRF-TOKEN",
    "path": "/",
    "sameSite": "lax",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "c7e85b7c-248c-44c7-9a32-63d0494f227a",
    "id": 19
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1923020689.080613,
    "hostOnly": false,
    "httpOnly": false,
    "name": "cna",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "naclFvp+mTwCAXccytAhzRkR",
    "id": 20
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1627743302,
    "hostOnly": false,
    "httpOnly": false,
    "name": "console_base_assets_version",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "3.22.4",
    "id": 21
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "cookie2",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "102609bf9c62b98050b3738964f1d9e9",
    "id": 22
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "csg",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "2e900693",
    "id": 23
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1627743299,
    "hostOnly": false,
    "httpOnly": false,
    "name": "currentRegionId",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "cn-shanghai",
    "id": 24
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "FECS-UMID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "%7B%22token%22%3A%22Y1f38f991e50593c3b8f284894767fab1%22%2C%22timestamp%22%3A%2283360701595F5A46514E657C%22%7D",
    "id": 25
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "FECS-XSRF-TOKEN",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "8680845e-5a40-4f9c-82c3-aa5a83679042",
    "id": 26
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "hsite",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "6",
    "id": 27
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "hssid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "16edlm8qr2pw-3wZ2AV_Ayg1",
    "id": 28
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1627744326,
    "hostOnly": false,
    "httpOnly": false,
    "name": "isg",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "BLKy42gPBtUCfTrnOnC4-JP7A_iUQ7bdlFiPt3yLw2VQD1IJZNY67Yln-6uzfy51",
    "id": 29
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1627744326,
    "hostOnly": false,
    "httpOnly": false,
    "name": "l",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "eBTjOVxRjNKQlbU9BOfwnurza77O_IRAguPzaNbMiOCPOX5J5gtAW6Mtg7YvCnGVh6DyR3ljL4J6BeYBqBOInxv9yIDpAHMmn",
    "id": 30
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "login_aliyunid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "\"%E7%A3%81%E5%9C%BA%E7%9A%84%E5%B0%BD%E5%A4%B4\"",
    "id": 31
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "login_aliyunid_abi",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "\"BG+6h4NSxB84e0d9fae2d543f40744da4cb68e1001f+rbEzydASGzVOaJin8OVTHkuohe4t1kDZ9pMBVeK8/SzP2YFgIq0=\"",
    "id": 32
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "login_aliyunid_csrf",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "_csrf_tk_1339512189454977",
    "id": 33
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "login_aliyunid_luid",
    "path": "/",
    "sameSite": "lax",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "\"BG+Yv1ozSM05601b4195bae9151075fd648e18c1e4e+C8zs72v520vFnmiUOaav2g==\"",
    "id": 34
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1643725454.105469,
    "hostOnly": false,
    "httpOnly": false,
    "name": "login_aliyunid_pk",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1326899316147817",
    "id": 35
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1643725454.105536,
    "hostOnly": false,
    "httpOnly": false,
    "name": "login_aliyunid_pks",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "\"BG+9mRGZ12ZVVha3ZYzejYXL7uufrJvnZHRYkaqxuGYD/w=\"",
    "id": 36
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "login_aliyunid_ticket",
    "path": "/",
    "sameSite": "lax",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "_k0pof_BNTwUhTOoNC1ZBeeMfKJzxdnb95hYssNIZor6q7SCxRtgmGCbifG2Cd4ZWazmBdHI6sgXZqg4XFWQfyKpeu*0vCmV8s*MT5tJl3_1$$wsCOxSTAB*oyWK6cuYVLs9i0pvrfApMiRWEIa0WoNh0",
    "id": 37
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "ping_test",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "true",
    "id": 38
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "t",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "98d70a3eaf92332e288a8ed69784af84",
    "id": 39
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1627744326,
    "hostOnly": false,
    "httpOnly": false,
    "name": "tfstk",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "cRjcBvsH4Z8bbkYlRotfLaQN4bQGa0kJMht54gIBXqgdNbjH3svSzVHXAYdYAe01.",
    "id": 40
},
{
    "domain": ".aliyun.com",
    "hostOnly": false,
    "httpOnly": true,
    "name": "UC-XSRF-TOKEN",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "c946ebb9-06ff-490a-bb6c-f3eb9b65dfab",
    "id": 41
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1624861871,
    "hostOnly": false,
    "httpOnly": false,
    "name": "UM_distinctid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "176a80b2633edb-01bf7ccd41f584-59492816-161012-176a80b2634b3f",
    "id": 42
},
{
    "domain": ".aliyun.com",
    "expirationDate": 1612270771,
    "hostOnly": false,
    "httpOnly": false,
    "name": "xlly_s",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 43
},
{
    "domain": "edu.aliyun.com",
    "expirationDate": 1627742935.064125,
    "hostOnly": true,
    "httpOnly": false,
    "name": "_bl_uid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "U5kCgkb9mFwo88u9zukexqRk66Cm",
    "id": 44
},
{
    "domain": "edu.aliyun.com",
    "expirationDate": 1612192733.823488,
    "hostOnly": true,
    "httpOnly": true,
    "name": "acw_tc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "781bad0c16121909339585605e7d3d1cd2cf129431ecdb7ec643428d47064b",
    "id": 45
},
{
    "domain": "edu.aliyun.com",
    "hostOnly": true,
    "httpOnly": true,
    "name": "aliyungf_tc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "923cdf540298d2111ce28f9777cc9714bef2f5c40b342554e80abd4b8106c200",
    "id": 46
},
{
    "domain": "edu.aliyun.com",
    "expirationDate": 1627916983,
    "hostOnly": true,
    "httpOnly": false,
    "name": "CNZZDATA1261859658",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "208029908-1612187052-https%253A%252F%252Fdeveloper.aliyun.com%252F%7C1612187052",
    "id": 47
},
{
    "domain": "edu.aliyun.com",
    "hostOnly": true,
    "httpOnly": true,
    "name": "PHPSESSID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "hg63m5gismp6qm0v1fef5seen5",
    "id": 48
},
{
    "domain": "edu.aliyun.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "SERVERID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "f75e42367999ddecfa6104b9951aee0b|1612192458|1612192458",
    "id": 49
}
]"""
for eachline in inputstr.split("\n"):
    if keyword[0] in eachline:
        result+=eachline[eachline.index(":")+3:eachline.rindex('"')]+"="
    if keyword[1] in eachline:
        result+=eachline[eachline.index(":")+3:eachline.rindex('"')]+";"
exit(0)