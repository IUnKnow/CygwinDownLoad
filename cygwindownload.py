import urllib 
import urllib2 
import re
import os


strUrl = 'http://mirrors.163.com/cygwin/x86_64/'

#��ȡhtml ��Ϣ
def getHtml(strUrl):
    page = urllib.urlopen(strUrl); #������
    html = page.read();     #��ȡhtml
    return html ;

def getFileNameList(strHtml):
    
    reg = r'<a href="(.+?)"';#���� 
    imgre = re.compile(reg); #ʹ��������ʽ
    fileNameList = re.findall(imgre,strHtml);#��ȡ��Ҫ����Ϣ
    
    for name in fileNameList:   #�����ַ�������  ɾ�� '../'�ַ�
        if name == '../':
            fileNameList.remove('../');
        
    print fileNameList;
    return fileNameList; 

      
#def downLoad(listFileName):
    
    

      
      
if __name__ == "__main__":
    
    html = getHtml(strUrl);
    listFileName = getFileNameList(html);
   # downLoad(listFileName);