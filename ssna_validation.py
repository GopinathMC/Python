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


USERNAME = "ps573034@NA.CORP.CARGILL.COM"

PASSWORD = "i_b_pP2$01"

DRIVER = "/opt/cloudera/impalaodbc/lib/64/libclouderaimpalaodbc64.so"

HOST = "peanut-impala.cargill.com"

PORT = "21050"

SEND_FROM = "-datalake-production-support-team@Cargill.com"

SEND_TO = ["-datalake-production-support-team@Cargill.com"]

def getImpalaConnection(uid,pwd):	
	try:
		connString = "Driver="+DRIVER+";Host=" +HOST+ ";Port=" +PORT+";AuthMech=3;UseSASL=1;UID=" +uid+ ";PWD=" +pwd+ ";SSL=1;AllowSelfSignedServerCert=1;kerberos_service_name=impala;"
		cnxn= pyodbc.connect(connString, autocommit = True)
	except pyodbc.Error as ex:
		sqlstate = ex.args[1]
		print(sqlstate)
		print("Connection Failed")
		cnxn = None
	return cnxn
	
def execute_query_col(cnxn,query):
	cursor = cnxn.cursor()
	try:
		cursor.execute(query) 
		columns = cursor.description 
		query_opt = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

	except:
		query_opt = None
	return query_opt

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

if __name__== "__main__":
	cnxn = getImpalaConnection(USERNAME,PASSWORD)
	
	if cnxn:
		cmmp_query = """
				select "fdtb09pibp" as tbl_name , count(*) as count from prd_internal_corn_mill_mpls.fdtb09pibp union all
				select "fdtb13pibp" as tbl_name, count(*) from prd_internal_corn_mill_mpls.fdtb13pibp
				union all
				select "fdtb17pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fdtb17pibp
				union all
				select "fdtb22pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fdtb22pibp
				union all
				select "fdtb86pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fdtb86pibp
				union all
				select "fdtba5pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fdtba5pibp
				union all
				select "fdtbaupibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fdtbaupibp
				union all
				select "ffdm01p"as tbl_name,count(*) from prd_internal_corn_mill_mpls.ffdm01p
				union all
				select "fqtb04pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fqtb04pibp
				union all
				select "fscu01pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fscu01pibp
				union all
				select "fscu02pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fscu02pibp
				union all
				select "fscu03pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fscu03pibp
				union all
				select "fscu04pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fscu04pibp
				union all
				select "fsin01pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fsin01pibp
				union all
				select "fscu07pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fscu07pibp
				union all
				select "fsin05pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fsin05pibp
				union all
				select "fsmc01ibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.fsmc01ibp
				union all
				select "ftfp02pibp"as tbl_name,count(*) from prd_internal_corn_mill_mpls.ftfp02pibp;
			"""
		cmmp_table_count = execute_query_col(cnxn,cmmp_query)
		print("Data loads from Corn Mill Mpls CMMP ---> Count")
		print(cmmp_table_count)
		intr_cmmp_query = """
				select "fdtb09pibp" as tbl_name , count(*) as count from prd_internal_cmmp.fdtb09pibp union all
				select "fdtb13pibp" as tbl_name, count(*) from prd_internal_cmmp.fdtb13pibp
				union all
				select "fdtb17pibp"as tbl_name,count(*) from prd_internal_cmmp.fdtb17pibp
				union all
				select "fdtb22pibp"as tbl_name,count(*) from prd_internal_cmmp.fdtb22pibp
				union all
				select "fdtb86pibp"as tbl_name,count(*) from prd_internal_cmmp.fdtb86pibp
				union all
				select "fdtba5pibp"as tbl_name,count(*) from prd_internal_cmmp.fdtba5pibp
				union all
				select "fdtbaupibp"as tbl_name,count(*) from prd_internal_cmmp.fdtbaupibp
				union all
				select "ffdm01p"as tbl_name,count(*) from prd_internal_cmmp.ffdm01p
				union all
				select "fqtb04pibp"as tbl_name,count(*) from prd_internal_cmmp.fqtb04pibp
				union all
				select "fscu01pibp"as tbl_name,count(*) from prd_internal_cmmp.fscu01pibp
				union all
				select "fscu02pibp"as tbl_name,count(*) from prd_internal_cmmp.fscu02pibp
				union all
				select "fscu03pibp"as tbl_name,count(*) from prd_internal_cmmp.fscu03pibp
				union all
				select "fscu04pibp"as tbl_name,count(*) from prd_internal_cmmp.fscu04pibp
				union all
				select "fsin01pibp"as tbl_name,count(*) from prd_internal_cmmp.fsin01pibp
				union all
				select "fscu07pibp"as tbl_name,count(*) from prd_internal_cmmp.fscu07pibp
				union all
				select "fsin05pibp"as tbl_name,count(*) from prd_internal_cmmp.fsin05pibp
				union all
				select "fsmc01ibp"as tbl_name,count(*) from prd_internal_cmmp.fsmc01ibp
				union all
				select "ftfp02pibp"as tbl_name,count(*) from prd_internal_cmmp.ftfp02pibp;
			"""
		intr_cmmp_table_count = execute_query_col(cnxn,intr_cmmp_query)
		print("Data loads from Internal CMMP ---> Count")
		print(intr_cmmp_table_count)
		internal_cmmp =  [i for i in intr_cmmp_table_count if i not in cmmp_table_count]
		internal_corn_mill_mpls = [j for j in cmmp_table_count if j not in intr_cmmp_table_count]
		if internal_cmmp and internal_corn_mill_mpls:
			send_from = SEND_FROM
			send_to = SEND_TO
			subject = ("SSNA CMMP Notification")
			messageHTML = """
			<p>Hi Team,</p>
			<div>
			<p>Please find difference count</p>
			<p>prd_internal_cmmp : """+str(internal_cmmp)+"""</p>
			<p>prd_internal_corn_mill_mpls : """+str(internal_corn_mill_mpls)+"""</p>
			</div>
			<p>&nbsp;</p>
			<p><em>Regards,</em></p>
			<p><strong><em>Cargill Data Lake Support</em></strong></p>
			</div>
			<p>&nbsp;</p>
			"""
			send_mail(send_from, send_to, subject, messageHTML)

