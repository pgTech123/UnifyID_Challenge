import string
import urllib2
import numpy.random   # !!! Used only for testing so that we don't have to use our data !!!

# Constants
MAX_NUM_PER_REQUEST = 10000     # See "https://www.random.org/clients/http/#integers" for more info


# This function requests random numbers from the server but
# has no protection regarding the number of numbers required.
def _internal_get_random(num, min, max):
    # Request random numbers
    url = "https://www.random.org/integers/?num="+str(num)+"&min="+str(min)+"&max="+str(max)+"&col=1&base=10&format=plain&rnd=new"
    # Allow 3 minutes to get the answer. See "https://www.random.org/clients/" for more info.
    response = urllib2.urlopen(url, timeout=360).read()

    # Rearange response => array.
    random = []
    lines = string.split(response, '\n')
    for line in lines:
        if line == '':
            continue
        random.append(int(line))
    return random


# Returns an array of num random numbers between min and max
def get_random(num, min, max):
    remaining = 0
    random = []
    loops = num/MAX_NUM_PER_REQUEST
    remaining = num%MAX_NUM_PER_REQUEST

    # FIXME: This implementation could be improved for performance
    for loop in range(loops):
        # print "Loop: " + str(loop) + " / " + str(loops)
        random = random + _internal_get_random(MAX_NUM_PER_REQUEST, min, max)

    random = random + _internal_get_random(remaining, min, max)

    return random


# WARNING: This function should only be used for testing
# Returns an array of pseudorandom numbers. USED ONLY FOR TESTING.
# This way, we don't overload the server and acceelerate the dev and testing process.
def get_random_test(num, min, max):
    return numpy.random.random_integers(min, max, num)


# Returns the current quota
def check_quota():
    return urllib2.urlopen("https://www.random.org/quota/?format=plain").read()


def main():
    print "Number of requests left: " + str(check_quota())
    print get_random(15, 1, 25)


if __name__ == '__main__':
    main()
