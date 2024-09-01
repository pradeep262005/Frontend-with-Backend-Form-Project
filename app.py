from flask import Flask, render_template,request
import psycopg2

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    if request.method== 'POST':
        email=request.form['mail']
        pwd=request.form['pwd']

        #Connection

        conn=psycopg2.connect(
            host='localhost',
            database='pradeep',
            user='postgres',
            password='1234'
        )
        cur=conn.cursor()

        cur.execute('INSERT INTO pradeep_40 VALUES(%s,%s)',(email,pwd))

        conn.commit()
        cur.close()
        conn.close()

        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
