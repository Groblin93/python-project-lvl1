install: #установить зависимость
	poetry install

brain-games: #запустить пакет
	poetry run brain-games

build: #сборка покета
	poetry build

publish: #отладка без добавления в каталог PyPI
	poetry publish --dry-run

package-install: #установка пакета из ОС
	python3 -m pip install --user dist/*.whl
