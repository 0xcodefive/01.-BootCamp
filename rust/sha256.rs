use crypto::digest::Digest;
use crypto::sha2::Sha256;

fn find_hash() {
    let mut nonce: u64 = 0;
    loop {
        let mut hasher = Sha256::new();
        let message = format!("zero2hero+{}", nonce);
        hasher.input_str(&message);
        let hash_result = hasher.result_str();
        if hash_result.starts_with("00") {
            println!("Found hash: {}", hash_result);
            return;
        }
        nonce += 1;
    }
}