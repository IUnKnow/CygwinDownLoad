import urllib 
import urllib2 
import re
import os


strUrl = 'http://mirrors.163.com/cygwin/x86_64/'

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

      
#def downLoad(listFileName):
    
    

      
      
if __name__ == "__main__":
    
    html = getHtml(strUrl);
    listFileName = getFileNameList(html);
   # downLoad(listFileName);