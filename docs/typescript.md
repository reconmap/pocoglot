# [Pocoglot](/README.md) - Typescript

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

Invoke command to generate `vulnerability.ts`:

```
$ ./main.py -from vulnerability.yaml -to vulnerability.ts -lang typescript
18:00:12.019 INFO Generating code in "typescript" from "vulnerability.yaml" to "vulnerability.ts"
18:00:12.025 INFO Done!
```

The file `vulnerability.ts` now contains:

```golang
/**
 * Autogenerated model, do not edit manually.
 */
export default interface Attachment {

	id?: number
	parent_type: string
	parent_id: number
	submitter_uid: number
	client_file_name: string
	file_name: string
	file_size: number
	file_mimetype?: string
	file_hash: string
}
```