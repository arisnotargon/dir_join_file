from Crypto.Cipher import AES
import time
from io import BytesIO
import tarfile


class Hide():
    def __init__(self, key: str):
        self.key = bytes(key, encoding="UTF-8")
        self.aes = AES.new(self.pad(self.key), AES.MODE_ECB)

    def pad(self, text: bytes) -> bytes:
        while len(text) % 16 != 0:
            text += b' '
        return text

    def encode(self, content) -> bytes:
        return self.aes.encrypt(self.pad(content))

    def decode(self, content) -> bytes:
        return self.aes.decrypt(content)

    def merge(self, fileName: str, content: bytes):
        nowTime = time.localtime()
        prefix = "out_" \
                 + str(nowTime.tm_year) \
                 + str(nowTime.tm_mon) \
                 + str(nowTime.tm_mday) \
                 + str(nowTime.tm_hour) \
                 + str(nowTime.tm_min) \
                 + str(nowTime.tm_sec) \
                 + "_"

        with open(fileName, 'rb') as fr:
            frContent = fr.read()
            with open('size.txt', 'w') as fs:
                fs.write(str(len(frContent)))
            with open(prefix + fileName, 'wb') as fo:
                fo.write(frContent)
                fo.write(content)

    def splite(self, fileName: str, preLenth: int) -> bytes:
        with open(fileName, 'rb') as fr:
            _ = fr.read(preLenth)
            frContent = fr.read()

        return frContent

    def package(self, fileName: str) -> bytes:
        buffer = BytesIO()
        tar = tarfile.open(fileobj=buffer, mode='w')
        tar.add(fileName)

        buffer.seek(0)

        return buffer.read()

    def unpackage(self,content:bytes):
        buffer = BytesIO()
        buffer.write(content)
        buffer.seek(0)
        tar = tarfile.open(fileobj=buffer,mode='r')
        fileNames = tar.getnames()
        for fileName in fileNames:
            tar.extract(fileName, "./outdir")

