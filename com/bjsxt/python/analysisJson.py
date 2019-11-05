# import json;
# data1 = {
#            'name' : 'jack',
#             'age' : 20,
#             'like': ('sing','dance','swim'),
#             'score': {'chinese':80,'math':60,'english':99}
# }
#
# data2 = json.dumps(data1);
# data3 = json.loads(data2);
# print('原始数据');
# print(data1);
# print('转化成json格式');
# print(data2);
# print('再转化成python格式');
# print(data3);


#
import json;

# json.dump()  把数据写入json文件
# json.load()  把json文件内容读入python

# data1 = {
#            'name' : 'jack',
#             'age' : 20,
#             'like': ('sing','dance','swim'),
#             'score': {'chinese':80,'math':60,'english':99},
#             'love': None
# }
#
#
#
# #把python数据data1直接写入json文件中
# json.dump(data1, open('jack.json', "w"));

# 直接从json文件中读取数据返回一个python对象
# file = open('jack.json','r')
# data3 = json.load(file);
# print(type(data3))
# print(data3);
#
# print(data3.keys())
# print(data3.values())
#
# for i in data3.keys():
#     print(i+":", end='')
#     print(data3[i])
# print("-------------------------")
# print(type(data3["like"]))
# print(data3["like"])
#
# print("-------------------------")
# print(type(data3["score"]))
# print(data3["score"])


jsonFile = open('test.json', 'r', encoding="utf8")
jsonObjct = json.load(jsonFile)
print(jsonObjct.keys())
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
print(type(applyInfo))
# 客户id
_id = applyInfo["_id"];
userRealname = applyInfo["userRealname"]
userIdcardNo = applyInfo["userIdcardNo"]

for i in applyInfo.keys():
    print(i + ":", end='')
    print(applyInfo[i])

for j in bbgReport.keys():
    print(j + '', end="")
    print(bbgReport[j])

# bbgReport->CreditDetail
print('********************')
CreditDetail = bbgReport["CreditDetail"]
print(type(CreditDetail))
for k in CreditDetail.keys():
    print(k + ':', end='')
    print(CreditDetail[k])

# CreditDetail-> Loan(list)
print('********************')
Loan = CreditDetail['Loan']
print("=====Loan:=========")
print(type(Loan))

# Loan(list)-> ContractInfo
# Loan(list)-> CurrAccountInfo
print('_____________________________')
# ContractInfo = Loan['']

for l in Loan:
    print("test")
    print(l)
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
        print("xxxxxxxxxxxxxxxxxxxxx")
        print()
        print(type(l))
        ContractInfo = l["ContractInfo"]
        Type = ContractInfo["Type"]
        if('PaymentCyc' in ContractInfo):
            PaymentCyc = ContractInfo["PaymentCyc"]
        GuaranteeType = ContractInfo["GuaranteeType"]
        CreditLimitAmount = ContractInfo["CreditLimitAmount"]
        OpenDate = ContractInfo['OpenDate']
        EndDate = ContractInfo['EndDate']
        PaymentRating = ContractInfo['PaymentRating']

    if ('CurrAccountInfo' in l):
        CurrAccountInfo = l["CurrAccountInfo"]
        # print(type(CurrAccountInfo))
        # print("CurrAccountInfo:", end='')
        # print(CurrAccountInfo)
        ScheduledPaymentAmount = CurrAccountInfo['ScheduledPaymentAmount']
        Balance = CurrAccountInfo['Balance']
        pass
    s = str.format(_id=_id, userRealname=userRealname, userIdcardNo=userIdcardNo,
               Type=Type, PaymentCyc=PaymentCyc, GuaranteeType=GuaranteeType,
               CreditLimitAmount=CreditLimitAmount, OpenDate=OpenDate,
               EndDate=EndDate, PaymentRating=PaymentRating,
               ScheduledPaymentAmount=ScheduledPaymentAmount, Balance=Balance)
    print(s)
# print(jsonObjct)
