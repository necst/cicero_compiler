
from re import error
from re2compiler import compile
from emulate_execution import _run_asap
import os
import urllib.request
import warnings
import itertools

verbose = False
ok = 0
total = 0
path_regex = "clamAV.regex"
path_input = "clamAv.input"
if not os.path.exists(path_regex):
    with urllib.request.urlopen("https://raw.githubusercontent.com/jackwadden/ANMLZoo/master/ClamAV/regex/515_nocounter.1chip.anml") as response:
        html = response.read()
        with open(path_regex,'w') as f:
            f.write(html.decode('utf-8'))

if not os.path.exists(path_input):
    with urllib.request.urlopen("https://github.com/jackwadden/ANMLZoo/blob/master/ClamAV/inputs/vasim_1MB.input?raw=true") as response:
        html = response.read()
        with open(path_input,'wb') as f:
            f.write(html)

with open(path_regex) as f:
    for i,line in enumerate(f.readlines()):
        if verbose:
            print(f'regex {i+1}',flush=True)
            warnings.simplefilter('once')
        try:
            code        = compile(data=line, no_postfix=False, no_prefix=False, O1=True, frontend="pcre") 
            num_instr   = len(code.split("\n"))
            if num_instr<512:
                ok+=1
        except Exception as e:
            print(f'Problem with regex {i+1} ({line})', e)
        
        total+=1
        if verbose:
            warnings.resetwarnings()
            print(f'code length: {num_instr}')
print(f'{ok} out of {total} correctly compiled')

with open(path_input,'rb') as f:
    inputs = f.read().split(b'\n')
    print(f'found {len(inputs)} inputs')
    inputs = filter(lambda x: len(x) > 50, inputs)
    inputs = list(itertools.islice(inputs,100))
    print(f'took {len(inputs)} inputs')

ok      = 0
total   = 0
with open(path_regex) as f:
    for i,line in enumerate(f.readlines()):
        
        try:
            code        = compile(data=line, no_postfix=False, no_prefix=False, O1=True, frontend="pcre",backend="python") 
            
            for j,string in enumerate(inputs):
                res ,cc        = _run_asap(code=code, string=string, debug=False) 
                print(f'regex {i} \t, input {j} (len: {len(string)})\t, match {res}\t, number of cycles {cc}')

                if res :
                    ok+=1
        except Exception as e:
            print(f'Problem with regex {i+1} ({line})', e)
        
        total+=1

print(f'{ok} out of {total} accepted')    