import json
file = open('1.json','r',encoding='utf8')
lines = file.readlines()
strALl = ''
# 结果文件
resultFile = open('resultFile1.csv', 'w',encoding='utf-8')
for line in lines:
    # print(line)
    strALl += line
# strAll 存储了整个文件字符串
jsonArr = strALl.split(";")
i = 0
for sigleJson in jsonArr:
    i += 1
    # print(sigleJson)
    # 1.将字符串转换成json格式的字符串
    # jsonOrigin = json.dumps(sigleJson)
    # 2.将json格式字符串转换成python对象
    jsonObjct = json.loads(sigleJson)


    # 输出格式
    str = "{_id},{userRealname},{userIdcardNo},{Type}," \
          "{PaymentCyc},{GuaranteeType},{CreditLimitAmount},{OpenDate},{EndDate},{PaymentRating}," \
          "{ScheduledPaymentAmount},{Balance}"

    # 申请信息 applyInfo
    applyInfo = jsonObjct["applyInfo"]
    _id = ''
    userRealname = ''
    userIdcardNo = ''
    # 报表信息 bbgReport
    bbgReport = jsonObjct["bbgReport"]
    # 客户id
    _id = applyInfo["_id"];
    userRealname = applyInfo["userRealname"]
    userIdcardNo = applyInfo["userIdcardNo"]
    # bbgReport->CreditDetail
    CreditDetail = bbgReport["CreditDetail"]
    # CreditDetail-> Loan(list)
    Loan = CreditDetail['Loan']
    for l in Loan:
        Type = ''
        PaymentCyc = ''
        GuaranteeType = ''
        CreditLimitAmount = ''
        OpenDate = ''
        EndDate = ''
        PaymentRating = ''
        ScheduledPaymentAmount = ''
        Balance = ''
        # Type	PaymentCyc	GuaranteeType	CreditLimitAmount	OpenDate	 EndDate	PaymentRating
        # GuaranteeType CreditLimitAmount OpenDate EndDate PaymentRating
        #   ScheduledPaymentAmount	Balance
        if ('ContractInfo' in l):
            ContractInfo = l["ContractInfo"]
            Type = ContractInfo["Type"]
            if ('PaymentCyc' in ContractInfo):
                PaymentCyc = ContractInfo["PaymentCyc"]
            GuaranteeType = ContractInfo["GuaranteeType"]
            CreditLimitAmount = ContractInfo["CreditLimitAmount"]
            OpenDate = ContractInfo['OpenDate']
            EndDate = ContractInfo['EndDate']
            PaymentRating = ContractInfo['PaymentRating']

        if ('CurrAccountInfo' in l):
            CurrAccountInfo = l["CurrAccountInfo"]
            ScheduledPaymentAmount = CurrAccountInfo['ScheduledPaymentAmount']
            Balance = CurrAccountInfo['Balance']
            pass
        s = str.format(_id=_id, userRealname=userRealname, userIdcardNo=userIdcardNo,
                       Type=Type, PaymentCyc=PaymentCyc, GuaranteeType=GuaranteeType,
                       CreditLimitAmount=CreditLimitAmount, OpenDate=OpenDate,
                       EndDate=EndDate, PaymentRating=PaymentRating,
                       ScheduledPaymentAmount=ScheduledPaymentAmount, Balance=Balance)
        print(s)
        resultStr = s+'\n';
        resultFile.write(resultStr)
    print(i)
    print("===================================")


# 关闭结果文件
resultFile.close()

file.close()


str = 'asd\n123123'
if not(str is None or str.__eq__('')):
    print(str)
