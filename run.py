from website import app, db
import os

# creating db and output file when they do not already exist
if not os.path.exists("website/site.db"):
    db.create_all()
if not os.path.exists("website/static/out"):
    os.mkdir("website/static/out")

if __name__=='__main__':
    app.run(debug=True)