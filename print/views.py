# -*-coding: utf-8 -*-
import datetime
import sys
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import *
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY

import reportlab.rl_config
from reportlab.platypus import flowables

reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', 'SURSONG.TTF'))
pdfmetrics.registerFont(TTFont('tm', 'Times .ttf'))

from reportlab.lib import fonts, colors

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from info.models import ApplicationForm

# Create your views here.
A={"AF":"阿富汗"
,"AX":"奥兰群岛"
,"AL":"阿尔巴尼亚"
,"DZ":"阿尔及利亚"
,"AS":"美属萨摩亚"
,"AD":"安道尔"
,"AO":"安哥拉"
,"AI":"安圭拉"
,"AQ":"南极洲"
,"AG":"安提瓜和巴布达"
,"AR":"阿根廷"
,"AM":"亚美尼亚"
,"AW":"阿鲁巴"
,"AU":"澳大利亚"
,"AT":"奥地利"
,"AZ":"阿塞拜疆"
,"BS":"巴哈马"
,"BH":"巴林"
,"BD":"孟加拉国"
,"BB":"巴巴多斯"
,"BY":"白俄罗斯"
,"BE":"比利时"
,"BZ":"伯利兹"
,"BJ":"贝宁"
,"BM":"百慕大"
,"BT":"不丹"
,"BO":"玻利维亚"
,"BA":"波黑"
,"BW":"博茨瓦纳"
,"BV":"布维岛"
,"BR":"巴西"
,"IO":"英属印度洋领地"
,"BN":"文莱"
,"BG":"保加利亚"
,"BF":"布基纳法索"
,"BI":"布隆迪"
,"KH":"柬埔寨"
,"CM":"喀麦隆"
,"CA":"加拿大"
,"CV":"佛得角"
,"KY":"开曼群岛"
,"CF":"中非"
,"TD":"乍得"
,"CL":"智利"
,"CN":"中国"
,"CX":"圣诞岛"
,"CC":"科科斯（基林）群岛"
,"CO":"哥伦比亚"
,"KM":"科摩罗"
,"CG":"刚果（布）"
,"CD":"刚果（金）"
,"CK":"库克群岛"
,"CR":"哥斯达黎加"
,"CI":"科特迪瓦"
,"HR":"克罗地亚"
,"CU":"古巴"
,"CY":"塞浦路斯"
,"CZ":"捷克"
,"DK":"丹麦"
,"DJ":"吉布提"
,"DM":"多米尼克"
,"DO":"多米尼加"
,"EC":"厄瓜多尔"
,"EG":"埃及"
,"SV":"萨尔瓦多"
,"GQ":"赤道几内亚"
,"ER":"厄立特里亚"
,"EE":"爱沙尼亚"
,"ET":"埃塞俄比亚"
,"FK":"福克兰群岛（马尔维纳斯）"
,"FO":"法罗群岛"
,"FJ":"斐济"
,"FI":"芬兰"
,"FR":"法国"
,"GF":"法属圭亚那"
,"PF":"法属波利尼西亚"
,"TF":"法属南部领地"
,"GA":"加蓬"
,"GM":"冈比亚"
,"GE":"格鲁吉亚"
,"DE":"德国"
,"GH":"加纳"
,"GI":"直布罗陀"
,"GR":"希腊"
,"GL":"格陵兰"
,"GD":"格林纳达"
,"GP":"瓜德罗普"
,"GU":"关岛"
,"GT":"危地马拉"
,"GG":"格恩西岛"
,"GN":"几内亚"
,"GW":"几内亚比绍"
,"GY":"圭亚那"
,"HT":"海地"
,"HM":"赫德岛和麦克唐纳岛"
,"VA":"梵蒂冈"
,"HN":"洪都拉斯"
,"HK":"香港"
,"HU":"匈牙利"
,"IS":"冰岛"
,"IN":"印度"
,"ID":"印度尼西亚"
,"IR":"伊朗"
,"IQ":"伊拉克"
,"IE":"爱尔兰"
,"IM":"英国属地曼岛"
,"IL":"以色列"
,"IT":"意大利"
,"JM":"牙买加"
,"JP":"日本"
,"JE":"泽西岛"
,"JO":"约旦"
,"KZ":"哈萨克斯坦"
,"KE":"肯尼亚"
,"KI":"基里巴斯"
,"KP":"朝鲜"
,"KR":"韩国"
,"KW":"科威特"
,"KG":"吉尔吉斯斯坦"
,"LA":"老挝"
,"LV":"拉脱维亚"
,"LB":"黎巴嫩"
,"LS":"莱索托"
,"LR":"利比里亚"
,"LY":"利比亚"
,"LI":"列支敦士登"
,"LT":"立陶宛"
,"LU":"卢森堡"
,"MO":"澳门"
,"MK":"前南马其顿"
,"MG":"马达加斯加"
,"MW":"马拉维"
,"MY":"马来西亚"
,"MV":"马尔代夫"
,"ML":"马里"
,"MT":"马耳他"
,"MH":"马绍尔群岛"
,"MQ":"马提尼克"
,"MR":"毛利塔尼亚"
,"MU":"毛里求斯"
,"YT":"马约特"
,"MX":"墨西哥"
,"FM":"密克罗尼西亚联邦"
,"MD":"摩尔多瓦"
,"MC":"摩纳哥"
,"MN":"蒙古"
,"ME":"黑山"
,"MS":"蒙特塞拉特"
,"MA":"摩洛哥"
,"MZ":"莫桑比克"
,"MM":"缅甸"
,"NA":"纳米比亚"
,"NR":"瑙鲁"
,"NP":"尼泊尔"
,"NL":"荷兰"
,"AN":"荷属安的列斯"
,"NC":"新喀里多尼亚"
,"NZ":"新西兰"
,"NI":"尼加拉瓜"
,"NE":"尼日尔"
,"NG":"尼日利亚"
,"NU":"纽埃"
,"NF":"诺福克岛"
,"MP":"北马里亚纳"
,"NO":"挪威"
,"OM":"阿曼"
,"PK":"巴基斯坦"
,"PW":"帕劳"
,"PS":"巴勒斯坦"
,"PA":"巴拿马"
,"PG":"巴布亚新几内亚"
,"PY":"巴拉圭"
,"PE":"秘鲁"
,"PH":"菲律宾"
,"PN":"皮特凯恩"
,"PL":"波兰"
,"PT":"葡萄牙"
,"PR":"波多黎各"
,"QA":"卡塔尔"
,"RE":"留尼汪"
,"RO":"罗马尼亚"
,"RU":"俄罗斯联邦"
,"RW":"卢旺达"
,"SH":"圣赫勒拿"
,"KN":"圣基茨和尼维斯"
,"LC":"圣卢西亚"
,"PM":"圣皮埃尔和密克隆"
,"VC":"圣文森特和格林纳丁斯"
,"WS":"萨摩亚"
,"SM":"圣马力诺"
,"ST":"圣多美和普林西比"
,"SA":"沙特阿拉伯"
,"SN":"塞内加尔"
,"RS":"塞尔维亚"
,"SC":"塞舌尔"
,"SL":"塞拉利昂"
,"SG":"新加坡"
,"SK":"斯洛伐克"
,"SI":"斯洛文尼亚"
,"SB":"所罗门群岛"
,"SO":"索马里"
,"ZA":"南非"
,"GS":"南乔治亚岛和南桑德韦奇岛"
,"ES":"西班牙"
,"LK":"斯里兰卡"
,"SD":"苏丹"
,"SR":"苏里南"
,"SJ":"斯瓦尔巴岛和扬马延岛"
,"SZ":"斯威士兰"
,"SE":"瑞典"
,"CH":"瑞士"
,"SY":"叙利亚"
,"TW":"台湾"
,"TJ":"塔吉克斯坦"
,"TZ":"坦桑尼亚"
,"TH":"泰国"
,"TL":"东帝汶"
,"TG":"多哥"
,"TK":"托克劳"
,"TO":"汤加"
,"TT":"特立尼达和多巴哥"
,"TN":"突尼斯"
,"TR":"土耳其"
,"TM":"土库曼斯坦"
,"TC":"特克斯和凯科斯群岛"
,"TV":"图瓦卢"
,"UG":"乌干达"
,"UA":"乌克兰"
,"AE":"阿联酋"
,"GB":"英国"
,"US":"美国"
,"UM":"美国本土外小岛屿"
,"UY":"乌拉圭"
,"UZ":"乌兹别克斯坦"
,"VU":"瓦努阿图"
,"VE":"委内瑞拉"
,"VN":"越南"
,"VG":"英属维尔京群岛"
,"VI":"美属维尔京群岛"
,"WF":"瓦利斯和富图纳"
,"EH":"西撒哈拉"
,"YE":"也门"
,"ZM":"赞比亚"
,"ZW":"津巴布韦"}
fonts.addMapping('song', 0, 0, 'song')
fonts.addMapping('song', 0, 1, 'song')
fonts.addMapping('tm', 1, 0, 'tm')
fonts.addMapping('tm', 1, 1, 'tm')
stylesheet = getSampleStyleSheet()

