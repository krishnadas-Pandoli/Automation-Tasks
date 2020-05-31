import imaplib
import email
import os
from datetime import datetime
from datetime import datetime, timedelta
import pandas as pd

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

dfObj = pd.DataFrame(columns=['Country', 'Scode', 'Filename','Date'])
server = 'outlook.office365.com'
user = 'bireports@sdsds.com'
password = 'sdsdsd'

outputdir = 'C:/Python_File_Transfer/F21Sales/'
subject = 'Sales data' #subject line of the emails you want to download attachments from

# connects to email client through IMAP
def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

# downloads attachment for an email id, which is a unique identifier for an
# email, which is obtained through the msg object in imaplib, see below
# subjectQuery function. 'emailid' is a variable in the msg object class.

def downloaAttachmentsInEmail(m, emailid, outputdir,dfObj):
    try:

        resp, data = m.fetch(emailid, "(BODY.PEEK[])")
        email_body = data[0][1]
        mail = email.message_from_bytes(email_body)
        #print('Date:',mail['Date'])
        date_tuple = email.utils.parsedate_tz(mail['Date'])
        if date_tuple:
            local_date = datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_date = datetime.strftime(local_date, '%d-%b-%Y')
            today2 = datetime.strftime(datetime.now(),'%d-%b-%Y')
            #today2 = datetime.strftime(datetime.now()-timedelta(1), '%d-%b-%Y')#comment
            #print(local_date)
            #print(today2)
            if today2==local_date:
                if mail.get_content_maintype() != 'multipart':
                    return
                today=datetime.now()
                if os.path.exists(outputdir + today.strftime('%Y%m%d')) == False:
                    os.mkdir(outputdir + today.strftime('%Y%m%d'))
                outputdir = outputdir + today.strftime('%Y%m%d')
                for part in mail.walk():
                    if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                        if part.get_filename().startswith(("IX","PY","TX")):
                            if part.get_filename().split(".")[1] == "DAT":

                                print(part.get_filename()+"is going to be downloaded")

                                uaePath = "X:/UAE/UAE_EDI"
                                uaelist=['801','803','825','833','804','846','805']

                                bahpath="X:/BAHRAIN/BAH_EDI"
                                bahlist = ['809', '819']

                                indopath = "X:/INDONESIA/IND_EDI"
                                indolist = ['815','845','847']

                                jordpath = "X:/JORDAN/JDN_EDI"
                                jordlist = ['848']

                                kuwpath = "X:/KUWAIT/KUW_EDI"
                                kuwlist = ['812']

                                lebpath = "X:/LEBANON/LBN_EDI"
                                leblist = ['841']

                                malpath = "X:/MALAYSIA/MAL_EDI"
                                mallist = ['811','817','818','807']


                                muspath = "X:/MUSCAT/MCT_EDI"
                                muslist = ['814']

                                ksapath = "X:/SAUDI/SAU_EDI"
                                ksalist = ['810', '823', '836', '840']

                                rsapath = "X:/SOUTH_AFRICA/SFA_EDI"
                                rsalist = ['961', '962', '963',]




                                if part.get_filename()[3:6] in uaelist:
                                    #print('UAE')
                                    open(uaePath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'UAE', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)
                                elif part.get_filename()[3:6] in bahlist:
                                    #print('BAHRAIN')
                                    open(bahpath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'BAHRAIN', 'Scode': part.get_filename()[3:6],
                                                          'Filename': part.get_filename(), 'Date': today},
                                                         ignore_index=True)

                                elif part.get_filename()[3:6] in indolist:
                                    #print('INDONESSIA')
                                    open(indopath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'INDONESSIA', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)
                                elif part.get_filename()[3:6] in jordlist:
                                    #print('JORDAN')
                                    open(jordpath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'JORDAN', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)
                                elif part.get_filename()[3:6] in kuwlist:
                                    #print('KUWAIT')
                                    open(kuwpath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'KUWAIT', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)
                                elif part.get_filename()[3:6] in leblist:
                                    #print('LEBANON')
                                    open(lebpath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'LEBANON', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)
                                elif part.get_filename()[3:6] in mallist:
                                    #print('MALAYSIA')
                                    open(malpath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'MALAYSIA', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)
                                elif part.get_filename()[3:6] in muslist:
                                    #print('MUSCAT')
                                    open(muspath + '/' + part.get_filename(), 'wb').write(
                                        part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'MUSCAT', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)

                                elif part.get_filename()[3:6] in ksalist:
                                    #print('KSA')
                                    open(ksapath + '/' + part.get_filename(), 'wb').write(
                                    part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'KSA', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)

                                elif part.get_filename()[3:6] in rsalist:
                                    #print('RSA')
                                    open(rsapath + '/' + part.get_filename(), 'wb').write(
                                    part.get_payload(decode=True))
                                    dfObj = dfObj.append({'Country': 'RSA', 'Scode': part.get_filename()[3:6], 'Filename': part.get_filename(), 'Date': today}, ignore_index=True)

                                print(".... "+part.get_filename() + " Downloaded to RTS PATH")


                                open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))
                                print(".... "+part.get_filename()+ " Downloaded to Local")

    except Exception as e:
        print(e)
    return dfObj

