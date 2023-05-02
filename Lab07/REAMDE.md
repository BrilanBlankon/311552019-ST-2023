# Software Testing Lab07

## PoC: the file that can trigger the vulnerability
![](https://i.imgur.com/bIQC8vM.png)


## The commands (steps) that you used in this lab
```shell
$ cd Lab07
$ export CC=~/AFL/afl-gcc
$ export AFL_USE_ASAN=1
$ make
$ mkdir in
$ cp test.bmp in/
$ ~/AFL/afl-fuzz -i in -o out -m none -- ./bmpgrayscale @@ a.bmp

```

## Screenshot of AFL running (with triggered crash)
![](https://i.imgur.com/swdumYF.png)


## Screenshot of crash detail (with ASAN error report)
![](https://i.imgur.com/pl1ueMK.png)
