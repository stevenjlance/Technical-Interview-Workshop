A tree is just a concept that is usually applied using Object Oriented Programming, but we can use a dictionary to illustrate the same thing.

```py
tree = {
    "value": 5,
    "left": {
        "value":2,
        "left":{
            "value":1,
            "left":None,
            "right":None
        },
        "right":{
            "value":3,
            "left":None,
            "right":{
                "value":4,
                "left":None,
                "right":None
            }
        }
    },
    "right": {
        "value":8,
        "left":{
            "value":6,
            "left":None,
            "right":{
                "value":7,
                "left":None,
                "right":None
            }
        },
        "right":{
            "value":9,
            "left":None,
            "right":{
                "value":10,
                "left":None,
                "right":None
            }
        }
    }
}
```

- In the code snippet above, how many attributes does `tree` have?
- What are the values that have none for both their left and right child node?
- Which parent nodes have both their left and right child?