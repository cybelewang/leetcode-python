"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""
class Codec:
    def __init__(self):
        self.longURLs = []
        self.letters = list('0123456789') + list('abcdefghijklmnopqrstuvwxyz') + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.id = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.id = len(self.longURLs)
        self.longURLs.append(longUrl)
        
        shortUrl = self.get_shortUrl(self.id)

        return 'http://' + shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl.startswith('https://'):
            shortUrl = shortUrl[8:]
        elif shortUrl.startswith('http://'):
            shortUrl = shortUrl[7:]

        id = self.get_id(shortUrl)

        return self.longURLs[id]
        
    def get_id(self, shortUrl):
        """
        recovers the id from shortUrl
        """
        id = 0
        for c in shortUrl:
            id *= 62
            if ord(c) < ord('a'):
                id += ord(c) - ord('0')
            elif ord(c) < ord('z'):
                id += ord(c) - ord('a')
            else:
                id += ord(c) - ord('A')

        return id 

    def get_shortUrl(self, id):
        """
        converts the id to fixed length (6 characters) URL
        """
        url = ''
        for _ in range(6):
            url += self.letters[id % 62]
            id //= 62

        return url

# Your Codec object will be instantiated and called as such:
codec = Codec()
s = codec.encode('https://www.w3schools.com/js/js_popup.asp')
print(s)
l = codec.decode(s)
print(l)