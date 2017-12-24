from lxml import etree

PRICE_MIN = 110

prefix = "//item[price>=%d]" % PRICE_MIN
xml = etree.parse(open("data.xml", 'r'), parser=etree.XMLParser())

print("============\nItems(>=%d)\n============" % PRICE_MIN)
for item in xml.xpath(prefix):
    name = item.xpath("name/text()")[0]
    price = int(item.xpath("price/text()")[0])
    print("%s: %d" % (name, price))

total = int(xml.xpath("sum("+prefix+"/price)"))
print("------------\nTotal: %d\n------------" % total)
