pytest --cov=cv_creator tests/

pytest --cov=cv_creator tests/ --cov-report term-missing

mypy cv_creator


To mark test as failing including reason, its executed in pytest but doesn't fail execution -> @pytest.mark.xfail(reason="")
