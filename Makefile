init:
	php ~/bin/composer.phar install
	mkdir cache
	chmod 777 cache
	chmod 777 data
clean:
	sudo rm -rf cache/*