###### Mutable are Modifyable objects

> LIST AND DICTIONARIES ARE MUTABLE

```l = [1,2,3,4,5,6,7,8]
l[2]
l[2] = 9
l[2]
```
```d = {
  'type' : 'directory',
  'content' ":{
      'folders' : ['bin','src', 'sbin', 'extra',],
      'files' : ['index.sh','index.py','sample.json']
  }
}

d['content']
d['content']['folders'][2] = 'media'
d['content']
```


> TOUPLE AND SET ARE IMMUTABLE

```l = (1,2,3,4,5,6,7,8)
l[2]
l[2] = 9
l[2]
```
