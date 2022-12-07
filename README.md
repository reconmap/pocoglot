# Pocoglot

Pocoglot is a simple command line application that takes an entity definition file and generates code in one of many supported languages. If you are writing multi-tier applications in multiple languages this tool can save you from a lot of repeated typing and out-of-sync models.

### Supported languages

[Golang](docs/golang.md) • **Python 3** • [PHP 8](docs/php.md) • **C#** • [Typescript](docs/typescript.md) •  **MySQL**

## Usage

```shell
$ pocoglot --help
Usage: pocoglot [OPTIONS]

Options:
  -from, --from-file PATH         Path to the source YAML file containing
                                  definitions  [required]
  -to, --to-file PATH             Path to where the targe code is going to be
                                  generated  [required]
  -lang, --to-language [java|php8|typescript|golang|csharp|python3]
                                  Language used for the generated code
                                  [required]
  -override, --override-file PATH
                                  Path to the YAML file containing overrides
  --help                          Show this message and exit.
```

## Support

- Please star this project on Github
- Report any issues and feature requests
- Add pull requests to support new languages

## Related projects

- [Quicktype](https://quicktype.io/)

## License

This software is published under the permissive [MIT license](LICENSE.md)
