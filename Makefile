init:
	php ~/bin/composer.phar install
	mkdir -p cache
	chmod 777 cache
	chmod 777 data
	chmod 777 data-answers
clean:
	sudo rm -rf cache/*