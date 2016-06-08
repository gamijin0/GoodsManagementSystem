import requests
import csv
import time
from selenium import webdriver


class UserAddRequests:

    username = ""
    password = ""
    email = ""
    nickname = ""
    sex = ""

    def __init__(self,username,email,nickname,sex):
        self.nickname=nickname
        self.username=username
        self.email=email
        self.sex=sex
        self.password=self.username[-6:]


    url = "http://127.0.0.1/accounts/user/add/"
    header = {
        'Host':' 127.0.0.1',
        #'User - Agent': 'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv:46.0) Gecko / 20100101Firefox / 46.0',
        #'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8',
        #'Accept - Language': 'en - US, en;q = 0.5',
        #'Accept - Encoding':' gzip, deflate',
        'Referer':'http://127.0.0.1/accounts/user/add/',
        'Cookie':'csrftoken=vSJTyLywr0R056LaaQ3nEImM8Kj7ULdR; sessionid=rapzsaq0tlu5vcbi3x2ltttuk06dkvbh',
        'Connection':' keep - alive',
    }


    def postRequest(self):
        data = {
            'csrfmiddlewaretoken': 'vSJTyLywr0R056LaaQ3nEImM8Kj7ULdR',
            'username': self.username,  # 学号
            'password': self.password,  # 密码
            'email': self.email,  # 邮箱
            'nickname': self.nickname,  # 名字
            'sex': self.sex,  # 性别
            'role': '',
            'is_active': 'True',
        }

        print(data)

        res=requests.post(url=self.url,data=data)
        print(res.text)


def ReadCsv(filename ):

    Res_list=list()

    with open(filename,'r') as file:
        f=csv.reader(file)
        for line in f :
            #print(line)
            tempLine=list()
            tempLine.append(line[1])
            tempLine.append(line[2])
            tempLine.append(line[9])
            tempLine.append(line[3])
            Res_list.append(tempLine)

    return Res_list


class MyDriver:
    url = "http://chaos.ac.cn"
    driver =webdriver.Firefox()




    def login_as_root(self,username,passwd):
        self.driver.get(self.url)
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(passwd)
        self.driver.find_element_by_id("btSubmit").click()

    def AddNewUser(self,data_line):

        time.sleep(0.5)
        self.driver.get(self.url+"/accounts/user/add/")

        print(data_line)
        username = data_line[0]
        password = username[-6:]
        nickname= data_line[1]
        email = data_line[2]
        sex = data_line[3]

        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("nickname").send_keys(nickname)

        if (sex=="男"):
            self.driver.find_element_by_id("id_sex_0").click()
        else:
            self.driver.find_element_by_id("id_sex_1").click()

        selallOptions = self.driver.find_elements_by_tag_name("option")

        for o in selallOptions:
            if(o.get_attribute("value")=="True"):
                o.click()

        self.driver.find_element_by_id("btAddUser").click()


        return


if __name__=="__main__":
    Res_list=ReadCsv('2014-ruangong.csv')
    #print(Res_list)

    one = MyDriver()
    one.login_as_root('chaos', 'xlsd1996')

    for i in range(2,39):
        one.AddNewUser(Res_list[i])