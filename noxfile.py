import nox

nox.options.sessions = ["pre_commit", "tests", "coverage"]


@nox.session
def pre_commit(session):
    """pre-commit checks"""
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a")


@nox.session
def tests(session):
    """Run unit test over different python env with code coverage"""
    session.install("pytest", "pytest-cov", "-e", ".")
    session.run(
        "py.test",
        "--cov=xrectsel",
        "--cov-report=xml",
        "--cov-branch",
        "--color=yes",
        "-s",
        "-v",
    )


@nox.session
def coverage(session):
    """This is only to run test on ci"""
    session.install("coverage")
    session.run("coverage", "report")


@nox.session
def package(session):
    session.install("twine", "setuptools", "wheel")
    session.run("python", "setup.py", "sdist", "bdist_wheel")
    session.run("ls", "-l", "dist")
    session.run("python", "-m", "twine", "check", "dist/*")
    session.run("rm", "-rf", "build", "dist", external=True)


@nox.session
def dev_setup(session):
    """Ensure development environment works"""
    session.run("python", "-m", "pip", "install", "-e", ".[dev]")
    session.run("python", "-c", "from xrectsel import XRectSel; XRectSel()")
