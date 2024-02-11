from flask import Flask, abort, flash, make_response, redirect, render_template, g, request, url_for
import psycopg2
import os

app = Flask(__name__)

dbase = None
app.config['SECRET_KEY'] = 'home56172'

hesh = []

@app.route("/")
def index():
  directory = directory = r"C:\Users\danii\OneDrive\Документы\GitHub\studing_Vue.js_2.0"
  files = os.listdir(directory)
  return render_template('main_template.html', title="Главная", menu=hesh, files = files)

@app.route("/book_image/<book_id>")
def book_image(book_id):
  img = dbase.getBookImage(book_id)
  if img:
    img = img.tobytes()

  if img == None:
    img = open('./static/images/default.jpg', "rb")
    img = img.read()
    
  
  h = make_response(img)
  h.headers['Content-Type'] = 'image/jpg'
  return h

@app.route("/show_image/<book_id>")
def show_image(book_id):
  return book_image(book_id)

# comment to create db
if __name__ == "__main__":
  app.run(debug = True)

# umcomment to create db
# create_db()