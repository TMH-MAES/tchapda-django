from flask import Flask,render_template
from donnees import description4, liste, taille

application = Flask(__name__)





  
#racine de l'application
@application.route('/')
@application.route('/home')
def main():
    return render_template('index.html')

@application.route('/produits')

def contenus():
    return render_template('produits.html', data = liste, taille = taille)


@application.route('/achats')

def acheter():
    return "creer d'abord un compte ✅"

@application.route('/description1')

def description1():
    return render_template("description1.html")

@application.route('/description2')
def description2():
    return render_template("description2.html")

@application.route("/description3")
def description3():
    return render_template("description3.html")

@application.route('/description/<int:id>')
def show_product_description(id):
    for p in range(taille):
        if p==id:
            print(liste[id])
@application.route('/test')
def testing():
    return render_template('testing.html', d=description4, data = liste, taille = taille)




if __name__ == '__main__':
    application.run(debug=True)
