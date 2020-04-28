index.html: generate_index.py data.py sidebar.html
	./generate_index.py > temp.html
	mjpage --output CommonHTML < temp.html > "$@"
	rm temp.html
