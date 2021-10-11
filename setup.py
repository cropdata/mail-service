import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mail-service',
    version='0.4.0',
    author='Rishabh Oswal',
    author_email='rishabh.oswal@cropdata.in',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cropdata/mail-service.git',
    project_urls={
        "Bug Tracker": "https://github.com/cropdata/mail-service.git"
    },
    license='MIT',
    packages=['mail_service'],
    install_requires=['requests', 'sendgrid'],
)
