from setuptools import setup, find_packages

setup(name="setup_demo", version="0.10",
      description="My test module",
      author="super he",
      url="https://66super.com",
      license="MIT",
      # packages=find_packages(),
      packages=['hc_test_pack'],  # 需要打包的包名
      )
