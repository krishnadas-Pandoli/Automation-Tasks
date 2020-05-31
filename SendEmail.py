import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from datetime import datetime

username = 'krishnadas@dfdfdfdf.com'
password = 'sdsdsdsd'
server = smtplib.SMTP('')
today = datetime.now()


fcount=0            #  PickTicket folder exists or not
pickticket=0        #  number of PickTicket files
pickticketitem=0    #  number of Item files
pickticketbarcode=0 #  number of Barcode files
pickticketmaster=0  #  number of master files
tcount = 0          #  Total PickTicket files
datepath="C:/Python_File_Transfer/PickTicket/"+ today.strftime('%Y%m%d')

confcount=0         #  PickConfirm Folder exists or not
pickCofirm=0        #  number of PickConfirm files
ackcount=0          #  number of Ack files
sohcount=0          #  number of SOH files
grncount=0          #  number of GRN files
conftotalcount=0    #  Total PickConfirm files
datepathpc="C:/Python_File_Transfer/PickConfirm/"+ today.strftime('%Y%m%d')

salescount=0        #  Sales Folder exists or not
salestotalcount=0   #  Total Sales files
datepathsales = "C:/Python_File_Transfer/Sales/" + today.strftime('%Y%m%d')
"""
SMTP Server Information
Office 365: outlook.office365.com
"""
# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg):
    server = smtplib.SMTP('outlook.office365.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

# Read email list txt
email_list = [line.strip() for line in open('email.txt')]

for to_addrs in email_list:
    msg = MIMEMultipart()

    msg['Subject'] = "File Transfer Notification..! This is an Automatic email"
    msg['From'] = username
    msg['To'] = to_addrs

    try:

        if os.path.isdir(datepath)==True:
            fcount=1
            list_dir = []
            list_dir = os.listdir(datepath)
            for file in list_dir:
                if file.startswith('PICKTICKET'):  # eg: '.txt'
                    pickticket += 1
                if file.startswith('COG_ITEM'):  # eg: '.txt'
                    pickticketitem += 1
                if file.startswith('COG_BARCODE'):  # eg: '.txt'
                    pickticketbarcode += 1
                if file.startswith('MASTERDATA'):  # eg: '.txt'
                    pickticketmaster += 1
                tcount += 1

        if os.path.isdir(datepathpc)==True:
            confcount=1
            list_dir = []
            list_dir = os.listdir(datepathpc)
            for file in list_dir:
                if file.startswith('0_PIXC'):  # eg: '.txt'
                    pickCofirm += 1
                if file.startswith('RL_Ack_COG'):  # eg: '.txt'
                    ackcount += 1
                if file.startswith('Prod'):  # eg: '.txt'
                    sohcount += 1
                if file.startswith('0_PIXGRNUAE'):  # eg: '.txt'
                    grncount += 1
                conftotalcount += 1

        if os.path.isdir(datepathsales)==True:
            salescount=1
            list_dir = []
            list_dir = os.listdir(datepathsales)
            for file in list_dir:
                salestotalcount += 1
                conftotalcount += 1

        # Create the body of the message (a HTML version for formatting).
        html = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html style="width:100%;font-family:verdana, geneva, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">
         <head> 
          <meta charset="UTF-8"> 
          <meta content="width=device-width, initial-scale=1" name="viewport"> 
          <meta name="x-apple-disable-message-reformatting"> 
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
          <meta content="telephone=no" name="format-detection"> 
          <title>Copy of New email template 2020-05-22</title> 
          <!--[if (mso 16)]>
            <style type="text/css">
            a {text-decoration: none;}
            </style>
            <![endif]--> 
          <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> 
          <style type="text/css">
        @media only screen and (max-width:600px) {p, ul li, ol li, a { font-size:16px!important; line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:26px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } h1 a { font-size:30px!important } h2 a { font-size:26px!important } h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:14px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:14px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:inline-block!important } a.es-button { font-size:18px!important; display:inline-block!important } .es-btn-fw { border-width:10px 0px!important; text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } .es-desk-hidden { display:table-row!important; width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } .es-desk-menu-hidden { display:table-cell!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } }
        a {
        	font-family:verdana, geneva, sans-serif;
        	font-size:14px;
        	text-decoration:underline;
        }
        #outlook a {
        	padding:0;
        }
        .ExternalClass {
        	width:100%;
        }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
        	line-height:100%;
        }
        .es-button {
        	mso-style-priority:100!important;
        	text-decoration:none!important;
        }
        a[x-apple-data-detectors] {
        	color:inherit!important;
        	text-decoration:none!important;
        	font-size:inherit!important;
        	font-family:inherit!important;
        	font-weight:inherit!important;
        	line-height:inherit!important;
        }
        .es-desk-hidden {
        	display:none;
        	float:left;
        	overflow:hidden;
        	width:0;
        	max-height:0;
        	line-height:0;
        	mso-hide:all;
        }
        </style> 
         </head> 
         <body style="width:100%;font-family:verdana, geneva, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;"> 
          <div class="es-wrapper-color" style="background-color:#FFFFFF;"> 
           <!--[if gte mso 9]>
        			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
        				<v:fill type="tile" color="#ffffff" origin="0.5, 0" position="0.5,0"></v:fill>
        			</v:background>
        		<![endif]--> 
           <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;"> 
             <tr style="border-collapse:collapse;"> 
              <td valign="top" style="padding:0;Margin:0;"> 
               <table class="es-header" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;"> 
                 <tr style="border-collapse:collapse;"> 
                  <td class="es-adaptive" align="center" style="padding:0;Margin:0;"> 
                   <table class="es-header-body" width="700" cellspacing="0" cellpadding="0" bgcolor="#f6f6f6" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;"> 
                     <tr style="border-collapse:collapse;"> 
                      <td style="Margin:0;padding-top:10px;padding-bottom:10px;padding-left:10px;padding-right:10px;background-color:#741B47;" bgcolor="#741b47" align="left"> 
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="680" valign="top" align="center" style="padding:0;Margin:0;"> 
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="center" style="padding:0;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:40px;font-family:verdana, geneva, sans-serif;line-height:60px;color:#CCCCCC;"><span style="color:#FFFFFF;">&nbsp; &nbsp; &nbsp; SHARAF RETAIL</span>&nbsp;💬<br><span style="font-size:22px;color:#FFFFFF;">File Transfer Details</span></p></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                     <tr style="border-collapse:collapse;"> 
                      <td align="left" bgcolor="#ffffff" style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px;background-color:#FFFFFF;"> 
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="700" valign="top" align="center" style="padding:0;Margin:0;"> 
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td style="padding:0;Margin:0;"> 
                               <table class="es-menu" width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                                 <tr class="links" style="border-collapse:collapse;"> 
                                  <td style="Margin:0;padding-left:5px;padding-right:5px;padding-top:10px;padding-bottom:10px;border:0;" width="50%" bgcolor="#741b47" align="center"><a target="_blank" style="font-family:verdana, geneva, sans-serif;font-size:16px;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;display:block;color:#FFFFFF;" href="http://www.sharafgroup.com/english/our-companies/retail">Home</a></td> 
                                  <td style="Margin:0;padding-left:5px;padding-right:5px;padding-top:10px;padding-bottom:10px;border:0;" width="50%" bgcolor="#ffffff" align="center"><a target="_blank" style="font-family:verdana, geneva, sans-serif;font-size:16px;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;display:block;color:#333333;" href="https://http://www.sharafgroup.com/english/contact-us/sharaf-worldwide">Contact</a></td> 
                                 </tr> 
                               </table></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table> 
               <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> 
                 <tr style="border-collapse:collapse;"> 
                  <td align="center" style="padding:0;Margin:0;"> 
                   <table class="es-content-body" width="700" cellspacing="0" cellpadding="0" bgcolor="#f6f6f6" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#F6F6F6;"> 
                     <tr style="border-collapse:collapse;"> 
                      <td align="left" bgcolor="#ffffff" style="padding:0;Margin:0;padding-top:20px;padding-bottom:20px;background-color:#FFFFFF;"> 
                       <!--[if mso]><table width="700" cellpadding="0" cellspacing="0"><tr><td width="334" valign="top"><![endif]--> 
                       <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="334" class="es-m-p20b" align="left" style="padding:0;Margin:0;"> 
                           <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="center" bgcolor="#ffffff" style="padding:0;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:20px;font-family:verdana, geneva, sans-serif;line-height:30px;color:#333333;"><strong>COG To RL</strong></p></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table> 
                       <!--[if mso]></td><td width="40"></td><td width="326" valign="top"><![endif]--> 
                       <table cellpadding="0" cellspacing="0" class="es-right" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="326" align="left" style="padding:0;Margin:0;"> 
                           <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="center" bgcolor="#ffffff" style="padding:0;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:20px;font-family:verdana, geneva, sans-serif;line-height:30px;color:#333333;"><strong>RL To COG</strong></p></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table> 
                       <!--[if mso]></td></tr></table><![endif]--></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table> 
               <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;"> 
                 <tr style="border-collapse:collapse;"> 
                  <td align="center" style="padding:0;Margin:0;"> 
                   <table class="es-content-body" width="700" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#F6F6F6;"> 
                     <tr style="border-collapse:collapse;"> 
                      <td align="left" bgcolor="#ffffff" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#FFFFFF;"> 
                       <!--[if mso]><table width="660" cellpadding="0" cellspacing="0"><tr><td width="310" valign="top"><![endif]--> 
                       <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="310" class="es-m-p20b" align="left" style="padding:0;Margin:0;"> 
                           <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="left" style="padding:5px;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:15px;font-family:verdana, geneva, sans-serif;line-height:23px;color:#333333;"><strong>Total Files Sent Today :""" + str(
            tcount) + """<br>Pick Ticket :""" + str(pickticket) + """<br>Item Master:"""+ str(pickticketitem) +"""<br>Barcode:"""+ str(pickticketbarcode) +"""<br>Master Data:"""+ str(pickticketmaster) +"""<br>Others:</strong></p></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table> 
                       <!--[if mso]></td><td width="40"></td><td width="310" valign="top"><![endif]--> 
                       <table cellpadding="0" cellspacing="0" class="es-right" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="310" align="left" style="padding:0;Margin:0;"> 
                           <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="left" style="padding:5px;Margin:0;"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:15px;font-family:verdana, geneva, sans-serif;line-height:23px;color:#333333;"><strong>Total File Sent Today:""" + str(
            conftotalcount) + """<br>Pick Confirmation :""" + str(pickCofirm) + """<br>SOH :""" + str(
            sohcount) + """<br>Sales:""" + str(salestotalcount) + """<br>Acknowledge :""" + str(
            ackcount) + """<br>Grn : """ + str(grncount) + """</strong></p></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table> 
                       <!--[if mso]></td></tr></table><![endif]--></td> 
                     </tr> 
                     <tr style="border-collapse:collapse;"> 
                      <td align="left" style="padding:0;Margin:0;"> 
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                         <tr style="border-collapse:collapse;"> 
                          <td width="700" valign="top" align="center" style="padding:0;Margin:0;"> 
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                             <tr style="border-collapse:collapse;"> 
                              <td align="center" style="Margin:0;padding-top:10px;padding-bottom:10px;padding-left:20px;padding-right:20px;font-size:0;"> 
                               <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;"> 
                                 <tr style="border-collapse:collapse;"> 
                                  <td style="padding:0;Margin:0px;border-bottom:1px solid transparent;background:#FFFFFFnone repeat scroll 0% 0%;height:1px;width:100%;margin:0px;"></td> 
                                 </tr> 
                               </table></td> 
                             </tr> 
                           </table></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table> 
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
               </table></td> 
             </tr> 
           </table> 
          </div>  
         </body>
        </html>
        """

        # Attach HTML to the email
        body = MIMEText(html, 'html')
        msg.attach(body)
        # Mail Content set
        send_mail(username, password, username, to_addrs, msg)
        print("cog to RL",tcount)
        print("RL to cog",conftotalcount )
        print ("Email successfully sent to", to_addrs)
    except smtplib.SMTPAuthenticationError:
        print('SMTPAuthenticationError')
        print ("Email not sent to", to_addrs)