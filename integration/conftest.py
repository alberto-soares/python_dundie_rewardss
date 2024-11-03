MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers', line
    ), MARKER.split("\n")) # outra forma p/ o comando for abaixo  

#    for line in MARKER.split("\n"):
#        config.addinivalue_line('markers', line)
