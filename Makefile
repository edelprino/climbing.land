start:
	docker-compose up -d
	make logs

stop:
	docker-compose down

restart:
	make stop
	make start

shell:
	docker-compose run --rm jekyll sh

logs:
	docker-compose logs -f

import:
	cd .github && python3 import.py
	cd .github && python3 import_users.py