stylesheet.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
stylesheet['Justify'].fontName = 'song'
stylesheet['Justify'].fontSize = 10.5

from django.http import StreamingHttpResponse
def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
def downloadpdf(request):
    # do something...

    #the_file_name = str(datetime.datetime.now().strftime('%H:%M:%S')+'.pdf')
    time=datetime.datetime.now().strftime('%Y%m%d')
    the_file_name = 'test1_'+time+'.pdf'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response

def printpdf1(request):
    elements = []
    time=datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
    the_file_name = 'test1_'+time+'.pdf'
    doc = SimpleDocTemplate(the_file_name,topMargin=0)

    elements.append(flowables.Image("/home/song/mysite/print/images/hit.png", width=8.3 * inch, height=4 * inch))
    elements.append(Paragraph(u'<font name="song"size=22><b>关于申请为留学生办理签证手续的函</b></font>', stylesheet['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(u'<font name="song"size=14><b>哈尔滨市公安局出入境管理局：</b></font>', stylesheet['Normal']))
    elements.append(Spacer(1, 12))
    import MySQLdb
    conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="mysite",charset="utf8")
    cur = conn.cursor()
    sql = "select * from info_applicationform where id=(select max(id) from info_applicationform where user_email_id=\'" +str(request.user.email)+"\');"
    print "\n\n\n\n\n\n\n"+sql;
    cur.execute(sql)
    result = cur.fetchall()
    d = []
    d.append(['序号', '学生姓名', '国籍', '出生日期', '护照号码', '学习期限'])

    i=1
    counter = 0
    nationmaxlen=0
    namemaxlen=0
    inpdf=[]
    for l in result:
        # if l[0]==int(request.POST['id']):
        l=list(l)
        inpdf.append(i)
        i += 1
        if namemaxlen<len(str(l[3])+" "+str(l[4])):
            namemaxlen=len(str(l[3])+" "+str(l[4]))
        inpdf.append(str(l[3])+" "+str(l[4]))
        if nationmaxlen<len(A[str(l[6])]):
            nationmaxlen=len(A[str(l[6])])
        inpdf.append(A[str(l[6])])
        inpdf.append(l[7].strftime("%Y%m%d"))
        inpdf.append(l[8])
        inpdf.append(l[27].strftime("%Y%m-")+l[28].strftime("%Y%m"))
        d.append(inpdf)
        counter += 1
        if counter == 1:
            x = inpdf[2]
            y = inpdf[1]
            elements.append(Paragraph(
                    "<para fontname='song' fontsize=14 leading=24 firstLineIndent=24>"+x+"<b>籍 留学生 </b>"+"<font name='tm'>"+y+"</font>"+ "<b> 等</b>" +str(len(result))+ "<b>名(名单如下) 留学生现在校学习 ,现申请为其办理签证手续 , 请予以协助.</b></para>",
                stylesheet['Normal']))
            elements.append(Spacer(1, 24))
        inpdf=[]
        ts = [('GRID', (0, 0), (-1, -1), 0.25, colors.black), ('FONT', (0, 0), (-1, -1), 'song'),('ALIGN',(0,0),(-1,-1),'CENTER'),('FONTSIZE',(0,0),(-1,-1),10.5)]
        table = Table(d, 1.0 * inch, 0.24 * inch, ts)
        table._argW[0]=0.4*inch
        table._argW[1]=namemaxlen*inch/14
        table._argW[2]=nationmaxlen*inch/15
        table._argW[3]=0.8*inch
        table._argW[4]=0.9*inch
        elements.append(table)
        d=[]

    elements.append(Spacer(1, 80))
    elements.append(Paragraph("<para fontname='song' fontsize=14 alignment=right><b>哈尔滨工业大学</b></para>",stylesheet["Normal"]))
    elements.append(Spacer(1,12))
    elements.append(Paragraph("<para fontname='song' fontsize=14 alignment=right><b>"+datetime.datetime.now().date().strftime("%Y年%m月%d日")+"</b></para>",stylesheet["Normal"]))
    doc.build(elements)

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
    #return render(request, "print/index.html", {})


def caldate1(datestr):
    if datetime.date.today().month>=7 and datetime.date.today().day>=15:
         datestr=str(datetime.date.today().year+1)+"0715"
    elif datetime.date.today().month==1 and datetime.date.today().day<15:
         datestr=str(datetime.date.today().year)+"0715"
    else:
         datestr=str(datetime.date.today().year+1)+"0115"
    return  datestr
def caldate2(datestr):
    if datetime.date.today().month>=7 and datetime.date.today().day>=15:
        datestr=str(datetime.date.today.year+1)+"0115"
    elif datetime.date.today().month==1 and datetime.date.today().day<15:
        datestr=str(datetime.date.today().year)+"0115"
    else:
        datestr=str(datetime.date.today().year+1)+"0715"
    return datestr

def printpdf2(request):
    attrs = []

    import MySQLdb
    conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="mysite",charset="utf8")
    cur = conn.cursor()
    sql = "select * from info_applicationform where id=(select max(id) from info_applicationform where user_email_id=\'" +str(request.user.email)+"\');"
    cur.execute(sql)
    result = cur.fetchall()

    for l in result:
        l=list(l)
        time=datetime.datetime.now().strftime('%Y%m%d-%H')
        the_file_name = 'test2_'+str(l[0])+'_'+time+'.pdf'
        docx = SimpleDocTemplate(the_file_name,topMargin=0)

        im=flowables.Image("/home/song/mysite/print/images/shenpi.png", width=8.3 * inch, height=4 * inch)
        attrs.append(im)
        attrs.append(Spacer(1, 12))
        attrs.append(
                Paragraph(u"<para alignment=center><font name='song'size=24>外国人签证证件申请表</font></para>", stylesheet['Title']))
        attrs.append(Spacer(1, 2))
        attrs.append(Paragraph(
                "<para alignment=center><font name='tm'size=12><b>FOREIGNER VISA DOCUMENTS APPLICATION FORM</b></font></para>",
                stylesheet['Title']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted("<para alignment=center><font name='song'size=10.5>              (请用黑色或蓝色水笔填写内容,不能用圆珠笔填写)</font>               <img src='/home/song/mysite/print/images/1.png' width='102' height='130' valign='top'/></para>",
                               stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(Paragraph(
                "<para alignment=center><font name='tm'size=10.5>Please complete the form in black or blue ink(no ballpoint)</font><para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 4))
        # 1111111111111111111111111111111111111111111111111111111111111111111111111
        i=0
        blankstr="                  "
        while i<len(l[3]):
            blankstr += " "
            i += 1
        i=0
        attrs.append(
                XPreformatted("<para LeftIndent=-16><font name='song'size=10.5><b>1、姓"+blankstr+"名</b></font></para>",
                              stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted(
                "<para><font name='tm'size=10.5><b>Surname<u> "+l[3].upper()+"</u>  Given name<u> "+l[4].upper()+"</u></b></font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        blankstr="              "
        while i<len(A[l[6]]):
            blankstr += " "
            i += 1
        i=0
        attrs.append(XPreformatted(
                "<para><font name='song'size=10.5><b>中文姓名                   国籍"+blankstr+"出生地</b></font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted(
                "<para fontname='tm' fontsize=10.5><b>Name in Chinese____ Nationality<font name='song'><u> "+A[l[6]]+"</u></font>  Birth place<font name='song'><u> "+A[l[6]]+"</u></font></b></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted(
                "<para><font name='song'size=10.5><b>出生日期</b>               年       月      日        <b>性别：   </b>男         女</font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 0))
        if str(l[5])=='M':
            flagM='■'
            flagF='□'
        elif str(l[5])=='F':
                flagM='□'
                flagF='■'
        else:
                print 'Error:Sex failed to write!!!'
        datestr=l[7].strftime("%Y%m%d")
        attrs.append(XPreformatted(
                "<para><font name='tm'size=10.5><b>Date of birth</b><u>  "+datestr[0:4]+"__</u>Y<u>  "+datestr[4:6]+"_</u>M<u>  "+datestr[6:8]+"_</u>D         <b>Sex         </b>M. <font size=14>"+flagM+"</font>     F. <font size=14>"+flagF+"</font></font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 6))
        blankstr="               "
        while i<len(l[1]):
            blankstr += "   "
            i += 1
        i=0
        attrs.append(XPreformatted(
                "<para><font name='song'size=10.5><b>在华住址"+blankstr+"申请人电话</b></font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted(
                "<para><font name='tm'size=10.5><b>Address in China<font name='song'><u> "+l[1]+"</u></font>  Tel<u> 86403742</u></b></font>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted(
                "<para><font name='song'size=10.5><b>在华单位                                                    联系人姓名和电话</b></font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1, 2))
        attrs.append(XPreformatted(
                "<para fontsize=10.5><font name='tm'><b>Company/School in China<font name='song'><u> 哈尔滨工业大学</u></font>  Contact person & tel.<u> </u></b></font></para>",
                stylesheet['Normal']))
        attrs.append(Spacer(1,4))
    #22222222222222222222222222222222222222222222222222222222222222222222222222222
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5><b>2、护照种类            </b>外交                公务(官员)                普通             其他</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,0))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5><b>Passport type        </b>Diplomatic□     Service (Official) □     Ordinary<font size=14>■</font>    Other□    </font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,6))
        blankstr="               "
        while i<len(l[8]):
            blankstr += " "
            i += 1
        i=0
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5><b>护照号码"+blankstr+"有效期至               </b>年         月        日</font>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        datestr=l[9].strftime("%Y%m%d")
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5><b>Passport No.<u> "+l[8]+" </u> Valid until  <u>"+datestr[0:4]+"</u></b>Y<u>  "+datestr[4:6]+"  </u> M<u>  "+datestr[6:8]+"  </u>D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,4))
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5><b>3、现持有效签证证件种类          </b>签证      停留证件           居留证件</font><para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,0))
        if l[10]=='X1':
            flagVisa='■'
            flagSP='□'
            flagRP='□'
            Visa_number=str(l[12])
        elif l[10]=='JL':
            flagVisa='□'
            flagSP='□'
            flagRP='■'
            Visa_number=str(l[14])
        elif l[10]=='MQ':
            flagVisa='□'
            flagSP='□'
            flagRP='□'
            Visa_number='       '
        elif l[10]=='X2':
            flagVisa='■'
            flagSP='□'
            flagRP='□'
            Visa_number=str(l[19])
        elif l[10]!=None:
            flagVisa='■'
            flagSP='□'
            flagRP='□'
            Visa_number=str(l[16])
        else:
            print 'Visa WRONG!!!!!!!'
        attrs.append(XPreformatted(
                "<para><font name='tm'size=10.5><b>Current visa category                 </b>Visa<font size=14>"+flagVisa+"</font>     Stay permit<font size=14>"+flagSP+"</font>       Residence permit<font size=14>"+flagRP+"</font></font></para>",
                stylesheet['Normal']
        ))
        attrs.append(Spacer(1,6))
        blankstr="       "
        while i<len(Visa_number):
            blankstr += " "
            i += 1
        i=0
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5><b>证件号码"+blankstr+"有效期至              </b>年        月        日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        datestr=l[25].strftime("%Y%m%d")
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5><b>Visa No.<u> "+Visa_number+" </u> Valid until<u>  "+datestr[0:4]+"__</u></b>Y<u>  "+datestr[4:6]+"__</u>M<u>  "+datestr[6:8]+"__</u>D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,4))
    #444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>4、使用同一护照的偕行人  </font><font name='tm' size=10.5>Dependents on same passport </font></b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>姓               名                    性别          出生日期         与申请人关系 </font><para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Surname       Given name       Sex          Date of birth        Relationship  </font><para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
        attrs.append(XPreformatted(
            "<para>______________________________________________________________________________</para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
        attrs.append(XPreformatted(
            "<para>______________________________________________________________________________<para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
        attrs.append(XPreformatted(
            "<para alignment=right><b><font name='song'size=10.5>请填写双面</font>  <font name='tm'size=10.5>Please fill out both sides </font></b><para>",
            stylesheet['Normal']
        ))



        #print sys.stderr,l[3],A[l[4]],l[5],l[7],l[12],len(blankstr),len(A[l[4]]),len(l[6]),l[20],l[21],l[22],l[23],l[24]
    #分页分页分页
        attrs.append(PageBreak())

        if l[10] in ('X1','JL'):
            flagS7='■'
            flagS6='□'
            flagS5='□'
        elif l[10]=='MQ':
            flagS7='□'
            flagS6='■'
            flagS5='□'
        elif l[10]!=None:
            if l[26]=='LANGUAGE':
                flagS7='□'
                flagS6='□'
                flagS5='■'
            elif l[26]=='SELFPAID':
                if l[31]==True:
                    flagS7='■'
                    flagS6='□'
                    flagS5='□'
                else:
                    flagS7='□'
                    flagS6='□'
                    flagS5='■'
        if l[6] in ('AF','IR','IQ','NG','PK','LK'):
            if l[28]-datetime.date.today()<=datetime.timedelta(days=365):
                datestr=l[28].strftime("%Y")+"0731"
            else:
                l[25].year+=1
                datestr=l[25].strftime("%Y%m%d")
        elif l[26]=='LANGUAGE':
            if l[29]=='F':
                if l[10]=='MQ':
                    datestr=str(datetime.date.today()+datetime.timedelta(days=180))
                else:
                    if datetime.date.today().month>=7 and datetime.date.today().day>=15:
                        datestr=str(datetime.date.today.year+1)+"0715"
                    elif datetime.date.today().month==1 and datetime.date.today().day<15:
                        datestr=str(datetime.date.today().year)+"0715"
                    else:
                        datestr=str(datetime.date.today().year+1)+"0115"
            elif l[29]=='H':
                datestr=caldate2(datestr)
            else:
                print "tuition_fee_type_language is WRONG!!!!!!"
        elif l[26]=='EXCHANGE':
            if l[28]!=None and l[27]!=None:
                if (l[28]-l[27])>=datetime.timedelta(days=270):
                    datestr=caldate1(datestr)
                else:
                    datestr=caldate2(datestr)
            else:
                print "study_duration_start or study_duration_end is WRONG!!!!!!!!!!!!!!!"
        elif l[26]=='SELFPAID':
            if l[28]-datetime.date.today()<=datetime.timedelta(days=365):
                datestr=l[28].strftime("%Y")+"0731"
            else:
                l[25].year+=1
                datestr=l[25].strftime("%Y%m%d")
        elif l[26]=='CSCORHIT':
            datestr=str(l[28].year)+"0731"
    #5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
        attrs.append(Spacer(1,40))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>5、申请签证填写</font>  <font name='tm'size=10.5>For visa only</font></b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            '''<para><font name='song'size=10.5>F访问                                  L旅游         M贸易         Q2团聚                   J2记者</font><para>''',
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Non-commercial business□    Tourist□     Business□      Family reunion□      Journalist□</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>S2私人事务                         X2学习       R人才          G过境                   C乘务</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,0))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Personal affair□                      Student<font size=14>"+flagS5+"</font>      Talent□         Transit□                   Crew□</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,6))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>团体签证分离                       团签              申请停留期限至    年          月         日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        if flagS5=='■' :
            y=datestr[0:4]
            m=datestr[4:6]
            d=datestr[6:8]
        else:
            y="    "
            m="  "
            d="  "
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Separation from group visa□    Group visa□   Valid until<u>    "+y+"___</u>Y<u>    "+m+"___</u>M<u>    "+d+"___</u>D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>换发         补发        入境次数   停留天数                 入境有效期至    年    月    日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Renewal□  Reissue □  Entries___ Duration of stay____ Entry before____Y___M __D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,4))
    #6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>6、申请停留证件填写</font>  <font name='tm' size=10.5>For stay permit only</font></b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            '''<para><font name='song'size=10.5>免签           船员         退籍                     人道主义             其他</font></para>''',
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Visa free"+flagS6+"    Crew□       Renouncement□     Humanitarian□     Others□</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>补发           申请停留期限至            年            月            日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        if flagS6=='■' :
            y=datestr[0:4]
            m=datestr[5:7]
            d=datestr[8:10]
        else:
            y="    "
            m="  "
            d="  "
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Reissue□      Valid until<u>    "+y+"____</u>Y<u>  "+m+"__</u>M<u>  "+d+"__</u>D</font><para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
    #77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>7、申请居留证件填写</font>  <font name='tm'size=10.5>For residence permit only</font></b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>工作              学习            记者              团聚                  私人事务</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,0))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Employee□     Student<font size=14>"+flagS7+"</font>      Journalist□    Family reunion□   Personal affair□</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,6))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>换发            补发           申请居留期限至      年           月            日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        if flagS7=='■':
            y=datestr[0:4]
            m=datestr[4:6]
            d=datestr[6:8]
        else:
            y="    "
            m="  "
            d="  "
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Renew□        Reissue□     Valid until<u>    "+y+"___</u>Y<u>    "+m+"___</u>M<u>    "+d+"___</u>D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
    #88888888888888888888888888888888888888888888888888888888888888888888888888888888
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>8、申请其他证件填写</font>  <font name='tm'size=10.5>For other documents</font></b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>外国人旅行证                                     旅行地点</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Foreign citizen travel documents□          Destination___________________________</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>外国人出入境证                                 申请日期至       年       月      日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Foreign citizen exit-entry permit□          Valid until_________Y_______M_______D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>勤工助学或校外实习加注                   申请日期至       年       月      日</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Study-work□                                              Valid until_________Y_______M_______D</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
    #999999999999999999999999999999999999999999999999999999999999999999
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>9、申请变更填写</font>  <font name='tm'size=10.5>Change of</font></b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>姓名                   护照号码                 签发地                      事由                   地址</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Name□                  Passport No.□            Place of issue□           Purpose□              Address□</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='song'size=10.5>单位/院校                其他           增/减              偕行人数                     其他注明</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para><font name='tm'size=10.5>Company/school□       Other□       Add/Delete       and No.dependents_____Or others _______</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
    #00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><b><font name='song'size=10.5>10、备注</font> <font name='tm'size=10.5>Notes</font>_______________________________________________________________</b></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,8))
    ###########################################################################################################
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5><b>我保证</b>以上填写的内容真实、准确、完整，并保证在停留居留期间遵守中华人民共和国的法</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5>律。</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='tm'size=10.5><b>I hereby declare</b> that the information given above is true, correct and complete. I shall abide by </font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='tm'size=10.5>the Chinese laws and regulations during my stay in the People’s Republic of China.</font></para>",
            stylesheet['Normal']
        ))
        attrs.append(Spacer(1,12))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5>申请人签字                                                        代办人签字</font></para>",
            stylesheet['Justify']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='tm'size=10.5>Applicant's signature___________________          Agent's signature_______________________</font></para>",
            stylesheet['Justify']
        ))
        attrs.append(Spacer(1,12))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5>联系电话                                                           联系电话 </font></para>",
            stylesheet['Justify']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='tm'size=10.5>Applicant's Tel__________________________     Agent's Tel____________________________</font></para>",
            stylesheet['Justify']
        ))
        attrs.append(Spacer(1,16))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='song'size=10.5>申请日期                    年             月          日     单位印章</font></para>",
            stylesheet['Justify']
        ))
        attrs.append(Spacer(1,2))
        attrs.append(XPreformatted(
            "<para LeftIndent=-16><font name='tm'size=10.5>Application date______Y________M______D      Company/School’s seal</font></para>",
            stylesheet['Justify']
        ))
        attrs.append(Spacer(1,16))
        attrs.append(XPreformatted(
            "<para alignment=right><font name='song' size=10.5>哈尔滨市出入境管理局制</font></para>",
        stylesheet['Normal']
        ))
        docx.build(attrs)
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response
    #return render(request, "print/index.html", {})