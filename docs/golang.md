# [Pocoglot](/README.md) - Golang

Pocoglot is a simple command line application that takes an entity definition file and generates code in one of many supported languages. If you are writing multi-tier applications in multiple languages this tool can save you from a lot of repeated typing and out-of-sync models.

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

Invoke command to generate `vulnerability.go`:

```
$ ./main.py -from vulnerability.yaml -to vulnerability.go -lang golang
18:00:12.019 INFO Generating code in "golang" from "vulnerability.yaml" to "vulnerability.go"
18:00:12.025 INFO Done!
```

The file `vulnerability.go` now contains:

```golang
type Attachment struct {

	ID int
	ParentType string
	ParentId int
	SubmitterUid int
	ClientFileName string
	FileName string
	FileSize int
	FileMimetype string
	FileHash string
}
```
