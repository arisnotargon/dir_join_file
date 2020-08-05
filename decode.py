from hide import Hide

if __name__ == "__main__":
    hide = Hide('password123')
    # the 2nd param of splite method is the length of the original,after encode.py be executed,you can git it in size.txt
    encoded = hide.splite('out_20205314919_r.mp4',8033519)
    encoded = hide.decode(encoded)
    hide.unpackage(encoded)