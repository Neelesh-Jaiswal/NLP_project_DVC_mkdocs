# Data preparation Stage

- Convert my data into train and test.tsv in 70:30 ratio

```
data.xml
|-train.tsv
|-test.tsv
```
-  We are choosing only 3 tags in the xml data:
    1. row id
    2. title
    3. Tags(Stackover flow tags specific to python)

|Tags|Feature names|
|-|-|
|row Id| row ID|
|title and body|text|
|stackoverflow tags|Label1 - Python|