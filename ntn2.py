import time
import os
from statistics import mean
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AESCCM, ChaCha20Poly1305

def encrypt_decrypt_gcm(key_length, payload, num_runs):
    """Encrypt and decrypt using AES-GCM (128 or 256-bit key) for multiple runs."""
    key = os.urandom(key_length // 8)
    aesgcm = AESGCM(key)
    enc_times, dec_times = [], []
    
    for _ in range(num_runs):
        # Encryption
        nonce = os.urandom(12)  # GCM standard nonce size
        start_time = time.perf_counter()
        ciphertext = aesgcm.encrypt(nonce, payload, None)
        enc_times.append(time.perf_counter() - start_time)
        
        # Decryption
        start_time = time.perf_counter()
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        dec_times.append(time.perf_counter() - start_time)
    
    return enc_times, dec_times, plaintext == payload

def encrypt_decrypt_chacha20(payload, num_runs):
    """Encrypt and decrypt using ChaCha20-Poly1305 for multiple runs."""
    key = os.urandom(32)  # 256-bit key
    chacha = ChaCha20Poly1305(key)
    enc_times, dec_times = [], []
    
    for _ in range(num_runs):
        # Encryption
        nonce = os.urandom(12)  # ChaCha20-Poly1305 nonce size
        start_time = time.perf_counter()
        ciphertext = chacha.encrypt(nonce, payload, None)
        enc_times.append(time.perf_counter() - start_time)
        
        # Decryption
        start_time = time.perf_counter()
        plaintext = chacha.decrypt(nonce, ciphertext, None)
        dec_times.append(time.perf_counter() - start_time)
    
    return enc_times, dec_times, plaintext == payload

def encrypt_decrypt_ccm(key_length, payload, num_runs, tag_length=16):
    """Encrypt and decrypt using AES-CCM (default or 8-byte tag) for multiple runs."""
    key = os.urandom(key_length // 8)
    aesccm = AESCCM(key, tag_length=tag_length)
    enc_times, dec_times = [], []
    
    for _ in range(num_runs):
        # Encryption
        nonce = os.urandom(13)  # CCM typically uses 13-byte nonce for 5G/TLS
        start_time = time.perf_counter()
        ciphertext = aesccm.encrypt(nonce, payload, None)
        enc_times.append(time.perf_counter() - start_time)
        
        # Decryption
        start_time = time.perf_counter()
        plaintext = aesccm.decrypt(nonce, ciphertext, None)
        dec_times.append(time.perf_counter() - start_time)
    
    return enc_times, dec_times, plaintext == payload

def compare_ciphers(payload, num_runs):
    """Run encryption/decryption for all ciphers and compare performance over multiple runs."""
    results = []
    
    # TLS_AES_128_GCM_SHA256
    enc_times, dec_times, success = encrypt_decrypt_gcm(128, payload, num_runs)
    total_times = [e + d for e, d in zip(enc_times, dec_times)]
    results.append(("TLS_AES_128_GCM_SHA256", enc_times, dec_times, total_times, success))
    
    # TLS_AES_256_GCM_SHA384
    enc_times, dec_times, success = encrypt_decrypt_gcm(256, payload, num_runs)
    total_times = [e + d for e, d in zip(enc_times, dec_times)]
    results.append(("TLS_AES_256_GCM_SHA384", enc_times, dec_times, total_times, success))
    
    # TLS_CHACHA20_POLY1305_SHA256
    enc_times, dec_times, success = encrypt_decrypt_chacha20(payload, num_runs)
    total_times = [e + d for e, d in zip(enc_times, dec_times)]
    results.append(("TLS_CHACHA20_POLY1305_SHA256", enc_times, dec_times, total_times, success))
    
    # TLS_AES_128_CCM_SHA256
    enc_times, dec_times, success = encrypt_decrypt_ccm(128, payload, num_runs)
    total_times = [e + d for e, d in zip(enc_times, dec_times)]
    results.append(("TLS_AES_128_CCM_SHA256", enc_times, dec_times, total_times, success))
    
    # TLS_AES_128_CCM_8_SHA256
    enc_times, dec_times, success = encrypt_decrypt_ccm(128, payload, num_runs, tag_length=8)
    total_times = [e + d for e, d in zip(enc_times, dec_times)]
    results.append(("TLS_AES_128_CCM_8_SHA256", enc_times, dec_times, total_times, success))
    
    # Print results
    print("\nCipher Performance Results (Min/Max/Avg Times in Seconds):")
    print("-" * 110)
    print(f"{'Cipher':<25} {'Enc Min':<10} {'Enc Max':<10} {'Enc Avg':<10} "
          f"{'Dec Min':<10} {'Dec Max':<10} {'Dec Avg':<10} {'Total Avg':<10} {'Success':<10}")
    print("-" * 110)
    for cipher, enc_times, dec_times, total_times, success in results:
        print(f"{cipher:<25} {min(enc_times):<10.6f} {max(enc_times):<10.6f} {mean(enc_times):<10.6f} "
              f"{min(dec_times):<10.6f} {max(dec_times):<10.6f} {mean(dec_times):<10.6f} "
              f"{mean(total_times):<10.6f} {success:<10}")
    
    # Find fastest cipher based on average total time
    fastest = min(results, key=lambda x: mean(x[3]))
    print("-" * 110)
    print(f"Fastest Cipher: {fastest[0]} (Average Total Time: {mean(fastest[3]):.6f} seconds)")

def main():
    # Get user input for number of runs
    while True:
        try:
            num_runs = int(input("Enter number of runs for each cipher (1-1000): ").strip())
            if 1 <= num_runs <= 1000:
                break
            print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Get user input for payload
    payload_input = input("Enter payload to encrypt (or press Enter for default): ").strip()
    payload_multiply = input("Enter payload multiplyer (default = 1000)")
    if not payload_input:
        payload_input = "This is a sample payload for testing TLS 1.3 ciphers in 5G NTN."
    if not payload_multiply:
         payload_multiply =  1000
    payload = int(payload_multiply) * payload_input.encode('utf-8')
    
    print(f"\nTesting ciphers with payload: {payload_input}")
    print(f"Payload size: {len(payload)} bytes")
    print(f"Number of runs per cipher: {num_runs}")
    
    # Run comparison
    compare_ciphers(payload, num_runs)

if __name__ == "__main__":
    main()
