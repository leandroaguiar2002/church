
# Church booleans
#true = true => false => true
TRUE = (lambda x: lambda y: x)
#false = true => false => false
FALSE = (lambda x: lambda y: y)

# AND true false
# ((true => false => true) (true => false => false)) (true => false => false)
# (false => (true => false => false)) (true => false => false)
# (true => false => false)
AND = (lambda x: lambda y: (x(y)(x)))
OR = (lambda x: lambda y: (x(x)(y)))
# NOT true
# ((true => false => true) (false) (true))
# (false => false) (true)
# false
NOT = (lambda x: x (FALSE)(TRUE))
# if p then x else y
IF = (lambda f: lambda x: lambda y: (f(x))(y))

# Church Numerals
ZERO = (lambda f: lambda x: x)
ONE = (lambda f: lambda x: f(x))
TWO = (lambda f: lambda x: f(f(x)))
THREE = (lambda f: lambda x: f(f(f(x))))

PLUS = (lambda m: lambda n: lambda f: lambda x: (m(f)) (n(f)(x)))
# PLUS ONE TWO
# (f(x) (f)) (f(f(x)) (f) (x))
# (f(x)) (f(f(x)))
# (f(f(f(x))))