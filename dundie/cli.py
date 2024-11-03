import argparse
from dundie.core import load  # Import Absoluto
# from .core import load  # Import Relativo problemas e retornamos ao absoluto

def main():
#    print("Executing entry point for dundie ... new information")
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with cautious.",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        # required=False
        default="help"
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        # required=False
        default=None
    )
    args = parser.parse_args()
    # print(args)

    # Resultado ao executar a linha de comando
    # (.venv) (base) albertosoares@MacBook-Pro-de-Alberto 
    # python_dundie_rewardss % dundie load people.csv
    # Hello initializing dundie
    # Namespace(subcommand='load', filepath='people.csv')

    # try:
    # globals()[args.subcommand](args.filepath) # choices ja resolve
    #
    # except KeyError:
       # print("Subcommand is invalid.")
    # print("Executing dundie from entry point.") # o print foi alterado
    # print(globals()[args.subcommand](args.filepath))
    # |>  alteracao no core.py para return na funcao load imprime uma lista
    print(*globals()[args.subcommand](args.filepath)) #, end="") #, sep="\n")
    # |                                                |> nao imprime linha 5 
    # | 
    # |> alteracao para nao imprimir uma lista mas pulando linha

#
#
# main()  ==> observar que o setup.py já invoca a main()
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# python -m dundie
# Hello initializing dundie
# Executing entry point for dundie ... new information
# Mas quando vc roda
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
# dundie
# Hello initializing dundie
# Executing entry point for dundie ... new information
# Executing entry point for dundie ... new information
#
#
# *****************************************************************
# * Execucao apos alteracao no core.py para return na funcao load *
# *****************************************************************
#
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# dundie load assets/people.csv
# ['Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com\n', 
# 'Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com\n',
#  'Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com\n',
#  '  ']
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
#
#
# **************************************************************************
# * Apos alterar o print para imprimir pulando linha, e nao mais uma lista *
# **************************************************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
# dundie load assets/people.csv
#Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com
# Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com
# Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com
#  
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
