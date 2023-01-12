<h1 align="center">
  <code>ekam</code>
</h1>

<div align="center"><p>
    <a href="https://github.com/piqoni/matcha/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/piqoni/matcha/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/piqoni/matcha/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/piqoni/matcha/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/HoangTuan110/ekam?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41" />
    </a>
</div>

<p class="desc">
  Ekam is the command runner for those who hates themselves.

  Influenced by [`just`](https://github.com/casey/just).

  Commands, called recipes, are stored in `Ekamfile`:

  ```
  # == Just ==
  alias b := build

  host := 'uname -a'

  # build main
  build:
    cc *.c -o main

  # test everything
  test-all: build
    ./test --all

  test TEST: build
    ./test --test {{TEST}}

  # == Ekam ==
  -> $b $build

  <- 'uname -a' $host

  # build main
  : $build [] [ 'cc *.c -o main' ]

  # test everything
  : $test-all [] [ $build './test --all' ]

  # run a specific test
  : $test [$name] [ $build './test --test $name' ]
  ```

  ```
  # Running recipes and listing all of them

  # Just
  just <recipe>
  just -l

  # Ekam
  ekam ply <recipe>
  ekam docket
  ```
</p>

## Features
- Written in Python, so platform-agnostic, lightweight, and run fast enough to be tolerable by many
- Ugly-looking syntax
- Errors are as few and as obscure as possible, 'cause f-you, that's why
- Cryptic help messages
- Recipes can take command-line arguments, _just like `just`_.
