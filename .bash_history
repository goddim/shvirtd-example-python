git pull origin main
git pull origin main --rebase
git pull origin main --no-rebase
git add .  # Добавить все непроиндексированные файлы
git commit -m "Сохранение непроиндексированных изменений"
git pull origin main --no-rebase
git pull origin main --force
git pull origin main --no-rebase
git add .
git commit -m "Сохранение изменений перед переустановкой ветки main"
git fetch origin
git reset --hard origin/main
