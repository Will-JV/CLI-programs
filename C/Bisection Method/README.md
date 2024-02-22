# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
1. Find a,b, where f(a)f(b)<0. Set e to be a small positive real number.
2. End if |b-a|<e. Solution is a or b.
3. Let c=(a+b)/2. Calculate s=f(a)f(c).
4. Set b=c if s<0, else set a=c. Return to step 2. 
