install: #установить зависимости
	poetry install
	poetry add prompt
	portry add flake8

brain-games: #запустить пакет
	poetry run brain-games

build: #сборка пaкета
	poetry build

publish: #отладка без добавления в каталог PyPI
	poetry publish --dry-run

package-install: #установка пакета из ОС
	python3 -m pip install --user dist/*.whl

package-reinstall: #переустановка пакета
	pip install --user --force-reinstall dist/*.whl

lint: #код ревью
	poetry run flake8 brain_games
