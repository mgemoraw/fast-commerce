#/usr/bin/bash
# commit.sh - A script to commit changes to a Git repository with a message
git add .
echo -p "Enter commit message: "
read message
if [ -z "$message" ]; then
    echo "Commit message cannot be empty."
    exit 1
fi
if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit."
    exit 0
fi
git commit -m "$message"

echo "Changes committed with message: $message"
echo "Pushing changes to remote repository..."

# Push changes to the main branch
git push origin main