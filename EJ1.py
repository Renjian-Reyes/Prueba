from bottle import Bottle, route, run, request, error, redirect
import json

nicks = ['paco']
passwords = ['feo']


@route('/login')
def login():
    return '''
        <h1> Cliente,introduzca sus datos
        <form action="/login" method="post">
        <br /> Usuario: <input name="username" type="text" />
            Contraseña: <input name="password" type="password" />
            <input value="Loggearse" type="submit" />
        </form>'''


@route('/login', method='post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    for i,j in zip(nicks,passwords):
        if i == username and j == password:
                return redirect('/login/main')
    else:
        return redirect('/error_register')


@route('/error_register')
def error_register():
    return '''
            El cliente no existe, dale click
            <a href=/login> aqui </a>
            para volver a introducir tus datos <br />   
            Si desea registrase, dele click
            <a href=/register> aqui </a>
            '''


@route('/register')
def register():
    return '''
        Ingrese sus datos para registrarse en la Pagina
        <form action="/register" method="post">
      <br />Usuario: <input name="username" type="text" />
            Contraseña: <input name="password" type="password" />
            <input value="Aceptar" type="submit" />
          </form>'''


@route('/register', method='post')
def do_register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    nicks.append(username)
    passwords.append(password)
    return redirect('/login')


@route('/login/main')
def main():
    return "<li> <a href=/login/hola> Saludos  <br /> </a>" \
           "     <a href=/alta> Dar de alta </a> </li>"


@route('/login/hola')
def hola():
    return "Hola, te damos la bienvenida a nuestra Pagina Web <br />" \
           "<a href=/login/main> Volver al Menu Principal <a>"


@error(404)
def error404(error):
    return 'Lo sentimos, La Pagina Web no se encuentra a su disposicion, vuelta en otro momento'


run(host='localhost', port=8080)
