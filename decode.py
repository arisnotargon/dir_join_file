from hide import Hide

if __name__ == "__main__":
    hide = Hide('password123')
    encoded = hide.splite('out_20205314919_r.mp4',19012544)
    encoded = hide.decode(encoded)
    hide.unpackage(encoded)