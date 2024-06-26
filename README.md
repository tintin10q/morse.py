# morse.py
A simple 65 line python file to encode and decode morse code. No dependencies.


The rules of morse code are like this:

1. The length of a dot is one unit
2. A dash is three units
3. The space between parts of the same letter is one unit  
4. The space between letters is three units
5. The space between a word is seven letters

I encode spaces as `#` so the message `attack at dawn` becomes:

```
.#-###-###-###.#-###-#.#-#.###-#.#-#######.#-###-#######-#.#.###.#-###.#-#-###-#.###
```

Having the spaces as # is nice because iterating over the string becomes very easy. 
Something like this:

```python
short = 50 # ms
long = short * 3

for char in self.morse:
  if char == '-':
    on_long()  
  elif char == '.':
    on()
  elif char == '#':
    off()
```

## CLI

You can use the python script as a cli:

```
$ python morse.py --help
usage: morse.py [-h] [-e] [-d] [text ...]

Morse code encoder and decoder. By default we encode

positional arguments:
  text          Input text to encode or decode (optional) you can also use
                stdin instead

options:
  -h, --help    show this help message and exit
  -e, --encode  Encode text into morse
  -d, --decode  Decode morse code
```

<div style="background-color: red;">
<img alt="Morse code alphabeth" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/800px-International_Morse_Code.svg.png" style="height: 40rem; mix-blend-mode: multiply; background-color: white">
</div>


