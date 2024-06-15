PYTHONPATH = PYTHONPATH=./
TEST = $(PYTHONPATH) pytest --verbosity=2 --showlocals $(arg) -k "$(k)"

.PHONY: test test-fast test-failed

test:
	$(TEST)

test-fast:
	$(TEST) --exitfirst

test-failed:
	$(TEST) --last-failed
