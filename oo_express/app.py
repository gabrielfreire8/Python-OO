from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao("gabriel", 5)
restaurante_praca.receber_avaliacao("pedro", 4)



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()