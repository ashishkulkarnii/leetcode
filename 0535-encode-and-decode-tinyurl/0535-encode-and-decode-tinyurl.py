class Codec:
    
    def __init__(self):
        self.u_t = dict()
        self.t_u = dict()

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.u_t.keys():
            res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
            self.t_u[res] = longUrl
            self.u_t[longUrl] = res
        return self.u_t[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.t_u[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))