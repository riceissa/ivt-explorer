index.html: generate_index.py data.py sidebar.html
	./generate_index.py > "$@"
