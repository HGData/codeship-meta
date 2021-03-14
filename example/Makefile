#
# Makefiles: for when you need a toolchain for your toolchain's toolchain.
#
META_CODESHIP_DIR=../src
IMAGE=cdeutsch/meta-codeship:latest
META_STEPS=$(shell pwd)/codeship-meta.yml:/codeship-meta.yml

all: codeship-services.yml codeship-steps.yml
	jet steps

image:
	$(MAKE) -C $(META_CODESHIP_DIR)

codeship-steps.yml: image codeship-meta.yml codeship-steps.in.yml
	docker run \
		-v $(META_STEPS) \
	  -v $(shell pwd)/codeship-steps.in.yml:/codeship-steps.in.yml \
	  $(IMAGE) /codeship-steps.in.yml > codeship-steps.yml

codeship-services.yml: image codeship-meta.yml codeship-services.in.yml
	docker run \
		-v $(META_STEPS) \
		-v $(shell pwd)/codeship-services.in.yml:/codeship-services.in.yml \
		$(IMAGE) /codeship-services.in.yml > codeship-services.yml
