import urllib 
import urllib2 
import re
import os


strUrl = 'http://mirrors.163.com/cygwin/x86_64/';
path = 'H:\\mytest';
tempUrl = ''.join(strUrl);
tempName = '';
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

      
def downLoad(listFileName):
    
    global tempUrl;
    global tempName;
    for name in listFileName:
        nCount = name.find('/');
        if nCount == -1:     #nCount Ϊ-1 ����Ŀ¼ ������ 
            #print "����Ŀ¼����";
            print name; 
        else:
            #print "��Ŀ¼������������ļ�";
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
    