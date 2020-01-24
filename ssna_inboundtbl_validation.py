# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:02:22 2019

@author: g440051
"""
import requests
import pyodbc
import json, ast
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import COMMASPACE, formatdate


uid = "ps573034@NA.CORP.CARGILL.COM"

pwd = "i_b_pP2$01"

DRIVER = "/opt/cloudera/impalaodbc/lib/64/libclouderaimpalaodbc64.so"

HOST = "peanut-impala.cargill.com"

PORT = "21050"

query = """
select "md_ibp_outbound_customer" as tbl_name,count(*) from prd_internal_fibi_ibp.md_ibp_outbound_customer union all 
select "md_ibp_outbound_location" as tbl_name,count(*) from prd_internal_fibi_ibp.md_ibp_outbound_location union all 
select "md_ibp_outbound_uom" as tbl_name,count(*) from prd_internal_fibi_ibp.md_ibp_outbound_uom union all 
select "md_ibp_outbound_product" as tbl_name,count(*) from prd_internal_fibi_ibp.md_ibp_outbound_product union all
select "md_ibp_outbound_customerproduct" as tbl_name,count(*) from prd_internal_fibi_ibp.md_ibp_outbound_customerproduct union all
select "ibp_outbound_supply_percom" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_percom union all 
select "ibp_outbound_supply_perprodcust" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodcust union all 
select "ibp_outbound_supply_perloc" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perloc union all
select "ibp_outbound_supply_perprodloc" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodloc union all
select "ibp_outbound_supply_perprodloccompsrc" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodloccompsrc union all
select "ibp_outbound_supply_perprodloccust" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodloccust union all
select "ibp_outbound_supply_perprodloclocfr" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodloclocfr union all
select "ibp_outbound_supply_perprodlocsrc" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodlocsrc union all
select "ibp_outbound_supply_perprodlocsrcagg" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodlocsrcagg union all
select "ibp_outbound_supply_perprodloctoloc" as tbl_name,count(*) from prd_internal_fibi_ibp.ibp_outbound_supply_perprodloctoloc union all
select "td_ibp_outbound_supply_keyfigures" as tbl_name,count(*) from prd_internal_fibi_ibp.td_ibp_outbound_supply_keyfigures union all
select "td_ibp_outbound_demand_keyfigures_union" as tbl_name,count(*) from prd_internal_fibi_ibp.td_ibp_outbound_demand_keyfigures_union union all
select "td_ibp_outbound_supply_keyfigures_union" as tbl_name,count(*) from prd_internal_fibi_ibp.td_ibp_outbound_supply_keyfigures_union union all
select "td_ibp_outbound_demand_keyfigures_lag" as tbl_name,count(*) from prd_internal_fibi_ibp.td_ibp_outbound_demand_keyfigures_lag 
"""
empty_tbls = []

SEND_FROM = "-datalake-production-support-team@Cargill.com"

SEND_TO = ["-datalake-production-support-team@Cargill.com"]



def send_mail(send_from, send_to, subject, messageHTML, server="mailrelayapp.na.corp.cargill.com"):
	assert isinstance(send_to, list)
	
	email = send_from
	send_to_email = COMMASPACE.join(send_to) 

	msg = MIMEMultipart('alternative')
	msg['From'] = email
	msg['To'] = send_to_email
	msg['Subject'] = subject

	msg.attach(MIMEText(messageHTML, 'html'))

	server = smtplib.SMTP(server)
	server.starttls()
	text = msg.as_string()
	server.sendmail(email, send_to_email, text)
	server.quit()


connString = "Driver="+DRIVER+";Host=" +HOST+ ";Port=" +PORT+";AuthMech=3;UseSASL=1;UID=" +uid+ ";PWD=" +pwd+ ";SSL=1;AllowSelfSignedServerCert=1;kerberos_service_name=impala;"
cnxn= pyodbc.connect(connString, autocommit = True)
cursor = cnxn.cursor()
ct = cursor.execute(query)
result = ct.fetchall()
print(result)
for row in result:
    ls = list(row)
    if ls[1] == 0:
        print("Error - "+ls[0] +" table is empty")
        empty_tbls.append(ls[0])
    else:
        pass;
    
if empty_tbls:
    send_from = SEND_FROM
    send_to = SEND_TO
    subject = ("SSNA Inbound Table Error Notification -- Testing")
    messageHTML = """
    <p>Hi Team,</p>
    <div>
    <p>Please find the SSNA inbound tables which are/is empty</p>
    <p>"""+str(empty_tbls)+"""</p>
    </div>
    <p>&nbsp;</p>
    <p><em>Regards,</em></p>
    <p><strong><em>Cargill Data Lake Support</em></strong></p>
    </div>
    <p>&nbsp;</p>
    """
    send_mail(send_from, send_to, subject, messageHTML)

else:
    print("All inbound tables is having record")

