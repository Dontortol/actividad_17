# Un programa para libreria de juegos


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
    print("Ingresar un nuevo juego")
    while True:
        game_id = input("Ingresa el ID del juego: ").upper()
        if game_id not in games:
            break
        else:
            print("Ya existe esta ID")
    name = input("Ingresa el nombre del juego: ").lower().capitalize()
    description = input("Ingres la descripcion del juego: ").lower()
    while True:
        try:
            price = int(input("Ingresa el precio del juego en dolares: "))
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

