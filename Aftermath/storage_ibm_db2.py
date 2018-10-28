import pandas as pd
import ibm_db as database
import numpy 
import ibm_db_dbi
# Credentials Copied from IBM Cloud
authentication={
  "hostname": "dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net",
  "password": "_42XiQQWr_uf",
  "https_url": "https://dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net:8443",
  "port": 50000,
  "ssldsn": "DATABASE=BLUDB;HOSTNAME=dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=dash14124;PWD=_42XiQQWr_uf;Security=SSL;",
  "host": "dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net",
  "jdbcurl": "jdbc:db2://dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB",
  "uri": "db2://dash14124:_42XiQQWr_uf@dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB",
  "db": "BLUDB",
  "dsn": "DATABASE=BLUDB;HOSTNAME=dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=dash14124;PWD=_42XiQQWr_uf;",
  "username": "dash14124",
  "ssljdbcurl": "jdbc:db2://dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net:50001/BLUDB:sslConnection=true;"
}
def data_query_multiple_arguments(query):
	data_secure_newtwork = authentication.get("dsn")
	#Standard code to connect to ibm_db2
	connection_to_data_base = database.connect(data_secure_newtwork, "", "")
	stmt = database.exec_immediate(connection_to_data_base, query)


def data_query(query):
	data_secure_newtwork = authentication.get("dsn")
	#Standard code to connect to ibm_db2
	connection_to_data_base = database.connect(data_secure_newtwork, "", "")
	stmt = database.exec_immediate(connection_to_data_base, query)
	database.fetch_both(stmt)
	pconn = ibm_db_dbi.Connection(connection_to_data_base)
	data_frame_from_data_base = pd.read_sql(query, pconn)
	return data_frame_from_data_base
#print(data_query(""" SELECT * FROM DASH14124.SAFE """))
pre_string = "We understand that you are filled with "
string = "I feel"
post_string = " feelings. Ups and downs are common in life.If you would like to talk to someone. Please Call us at +1800(256)8990"
response_string_to_get_city_input = "Thanks for the response." 
