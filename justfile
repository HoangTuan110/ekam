alias t := test

# build
build:
  nuitka3 main.py --follow-imports -o ekam

# test our example
test: build
  ./ekam -t true
