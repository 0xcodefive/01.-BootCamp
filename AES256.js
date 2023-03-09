const crypto = require('crypto');

function encryptAES256(message, key) {
    const hash = crypto.createHash('sha256').update(key).digest();
  
    const cipher = crypto.createCipheriv('aes-256-cbc', hash, '');
    let encrypted = cipher.update(message);
    encrypted = Buffer.concat([encrypted, cipher.final()]);
  
    return {
        hash: hash.toString('hex'),
        encryptedData: encrypted.toString('base64'),
  };
}

function decryptAES256(message, key) {
    const hash = crypto.createHash('sha256').update(key).digest();
    const decipher = crypto.createDecipheriv('aes-256-cbc', hash, '');
    let decrypted = decipher.update(message, 'base64', 'utf-8');
    decrypted += decipher.final('utf-8');
    return decrypted;
  }

const message = 'Hello, world!';
const key = '0xc0de';

const resultEncrypt = encryptAES256(message, key);
console.log(resultEncrypt);

const resultDecrypt = decryptAES256(resultEncrypt.encryptedData, key);
console.log(resultDecrypt);
