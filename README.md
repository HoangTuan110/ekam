<h1 align="center">
  <code>ekam</code>
</h1>

<div align="center"><p>
    <a href="https://github.com/HoangTuan110/ekam/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/HoangTuan110/ekam/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/HoangTuan110/ekam/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/HoangTuan110/ekam/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41" />
    </a>
</div>

<p class="desc">
  Ekam is the command runner for those who feel that thier utilitarian tools should be a bit more challenging to use.
  It tries to balance between usability and inconviniences.

  Ekam takes major influence from [`just`](https://github.com/casey/just).

  Commands, called recipes, are stored in `Ekamfile` with a command-first, argument-second structure:

  ```
  # `->` is alias
  -> $b $build

  # `<-` is set
  <- 'uname -a' $host

  # build main
  : $build [] [ 'cc *.c -o main' ]

  # test everything
  : $test-all [] [ $build './test --all' ]
  ```

  You can then execute and list all of them with:

  ```
  ekam ply <recipe>
  ekam docket
  ```
</p>

## Features (and inconviniences)
- Written in Python, so platform-agnostic, lightweight, and runs fast enough to be tolerable by many
- Errors are as few and as obscure as possible, 'cause they are for the plebs
- Equally obscure help messages. Who needs those?
- No CLI arguments handling for recipes. Doing that will add more complexity to the spagetti code that I ported from
  another of my abandoned project
- Brutalist by design: No control flow, no functions (although recipes are kinda like functions).
  Although you still have the necessary features (variables, recipes, aliases, executing recipes within recipes, etc.)
- You can't change your shell, `ekam` use whatever the shell you are using
- No multiline commands. All of the shell commands must be contained in a single string
- `.env` files? What's that?

## Installation

### The sane way

### The `git clone` way

```sh
git clone https://github.com/HoangTuan110/ekam
cd ekam
pip install -r requirements.txt
```

To run Ekam without compiling: `python main.py`

To compile Ekam and run it (warning: can be quite long): `python main.py ply b; ./ekam`

## Author and License

Ekam is written by Tsuki.

This thing is under the boring ass MIT license.
