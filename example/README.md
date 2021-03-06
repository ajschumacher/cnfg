# example using `cnfg`

An application can be distributed like this.

The configuration file [.examplerc][] needs to be moved to your home
directory and customized, as documented also in [.examplerc][] itself.

The `cnfg` package needs to be installed. This is specified in
[requirements.txt][], but the use of [requirements.txt][] or any
`virtualenv` system is not essential. You can just `pip install cnfg`.

Now [example.py][] can be run however you want and it will pick up its
configuration from the `.examplerc` in your home directory. In
particular, all of these can work, with relative directories as implied:

```python
./example.py
python ../example.py
cat example/example.py | python
```

[.examplerc]: .examplerc
[requirements.txt]: requirements.txt
[example.py]: example.py
