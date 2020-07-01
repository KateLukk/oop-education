from tesst1 import String


def test_is_empty():
    s = String(["f", 's', ' '])
    rez = s.is_empty()
    assert False == rez
    s1 = String([])
    rez1 = s1.is_empty()
    assert True == rez1

def test_space():
    s = String([' ', 'u', 'g', ' '])
    result = s.space()
    assert ['u', 'g'] == result

def test_small():
    s = String(['u', 'G'])
    result = s.small()
    assert ['u', 'g'] == result

def test_big():
    s = String(['u', 'G'])
    result = s.big()
    assert ['U', 'G'] == result

def test_slovo():
    s = String(['u', 'n', 'o'])
    result = s.is_slovo('no')
    result1 = s.is_slovo('kkk')
    assert True == result
    assert False == result1

def test_rf():
    s = String(['u', 'o', 'n', 'o'])
    result = s.rf('o')
    result1 = s.rf('l')
    assert 3 == result
    assert -1 == result1

def test_f():
    s = String(['u', 'n', 'n', 'o'])
    result = s.f('n')
    result1 = s.f('l')
    assert 1 == result
    assert -1 == result1

def test_double():
    s = String(['u', 'n', 'o'])
    result = s.double(2)
    assert ['u', 'n', 'o', 'u', 'n', 'o'] == result

def test_concat():
    s = String(['u', 'n', 'o'])
    st = ['d', 'o', 'u', 's']
    s.concat(st)
    assert ['u', 'n', 'o', 'd', 'o', 'u', 's'] == s.list

def test_len():
    s = String(['u', 'n', 'o'])
    result = s.length()
    assert 3 == result

test_space()
test_is_empty()
test_space()
test_small()
test_big()
test_slovo()
test_rf()
test_f()
test_double()
test_concat()
test_len()