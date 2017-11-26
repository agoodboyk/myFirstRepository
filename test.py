import os , xlrd ,sys ,time
import getSorce
INPUT_FILE = '成型142.xlsx'
OUTPUT_FILE = '124_CET4.txt'
STARTADDR = 6 #开始位置


data = xlrd.open_workbook(INPUT_FILE)
table =data.sheets()[0]

STOPADDR = table.nrows #结束位置

for i in range(STARTADDR,STOPADDR):
    f = open(OUTPUT_FILE,'a+')
    name = table.row(i)[4].value
    numId = table.row(i)[1].value

    sorce = getSorce.getSorce(numId,name)
    if sorce != False:
        #print(sorce)
        if int(sorce[0]) > 425:
            key = 'pass'
        else:
            key = '    failed'
        text = '%-2d——%s——%s——分数 : %-3d %-3d %-3d %-3d————%s\n' % (i,sorce[4] ,format(name,'\u3000<3'),int(sorce[0]),int(sorce[1]),int(sorce[2]),int(sorce[3]),key)
        print(text)
        f.write(text)
        f.close()
    else:
        f.write(str(i)+name+' 失败 \n')
        f.close()
        continue
    time.sleep(2)








