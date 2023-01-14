alias t := test

# build
build:
  nuitka3 main.py --onefile -o ekam

# test our example
test: build
  ./ekam -t true

# little dad joke at the end here
joke:
  echo "Where did all the lights go to when they commit a crime? Prism! (It's a light sentence)"
