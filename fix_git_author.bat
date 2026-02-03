@echo off
git config user.email "dwmom@hotmail.com"
git config user.name "Ramon Mendes - Software Engineer"
git rebase --root --exec "git commit --amend --no-edit --author=\"Ramon Mendes - Software Engineer <dwmom@hotmail.com>\""
