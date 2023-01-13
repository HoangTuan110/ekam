from ..ekam import eval

def test_eval():
    env = eval("""
    -> $b $build
    <- 'uname -a' $host
    """)
    assert env['b'] == {'t': 6, 'v': 'build'}
    assert env['host'] == {'t': 2, 'v': 'uname -a'}
