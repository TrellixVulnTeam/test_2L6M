import tarfile
import os

def compress(dir):
    filename = "{}.tar.gz".format(dir)
    with tarfile.open(filename, "w:gz") as t:
        t.add(dir, arcname="")

def decompress(targz):
    dir = targz.removesuffix(".tar.gz")
    with tarfile.open(targz, "r:gz") as t:
        t.extractall(path=(dir + "testtest"))

#compress("src")
decompress("src.tar.gz")

