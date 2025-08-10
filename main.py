# Un programa para libreria de juegos dia de creacion 9
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def user_info(self):
        print("Nombre de usuario:",self.name)
        print("Contraseña",self.password)

users = []
def add_user():
    print("--Registro de usuario--")
    user_name = input("Ingresa el nombre del usuario: ").lower()
    password = input("Crea una contraseña: ")
    usr = User(user_name, password)
    users.append(usr)

wallet = []
def money():
    print("Comprobacion antes de pagar")
    for usr in users:
        while True:
            user_name = input("Ingresa el nombre del usuario: ").lower()
            if usr.name == user_name:
                break
            else:
                print("El usuario no existe")

    for passw in users:
        while True:
            password = input("Ingrese la contraseña: ")
            if passw.password != password:
                print("Contraseña incorrecta, intente de nuevo")
            else:
                break
    while True:
        try:
            cash = int(input("Ingresa la cantidad de pelucholares que quiere ingresar a la cuenta: "))
            if cash <= 0:
                print("No se pueden ingresar numeros negativos a la cuenta")
            else:
                sum(wallet) + cash
                wallet.append(cash)
                break

        except ValueError:
            print("Debe ser un numero entero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)


class Game:
    def __init__(self, game_id, name, description, price):
        self.game_id = game_id
        self.name = name
        self.description = description
        self.price = price

    def info(self):
        print(f"\n--{self.name}--")
        print(f"ID del juego: {self.game_id}\n"
              f"Precio del juego: Q.{self.price}\n"
              f"Descripcion del juego: {self.description}")

games = []
def add_game():
    suma = sum(wallet) + 0
    print("Ingresar un nuevo juego")
    print(f"> Tienes: ${suma}")
    while True:
        gamid = input("Ingresa el ID del juego: ").upper()
        for a in games:
            if a.game_id == gamid:
                print("El ID ya existe")
                gamid = None
                break
        if gamid != None:
            break
    name = input("Ingresa el nombre del juego: ").lower()
    description = input("Ingres la descripcion del juego: ").lower()
    while True:
        try:
            price = int(input("Ingresa el precio del juego en pelucholares: "))
            if price <= 0:
                print("Debe ser un valor mayor a 0")
            elif price > suma:
                print("No tienes los fondos suficeintes para comprar el juego")
                break
            else:
                print("Gracias por tu compra", wallet)
                rest = sum(wallet) - price
                wallet.clear()
                wallet.append(rest)
                gamu = Game(gamid, name, description, price)
                games.append(gamu)
                break

        except ValueError:
            print("Debe ser un numero entero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)

def show_games():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        print("----Biblioteca----")
        i = 1
        for gamu in games:
            print(f"Juego {i}:", end="")
            gamu.info()
            i += 1
        print()

def delete_game():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        while True:
            gamu = input("Ingresa el ID del juego: ").upper()
            for a in games:
                if a.game_id == gamu:
                    games.remove(a)
                    print("Se ha eliminado el juego de la biblioteca")
                    break
            else:
                gamu = None
            if gamu != None:
                break
            else:
                print("El juego no se ha encontrado en la biblioteca")



def get_name(e):
    return e.name

def order_games():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        games.sort(key=get_name)
        print(games)

def searc_games():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        while True:
            gamu = input("Ingresa el ID del juego: ").upper()
            for a in games:
                if a.game_id == gamu:
                    a.info()
                    break
            else:
                gamu = None
            if gamu != None:
                break
            else:
                print("El juego no se ha encontrado en la biblioteca")


def secret():
        print("""       
                ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
                ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
                ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
                ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
                Has encontrado el secreto de mi biblioteca
                felicidades. Soy el creador de este programa
    
    """)


print("Bienvenido a Rodrigos Games, Tienda virtual de videojuegos")
add_user()
while True:
    print("----Rodrigos Games----\n"
          "1. Ingresar dinero a la cuenta\n"
          "2. Agregar juego\n"
          "3. Ver biblioteca\n"
          "4. Eliminar juego\n"
          "5. Buscar juego\n"
          "6. Ver datos de la cuenta\n"
          "7. Salir\n"
          "jijijiji dia mas 10")
    select_op = input("Ingrese una de las siguientes opciones: ")
    match select_op:
        case "1":
            money()
        case "2":
            if not wallet:
                print("No tienes dinero para comprar")
            else:
                add_game()
        case "3":
            if not games:
                print("No tienes juegos en la biblioteca")
            else:
                while True:
                    print("1. Ver bilbioteca\n"
                          "2. Ver en orden alfabetico\n"
                          "3. Regresar al menu")
                    select = input("Ingrese una de las siguientes opciones: ")
                    match select:
                        case "1":
                            show_games()
                        case "2":
                            order_games()
                        case "3":
                            print("Regresando al menu")
                            break
        case "4":
            delete_game()
        case "5":
            searc_games()
        case "6":
            print("--Datos de la cuenta--")
            for info in users:
                print(info.user_info())
            print("Tienes en la billetera: $",sum(wallet))
        case "7":
            print("Cerrando Rodrigos Games")
            break
        case "19":
            print("Bienvenido a la sala secreta")
            choose = input("Estas seguro que quieres conocer al jefe???? si/no: ").lower()
            match choose:
                case "si":
                    secret()
                case "no":
                    print("Regresando al menu")
                case _:
                    print("Debe ser dentro de las opciones")
        case _:
            print('Ingrese una opcion dentro del rango')