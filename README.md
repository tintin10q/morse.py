# morse.py
A simple 65 line python file to encode and decode morse code. No dependencies.

The rules of morse code are like this:

1. The length of a dot is one unit
2. A dash is three units
3. The space between parts of the same units is three units  
4. The space between letters is three units
5. The space between a word is seven letters

I encode spaces a `#` so the message `attack at dawn` becomes:

```
.-###-#-###.-###-.-.###-.-#######.-###-#######-..###.-###.--###-.###
```

Having the spaces as # is nice because then you can iterate over the string and you only have to do 2 different sleeps per character.


