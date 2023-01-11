<h1 style="text-align: center;">
  <pre>ekam</pre>
</h1>

<p class="desc">
  Ekam is the command runner for those who hates themselves.

  Influenced by [`just`](https://github.com/casey/just).

  Commands, called recipes, are stored in `Ekamfile` with a syntax you have never seen before:

  ```
  # Just
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

  # Ekam
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
- Errors are as few and as obscure as possible, 'cause f-you, that's why
- Recipes can take command-line arguments, just like `just`.
- No language-agnostic features like `just`, so you can only write your recipes in this diabolical mess
