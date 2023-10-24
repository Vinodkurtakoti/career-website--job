from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
      {
        'id':1,
        'role':'Data Analyst',
        'location':'Bengluru',
        'salary': 'RS 9,00,000'
      },
      {
        'id':2,
        'role':'Data Engineer',
        'location':'pune'

      },
      {
        'id':3,
        'role':'Data Scientist',
        'location':'Delhi',
        'salary': 'RS 10,00,000'
      },
      {
        'id':4,
        'role':' Front-end Engineer',
        'location':'Munbai',
        'salary': 'RS 13,00,000'
      }
    ]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name="VSK TECH")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)