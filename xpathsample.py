import sys
from lxml import etree

xml = etree.parse(open("data.xml", 'r'), parser=etree.XMLParser())

price_min = int(sys.argv[1])
prefix = "//item[price>=%d]" % price_min

print("============\nItems(>=%d)\n============" % price_min)
for item in xml.xpath(prefix):
    name = item.xpath("name/text()")[0]
    price = int(item.xpath("price/text()")[0])
    print("%s: %d" % (name, price))

total = int(xml.xpath("sum("+prefix+"/price)"))
print("------------\nTotal: %d\n------------" % total)
