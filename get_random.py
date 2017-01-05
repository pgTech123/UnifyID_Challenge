import string
import urllib2

MAX_NUM_PER_REQUEST = 10000

def _internal_get_random(num, min, max):
    # Request random numbers
    url = "https://www.random.org/integers/?num="+str(num)+"&min="+str(min)+"&max="+str(max)+"&col=1&base=10&format=plain&rnd=new"
    # Allow 3 minutes to get the answer. See random.org documentation for more info.
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


# Returns the current quota
def check_quota():
    return urllib2.urlopen("https://www.random.org/quota/?format=plain").read()


def main():
    print "Number of requests left: " + str(check_quota())
    print get_random(15, 1, 25)

if __name__ == '__main__':
    main()