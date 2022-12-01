import matplotlib.pyplot as plt

def generate_pie_char():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # plt.show()  # mostramos la gráfica
    plt.savefig('pie.png')  #queremos generar una imagen para que el programa no se detenga en esta parte
    plt.close()