import pytest
from subprocess import check_output #*

@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """Test command load"""
    out = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    ).decode("utf-8").split("\n")
    #breakpoint() # verifica pq imprime 5 linhas ==> ipdb
# Passo 1
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# export PYTHONBREAKPOINT=ipdb.set_trace
#
# Passo 2
# (.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -s -v tests integration
#=========================== test session starts =============================
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 2 items                                                                                                                            
#
#tests/test_load.py::test_load PASSED
#integration/test_load.py::test_load PASSED
#
#============================= 2 passed in 0.04s ==============================
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss % 
# pytest -s -v tests integration
#========================== test session starts ===============================
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 2 items                                                                                                                            
#
#tests/test_load.py::test_load PASSED
#integration/test_load.py::test_load 
#[TerminalIPythonApp] WARNING | File not found: '/Users/albertosoares/.vscode/extensions/ms-python.python-2024.12.3-darwin-arm64/python_files/pythonrc.py'
#> /Users/albertosoares/Projetos/python_dundie_rewardss/integration/test_load.py(9)test_load()
#      8     breakpoint()
#----> 9     assert len(out)  == 4
#     10 
#
#ipdb> 
#ipdb> out
#['Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com', 
# ' Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com', 
# ' Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com', 
# '   ', '']
#   |> essa e a linha 5 que esta sendo impressa em branco
#
    assert len(out)  == 2 # 2 ??? mas sao 3 registros no people.csv
#
# Resultado ao executar a linha de comando
#(.venv) (base) albertosoares@MacBook-Pro-de-Alberto python_dundie_rewardss %
# pytest -s -v tests integration
#=========================== test session starts ============================
#platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0 -- 
# /Users/albertosoares/Projetos/python_dundie_rewardss/.venv/bin/python
#cachedir: .pytest_cache
#rootdir: /Users/albertosoares/Projetos/python_dundie_rewardss
#collected 2 items                                                                                                                            
#
#tests/test_load.py::test_load PASSED
#integration/test_load.py::test_load FAILED
#
#================================= FAILURES =================================
#_____________________________ test_load _____________________________________
#
#    def test_load():
#        """Test command load"""
#        out = check_output(
#            ["dundie", "load", "tests/assets/people.csv"]
#        ).decode("utf-8").split("\n")
#>       assert len(out)  == 4
#E       AssertionError: assert 5 == 4
#E        +  where 5 = len(['Jim Helpert, Sales, Salesman, jim@dundlermilfflin.com', ' Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com', ' Alberto Santos, Tecnology, System Analisy, santos@dundlermilfflin.com', '   ', ''])
#
#integration/test_load.py:8: AssertionError
#====================== short test summary info ===============================
#FAILED integration/test_load.py::test_load - AssertionError: assert 5 == 4

