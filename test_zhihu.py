import time


import requests
import pandas as pd


if __name__ == '__main__':
    headers = {
        "authority": "www.zhihu.com",
        "x-udid": "AIACLBX1vAyPTnVp5XlxcVvsjPMRl5crPX4=",
        "referer": "https://www.zhihu.com/topic/20086364/top-answers",
        "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
        "cookie": ("q_c1=e6681084d1514969a550a84dd0e22d58|1507270450000|"
                   "1507270450000; _zap=0449b6df-f436-4458-8e6a-9c101902f30d; d_c0"
                   "=\"AIACLBX1vAyPTnVp5XlxcVvsjPMRl5crPX4 = |1511619143\"; z_c0=\"2 |"
                   " 1: 0 | 10: 1516959760 | 4: z_c0 | 92: Mi4xbkZOOEJRQUFBQUFBZ0FJc0Zm"
                   "VzhEQ1lBQUFCZ0FsVk5FRVpZV3dDTGwwUWMxdWVsMElaQ091QXZmbFJ4ZzBzS0RR | 9"
                   "d7c5443d8f12a015fa6003f72de807832132f5303ef7bb589b5c8fd138f3942\"; "
                   "q_c1=e6681084d1514969a550a84dd0e22d58|1519878195000|1507270450000; "
                   "_xsrf=d5f46aba-8d16-41e5-b8b5-5f978d8c6747; aliyungf_tc=AQAAAJ94MiL"
                   "70wgADEjidIK5t7rPAxUe; __utma=51854390.749062343.1511619151.1513751490"
                   ".1521086559.3; __utmc=51854390; __utmz=51854390.1521086559.3.3.utmcsr=z"
                   "hihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=518543"
                   "90.100--|2=registration_date=20170720=1^3=entry_date=20170720=1; __DAYU_P"
                   "P=za2r2fmEaj6mENeIYVfn2cdcd72d71e5"),
        "user-agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWeb"
                       "Kit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"),
    }
    list_ = []
    for i in range(0, 100, 20):

        url = ('https://www.zhihu.com/api/v4/topics/20086364/feeds/essence?'
               'include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.ta'
               'rget.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crel'
               'ationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_no'
               'thelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target'
               '.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_c'
               'ount%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5'
               'B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dt'
               'opic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.'
               'target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F'
               '%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_stic'
               'ky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_c'
               'ount%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2C'
               'badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dan'
               'swer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2'
               'Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author'
               '.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dar'
               'ticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.top'
               'ics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count&limit=20&of'
               'fset={}').format(i)
        content = requests.get(url, headers=headers).json()['data']

        for i_ in content:
            j = i_["target"]
            if "question" in j.keys():
                title = j["question"]["title"]
                url = j["question"]["url"]
            else:
                title = j["title"]
                url = j["url"]
            list_.append((title, url))
        time.sleep(1)

    excel_file = pd.DataFrame(list_)
    excel_file.to_excel('python爬虫资料及链接.xlsx')
