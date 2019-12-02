# Patch:

**Uasge**
> Suppose method "M" of class "A" calls the method "N" of class "B". 
To perform the unittest on such case. We patch the method "N" of class "B" to return desired value
to simulate the behaviour of instance of class A.

- Allows to mimic the desired behaviour by simulating the target without changing the code level implementation.
- Syntax: ``patch(target)``
    - Target might be methods/function of some module inside the package.
    - For eg: ``patch('package.module.class.method')`` **or** ``patch('package.module.function')``
    
  





