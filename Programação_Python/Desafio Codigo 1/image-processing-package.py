image-processing-package/
    README.md # Utilizado para fazer a documentação do pacote no site do Pypi
    setup.py # Usado para especificar como um pacote deve ser construído
    requirements.txt # Usado para passar as dependências que devem ser instaladas com o pacote. Opcionalmente, podem ser especificadas as versões (evitar)
    image_processing/
        processing/ # pasta com os modulos a serem empacotados
            __init__.py
            combination.py # manipulação em mais de uma imagem
            transformation.py # manipulação de apenas uma imagem
        utils/ # pasta com os modulos a serem empacotados
            __init__.py
            io.py # leitura e escrita em imagem
            plot.py # plotar imagem