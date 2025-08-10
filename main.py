# Un programa para libreria de juegos
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
            cash = int(input("Ingresa la cantidad de dinero que quiere ingresar a la cuenta: "))
            if cash <= 0:
                print("No se pueden ingresar numeros negativos a la cuenta")
            else:
                sum(wallet) + cash
                wallet.append(cash)
                break
            break

        except ValueError:
            print("Debe ser un numero entero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)


class Game:
    def __init__(self, game_id, name, description, price):
        self.id = game_id
        self.name = name
        self.description = description
        self.price = price

    def info(self):
        print(f"\n--{self.name}--")
        print(f"ID del juego: {self.id}\n"
              f"Precio del juego: Q.{self.price}\n"
              f"Descripcion del juego: {self.description}")

games = []
def add_game():
    suma = sum(wallet) + 0
    print("Ingresar un nuevo juego")
    print(f"> Tienes: ${suma}")
    while True:
        game_id = input("Ingresa el ID del juego: ").upper()
        if game_id not in games:
            break
        else:
            print("Ya existe esta ID")
    name = input("Ingresa el nombre del juego: ").lower()
    description = input("Ingres la descripcion del juego: ").lower()
    while True:
        try:
            price = int(input("Ingresa el precio del juego en dolares: "))
            if price <= 0:
                print("Debe ser un valor mayor a 0")
            if price > suma:
                print("No tienes los fondos suficeintes para comprar el juego")
                break
            if price >= 0 and price <= suma:
                print("Gracias por tu compra")
                rest = sum(wallet) - price
                wallet.remove(suma)
                wallet.append(rest)
                break

        except ValueError:
            print("Debe ser un numero entero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)
    gamu = Game(game_id, name, description, price)
    games.append(gamu)

def show_games():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        print("----Biblioteca----")
        i = 1
        for gamu in games:
            print(f"Libro {i}:", end="")
            gamu.info()
            i += 1
        print()

def delete_game():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        search_game = input("Ingresa el ID del juego: ").upper()
        for gamu in games:
            if gamu.id == search_game:
                games.remove(gamu)
                print("Se ha eliminado el juego de la biblioteca")
                break

def order_games():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        games.sort()
        print(games)

def searc_games():
    if not games:
        print("Aun no tienes juegos en la biblioteca")
    else:
        for i in games:
            while True:
                search =input("Ingresa el ID del juego: ").upper()
                if i.id == search:
                    i.info()
                    break
                else:
                    print("No se encontro el juego, intenta de nuevo")



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
          "7. Salir")
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