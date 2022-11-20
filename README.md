# Argparse-Workshop
### Short introduction to Argparse in 3 differents cases.

In this repository you'll see those Argparse introduction :  
  
- Basic arguments case
- infinite arguments and choices case
- Optionnal arguments case  
  
There's a correction part with the examples in it.  
And an exercise part to try out what you have learned (this is just an empty architecture folder tho).
  
### Basic case  
```
cd initiation_correction
./main a b c
  a       argument value, positive integer.
  b       argument value, positive integer.
  c       argument value, positive integer.
```  
  
### Infinite case  
```
cd initiation_correction
./main [foo] [bar] [baz], xi...
  func    [foo], [bar], [baz], the different choice of functions.
  xi      the positive integer values for testing, Argparse can handle infinite "xi".
```  
  
### Optional case  
```
cd initiation_correction
./main a [n | x y]
  a             argument value, positive integer.
  --size [n]    argument value, positive integer.
  --pos [x y]   Vector of Coordinates (X, Y) (optionnal).
```  
