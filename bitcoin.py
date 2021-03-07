#!/usr/bin/env python3

from hashlib import sha256
import time
start =time.time()
MAX_NONCE = 234000000000000000000000000

def SHA256(text):
	return sha256(text.encode("utf-8")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
	prefix_str = '0'*prefix_zeros
	for nonce in range(MAX_NONCE):
                #print(nonce)
                text = str(block_number) + transactions + previous_hash + str(nonce)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                        print("Yes! Successfull mined Bitcoins with nonce value:%f" %nonce)
                        return new_hash
	#	raise BaseException("Couldn't find any after trying %f" %MAX_NONCE )


if __name__=='__main__':

    transactions='''
	Dhaval->Bhavin->20,
	Mando->Cara->45
	'''
    difficulty = int(input('how many difficulty?'))
    print("start mining")
    new_hash = mine(5, transactions, '000770c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', difficulty)
    total_time = str(time.time() - start)
    print("end mining. Mining took:%s"%total_time)
    print(new_hash)
