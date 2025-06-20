<<<<<<< HEAD
# old-test-repo

Here is all my old commits
=======
# BadmintON onTOlogy (BadmintONTO-v0.1)

BadmintONTO is an ontology for the badmintion domain, representing the domain knowledge that can annotate play-by-play data in tournaments.

The play-by-play data is described at [HERE](./data/README.md)!

Example SPARQL queries are available at [HERE](./sparql_query/README.md)!

An live SPARQL server is accessed from [HERE](https://huanyu-li.github.io/BadmintONTO/demo/)!

## Developer guidelines

The code and ontology on the `main` branch is stable, should be viewed as the latest realease. No changes should be made directly on the `main` branch.

The development of the code or ontology takes place on the development branch (`develop`). When the development branch has been tested, a pull request should be created to merge changes into `main`.

## How to develop or update the ontology

Please follow the steps below:

1. Clone the project:
```bash
$ git@github.com:huanyu-li/BadmintONTO.git
```

2. Checkout the `develop` branch and pull the latest changes
```bash
$ git checkout develop
$ git pull
```
3. Create a new branch (e.g., `update-badmintonto-to-version-0.1`)
```bash
$ git checkout -b update-badmintonto-to-version-0.1
```

4. Add, commit and push:
```bash
$ git add ontology/0.1/BadmintONTO.ttl
$ git commit -m "update badmintonto to version 0.1"
$ git push origin update-badmintonto-to-version-0.1
```

5. At the GitHub page, create a pull request from your branch to `develop`.
6. Done!

## Contact
* Huanyu Li <huanyu.li@liu.se>
>>>>>>> old-repo/develop
