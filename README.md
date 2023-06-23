# Practical Software Engineering Practices

Please ensure that you have Git & GitHub CLI installed by running:

```bash
git --version
```

```bash
gh --version
```

---

## Git installation

We will be using [package managers](https://en.wikipedia.org/wiki/Package_manager) to install git, so we do not need to deal with any installation wizards!

For Windows 11 users, run:

```
winget install -e --id Git.Git
```

For Mac users please run:

```
xcode-select --install
```

For Ubuntu users, run:

```
sudo apt-get update && sudo apt-get install git
```

If you were unable to install with one of the options above, please install through the [git website](https://git-scm.com/downloads)

## Git Setup

If this is your first time using git, you will need to set up your username and email.

Configure your username by running:

```
git config --global user.name "<Your Username>"
```

Configure your email by running:

```
git config --global user.email johndoe@example.com
```

## GitHub Cli Installation

### macOS

`gh` is available via [Homebrew][], [MacPorts][], [Conda][], [Spack][], and as a downloadable binary from the [releases page][].

#### Homebrew

| Install:          | Upgrade:          |
| ----------------- | ----------------- |
| `brew install gh` | `brew upgrade gh` |

#### MacPorts

| Install:               | Upgrade:                                       |
| ---------------------- | ---------------------------------------------- |
| `sudo port install gh` | `sudo port selfupdate && sudo port upgrade gh` |

#### Conda

| Install:                                 | Upgrade:                                |
| ---------------------------------------- | --------------------------------------- |
| `conda install gh --channel conda-forge` | `conda update gh --channel conda-forge` |

Additional Conda installation options available on the [gh-feedstock page](https://github.com/conda-forge/gh-feedstock#installing-gh).

#### Spack

| Install:           | Upgrade:                                 |
| ------------------ | ---------------------------------------- |
| `spack install gh` | `spack uninstall gh && spack install gh` |

### Linux & BSD

`gh` is available via:

-   [our Debian and RPM repositories](./docs/install_linux.md);
-   community-maintained repositories in various Linux distros;
-   OS-agnostic package managers such as [Homebrew](#homebrew), [Conda](#conda), and [Spack](#spack); and
-   our [releases page][] as precompiled binaries.

For more information, see [Linux & BSD installation](./docs/install_linux.md).

### Windows

`gh` is available via [WinGet][], [scoop][], [Chocolatey][], [Conda](#conda), and as downloadable MSI.

#### WinGet

| Install:                         | Upgrade:                         |
| -------------------------------- | -------------------------------- |
| `winget install --id GitHub.cli` | `winget upgrade --id GitHub.cli` |

> **Note**  
> The Windows installer modifies your PATH. When using Windows Terminal, you will need to **open a new window** for the changes to take effect. (Simply opening a new tab will _not_ be sufficient.)

#### scoop

| Install:           | Upgrade:          |
| ------------------ | ----------------- |
| `scoop install gh` | `scoop update gh` |

#### Chocolatey

| Install:           | Upgrade:           |
| ------------------ | ------------------ |
| `choco install gh` | `choco upgrade gh` |

#### Signed MSI

MSI installers are available for download on the [releases page][].

### Codespaces

To add GitHub CLI to your codespace, add the following to your [devcontainer file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-features-to-a-devcontainer-file):

```json
"features": {
  "ghcr.io/devcontainers/features/github-cli:1": {}
}
```

## GitHub Cli Setup

Login to GitHub using your account:

```bash
gh auth login
```

## Exercise Setup

1. Open Terminal / Power Shell and change directory into where you would like to store project and run:

```
gh repo clone codersforcauses/practical_software_engineering_practices
```

2. Pick an issue on the [Issues page](https://github.com/codersforcauses/practical_software_engineering_practices/issues) and assign yourself to it.

3. Create a new branch for your group by running (please create branch with your name:

```
git branch <name of branch>
```

4. To view all branches available (not on github), Run:

```
git branch
```

Now that we have created our branch, it is time we checkout(switch to) that branch so we can edit code!

5. To change to the branch created, Run:

```
git checkout <name of your branch>
```

6. Let push your newly created branch to github by running:

(name of remote will be origin for today)

```
git push <name of remote> <name of branch>
```

---

## Exercise

Please ensure that you are on the branch you have created before continuing further!

1. Now that you are on your branch, you are free to do whatever you like with the code! For the excercise, create a copy of the template folder and rename it to your name. Run:

```
cp -r ./template/ ./<your name>
```

For this exercise, there is only 1 file that requires completion

```
addition.py
```

Lets start by correcting `addition.py`, modify the code so that it looks like this:

```py
def addition(a,b):
    return a+b
```

After saving your file, it is time to add this to the staging area by running:

```
git add addition.py
```

Once you are happy with your changes, it is time to commit! Don't forget to leave meaningful commit messages! Commit your change by running:

```
git commit -m "your commit message"
```

After commiting, we still need to push our changes to GitHub.
Push your changes by running:

```
git push origin <name of branch>
```

---

## Adding changes to the main code base

Now that you are satisfied with changes on your branch, we need to merge these changes with our main branch so that your changes can be added into the codebase. Head over to the [pull request section](https://github.com/codersforcauses/practical_software_engineering_practices/pulls) to create a new pull request.

There is no command for creating a pull request as a pull request is something that a cloud provider like GitHub, GitLab or BitBucket provide. It is not part of Git itself.

Once your code has been reviewed. Click squash and merge to merge your changes into the main branch.

---

## Suggestions and feed back

Please leave any suggestions for future events or feedback in `suggestions.txt` and submit by creating a pull request :)
