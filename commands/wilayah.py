import requests
import json

class Wilayah:
    def __init__(self, url):
        self.url = url
    def fetchData(self):
        try:
            data = self.url
            response = requests.get(data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan saat fetch URL: {e}")
            return None

class List(Wilayah):
    def __init__(self, cakupan, kode):
        self.url = f"https://www.emsifa.com/api-wilayah-indonesia/api/{cakupan}{f'/{kode}' if kode is not None else ''}.json"
        print(self.url)
    def show_data(self):
        data = self.fetchData()
        total = len(data)
        columns = 4  
        rows = -(-len(data) // columns) 
        split_data = [data[i * rows:(i + 1) * rows] for i in range(columns)]
        max_lens = [max(len(f"{item['id']}. {item['name']}") for item in col) + 5 for col in split_data if col]

        for row in range(rows):
            row_data = []
            for col in range(columns):
                if row < len(split_data[col]):
                    text = f"{split_data[col][row]['id']}. {split_data[col][row]['name']}".ljust(max_lens[col])
                    row_data.append(text)
                else:
                    row_data.append("".ljust(max_lens[col]))
            print("".join(row_data))
            
# CMD : provinsi list
dataprov = List("provinces", None)
dataprov.show_data()

# CMD : kabupaten list 32
# datakab = List("regencies", "32")
# datakab.show_data()

# # CMD : kecamatan list 3276
# datakab = List("districts", "3276")
# datakab.show_data()

# datakab = List("villages", "3276021")
# datakab.show_data()



def kodewilayah_formatter(s):
    parts = []
    lengths = [2, 2, 2, 4] 
    index = 0    

    for length in lengths:
        if index < len(s): 
            parts.append(s[index:index+length])
            index += length
    
    return ".".join(parts)



        
