from flask import Flask
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5001"), debug=True)
