"""Core module of dundie"""
from dundie.utils.log import get_logger # dundie=> principal e utils sub modulo
#    |
#    ==> import relativo nao funcionou, retornamos ao import absoluto                                     
# **************************
# * Executando (deu certo) *
# **************************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# ipython -i dundie/core.py
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.25.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: load
# Out[1]: <function __main__.load(filepath)>
#
# In [2]: load("assets/people.csv")
# Out[2]: 
# ['Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com\n',
# 'Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com\n',
# 'Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com\n',
# '  ']
#
# In [3]: retorno = load("assets/people.csv") ==> carregou conteudo do arquivo
#
# ***************************************
# * Verificando quantidade de registros *
# ***************************************
#
# In [4]: len(retorno)
# Out[4]: 4
#
# **************************************************
# * Verificando se quantidade de registros esta ok *
# **************************************************
#
# In [5]: assert len(retorno) == 4 (ok)
#
# In [6]: assert len(retorno) == 2 (AssertionError:)
# ----------------------------------------------
# AssertionErrorTraceback (most recent call last)
# Cell In[6], line 1
# ----> 1 assert len(retorno) == 2
#
# AssertionError: 
#
# from .utils.log import get_logger # import relativo
#  |    |     |     |     |
# *************************
# * Executando (deu erro) *
# *************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
#  ipython -i dundie/core.py
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.25.0 -- An enhanced Interactive Python. Type '?' for help.
# ----------------------------------------------
# ImportError  Traceback (most recent call last)
# File ~/Projetos/python_dundie_rewardss/dundie/core.py:2
#       1 """Core module of dundie"""
# ----> 2 from .utils.log import get_logger  # lembrando dundie e o modulo principal e 
#       3                                     # utils e o sub modulo
#       5 log = get_logger()
#
# ImportError: attempted relative import with no known parent package
#
# In [1]: exit()
#
#
log = get_logger()

def load(filepath):
    """Loads data from filepath to the database.
    
    >>> len(load('assets/people.csv'))
    3
    >>> load('assets/people.csv')[0][0]
    'J'
    """
# **************************************
# * Execucao depois incluir            *
# * >>> len(load('assets/people.csv')) *
# * 4                                  *
# **************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# python -m doctest dundie/core.py
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# python -m doctest -v dundie/core.py
# Trying:
#    len(load('assets/people.csv'))
# Expecting:
#    4
# ok
# 1 items had no tests:
#    core
# 1 items passed all tests:
#   1 tests in core.load
# 1 tests in 2 items.
# 1 passed and 0 failed.
# Test passed.
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %

    try:
        with open(filepath) as file_:
#            for line in file_:
#                print(line)
        #    return file_.readlines()
            return [line.strip() for line in file_.readlines()] 
    except FileNotFoundError as e:
#        print(f"File not found {e}")
        log.error(str(e))
        raise e
#
# Resolvendo
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
# dundie load people.csv
# Hello initializing dundie
# File not found [Errno 2] No such file or directory: 'people.csv'

# Resolvendo apos criar o 'people.csv'
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# dundie load assets/people.csv ==>  assets/people.csv filepath = caminho
# Hello initializing dundie
# Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com
#
# Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com
#
# Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com

# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# python -m dundie load assets/people.csv
# Hello initializing dundie
# Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com
#
# Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com
#
# Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com

# ************************************************************
# * Teste unitario chamando direto a funcao usando o ipython *
# ************************************************************

# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# ipython -i dundie/core.py
# Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.25.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: load
# Out[1]: <function __main__.load(filepath)>

# In [2]: load("assets/people.csv")
# Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com

# Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com

# Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com

# In [3]: exit()
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 

# *************************
# * Teste usando o pytest *
# *************************
#
# Passo 1:
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pip install -e '.[test]'
# ...
# ...
# Downloading pytest-8.3.3-py3-none-any.whl (342 kB)
#   ━━━━━━━━━━ 342.3/342… 407.3     eta 0:00:00
#              kB         kB/s 
# ...
# ...
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
#              
# Passo 2:
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % pytest
# ============ test session starts =============
# platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0
# rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
# collected 0 items                            
#
# =========== no tests ran in 0.00s ============
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %

# ****************************************
# * DOCTEST e outra ferramenta do Python *
# ****************************************

# def load(filepath):
#    """Loads data from filepath to the database"""
#    try:
#        with open(filepath) as file_:
#            return file_.readlines()
#    except FileNotFoundError as e:
#        log.error(str(e)) ==> micro ../python-base/logs.py
#        raise e
# Criar a pasta utils e dentro dela o log.py e chama-lo aqui no core.py   

