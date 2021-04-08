from flask import Flask, request
from hdbcli import dbapi
import pandas as pd

app = Flask(__name__)
@app.route("/")
def hello():
    conn = dbapi.connect(address='f7b3794a-0204-4e0e-bb55-47546c370b5f.hana.trial-us10.hanacloud.ondemand.com',port='443',user='DBADMIN',password='BrainyBHC1')
    cursor = conn.cursor()
    sql_command = "SELECT TOP 10 * FROM TCURF;"
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
	
    print(df.head())
    
    cursor.close()
	
    conn.close()
	
    return df.to_html(header="false", table_id="table")

@app.route('/events')
def query_example():
    conn = dbapi.connect(address='f7b3794a-0204-4e0e-bb55-47546c370b5f.hana.trial-us10.hanacloud.ondemand.com',port='443',user='DBADMIN',password='BrainyBHC1')
    cursor = conn.cursor()
    formulaNumber = request.args.get('formulaNumber')
    documentCurrency = request.args.get('docCurrency')
    exchangeRateType = request.args.get('exchRateType')
    sql_command = "SELECT TOP 10 * FROM TCURF WHERE FCURR ='USD' and TCURR = '"+documentCurrency+"' and KURST = '"+exchangeRateType+"'"
    cursor.execute(sql_command)
    df = pd.DataFrame.from_records(cursor, columns=[i[0] for i in cursor.description])
	
    print(df.head())
    
    cursor.close()
	
    conn.close()
	
    return '''<h1> Formula Number : {}</h1> <br><br> {}'''.format(formulaNumber,df.to_html(header="true", table_id="table"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
