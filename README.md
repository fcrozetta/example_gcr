# example_gcr

> The name should be **example_ghcr**, for GitHub Container registry, but i made a mistake, and I will not change it now.

This repository is an example of a fastapi application that is built as a container and pushed to github repositories, as an example of what has to be done to be able to deploy it in Azure (but probably could be done in other cloud providers as well)

## What should I learned while making this?

### Docker

The changes in licensing are still going on, so I decided to move away from it.

The first choice was to use **podman**, which is open source. Everything works great until we try to integrate with vscode plugins... VSCode has the configuration hardcoded, and it is not easy to configure the way we need.

The Second choice was **ranchman desktop** which installs everything like docker would, and has the docker commands installed. Docker Rootful is a security problem, but i don't want to spend much time on it at this moment.

### Docker build

it works, but there are some problems.
Since I am using a Macbook M1 (apple ARM64) laptop, it builds a arm64 image by default.

No errors are yield, no warnings shown. It builds. It pushes to the registries.

When you add the image in the cloud, it pulls, and tries to start. Then I got an error related to **uvicorn**, which is not where the error lies.

The correct command to build the image for linux/amd64 from an arm64 is:

```
docker build --platform linux/amd64 -t ghcr.io/<github_user>/<image_name>:<tag> .
```

### Github PAT

Following the tutorial [here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

In order to login into the registry/repository, I created a **P**ersonal **A**ccess **T**oken (classic) with access to read and write packages.

### Building and pushing images using Github actions

This is different than what I am doing at the moment, but i want to set up github actions to build and deploy the images. Hopefully multiple images for different platforms.

> Note: No promises, I just want to know github actions better to be able to do this

### Deploying on azure
Azure app services is the resource that engulfs web apps, API apps, and any kind of app into a single resource. Quite cool.

App services can deploy code, or a container directly. When deploying, there are two things we need to specify, which took me a few tries, and minutes of reading documentation:
- Registry URL (https://ghcr.io)
- Full image name (ghcr.io/<github_username>/<image_name>:<tag>)

The registry url **NEED** the protocol prepended. Thankfully Azure was showing that to me during deployment configuration.

## Next Steps

### Github Actions

Learn how to build and publish the container via actions
