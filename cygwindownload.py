import urllib 
import urllib2 
import re
import os


strUrl = 'http://mirrors.163.com/cygwin/x86_64/';
path = 'H:\\mytest';
tempUrl = ''.join(strUrl);
tempName = '';
#获取html 信息
def getHtml(strUrl):
    page = urllib.urlopen(strUrl); #打开连接
    html = page.read();     #获取html
    return html ;

def getFileNameList(strHtml):
    
    reg = r'<a href="(.+?)"';#正则 
    imgre = re.compile(reg); #使用正则表达式
    fileNameList = re.findall(imgre,strHtml);#获取想要的信息
    
    for name in fileNameList:   #遍历字符串链表  删除 '../'字符
        if name == '../':
            fileNameList.remove('../');
        
    print fileNameList;
    return fileNameList; 

      
def downLoad(listFileName):
    
    global tempUrl;
    global tempName;
    for name in listFileName:
        nCount = name.find('/');
        if nCount == -1:     #nCount 为-1 则是目录 继续进 
            #print "不是目录下载";
            print name; 
        else:
            #print "是目录继续进入查找文件";
            temp = tempUrl + name;
            tempUrl = temp;
            tempName = name;
            html = getHtml(temp);
            listTemp = getFileNameList(html);
            return downLoad(listTemp);
    return;
    
      
if __name__ == "__main__":
    
    
    #os.mkdir(path);    
    html = getHtml(strUrl);
    listFileName = getFileNameList(html);
    downLoad(listFileName);
    