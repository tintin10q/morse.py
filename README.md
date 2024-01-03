# morse.py
A simple 65 line python file to encode and decode morse code. No dependencies.


The rules of morse code are like this:

1. The length of a dot is one unit
2. A dash is three units
3. The space between parts of the same letter is one unit  
4. The space between letters is three units
5. The space between a word is seven letters

I encode spaces a `#` so the message `attack at dawn` becomes:

```
.#-###-###-###.#-###-#.#-#.###-#.#-#######.#-###-#######-#.#.###.#-###.#-#-###-#.###
```

Having the spaces as # is nice because then you can iterate over the string and you only have to do 2 different sleeps per character. And then a turn off and turn on and turn on long.
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

<div style="background-color: red;">
<img alt="Morse code alphabeth" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/800px-International_Morse_Code.svg.png" style="height: 40rem; mix-blend-mode: multiply; background-color: white">
</div>


