import json
# 初始化变量
_id = ''
userRealname = ''
userIdcardNo = ''

# 1.将json文件转换成python的数据类型(dict)
jsonFile = open('test2.json','r',encoding='utf8')
# jsonObject为dict类型--dict_keys(['applyInfo', 'bbgScoreCardResult', 'bbgReport'])
jsonObject = json.load(jsonFile)

print(jsonObject)
# 申请信息 applyInfo <class 'dict'>
applyInfo = jsonObject['applyInfo']
_id = applyInfo['_id']
userRealname = applyInfo['userRealname']
userIdcardNo = applyInfo['userIdcardNo']
print('%s,%s,%s'%(_id,userRealname,userIdcardNo))


# 申请分数 bbgScoreCardResult ,dict_keys(['contentList'])
if 'bbgScoreCardResult' in jsonObject:
    bbgScoreCardResult = jsonObject['bbgScoreCardResult']
    print(bbgScoreCardResult)
    # contentList --<class 'list'>
    contentList = bbgScoreCardResult['contentList']
    for item in contentList:
        # item  <class 'dict'>
        title = item['title']
        value = item['value']
        print(title+':'+value+',',end='')
        pass
    print('')
    print("结束")
    pass


# 申请报表 bbgReport <class 'dict'> key:Loan ,CurrAccountInfo
print("=================================================")
bbgReport = jsonObject['bbgReport']
print(bbgReport)
# CreditDetail,dict_keys(['Loan'])

CreditDetail = bbgReport['CreditDetail']
Header = bbgReport['Header']
Loan = CreditDetail['Loan']
print(type('Loan'))
for item in Loan:
    Type = ''
    PaymentCyc = ''
    GuaranteeType = ''
    CreditLimitAmount = ''
    OpenDate = ''
    EndDate = ''
    PaymentRating = ''
    ScheduledPaymentAmount = ''
    Balance = ''

    # item dict_keys(['ContractInfo', 'CurrAccountInfo'])
    print(type(item))
    print(item.keys())
    ContractInfo = item['ContractInfo']
    if 'ContractInfo' in item:
        ContractInfo = item['ContractInfo']

        Type = ContractInfo['Type']
        if ('PaymentCyc' in ContractInfo):
            PaymentCyc = ContractInfo["PaymentCyc"]
        GuaranteeType = ContractInfo['GuaranteeType']
        CreditLimitAmount = ContractInfo['CreditLimitAmount']
        OpenDate = ContractInfo['OpenDate']
        EndDate = ContractInfo['EndDate']
        PaymentRating = ContractInfo['PaymentRating']
        pass
    if 'CurrAccountInfo' in item:
        CurrAccountInfo = item['CurrAccountInfo']
        ScheduledPaymentAmount = CurrAccountInfo['ScheduledPaymentAmount']
        Balance = CurrAccountInfo['Balance']
        pass
    print('%s,%s,%s,%s,%s,%s,%s,%s,%s'%(Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
                                        OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance))
