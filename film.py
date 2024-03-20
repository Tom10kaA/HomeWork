import requests

class SWApi:
    @staticmethod
    def get_entity(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_film(self, film_id):
        base_url = 'https://swapi.dev/api/films/'
        film_url = f"{base_url}{film_id}/"
        film_info = self.get_entity(film_url)

        if film_info:
            title = film_info['title']
            characters = [self.get_entity(url)['name'] for url in film_info['characters']]
            vehicles = [self.get_entity(url)['name'] for url in film_info['vehicles']]
            starships = [self.get_entity(url)['name'] for url in film_info['starships']]
            species = [self.get_entity(url)['name'] for url in film_info['species']]

            print(f"Фільм: {title}")
            print("Персонажі:")
            for i, character in enumerate(characters, 1):
                print(f"  {i}. {character}")
            print("Транспортні засоби:")
            for i, vehicle in enumerate(vehicles, 1):
                print(f"  {i}. {vehicle}")
            print("Космічні кораблі:")
            for i, starship in enumerate(starships, 1):
                print(f"  {i}. {starship}")
            print("Види істот:")
            for i, specie in enumerate(species, 1):
                print(f"  {i}. {specie}")
        else:
            print("Інформацію про фільм не знайдено.")

    @staticmethod
    def choose_film():
        print("1:'A New Hope', 2:'The Empire Strikes Back', 3:'Return of the Jedi', 4:'The Phantom Menace', 5:'Attack of the Clones', 6:'Revenge of the Sith'.")
        print("Введіть номер фільму від 1 до 6 для отримання інформації про фільм:")

        film_id = input("Номер фільму: ")
        sw_api = SWApi()
        sw_api.get_film(film_id)