# download attachments from all emails with a specified subject line
# as touched upon above, a search query is executed with a subject filter,
# a list of msg objects are returned in msgs, and then looped through to
# obtain the emailid variable, which is then passed through to the above
# downloadAttachmentsinEmail function

def subjectQuery(subject,dfObj):
    try:
        today = datetime.strftime(datetime.now(),'%d-%b-%Y')
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d-%b-%Y')#change 2 to 1comment
        tomorrow = datetime.strftime(datetime.now() + timedelta(1), '%d-%b-%Y')
        #print(tomorrow)
        m = connect(server, user, password)
        print('BIReport Email Connected')
        m.select("Inbox")
        typ, msgs = m.search(None,'(SUBJECT "' + subject + '" FROM ssS.FRAN@dssd1.com since "' + yesterday + '" before "' + tomorrow + '")')
        #typ, msgs = m.search(None, '(SUBJECT "' + subject + '" FROM ssS.FRAN@sdsd1.com since "' + yesterday + '" before "' + today + '")')
        
        print('Emails Fetched')
        msgs = msgs[0].split()
        for emailid in msgs:
            dfObj= downloaAttachmentsInEmail(m, emailid, outputdir,dfObj)

    except Exception as e:
        print(e)
    return dfObj


dfObj= subjectQuery(subject,dfObj)
dfObj.sort_values("Country", axis = 0, ascending = True,
                 inplace = True, na_position ='last',ignore_index=True)
print(dfObj)
def send_Email(username, password, from_addr, to_addrs, msg):
    server = smtplib.SMTP('outlook.office365.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()
username = 'krishnadas@sdsdsd.com'
password = 'dssdsd'
server = smtplib.SMTP('')
today = datetime.now()

email_list = [line.strip() for line in open('email.txt')]
for to_addrs in email_list:
    msg = MIMEMultipart()

    msg['Subject'] = "F21 File Transfer Notification..! This is an Automatic email"
    msg['From'] = username
    msg['To'] = to_addrs

    try:
        # Attach HTML to the email
        html = """\
        <html>
          <head></head>
          <body>
            {0}
            <br>
            <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> 
                 <tr style="border-collapse:collapse;"></tr> 
                 <tr style="border-collapse:collapse;"> 
                  <td align="center" style="padding:0;Margin:0;"> 
                   <table class="es-footer-body" width="700" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;"> 
                     <tr style="border-collapse:collapse;"> 
                      <td style="Margin:0;padding-top:10px;padding-bottom:10px;padding-left:10px;padding-right:10px;background-color:#EFEFEF;" bgcolor="#efefef" align="left"> 
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="680" valign="top" align="center" style="padding:0;Margin:0;"> 
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="center" style="padding:0;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:11px;font-family:verdana, geneva, sans-serif;line-height:17px;color:#666666;">This is an automated&nbsp;message from Sharaf Retail, Dubai, United Arab Emirates.</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:11px;font-family:verdana, geneva, sans-serif;line-height:17px;color:#666666;"><a target="_blank" style="font-family:verdana, geneva, sans-serif;font-size:12px;text-decoration:underline;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#333333;" href="">Privacy Policy</a>.</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:11px;font-family:verdana, geneva, sans-serif;line-height:17px;color:#666666;">Make sure our messages get to your Inbox (and not your bulk or junk folders).&nbsp;</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:11px;font-family:verdana, geneva, sans-serif;line-height:17px;color:#666666;">You are receiving this email because you have been added Sharaf Retail Notification Mail List.</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:11px;font-family:verdana, geneva, sans-serif;line-height:17px;color:#666666;">If you wish to unsubscribe, kindly Cotact IT department.</p></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table>
          </body>
        </html>
        """.format(dfObj.to_html())
        body = MIMEText(html, 'html')
        msg.attach(body)
        # Mail Content set
        if dfObj.shape[0]>1:
            send_Email(username, password, username, to_addrs, msg)
            print("Email successfully sent to", to_addrs)
    except smtplib.SMTPAuthenticationError:
        print('SMTPAuthenticationError')
        print("Email not sent to", to_addrs)


