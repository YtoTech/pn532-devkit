# PN532 Devkit

Documentation and test programs for NXP PN532 NFC boards

# Test programs

## Install requirements

You need Python 3, with pipenv.

First install pip following https://pip.pypa.io/en/stable/installing/.

Then you can install [pipenv](https://docs.pipenv.org/) using pip:

```
sudo pip3 install pipenv
```

Right, you are now ready to install the project dependencies in a virtualenv:

```
make install
```

## Usage

Connect your PN532 board through UART.

Then do:

```
sudo make serial-read-test
```
