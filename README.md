# pythonxpathsample

## data.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<data>
    <item>
        <name>item1</name>
        <price>100</price>
    </item>
    <item>
        <name>item2</name>
        <price>200</price>
    </item>
    <item>
        <name>item3</name>
        <price>300</price>
    </item>
</data>
```

## Installing lxml
```
$ pip install lxml
```

## Run
```
$ python xpathsample.py 110
============
Items(>=110)
============
item2: 200
item3: 300
------------
Total: 500
------------
```
