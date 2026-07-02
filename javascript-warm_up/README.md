# javascript-warm_up

A first look at JavaScript: variables and constants, data types, conditionals,
loops, functions, scopes, arithmetic operators, and how to import files with
`require`.

## Learning Objectives

At the end of this project, you should be able to explain, without the help
of Google:

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are the differences between `var`, `const` and `let`
- What are all the data types available in JavaScript
- How to use the `if`, `if ... else` statements
- How to use comments
- How to assign values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- What is a function and how to use functions
- What a function that has no `return` statement returns
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate a dictionary (object)
- How to import a file

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted on Ubuntu 20.04 LTS using Node.js 14.x
- All files should end with a new line
- The first line of every file must be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the project folder, is mandatory
- Code must be semistandard compliant (version 16.x.x): rules of Standard +
  semicolons on top
- All files must be executable
- File length is checked with `wc`

### Install Node 14

```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semistandard

```
sudo npm install semistandard --global
```

Check a file with:

```
semistandard ./0-javascript_is_amazing.js
```

## Tasks

| File | Description |
| --- | --- |
| `0-javascript_is_amazing.js` | Prints "JavaScript is amazing" using a constant |
| `1-multi_languages.js` | Prints 3 lines with `console.log` |
| `2-arguments.js` | Prints a message depending on the number of arguments |
| `3-value_argument.js` | Prints the first argument passed to the script |
| `4-concat.js` | Prints two arguments in the format `<arg1> is <arg2>` |
| `5-to_integer.js` | Converts the first argument to an integer and prints it |
| `6-multi_languages_loop.js` | Prints 3 lines using an array and a loop |
| `7-multi_c.js` | Prints "C is fun" x times |
| `8-square.js` | Prints a square using the character X |
| `9-add.js` | Adds two integers using a function `add` |
| `10-factorial.js` | Computes a factorial recursively |
| `11-second_biggest.js` | Finds the second biggest integer in the arguments |
| `12-object.js` | Updates a value in an object |
| `13-add.js` / `13-main.js` | Exports an `add` function from a module |

## Usage examples

```
$ ./0-javascript_is_amazing.js
JavaScript is amazing

$ ./2-arguments.js
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found

$ ./7-multi_c.js 3
C is fun
C is fun
C is fun

$ ./8-square.js 3
XXX
XXX
XXX

$ ./10-factorial.js 5
120

$ ./13-main.js
8
```
