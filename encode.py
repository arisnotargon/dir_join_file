from hide import Hide

if __name__ == "__main__":
    # print(Hide)
    hide = Hide('password123')
    sourceBytes = hide.package('source')
    edcoded = hide.encode(sourceBytes)
    hide.merge('r.mp4',edcoded)
