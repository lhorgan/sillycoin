from Crypto.PublicKey import RSA

class User:
    def __init__(self):
        print "HELLO"
        pub_key, priv_key = self.gen_keys(2048)
        self.pub_key = pub_key
        self.priv_key = priv_key

    def gen_keys(self, bits):
        key = RSA.generate(bits, e=65537)
        pub_key = key.publickey().exportKey("PEM")
        priv_key = key.exportKey("PEM")
        return pub_key, priv_key
