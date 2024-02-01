from flask import Flask, render_template


app = Flask(__name__)


JOBS = [{'id':1,
       'title': 'Luxury beachfront',
       'location': 'Honolulu',
       'price':"$100000"},
       {'id':2,
          'title': 'Luxury apt',
          'location': 'Hono Island',
          'price':"$32321"},
       {'id':3,
          'title': 'Luxury villa',
          'location': 'Holalola',
          'price':"$99999"}]

@app.route("/")

def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="encering")

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True) 