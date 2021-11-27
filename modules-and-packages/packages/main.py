import pkg.mod1, pkg.mod2

print(pkg.mod1.foo())
x = pkg.mod2.Bar()
print(x)

from pkg.mod1 import foo
foo()

from pkg.mod2 import Bar as Qux
x = Qux()
print(x)

import pkg
print(pkg.A)