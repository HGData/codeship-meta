# codeship-meta

This is an example for how to setup a git repo with [Codeship](https://www.cloudbees.com/products/codeship)
in a slightly more DRY manner when dealing with a large number of images.

## How it works

Python `jinja2` templates and a `yaml` configuration file called `codeship-meta.yml`.
There is a working example in the `example/` directory.

## Usage

The steps and services are specified in the `codeship-meta.yml` file, which consists
of a number of blocks that look something this like:

```yaml
- name: myimage
  repo: myrepo1/myimage
  lint: true
  builder: true
  tests: true
```

The tests can be overriden. Consider an nginx image where we just want to make
sure that nginx can run; we don't have a builder image with `bats` and it would
not be useful to run a test suite.

```yaml
- name: nginx
  repo: hgdata1/nginx
  builder: false
  tests:
    enabled: true
    command: "nginx -t"
```

## Templates

The `codeship-meta.yml` contains blocks for each of the images that you want to
build. So you will also need templates, one for each Codeship build file. These use
[jinja2](https://jinja.palletsprojects.com/en/2.11.x/templates/) syntax:

* `codeship-services.in.yml`
* `codeship-steps.in.yml`

The script will read the `codeship-meta.yml` file and the services or steps
template and render the file. It could be run like this for testing:

```bash
$ python meta-codeship.py codeship-services.in.yml > codeship-services.yml
$ python meta-codeship.py codeship-steps.in.yml > codeship-steps.yml
```

## Building

The codeship-meta script could be run from anything, but since we're looking to use
templates to generate configuration for a CI system it's useful to regress
into something that can be run outside of the CI system with minimal effort.

I suggest using a Makefile as most developers will have a C toolchain installed.
But anything like `rake`, `gradle`, etc. would work.

```make
codeship-steps.yml: image codeship-meta.yml codeship-steps.in.yml
	docker run \
		-v codeship-meta.yml:/codeship-meta.yml \
	  -v $(shell pwd)/codeship-steps.in.yml:/codeship-steps.in.yml \
	  hgdata1/codeship-meta:latest /codeship-steps.in.yml > codeship-steps.yml

codeship-services.yml: image codeship-meta.yml codeship-services.in.yml
	docker run \
		-v $(META_STEPS) \
		-v $(shell pwd)/codeship-steps.in.yml:/codeship-steps.in.yml \
		$(IMAGE) /codeship-steps.in.yml > codeship-steps.yml
```

## Requirements

* `docker`
* `make`
