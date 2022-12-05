# Pocoglot

Pocoglot is a simple command line application that takes an entity definition file and generates code in one of many supported languages. If you are writing multi-tier applications in multiple languages this tool can save you from a lot of repeated typing and out-of-sync models.

### Supported languages

<img src=".github/images/python-language.png" width="40"/>

<img src=".github/images/php-language.png" width="40" />

## Usage example

Create definition file `vulnerability.yaml`:

```yaml
name: Vulnerability
props:
  - name: id
    type: integer
  - name: severity
    type: float
```

Invoke command to generate `vulnerability.py`:

```
$ ./main.py -from vulnerability.yaml -to vulnerability.py -lang python3
18:00:12.019 INFO Generating code in "python3" from "vulnerability.yaml" to "vulnerability.py"
18:00:12.025 INFO Done!
```

## Support

- Please star this project on Github
- Report any issues and feature requests
- Add pull requests to support new languages

## Related projects

- [Quicktype](https://quicktype.io/)
