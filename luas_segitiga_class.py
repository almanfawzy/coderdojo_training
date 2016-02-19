class Match:
    def hitung_luas_segitiga(self, height, base):
        return height * base / 2
segitiga1 = Match()
segitiga2 = Match()
segitiga3 = Match()

hasil4 = segitiga1.hitung_luas_segitiga(10,2)
hasil5 = segitiga2.hitung_luas_segitiga(30,5)
hasil6 = segitiga3.hitung_luas_segitiga(15,3)
print "segitiga pertama = ", hasil4
print "segitiga kedua = ", hasil5
print "segitiga ketiga = ", hasil6
