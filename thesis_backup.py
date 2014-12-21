import os
import time
import zipfile    # 用自带的zipfile包实现压缩

# 一个递归函数，目的是遍历整个目标文件夹
def trav(father,targetdir = ""):    # 两个参数，father是父亲节点（遍历的文件夹），
                                    # targetdir是记录压缩包中的存放路径
    travFile = os.listdir(father)   # 用listdir列出文件夹内所有第一级文件
    for i in travFile:              # 遍历刚才的list
        if i.find('.') == -1:       # 用str类的find方法，检测是否为文件夹
            trav(father+os.sep+i,targetdir + os.sep + i)
                                    # 若为文件夹，则递归引用，同时调整存放路径
        else:
            zipfile.write(father+os.sep+i,targetdir+os.sep+i)
                                    # 若为文件，则写入zip包

# 定义备份源
source = "C:\\Users\ibm\Desktop\本科毕业设计\文献翻译\Thesis"

# 定义备份目标
target_dir = 'D:\Transfer\SkyDrive\\backup'

# 用time包里的日期函数链接目标文件夹位置，作为每日不同的备份文件夹名称
today = target_dir + os.sep + time.strftime('%Y%m%d')

# 返回备份时间，写压缩包名字用
now = time.strftime('%H%M%S')

# 允许在文件名中产生一个注释
comment = input('Enter a comment --> ')
if len(comment) == 0:               # 若无注释
    target = today + os.sep + '文献翻译' + now + '.zip'
else:                               # 若有注释，把注释也置于文件名中
    target = today + os.sep + '文献翻译' + now + '_' +\
             comment.replace(' ', '_') + '.zip'

# 每日生成一个新的文件夹
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zipfile = zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED)
                                    # 写入一个zip文件
trav(source)                        # 调用递归函数
zipfile.close()                     # 关闭之

# 输出一个提示
print('Successful backup to', target)
