import urllib 
import urllib2 
import re
import os


strUrl = 'http://mirrors.163.com/cygwin/x86_64/';
path = 'H:\\mytest';
tempUrl = ''.join(strUrl);
listDirectory = [];
listDirectoryNumber = [];


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
    global listDirectory;
    number = len(listFileName);
   
    
    for name in listFileName:
        nCount = name.find('/');
        if nCount == -1:                #nCount Ϊ-1 ����Ŀ¼ ������ 
            #print "����Ŀ¼����";
            print name;    
            
            number = number - 1;  
            if number == 1:
                tempUrl = tempUrl[:len(tempUrl) - len(listDirectory[-1])];
                listDirectory.pop();
        
        else:
            listDirectory.append(name);
            #print "��Ŀ¼������������ļ�";
            tempUrl = tempUrl + name;
            html = getHtml(tempUrl);
            listTemp = getFileNameList(html);
            downLoad(listTemp);
        
    
      
if __name__ == "__main__":
    
    #os.mkdir(path);    
    html = getHtml(strUrl);
    listFileName = getFileNameList(html);
    downLoad(listFileName);
