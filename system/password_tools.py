import string
import random
import hashlib


class User:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.password = '0'

    @property
    def email(self):
        """Returns an email address contructed from first and last. Example:
        first.last@example.com.

        """
        return '{first}.{last}@example.com'.format(first=self.first.lower(),
                                                   last=self.last.lower())

    @property
    def full_name(self):
        """"Returns the full name of a person constructed from first and last."""
        return '{first} {last}'.format(first=self.first, last=self.last)

    @full_name.setter
    def full_name(self, name):
        """Alternate way to set the properties, first and last.

        Args:
            name (str): Full name of the person with a space as the separator.
        """
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def generate_password(self, length=10):
        """Generates a random string of *length*.

        Args:
            length (int): os.urandom returns bytes which is two
                hexidecimal numbers, hence we divide by to to get
                the correct length.
        """
        usable_characters = '{letters}{digits}'.format(
                                 letters=string.ascii_letters,
                                 digits=string.digits)
        self.password = ''.join(random.sample(usable_characters, length))

    def generate_hash(self, hash_type='sha256'):
        """Generate hash from given string.

        Args:
        hash_type (str, optional): any of the acceptable hash algorithms supported by
            the hashlib module ('sha256', 'sha512', 'md5', 'dsa', etc), list available
            using hashlib.algorithms_available. Defaults to sha256.
        """
        if hash_type in hashlib.algorithms_available:
            h = hashlib.new(hash_type)
            h.update(self.password.encode('utf-8'))
            return h.hexdigest()
        else:
            print('Incorrect hash type. Choose from:\n {}'.format(hashlib.algorithms_available))
            return


def generate_random_string(length=8):
    """Generates a random string of *length*.

    Args:
        length (int, optional): os.urandom returns bytes which is two
            hexidecimal numbers, hence we divide by to to get
            the correct length.
    """
    usable_characters = '{letters}{digits}'.format(
                             letters=string.ascii_letters,
                             digits=string.digits)

    return ''.join(random.sample(usable_characters, length))


def generate_hash(password, hash_type='sha256'):
    """Generate hash from given string.

    Args:
        hash_type (str, optional): Defaults to sha256, other options are sha512, md5, or dsa.
    """
    if hash_type in hashlib.algorithms_available:
        h = hashlib.new(hash_type)
        h.update(password.encode('utf-8'))
        return h.hexdigest()
    else:
        print('Incorrect hash type. Choose from:\n {}'.format(hashlib.algorithms_available))
        return


def main():
    user = User('Jim', 'Duncan')

    print('Defualt settings: Jim Duncan')
    print('User: {}'.format(user.full_name))
    print('Password: {}'.format(user.password))
    print('Email: {}'.format(user.email))
    print('\n')

    print('Set new name: Frank Miller')
    user.full_name = 'Frank Miller'
    print('User: {}'.format(user.full_name))
    print('Email: {}'.format(user.email))

    print('\nGenerate password:')
    user.generate_password(20)
    print('User: {}'.format(user.full_name))
    print('Email: {}'.format(user.email))
    print('Password: {}'.format(user.password))
    print('Print hash: {}'.format(user.generate_hash()))
    print('\n')


if __name__ == '__main__':
    main()
