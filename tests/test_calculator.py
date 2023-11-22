from simple_calculator.simple_calculator import adicao, subtracao, multiplicacao, divisao
def test_adicao():
    assert 4 == adicao(2.0, 2.0)
    assert 20.5 == adicao(20, 0.5)
    assert "Uma letra não pode ser operada" == adicao("a", 2)
    assert "Uma letra não pode ser operada" == adicao("a", "b")

def test_subtracao():
    assert 0 == subtracao(2.0, 2.0)
    assert 19.5 == subtracao(20.0, 0.5)
    assert "Uma letra não pode ser operada" == subtracao("a", 2.0)

def test_multiplicacao():
    assert 4 == multiplicacao(2.0, 2.0)
    assert 10 == multiplicacao(20.0, 0.5)
    assert "Uma letra não pode ser operada" == multiplicacao("a", 2.0)

def test_divisao():
    assert 1 == divisao(2.0, 2.0)
    assert "Divisão por zero" == divisao(2.0, 0.0)
    assert 40 == divisao(20.0, 0.5)
    assert "Uma letra não pode ser operada" == divisao("a", 2)