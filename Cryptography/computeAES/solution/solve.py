from Crypto.Cipher import AES

cipher = AES.new('azdvtH4bvfdS/mryKLTNqQ=='.decode('base64'),AES.MODE_ECB)
decoded = cipher.decrypt('R9TacKHy6cf1AZho/nwWWYaNzP5GfltKE5yW+kwRYe0LY+PdGk1hfoanS/iVZ7z1'.decode('base64'))

print decoded
