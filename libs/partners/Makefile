lock:
	@echo "Locking dependencies..."
	@for d in $$(find . -name pyproject.toml -exec dirname {} \;); do \
		(cd $$d && poetry lock); \
	done

lock-no-update:
	@echo "Locking dependencies..."
	@for d in $$(find . -name pyproject.toml -exec dirname {} \;); do \
		(cd $$d && poetry lock --no-update); \
	done

check:
	@echo "Checking dependencies..."
	@for d in $$(find . -name pyproject.toml -exec dirname {} \;); do \
		(cd $$d && echo "Checking $$d" && poetry check); \
	done