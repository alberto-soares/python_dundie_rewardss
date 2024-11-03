# Entry Point

# Resolvendo executar o comando dundie load people.txt com o import sys
#
# Usando o import sys

# import sys

# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# dundie load people.csv
# Hello initializing dundie
# Executing dundie from entry point.

# print(sys.argv) # sys.argv passa argumentos

# Capturando os argumentos passados 
# dundie load people.csv
# Hello initializing dundie
# ['/Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/dundie', 
# 'load', 'people.csv'] ==> print para identificar todos argumentos da lista
# Executing dundie from entry point.

# print(sys.argv[1:]) 

# Capturando o comando e o arquivo
# dundie load people.csv
# Hello initializing dundie 
# ['load', 'people.csv'] ==> print para identificar os argumentos a partir [1:]
# Executing dundie from entry point.

# Usando o import argparse

# import argparse ==> criado cli.py

from dundie.cli import main  # Import Absoluto
# from .cli import main # Import Relativo problema e retornamos ao absoluto
# Resolvendo
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# python -m dundie
# Hello initializing dundie
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# dundie
# Hello initializing dundie
# Executing entry point for dundie ... new information

# Criando a funcao load passando o arquivo ==> foi para core.py


# Soluçao final  
if __name__ == "__main__":
    main()
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# python -m dundie
# Hello initializing dundie
# Executing entry point for dundie ... new information
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
# dundie
# Hello initializing dundie
# Executing entry point for dundie ... new information

# *******************************************************
# * Resultado da execucao apos criacao cli.py e core.py *
# *******************************************************

# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# dundie load assets/people.csv
# Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com

# Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com

# Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com

