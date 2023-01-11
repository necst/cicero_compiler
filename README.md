# re2compiler
A compiler for [CICERO](https://github.com/necst/cicero)

---------------------------------------
# How to start?
Very simple!

1. clone this repo
2. run `pip install -r requirements.txt` to fetch required packages
3. run re2compiler.py

  to feed regular expression you can use several options:
  1. using cli input (by not providing a file neither specifying `-data`)
  2. using a file
  3. using the `-data` argument
  4. programmatically by recalling compile from another python script as in example.py
  ```
  import re2compiler

  data 	= '(a|b)*'
  output	= re2compiler.compile(data=data)
  print(output)
  ```
  ![screen shot example](https://github.com/necst/cicero_compiler/blob/master/wiki/howto.PNG)
  
# Optional arguments:
  
| option                     | description                                                                                  | example
|----------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| -h, --help                  | show this help message and exit                                                              |    
| -data [DATA]                | allows to pass the input string representing the regular expression directly via parameter . |
| -dotast DOTAST              | save abstract syntax tree representation using dot format in the given file.                 |![abstract syntax tree example](https://github.com/necst/cicero_compilerblob/master/wiki/ast.dot.svg)
| -dotirlowered DOTIRLOWERED  | save ir representation using dot format in the given file.                                   |![ir](https://github.com/necst/cicero_compilerblob/master/wiki/ir.dot.svg)
| -dotcode DOTCODE            | save a code representatio using dot format in the given file.                                |![code](https://github.com/necst/cicero_compilerblob/master/wiki/code.dot.svg) 
| -o [O]                      | output file containing the code that represent the regular expression.                       |
| -O1                         | perform simple optimization                                                                  |![optimized code](https://github.com/necst/cicero_compilerblob/master/wiki/code.dot.optimized.svg)


If you find this repository useful, please use the following citation:

```
@article{parravicini2021cicero,
    title = {{CICERO}: A Domain-Specific Architecture for Efficient Regular Expression Matching},
    author = {Daniele Parravicini and Davide Conficconi and Emanuele Del Sozzo and Christian Pilato and Marco D. Santambrogio}, 
    journal = {{ACM} Transactions on Embedded Computing Systems},
    year = 2021,
    month = {oct},
    publisher = {Association for Computing Machinery ({ACM})},
    volume = {20},
    number = {5s},
    pages = {1--24},
    doi = {10.1145/3476982},
    url = {https://doi.org/10.1145%2F3476982},
 } 
```
