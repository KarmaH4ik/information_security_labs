# Password Generator

a simple command line password generator i made in python. you give it a length and some flags, it gives you a password back. that's it.

uses python's `secrets` module so the passwords are actually random (don't use `random` for passwords kids).

## what you need

just python 3.9 or newer. no `pip install` stuff, no requirements.txt, nothing.

## how to run it

```
python3 genpass.py
```

that prints a 16 character password with letters, numbers and symbols.

if you want a longer one:

```
python3 genpass.py --length 32
```

## the flags

`--length`
how long the password is. default is 16.

`--lower` / `--no-lower`
turn lowercase letters on/off. on by default.

`--upper` / `--no-upper`
same but uppercase. also on by default.

`--digits` / `--no-digits`
the numbers 0-9. on by default.

`--symbols` / `--no-symbols`
stuff like `!@#$%`. on by default.

`-h` or `--help`
shows the help text if you forget any of this.

all the classes are on by default, so you only really need to use the `--no-*` ones to turn things off. like if a website wont accept symbols you do `--no-symbols`.

## some examples

```
# pin code
python3 genpass.py --length 6 --no-lower --no-upper --no-symbols

# password with no symbols (most websites)
python3 genpass.py --length 20 --no-symbols

# only lowercase + numbers
python3 genpass.py --no-upper --no-symbols
```

if you turn ALL the flags off it will just yell at you because there's nothing to pick from.

also if you put `--length 0` it errors out, you need at least 1 character obviously.

## what's inside genpass.py

it's one file with a few functions:

- `build_pool(...)` - takes the four true/false flags and builds the pool of characters to pick from. also returns the list of enabled classes separately so the generator can make sure each one shows up at least once. errors out if all four flags are false.

- `generate_password(length, pool, enabled_classes)` - the actual generator. picks `length` random characters from the pool using `secrets.choice`. then if you have enough length it overwrites the first few positions with one character from each enabled class, then shuffles the whole thing so the password is guaranteed to have at least one of each kind you asked for. without this you could ask for digits and get a password with zero digits (small chance but it happens).

- `parse_args()` - the argparse stuff. uses `BooleanOptionalAction` which is what gives you the `--lower / --no-lower` pair automatically.

- `main()` - the entry point. parses args, calls the other functions, prints the password. if anything raises a `ValueError` it prints the message to stderr and exits with code 2.

- the constants at the top (`LOWER`, `UPPER`, `DIGITS`, `SYMBOLS`) are just the character pools. `SYMBOLS` is hardcoded instead of using `string.punctuation` because `string.punctuation` has stuff like backslash and quotes that mess up shells/databases.

## why secrets and not random

`random` uses the mersenne twister which is good for like games and simulations but not for passwords because if someone sees enough output they can predict the next ones. `secrets.choice` reads from the OS random source so that doesn't happen.
