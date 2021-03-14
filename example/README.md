# example

Example setup for generating Codeship configuration.

## Usage

The example can be executed via:

```bash
$ make
```

To see static analysis fail, remove one of the `hadolint` ignore lines in the
Debian Dockerfile `docker/debian/Dockerfile`.

## Resources

* [Hadolint](https://github.com/hadolint/hadolint) for linting Dockerfiles
* [Bats](https://github.com/sstephenson/bats) for shell tests
