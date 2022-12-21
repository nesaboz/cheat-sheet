
Couldn't upload large files without git-lfs (lfs stands for [large file storage](https://stackoverflow.com/questions/67395259/git-clone-git-lfs-filter-process-git-lfs-command-not-found))

```
brew install git-lfs
git lfs install
```

Hugging space doesn't allow binary files in repo, so the file extensions needs to be added to `.gitattributes`.

We must have `requirements.txt` file in the hugging space repo:
```text
"If you need other Python packages to run your app, add them to a requirements.txt file at the root of the repository. The Spaces runtime engine will create a custom environment on-the-fly."
```

