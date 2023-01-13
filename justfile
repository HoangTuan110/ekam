alias t := test

# build
build:
  nuitka3 main.py --onefile -o ekam

# test our example
test: build
  ./ekam -t true
