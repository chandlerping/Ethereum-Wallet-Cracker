import bip39
import random

# [new feature] 
# Add more permutations to the original entropies
def generateEntropies(tempLine: bytes) -> list[bytes]:
	entropyList = []
	tempLineByteLength = len(tempLine)

	# get a list of raw entropies, with allowed keylengths
	for maxByteLength in [16, 20, 24, 28, 32]:
		if tempLineByteLength < 0:
			continue
		elif tempLineByteLength > maxByteLength:
			entropyList.append(tempLine[:maxByteLength])
			entropyList.append(tempLine[len(tempLine) - maxByteLength:])
		else:
			pad = maxByteLength - tempLineByteLength
			entropyList.append(bytes(pad) + tempLine)
			entropyList.append(tempLine + bytes(pad))
			entropyList.append(bytes(int(pad / 2)) + tempLine + bytes(int(pad / 2)) + bytes(int(pad % 2)))

	# fuzzing
	oldLen = len(entropyList)
	for i in range(0, oldLen):
		entropyList += [permutate(entropyList[i])]
		entropyList += [secodaryPermutate(entropyList[i])]
	
	return entropyList

# Permutate an entropy
def permutate(entropy: bytes) -> bytes:
	flag = random.randint(0, 3)
	length = len(entropy)
	# convert to list
	entropy = list(entropy)

	if flag == 0:
		# replace a part of the entropy with completely random bytes
		start = random.randint(0, int(length / 2))
		end = random.randint(int(length / 2), length - 1)
		for i in range(start, end):
			entropy[i] = random.randint(0, 255)
	elif flag == 1:
		# fuzz the byte by flipping some of its bits
		for i in range(length):
			entropy[i] ^= random.randint(0, 255)
	elif flag == 2:
		# shuffle it
		random.shuffle(entropy)
	elif flag == 3:
		# padding
		pivot  = random.randint(1, length - 1)
		entropy = entropy[pivot + 1 :] + entropy[0 : pivot + 1]
	# convert back to bytes
	return bytes(entropy)

# secondary fuzzing based on mnemonic phrases
def secodaryPermutate(entropy: bytes) -> bytes:
	mnemonic = bip39.encode_bytes(entropy).split()
	random.shuffle(mnemonic)
	shuffledStr = " ".join(mnemonic)
	return bip39.decode_phrase(shuffledStr)