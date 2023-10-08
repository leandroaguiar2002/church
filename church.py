
# Church booleans
#true = λx.λy.x => f(x,y) = x
TRUE = (lambda x: lambda y: x)
#false = λx.λy.y => f(x,y) = y
FALSE = (lambda x: lambda y: y)

# AND true false
# (((λx.λy.x y x) (λx.λy.x)) (λx.λy.y))
# (λy.(λx.λy.x) y (λx.λy.x)) (λx.λy.y)
# ((λx.λy.x) (λx.λy.y) (λx.λy.x))
# (λy.y) (λx.λy.x)
# (λx.λy.x)
# true
AND = (lambda x: lambda y: (x(y)(x)))
OR = (lambda x: lambda y: (x(x)(y)))

# NOT true
# (λx.x false true) (λx.λy.x)
# (λx.λy.x) false true
# (λy.false) true
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
# ((λm.λn.λf.λx m f (n f x) λf.λx.f(x)) λf.λx.f(f(x)))
# (λn.λf.λx λf.λx.f(x) f (n f x)) λf.λx.f(f(x))
# λf.λx λf.λx.f(x) f (λf.λx.(f(f(x)) f x))
# λf.λx.f(x) f(λf.λx.(f(f(x)) f x))