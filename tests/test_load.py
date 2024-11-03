import pytest
from dundie.core import load
#
# Criado o file constants para constantes repetitivas
from .constants import PEOPLE_FILE 
#

@pytest.mark.unit
#
#********************************************
# Resultado da execucao do pytest.mark.unit *
#********************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -s -m 'unit'
#============================ test session starts =============================
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#configfile: pyproject.toml
#testpaths: tests, integration
#collected 2 items / 1 deselected / 1 selected                                                                                                
#
#tests/test_load.py::test_load PASSED
#
#============================== warnings summary ==============================
#integration/test_load.py:4
#  /Users/albertosoares/Projetos/python_dundie_rewardss/integration/
# test_load.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.integration - 
# is this a typo?  You can register custom marks to avoid this warning - for 
# details, see https://docs.pytest.org/en/stable/how-to/mark.html
#    @pytest.mark.integration
#
#-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
#================= 1 passed, 1 deselected, 1 warning in 0.01s =================
#
#
@pytest.mark.high
#
#********************************************
# Resultado da execucao do pytest.mark.high *
#********************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -s -m 'unit and high'
#============================ test session starts =============================
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#configfile: pyproject.toml
#testpaths: tests, integration
#collected 2 items / 1 deselected / 1 selected                                                                                                
#
#tests/test_load.py::test_load PASSED
#
#======================= 1 passed, 1 deselected in 0.01s =====================
#

def test_load():
    """Test function load function."""
#    assert len(load('assets/people.csv')) == 4 # antes criar a pasta tests
#    assert len(load('tests/assets/people.csv')) == 4
    assert len(load(PEOPLE_FILE)) == 3 # PEOPLE_FILE  no constants.py
#    breakpoint() # para parar a execucao
#    assert load('assets/people.csv')[0][0] == 'J' # antes criar a pasta tests
#    assert load('tests/assets/people.csv')[0][0] == 'J'
    assert load(PEOPLE_FILE)[0][0] == 'J'
# 
# ********************************************
# * Execucao apos alteracao para PEOPLE_FILE *
# ********************************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# make test
#============================= test session starts ==============================
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 1 item                                                               
#
#tests/test_load.py::test_load PASSED
#
#============================= 1 passed in 0.01s ==============================
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss
#
# *********************************
# * 1º Verificar pytest instalado *
# *********************************
# 
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest
# ============ test session starts =============
# platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0
# rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
# collected 0 items
#
# =========== no tests ran in 0.00s ============
#
# ********************************************
# * 2º Criar o arquivo test_load.py  na raiz *
# ********************************************
#
# *************************************************
# * 3º Inserir na funcao o(s) comando(s) de teste *
# *************************************************
# assert len(load('assets/people.csv')) == 4
# assert load('assets/people.csv')[0][0] == 'J'
#
# ************************************************************
# * 4º Rodar novamente o pytest para capturar o test_load.py *
# ************************************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest
# ============ test session starts =============
# platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0
# rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
# collected 1 item                             
#
# test_load.py .                         [100%]
#
# ============= 1 passed in 0.01s ==============
#
# *******************************
# * Capturando mais informacoes *
# *******************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -v
# ============ test session starts =============
# platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
# collected 1 item                             
#
# test_load.py::test_load PASSED         [100%]
#
#============= 1 passed in 0.01s ==============
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -vv
# ============ test session starts =============
# platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
# collected 1 item                             
#
# test_load.py::test_load PASSED         [100%]
#
# ============= 1 passed in 0.01s ==============
#
# ********************
# * Para usar o ipdb * 
# ********************
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# export PYTHONBREAKPOINT=ipdb.set_trace
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
#
# ************************************
# * Se rodar pytest comum breakpoint * 
# ************************************
#
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -vv
# ============ test session starts =============
# platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
# collected 1 item                             
#
# test_load.py::test_load FAILED         [100%]
#
# ================== FAILURES ==================
# _________________ test_load __________________
#
#    def test_load():
#        """Test load function."""
#        assert len(load('assets/people.csv')) == 4
#        breakpoint() # para parar a execucao
#>       assert load('assets/people.csv')[0][0] == 'J'
#
#test_load.py:8: 
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#../../anaconda3/lib/python3.11/bdb.py:90: in trace_dispatch
#    return self.dispatch_line(frame)
#../../anaconda3/lib/python3.11/bdb.py:114: in dispatch_line
#    self.user_line(frame)
#../../anaconda3/lib/python3.11/pdb.py:331: in user_line
#    self.interaction(frame, None)
#.venv/lib/python3.11/site-packages/IPython/core/debugger.py:443: in interaction
#    OldPdb.interaction(self, frame, tb)
#../../anaconda3/lib/python3.11/pdb.py:426: in interaction
#    self._cmdloop()
#../../anaconda3/lib/python3.11/pdb.py:391: in _cmdloop
#    self.cmdloop()
#../../anaconda3/lib/python3.11/cmd.py:126: in cmdloop
#    line = input(self.prompt)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#
#self = <_pytest.capture.DontReadFromInput object at 0x101a7a450>
#size = -1
#
#    def read(self, size: int = -1) -> str:
#>       raise OSError(
#            "pytest: reading from stdin while output is captured!  Consider 
# using `-s`." 
#        )
#E       OSError: pytest: reading from stdin while output is captured!  Consider
# using `-s`.
#
#.venv/lib/python3.11/site-packages/_pytest/capture.py:209: OSError
#------------ Captured stdout call ------------
#> /Users/albertosoares/Projetos/python_dundie_rewardss/test_load.py(8)test_load()
#      7     breakpoint() # para parar a execucao
#----> 8     assert load('assets/people.csv')[0][0] == 'J'
#      9 #
#
#ipdb> 
#========== short test summary info ===========
#FAILED test_load.py::test_load - OSError: pytest: reading from stdin while 
# output is captured!  Consider using `-s`.
#============= 1 failed in 0.26s ==============
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
# 
# ************************
# * Resolvendo esse erro *
# ************************
#
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -vv -s
#============ test session starts =============
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 1 item                             
#
#test_load.py::test_load > /Users/albertosoares/Projetos/python_dundie_rewardss/test_load.py(8)test_load()
#      7     breakpoint() # para parar a execucao
#----> 8     assert load('assets/people.csv')[0][0] == 'J'
#      9 #
#
#ipdb> 
#
#
#ipdb> l
#      3 
#      4 def test_load():
#      5     """Test load function."""
#      6     assert len(load('assets/people.csv')) == 4
#      7     breakpoint() # para parar a execucao
#----> 8     assert load('assets/people.csv')[0][0] == 'J'
#      9 #
#     10 # *********************************
#     11 # * 1º Verificar pytest instalado *
#     12 # *********************************
#     13 #
#
#ipdb>
#
# ********************************
# * Em caso de erro,para depurar *
# ********************************
#
# **************************
# * Chamando a funcao load *
# **************************
#
# ipdb> load
# <function load at 0x10465d940>
#
# ******************************************
# * Execucao depois de criar a pasta tests *
# ******************************************
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -vv -s
#============ test session starts =============
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 1 item                             
#
#tests/test_load.py::test_load PASSED
#
#============= 1 passed in 0.01s ==============
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
