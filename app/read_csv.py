import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      # Unimos el header y el row para obtener tuplas
      iterable = zip(header, row)

      # Una form
      # country_dict = dict(iterable)

      # Tomamos la tupla y la convertimos en diccionario
      country_dict = {key: value for key, value in iterable}

      # agregar el diccionario
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(data[0])
