from flask import Flask, render_template

app = Flask(__name__)

#http://127.0.0.1:5000
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/<int:num_fila>/<int:num_columna>', methods=['GET'])
def fila(num_fila,num_columna):
    return render_template("edicion.html",num_fila=num_fila,num_columna=num_columna)

@app.route('/<int:num_fila>/<int:num_columna>/<color1>', methods=['GET'])
def filacolor(num_fila,num_columna,color1):
    return render_template("edicion.html",num_fila=num_fila,num_columna=num_columna,color1=color1)

@app.route('/<int:num_fila>/<int:num_columna>/<color1>/<color2>', methods=['GET'])
def edicion(num_fila,num_columna,color1,color2):
    return render_template("edicion.html", num_fila=num_fila , num_columna=num_columna , color1=color1, color2=color2)




if __name__ == '__main__':
    app.run(debug=True) 