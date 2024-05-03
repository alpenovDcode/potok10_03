import json

# with open("data/Moscow.json", "r") as city_file:
#     file_data = json.load(city_file)
# print(file_data["city_name"])

class CityData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.city = self.file_data["city_name"]
        self.max_temp = self.file_data["max_temp"]
        self.min_temp = self.file_data["min_temp"]

    def read_data(self):
        with open(self.file_path, "r") as city_file:
            return json.load(city_file)

class CityNameWithNewData(CityData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.rainy_days = self.file_data["rainy_days"]


moscow = CityData('data/Moscow.json')
kazan = CityNameWithNewData('data/Kazan.json')
print(moscow.file_data)
print(moscow.city)
print(moscow.max_temp)
print(moscow.min_temp)

print(kazan.file_data)
print(kazan.city)
print(kazan.max_temp)
print(kazan.min_temp)
print(kazan.rainy_days)
